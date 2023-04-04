variable "APP_VERSION" {
  type        = string
  description = "The version of the application to deploy"
}

variable "APP_AWS_DEFAULT_REGION" {
  type        = string
  description = "The AWS region to deploy the application to"
}

variable "APP_AWS_ACCESS_KEY_ID" {
  type        = string
  description = "The AWS access key ID to use for deployment"
}

variable "APP_AWS_SECRET_ACCESS_KEY" {
  type        = string
  description = "The AWS secret access key to use for deployment"
}

variable "APP_AWS_S3_BUCKET" {
  type        = string
  description = "The AWS S3 bucket to use for deployment"
}

variable "APP_AWS_SQS_QUEUE_URL" {
  type        = string
  description = "The AWS SQS queue URL to use for deployment"
  default     = ""
}

variable "APP_AWS_SNS_TOPIC_ARN" {
  type        = string
  description = "The AWS SNS topic ARN to use for deployment"
  default     = ""
}

variable "APP_AWS_DYNAMODB_REMOVEBG_TABLE_NAME" {
  type        = string
  description = "The AWS DynamoDB table name to use for deployment"
}


locals {

  stage = "production"

  lambda_name        = "removebg-${local.stage}"
  lambda_description = "Lambda function for removebg-${local.stage}"
  lambda_s3_bucket   = "fastapi-removebg-bucket"
  lambda_s3_key      = "production/${var.APP_VERSION}/lambda.zip"
  lambda_handler     = "app.main.handler"
  lambda_runtime     = "python3.9"
  lambda_timeout     = 300

  api_gateway_name              = "removebg-${local.stage}"
  api_gateway_description       = "API Gateway for removebg-${local.stage}"
  api_gateway_stage_name        = local.stage
  api_gateway_stage_description = "API Gateway stage for removebg-${local.stage}"

  dynamodb_removebg_table_name         = "removebg-${local.stage}"
  dynamodb_removebg_table_billing_mode = "PAY_PER_REQUEST"
  dynamodb_removebg_table_hash_key     = "id"

}

