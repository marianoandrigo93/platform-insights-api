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

variable "min_capacity" {
  description = "Minimum number of ECS tasks"
  type        = number
  default     = 1
}

variable "max_capacity" {
  description = "Maximum number of ECS tasks"
  type        = number
  default     = 3
}

variable "cpu_target" {
  description = "CPU target utilization percentage"
  type        = number
  default     = 70
}

variable "memory_target" {
  description = "Memory target utilization percentage"
  type        = number
  default     = 80
}