terraform {
  backend "s3" {
    bucket = "fastapi-removebg-bucket"
    key    = "terraform/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}

