# Rollback Strategy

## Objetivo

La estrategia de rollback permite restaurar rápidamente una versión estable de la aplicación utilizando GitHub Actions, Terraform y Amazon ECS, sin realizar cambios manuales sobre la infraestructura.

---

## Flujo de rollback

```text
GitHub Actions
        │
        ▼
Workflow Dispatch
(image_tag)
        │
        ▼
Terraform Apply
        │
        ▼
Nueva ECS Task Definition
        │
        ▼
Actualización del ECS Service
        │
        ▼
Rolling Update
        │
        ▼
Application Load Balancer
```

---

## Cómo funciona el rollback

El rollback se ejecuta mediante un workflow manual de GitHub Actions.

El operador selecciona el workflow **Rollback Platform Insights API** e ingresa el tag de la imagen Docker que desea restaurar.

Por ejemplo:

```text
1.0.0
```

Luego el pipeline ejecuta:

```bash
terraform apply -auto-approve -var="image_tag=<TAG>"
```

Terraform detecta el cambio en la imagen del contenedor, crea una nueva revisión de la ECS Task Definition y actualiza el ECS Service para utilizar esa nueva revisión.

---

## ¿Por qué se crea una nueva Task Definition?

Las Task Definitions de Amazon ECS son recursos **inmutables**.

Cuando cambia la imagen Docker, ECS no modifica la Task Definition existente, sino que registra una nueva revisión.

Posteriormente, Terraform actualiza el ECS Service para utilizar esa nueva revisión.

---

## ¿Por qué se actualiza el ECS Service?

El ECS Service es el componente responsable de mantener la cantidad deseada de Tasks en ejecución.

Cuando cambia la Task Definition, el Service debe actualizarse para apuntar a la nueva revisión.

A partir de ese momento, Amazon ECS inicia automáticamente un **Rolling Update**, reemplazando gradualmente las Tasks antiguas por nuevas Tasks creadas con la nueva imagen Docker.

---

## Estrategia de despliegue

El proyecto utiliza la estrategia nativa de Rolling Update de Amazon ECS.

Esto permite:

- Mantener disponibilidad durante el despliegue.
- Registrar las nuevas Tasks en el Load Balancer únicamente cuando superan el Health Check.
- Retirar automáticamente las Tasks anteriores una vez que las nuevas se encuentran saludables.

---

## Ventajas

- Rollback ejecutado desde GitHub Actions.
- No requiere cambios manuales en la consola de AWS.
- Infraestructura completamente gestionada mediante Terraform.
- Imágenes Docker versionadas en Amazon ECR.
- Trazabilidad completa de cada despliegue y rollback.

---
