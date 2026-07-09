terraform {
  backend "s3" {
    bucket = "platform-insights-api-tfstate-460210064623"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}