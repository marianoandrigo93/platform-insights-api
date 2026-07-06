# Platform Insights API

![AWS](https://img.shields.io/badge/AWS-ECS_Fargate-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-purple)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)

API REST diseñada para exponer información operacional de infraestructura de manera segura, escalable y preparada para producción utilizando servicios administrados de AWS.

Este proyecto fue desarrollado como una demostración de una arquitectura cloud moderna, priorizando buenas prácticas de diseño, seguridad, observabilidad, automatización e Infrastructure as Code.

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

- Amazon Route53 para la resolución DNS.
- AWS Certificate Manager (ACM) para la gestión del certificado TLS.
- AWS WAF como capa adicional de protección frente a amenazas comunes.
- Application Load Balancer como punto de entrada público y distribución del tráfico.
- Amazon ECS Fargate para la ejecución de la aplicación sin administración de servidores.
- Amazon ECR para el almacenamiento de imágenes Docker.
- AWS Secrets Manager para la gestión segura de secretos.
- Amazon CloudWatch para logs, métricas y alarmas.
- AWS IAM para la gestión de permisos siguiendo el principio de mínimo privilegio.

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

> En construcción. Será completado una vez implementada la API.

---

# Despliegue

> En construcción. Será completado una vez implementada la infraestructura con Terraform.

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
- Health Check para monitoreo del estado de la aplicación.

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

`docs/design-decisions.md`

---

# Uso de Inteligencia Artificial

Durante el desarrollo se utilizó IA como asistente de ingeniería para:

- Evaluar alternativas arquitectónicas.
- Revisar decisiones de diseño.
- Mejorar la documentación técnica.
- Validar buenas prácticas de infraestructura y seguridad.

Las decisiones finales de arquitectura e implementación fueron revisadas y validadas manualmente.

---

# Próximas Mejoras

- Incorporar persistencia de datos.
- Integración con métricas reales de AWS.
- Implementar despliegues Blue/Green.
- Incorporar pruebas de carga automatizadas.
- Agregar tracing distribuido con AWS X-Ray u OpenTelemetry.