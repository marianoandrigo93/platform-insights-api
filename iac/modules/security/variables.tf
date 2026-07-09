variable "vpc_id" {
  description = "VPC donde se crearán los Security Groups"
  type        = string
}

variable "project_name" {
  type = string
}

variable "environment" {
  type = string
}