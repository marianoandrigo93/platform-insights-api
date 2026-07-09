# Design Decisions

# Arquitectura

La siguiente imagen representa la arquitectura de despliegue implementada para el proyecto.

![Architecture](diagrams/architecture.png)

## Objetivo

El objetivo de este proyecto fue diseñar e implementar una API preparada para producción que exponga información operacional de infraestructura, aplicando buenas prácticas de arquitectura cloud, automatización, seguridad y operación.

Durante el desarrollo se priorizó construir una solución simple, mantenible y escalable, justificando cada una de las decisiones técnicas adoptadas.

---

# Arquitectura General

La solución se implementó utilizando una arquitectura basada completamente en servicios administrados de AWS.

```
Internet
    │
    ▼
AWS WAF
    │
    ▼
Application Load Balancer
    │
    ▼
Amazon ECS Fargate
    │
    ▼
FastAPI
```

La infraestructura fue definida íntegramente mediante Terraform y el ciclo de vida de despliegue se automatizó utilizando GitHub Actions.

---

# Decisiones Arquitectónicas

## ¿Por qué FastAPI?

Se eligió FastAPI por las siguientes razones:

- Excelente rendimiento para APIs REST.
- Soporte nativo para tipado mediante Python.
- Generación automática de documentación OpenAPI / Swagger.
- Validación automática de requests mediante Pydantic.
- Gran productividad para desarrollar APIs pequeñas y medianas.

Para este proyecto resultó una excelente alternativa frente a frameworks más pesados.

---

## ¿Por qué Amazon ECS Fargate?

El challenge consiste en desplegar una única API stateless.

Para este escenario, ECS Fargate ofrece varias ventajas:

- No requiere administrar nodos Kubernetes.
- Escalado completamente administrado por AWS.
- Menor complejidad operativa.
- Integración nativa con Application Load Balancer.
- Integración directa con CloudWatch Logs.
- Menor esfuerzo de mantenimiento.

Amazon EKS hubiese sido una alternativa válida para plataformas con múltiples microservicios o equipos operando Kubernetes, pero para una única API hubiese incrementado considerablemente la complejidad sin aportar beneficios significativos.

---

## ¿Por qué Terraform?

Toda la infraestructura se implementó utilizando Infrastructure as Code mediante Terraform.

Esto permite:

- Infraestructura reproducible.
- Versionado de infraestructura.
- Cambios auditables.
- Automatización completa mediante CI/CD.
- Eliminación sencilla del entorno.

Además se utilizó un estado remoto almacenado en Amazon S3 para permitir ejecuciones consistentes tanto desde el entorno local como desde GitHub Actions.

---

## ¿Por qué Docker?

La aplicación fue containerizada para garantizar consistencia entre el entorno local y producción.

Docker permite:

- Portabilidad.
- Reproducibilidad.
- Despliegue sencillo sobre Amazon ECS.
- Integración directa con Amazon ECR.

---

## ¿Por qué GitHub Actions?

Se eligió GitHub Actions por su integración nativa con GitHub y su simplicidad para construir pipelines declarativos.

El pipeline implementa:

- Tests automatizados.
- Análisis de calidad.
- Análisis de seguridad.
- Construcción de imágenes Docker.
- Publicación en Amazon ECR.
- Despliegue automático mediante Terraform.

Además se implementó un workflow independiente para ejecutar rollbacks manuales.

---

# Estrategia de Despliegue

Se eligió utilizar Rolling Update nativo de Amazon ECS.

Esta estrategia permite:

- Mantener disponibilidad durante el despliegue.
- Reducir downtime.
- Crear nuevas Tasks antes de eliminar las anteriores.
- Integrarse naturalmente con Terraform.

Como evolución futura podría incorporarse AWS CodeDeploy para implementar estrategias Blue/Green o Canary Deployment.

---

# Estrategia de Escalabilidad

La aplicación fue diseñada como un servicio stateless.

Esto permite escalar horizontalmente agregando nuevas Tasks en Amazon ECS.

Se implementó Auto Scaling utilizando métricas administradas por CloudWatch:

- CPU Utilization
- Memory Utilization

Cuando dichas métricas superan los umbrales configurados, Amazon ECS incrementa automáticamente la cantidad de Tasks del servicio.

---

# Estrategia de Seguridad

La solución incorpora diferentes capas de seguridad.

Infraestructura:

- Security Groups.
- AWS IAM.
- Amazon ECR privado.
- AWS WAF.
- CloudWatch Logs.

Pipeline:

- Ruff.
- Bandit.
- Trivy.

Las credenciales nunca forman parte del repositorio y se almacenan mediante GitHub Secrets.

Como mejora futura se recomienda utilizar GitHub OpenID Connect (OIDC) para eliminar el uso de Access Keys permanentes.

---

# Observabilidad

Se implementó observabilidad utilizando servicios administrados de AWS.

La solución utiliza:

- CloudWatch Logs para centralizar logs.
- CloudWatch Metrics para métricas de infraestructura.
- Health Check utilizado por el Application Load Balancer.
- Auto Scaling basado en métricas de CloudWatch.

Los endpoints de la API modelan información operacional utilizando datos simulados.

En un escenario productivo dichos datos podrían obtenerse dinámicamente desde CloudWatch, Amazon ECS, GitHub Actions, ArgoCD u otras plataformas de observabilidad sin modificar el contrato expuesto por la API.

---

# Uso de Datos Mock

Para mantener el alcance del challenge, los endpoints exponen información simulada.

La API fue diseñada desacoplando el contrato REST de la fuente de datos.

Esto permite reemplazar fácilmente los datos mock por integraciones reales sin afectar a los consumidores de la API.

---

# Decisiones de Alcance

Con el objetivo de mantener el proyecto enfocado en la automatización y arquitectura cloud se adoptaron las siguientes simplificaciones:

- Utilización de la VPC Default de AWS.
- Tasks de ECS con IP pública.
- Acceso mediante el DNS público del Application Load Balancer.
- HTTPS documentado como evolución futura, ya que requiere un dominio propio y AWS Certificate Manager.

Estas decisiones reducen la complejidad del laboratorio sin modificar los conceptos arquitectónicos implementados.

---

# Posibles Evoluciones

Como mejoras futuras podrían incorporarse:

- HTTPS mediante AWS Certificate Manager.
- Route53 con dominio propio.
- GitHub OIDC.
- AWS CodeDeploy para Blue/Green Deployment.
- OpenTelemetry.
- AWS X-Ray.
- Integración con CloudWatch Metrics reales.
- Integración con GitHub, ArgoCD o Jenkins para obtener información operacional en tiempo real.