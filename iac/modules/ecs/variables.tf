variable "project_name" {
  type = string
}

variable "environment" {
  type = string
}

variable "image_repository" {
  type = string
}

variable "image_tag" {
  type = string
}

variable "target_group_arn" {
  type = string
}

variable "ecs_security_group_id" {
  type = string
}

variable "subnet_ids" {
  type = list(string)
}