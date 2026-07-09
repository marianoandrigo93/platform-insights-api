# Platform Insights API - Runbook

Este documento describe cómo ejecutar, probar y desplegar la aplicación.

---

# Prerrequisitos

Antes de comenzar es necesario contar con:

- Python 3.12
- Docker Desktop
- Terraform >= 1.6
- AWS CLI configurado
- Git
- Una cuenta AWS con permisos sobre:
  - Amazon ECR
  - Amazon ECS
  - Elastic Load Balancer
  - IAM
  - CloudWatch
  - AWS WAF
  - Amazon S3

---

# Clonar el proyecto

```bash
git clone https://github.com/<usuario>/platform-insights-api.git

cd platform-insights-api
```

---

# Ejecutar localmente

Ingresar al directorio de la API.

```bash
cd api
```

Crear entorno virtual.

## Windows

```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

## Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Instalar dependencias.

```bash
pip install -r requirements.txt
```

Levantar la aplicación.

```bash
uvicorn app.main:app --reload
```

La aplicación quedará disponible en:

Swagger

```
http://localhost:8000/docs
```

Health Check

```
http://localhost:8000/health
```

---

# Ejecutar con Docker

Desde el directorio `api`.

Construir la imagen.

```bash
docker build -t platform-insights-api .
```

Ejecutar el contenedor.

```bash
docker run -p 8000:8000 platform-insights-api
```

o utilizando Docker Compose.

```bash
docker compose up --build
```

Endpoints disponibles.

```
http://localhost:8000/docs

http://localhost:8000/health
```

---

# Ejecutar tests

Desde el directorio `api`.

```bash
pytest
```

---

# Análisis de calidad

Ejecutar Ruff.

```bash
ruff check app tests
```

---

# Análisis de seguridad

Ejecutar Bandit.

```bash
bandit -r app
```

---

# Despliegue manual en AWS

## Inicializar Terraform

Ingresar al entorno.

```bash
cd iac/environments/dev
```

Inicializar Terraform.

```bash
terraform init
```

---

## Crear el repositorio ECR (primer despliegue)

```bash
terraform apply \
-target=module.ecr \
-var="image_tag=1.0.0"
```

---

## Publicar la imagen Docker

Ingresar al directorio de la API.

```bash
cd api
```

Login en Amazon ECR.

```bash
aws ecr get-login-password --region us-east-1 \
| docker login \
--username AWS \
--password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

Construir la imagen.

```bash
docker build -t platform-insights-api:1.0.0 .
```

Tag.

```bash
docker tag \
platform-insights-api:1.0.0 \
<AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/platform-insights-api-dev:1.0.0
```

Push.

```bash
docker push \
<AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/platform-insights-api-dev:1.0.0
```

---

## Crear la infraestructura completa

Volver al directorio Terraform.

```bash
cd ../iac/environments/dev
```

Aplicar infraestructura.

```bash
terraform apply \
-var="image_tag=1.0.0"
```

---

# Despliegue automático

El proyecto implementa un pipeline de CI/CD mediante GitHub Actions.

Flujo del pipeline.

```
Test
        │
        ▼
Quality & Security Analysis
        │
        ▼
Docker Build
        │
        ▼
Trivy Scan
        │
        ▼
Push Amazon ECR
        │
        ▼
Terraform Apply
        │
        ▼
Amazon ECS Rolling Update
```

Cada despliegue genera una nueva imagen Docker utilizando el SHA corto del commit como tag.

---

# Rollback

El proyecto incorpora un workflow manual de GitHub Actions para restaurar una versión anterior.

Workflow:

```
Rollback Platform Insights API
```

Se debe indicar el tag Docker que se desea desplegar.

Ejemplo:

```
1.0.0
```

Terraform actualiza la ECS Task Definition y Amazon ECS realiza automáticamente un Rolling Update hacia esa versión.

Para más información consultar:

```
docs/rollback-strategy.md
```

---

# Variables importantes

Terraform

```
image_tag
```

GitHub Secrets

```
AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_ACCOUNT_ID
```

---

# Consideraciones

Para simplificar el challenge:

- Se utiliza la VPC Default de AWS.
- Las Tasks de ECS utilizan IP pública.
- La aplicación se publica mediante un Application Load Balancer.
- Se implementa Rolling Update nativo de Amazon ECS.
- Se implementa Auto Scaling basado en CPU y memoria.
- AWS WAF protege el Application Load Balancer.
- El estado remoto de Terraform se almacena en Amazon S3.

En un entorno productivo se recomendaría:

- Subnets privadas.
- NAT Gateway o VPC Endpoints.
- HTTPS mediante AWS Certificate Manager.
- Route53 con dominio propio.
- GitHub OIDC para autenticación con AWS.
- Blue/Green Deployment mediante AWS CodeDeploy.