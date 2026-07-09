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

La solución contempla:

- Centralización de logs mediante Amazon CloudWatch Logs.
- Publicación de métricas operacionales.
- Alarmas configurables mediante CloudWatch Alarms.
- Endpoint `/health` para monitoreo del estado de la aplicación.
- Documentación OpenAPI generada automáticamente mediante Swagger.

---

# Seguridad

La arquitectura incorpora múltiples capas de seguridad:

- Comunicación cifrada mediante HTTPS utilizando AWS Certificate Manager.
- Protección de la aplicación mediante AWS WAF.
- Ejecución de contenedores en subredes privadas.
- Gestión segura de secretos mediante AWS Secrets Manager.
- Principio de mínimo privilegio utilizando AWS IAM.

---

# Decisiones de Diseño

Las principales decisiones arquitectónicas y sus justificaciones se encuentran documentadas en:

```
docs/design-decisions.md
```

---

# Flujo de despliegue

El despliegue de la aplicación sigue el siguiente flujo:

1. Construcción de la imagen Docker.
2. Publicación de la imagen en Amazon ECR.
3. Actualización de la infraestructura mediante Terraform.
4. Registro de una nueva revisión de la ECS Task Definition.
5. Rolling Update automático del ECS Service.

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