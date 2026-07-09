# Prompts utilizados durante el desarrollo

Durante el desarrollo del proyecto se utilizó IA como asistente técnico para acelerar tareas de diseño, documentación y validación de decisiones arquitectónicas.

La IA fue utilizada como herramienta de apoyo y todas las decisiones finales fueron revisadas e implementadas manualmente.

---

## 1. Diseño de arquitectura

**Objetivo**

Definir una arquitectura cloud simple, escalable y alineada con buenas prácticas de AWS.

**Prompt**

> Diseñá una arquitectura AWS para una API REST desplegada sobre ECS Fargate utilizando Terraform. El objetivo es minimizar la complejidad operativa, mantener alta disponibilidad y permitir futuras mejoras como Auto Scaling, WAF y HTTPS.

---

## 2. Modelado de la API

**Objetivo**

Definir recursos y endpoints para una API orientada a operaciones de infraestructura.

**Prompt**

> Proponé una API REST que exponga información operacional para equipos DevOps, incluyendo estado de servicios, despliegues, alertas y métricas de infraestructura.

---

## 3. Organización del proyecto Terraform

**Objetivo**

Diseñar una estructura modular reutilizable.

**Prompt**

> Diseñá una estructura de módulos Terraform separando responsabilidades para ECS, ALB, Security Groups, IAM, ECR y WAF siguiendo buenas prácticas.

---

## 4. Pipeline de GitHub Actions

**Objetivo**

Automatizar el ciclo completo de CI/CD.

**Prompt**

> Diseñá un pipeline de GitHub Actions que ejecute tests, análisis de calidad, análisis de seguridad, construcción de imágenes Docker, publicación en Amazon ECR y despliegue mediante Terraform.

---


## 5. Seguridad

**Objetivo**

Fortalecer la exposición pública de la API.

**Prompt**

> ¿Qué controles de seguridad agregarías a una API desplegada en Amazon ECS expuesta mediante Application Load Balancer?

---

## 6. Escalabilidad

**Objetivo**

Preparar la plataforma para soportar incrementos de carga.

**Prompt**

> Diseñá una estrategia de Auto Scaling para un servicio ECS Fargate basada en métricas de CPU y memoria utilizando Application Auto Scaling.

---

## 7. Documentación

**Objetivo**

Generar documentación técnica clara y orientada a un equipo de ingeniería en base a lo implementado y a las decisiones tomadas.

**Prompt**

> Ayudame a redactar un README, un Runbook y un documento de decisiones de arquitectura para este proyecto, justificando cada una de las tecnologías elegidas.

---

# Consideraciones

La IA fue utilizada principalmente para:

- Evaluar alternativas de arquitectura.
- Validar buenas prácticas de AWS.
- Generar documentación técnica.
- Revisar configuraciones de Terraform.
- Mejorar el pipeline de CI/CD.
- Explicar conceptos técnicos durante el desarrollo.

Todas las decisiones finales fueron analizadas, adaptadas e implementadas manualmente para ajustarse al alcance del challenge.