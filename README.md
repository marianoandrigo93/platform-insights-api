# Platform Insights API

![AWS](https://img.shields.io/badge/AWS-ECS_Fargate-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-purple)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)

API REST diseñada para exponer información operacional de infraestructura de manera segura, escalable y preparada para producción utilizando servicios administrados de AWS.

Este proyecto fue desarrollado como una demostración de una arquitectura cloud moderna, priorizando buenas prácticas de diseño, seguridad, observabilidad, automatización e Infrastructure as Code.

---

# Estado del proyecto

- ✅ API REST implementada
- ✅ Documentación OpenAPI (Swagger)
- ✅ Testing automatizado con Pytest
- ✅ Contenerización con Docker
- ⏳ Infraestructura como código con Terraform
- ⏳ Despliegue en AWS
- ⏳ Pipeline CI/CD con GitHub Actions

---

# Objetivos

El objetivo de este proyecto es demostrar el diseño e implementación de una API preparada para producción que permita:

- Exponer información operacional de infraestructura mediante una API REST.
- Implementar una arquitectura altamente disponible y escalable en AWS.
- Automatizar el aprovisionamiento de infraestructura mediante Terraform.
- Automatizar el ciclo de vida de despliegue mediante CI/CD.
- Aplicar buenas prácticas de seguridad y observabilidad.

---

# Arquitectura

La siguiente arquitectura representa el despliegue de la solución en AWS.

![Arquitectura](diagrams/architecture.png)

## Componentes principales

- Amazon Route53 para resolución DNS.
- AWS Certificate Manager (ACM) para certificados TLS.
- AWS WAF como capa adicional de protección.
- Application Load Balancer como punto de entrada público.
- Amazon ECS Fargate para ejecutar la aplicación.
- Amazon ECR para almacenar imágenes Docker.
- AWS Secrets Manager para la gestión de secretos.
- Amazon CloudWatch para logs, métricas y alarmas.
- AWS IAM siguiendo el principio de mínimo privilegio.

---

# Stack Tecnológico

| Componente | Tecnología |
|------------|------------|
| Lenguaje | Python 3.12 |
| Framework | FastAPI |
| Contenedores | Docker |
| Cloud | AWS |
| Runtime | ECS Fargate |
| Balanceador | Application Load Balancer |
| DNS | Route53 |
| Certificados | AWS Certificate Manager |
| Seguridad | AWS WAF |
| Secretos | AWS Secrets Manager |
| Observabilidad | Amazon CloudWatch |
| Registry | Amazon ECR |
| IaC | Terraform |
| CI/CD | GitHub Actions |

---

# Endpoints

| Método | Endpoint | Descripción |
|---------|----------|-------------|
| GET | `/health` | Verifica el estado de la aplicación. |
| GET | `/api/v1/services` | Obtiene el listado de servicios monitoreados. |
| GET | `/api/v1/services/{service_id}` | Obtiene el detalle de un servicio. |
| GET | `/api/v1/deployments` | Devuelve el historial de despliegues. |
| GET | `/api/v1/alerts` | Devuelve las alertas activas. |
| GET | `/api/v1/metrics/summary` | Devuelve un resumen de métricas operacionales. |

---

# Estructura del proyecto

```text
platform-insights-api/

├── api/
├── cicd/
├── diagrams/
├── docs/
├── iac/
├── prompts.md
└── README.md
```

---

# Ejecución local

## Requisitos

- Python 3.12
- Docker Desktop

## Ejecución con Python

Desde el directorio `api/`:

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn app.main:app --reload
```

La aplicación quedará disponible en:

- http://localhost:8000/health
- http://localhost:8000/docs

---

## Ejecución con Docker

Desde el directorio `api/`:

```bash
docker compose up --build
```

La aplicación quedará disponible en:

- http://localhost:8000/health
- http://localhost:8000/docs

---

## Ejecución de tests

Desde el directorio `api/`:

```bash
pytest
```

---

# Despliegue

La infraestructura será aprovisionada mediante Terraform y desplegada sobre AWS utilizando los siguientes servicios:

- Amazon ECR
- Amazon ECS Fargate
- Application Load Balancer
- AWS WAF
- AWS Secrets Manager
- Amazon CloudWatch

El despliegue será automatizado mediante GitHub Actions.

---

# Infraestructura

Toda la infraestructura se define mediante Terraform y se encuentra en el directorio `iac/`.

La solución fue diseñada siguiendo el paradigma **Infrastructure as Code**, permitiendo crear, modificar y destruir el entorno de manera reproducible.

---

# Observabilidad

La solución incorpora mecanismos de observabilidad para facilitar el monitoreo, troubleshooting y operación de la aplicación.

## Logs

La aplicación envía los logs del contenedor a **Amazon CloudWatch Logs** mediante el driver nativo de Amazon ECS.

Esto permite:

- Centralizar los logs de todas las Tasks.
- Consultar históricos de ejecuciones.
- Facilitar el análisis de incidentes.

---

## Health Checks

La aplicación expone un endpoint:

```text
GET /health
```

Este endpoint es utilizado por el **Application Load Balancer** para determinar el estado de salud de cada Task.

Las Tasks únicamente reciben tráfico cuando el Health Check es satisfactorio.

---

## Métricas

Amazon ECS publica automáticamente métricas operacionales en **Amazon CloudWatch**, entre ellas:

- CPU Utilization
- Memory Utilization
- Running Tasks
- Desired Tasks

Estas métricas permiten implementar políticas de escalado automático y generar alarmas operacionales.

---

## Logs del Pipeline

Cada ejecución del pipeline queda registrada en **GitHub Actions**, proporcionando trazabilidad completa sobre:

- Ejecución de pruebas.
- Análisis de calidad.
- Escaneo de seguridad.
- Construcción de imágenes.
- Despliegues.
- Rollbacks.

---

# Seguridad

La solución incorpora múltiples capas de seguridad tanto en la infraestructura como durante el proceso de integración y despliegue.

## Seguridad de la infraestructura

- Comunicación cifrada mediante HTTPS (preparada para utilizar AWS Certificate Manager).
- Protección de la aplicación mediante AWS WAF (preparado para una futura integración).
- Ejecución de contenedores en Amazon ECS Fargate.
- Gestión de permisos mediante AWS IAM siguiendo el principio de mínimo privilegio.
- Gestión de imágenes privadas mediante Amazon ECR.

---

## Seguridad del pipeline

El pipeline implementa diferentes controles de calidad y seguridad antes del despliegue.

| Herramienta | Objetivo |
|------------|----------|
| Pytest | Validación funcional mediante pruebas unitarias. |
| Ruff | Análisis de calidad y estilo del código Python. |
| Bandit | Detección de vulnerabilidades comunes en el código Python. |
| Trivy | Escaneo de vulnerabilidades sobre la imagen Docker antes de publicarla en Amazon ECR. |

El despliegue únicamente continúa si las etapas anteriores finalizan correctamente.

---

## Gestión de credenciales

GitHub Actions utiliza **GitHub Secrets** para almacenar las credenciales necesarias para acceder a AWS.

Las credenciales nunca forman parte del código fuente ni del repositorio.

---

# Decisiones de Diseño

Las principales decisiones arquitectónicas y sus justificaciones se encuentran documentadas en:

```
docs/design-decisions.md
```

---

# CI/CD

El proyecto implementa un pipeline completo mediante **GitHub Actions**.

## Flujo del pipeline

```text
Push
    │
    ▼
Test
    │
    ▼
Quality & Security Analysis
    │
    ▼
Docker Build
    │
    ▼
Push a Amazon ECR
    │
    ▼
Terraform Apply
    │
    ▼
Amazon ECS Rolling Update
```

## Jobs implementados

El pipeline se encuentra dividido en los siguientes jobs:

| Job | Descripción |
|------|-------------|
| Test API | Ejecuta los tests unitarios mediante Pytest. |
| Quality & Security Analysis | Ejecuta análisis de calidad con Ruff y análisis de seguridad con Bandit. |
| Build and Push Docker Image | Construye la imagen Docker, ejecuta Trivy y publica la imagen en Amazon ECR. |
| Deploy with Terraform | Actualiza la infraestructura y despliega la nueva versión en Amazon ECS. |

---

## Estrategia de versionado

Cada despliegue genera una imagen Docker versionada utilizando el **SHA corto del commit de Git**.

Ejemplo:

```text
platform-insights-api-dev:f16da7c
```

Esto permite identificar exactamente qué versión del código se encuentra desplegada en cada momento.


# Uso de Inteligencia Artificial durante el desarrollo

Durante el desarrollo de este proyecto se utilizó inteligencia artificial como asistente técnico para:

- Evaluar alternativas de arquitectura.
- Revisar decisiones de diseño.
- Mejorar la documentación técnica.
- Validar buenas prácticas de desarrollo.
- Revisar código.
- Diseñar la estrategia de testing.
- Diseñar la infraestructura como código.

La inteligencia artificial fue utilizada exclusivamente como herramienta de asistencia. Todas las decisiones técnicas, implementaciones y validaciones finales fueron revisadas manualmente antes de incorporarse al proyecto.

---

# Próximas Mejoras

- Integración con métricas reales provenientes de AWS CloudWatch.
- Incorporación de persistencia de datos.
- Implementación de despliegues Blue/Green.
- Incorporación de OpenTelemetry para tracing distribuido.
- Integración con Amazon X-Ray.
- Implementación de autenticación y autorización mediante JWT.