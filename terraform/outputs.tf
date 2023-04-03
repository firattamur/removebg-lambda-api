output "removebg-api-gateway-url" {
  description = "The URL of the API Gateway"
  value       = aws_api_gateway_deployment.removebg-api-gateway-deployment.invoke_url
}

output "removebg-api-sqs-queue-url" {
  description = "The URL of the created SQS queue"
  value       = aws_sqs_queue.removebg-api-sqs-queue.url
}

output "removebg-api-sns-topic-arn" {
  description = "The ARN of the created SNS topic"
  value       = aws_sns_topic.removebg-api-sns-topic.arn
}
