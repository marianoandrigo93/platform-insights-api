variable "repository_name" {
  description = "Nombre del repositorio ECR"
  type        = string
}

variable "image_tag_mutability" {
  description = "Define si los tags de imagen pueden sobrescribirse"
  type        = string
  default     = "MUTABLE"
}