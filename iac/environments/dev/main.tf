data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {

  filter {

    name = "vpc-id"

    values = [
      data.aws_vpc.default.id
    ]

  }

}

module "ecr" {
  source = "../../modules/ecr"

  repository_name = "${var.project_name}-${var.environment}"
}

module "security" {
  source = "../../modules/security"

  vpc_id       = data.aws_vpc.default.id
  project_name = var.project_name
  environment  = var.environment
}

module "alb" {

  source = "../../modules/alb"

  project_name = var.project_name

  environment = var.environment

  vpc_id = data.aws_vpc.default.id

  subnet_ids = data.aws_subnets.default.ids

  security_group_id = module.security.alb_security_group_id

}

module "ecs" {
  source = "../../modules/ecs"

  project_name = var.project_name
  environment  = var.environment

  image_repository = module.ecr.repository_url
  image_tag        = var.image_tag

  target_group_arn     = module.alb.target_group_arn
  ecs_security_group_id = module.security.ecs_security_group_id

  subnet_ids = data.aws_subnets.default.ids
}

