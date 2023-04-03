output "removebg-api-gateway-url" {
  value = aws_api_gateway_deployment.removebg-api-gateway-deployment.invoke_url
}
