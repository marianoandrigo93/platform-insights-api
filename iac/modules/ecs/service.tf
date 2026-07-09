resource "aws_ecs_service" "this" {

  name = "${var.project_name}-${var.environment}"

  cluster = aws_ecs_cluster.this.id

  task_definition = aws_ecs_task_definition.this.arn

  desired_count = 1

  launch_type = "FARGATE"

  deployment_minimum_healthy_percent = 100
  deployment_maximum_percent         = 200

  network_configuration {

    subnets = var.subnet_ids

    security_groups = [
      var.ecs_security_group_id
    ]

    assign_public_ip = true

  }

  load_balancer {

    target_group_arn = var.target_group_arn

    container_name = var.project_name

    container_port = 8000

  }

  depends_on = [
    aws_ecs_task_definition.this
  ]

}