variable "aws_region" {
  description = "Región de AWS"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Nombre del proyecto"
  type        = string
  default     = "platform-insights-api"
}

variable "environment" {
  description = "Ambiente"
  type        = string
  default     = "dev"
}

variable "image_tag" {
  description = "Tag de la imagen Docker a desplegar"
  type        = string
}
