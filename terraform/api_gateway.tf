resource "aws_api_gateway_rest_api" "removebg-api-gateway" {
  name        = local.api_gateway_name
  description = local.api_gateway_description

  tags = {
    name        = local.api_gateway_name
    environment = local.stage
  }

}


resource "aws_api_gateway_resource" "removebg-api-gateway-resource" {
  rest_api_id = aws_api_gateway_rest_api.removebg-api-gateway.id
  parent_id   = aws_api_gateway_rest_api.removebg-api-gateway.root_resource_id
  path_part   = "{proxy+}"

}


resource "aws_api_gateway_method" "removebg-api-gateway-method" {

  rest_api_id = aws_api_gateway_rest_api.removebg-api-gateway.id
  resource_id = aws_api_gateway_resource.removebg-api-gateway-resource.id

  http_method   = "ANY"
  authorization = "NONE"

}


resource "aws_api_gateway_integration" "removebg-api-gateway-lambda" {

  rest_api_id = aws_api_gateway_rest_api.removebg-api-gateway.id
  resource_id = aws_api_gateway_resource.removebg-api-gateway-resource.id
  http_method = aws_api_gateway_method.removebg-api-gateway-method.http_method

  type                    = "AWS_PROXY"
  integration_http_method = "POST"
  uri                     = aws_lambda_function.removebg-api-lambda.invoke_arn

}

resource "aws_api_gateway_integration" "removebg-api-gateway-lambda-root" {

  rest_api_id = aws_api_gateway_rest_api.removebg-api-gateway.id
  resource_id = aws_api_gateway_rest_api.removebg-api-gateway.root_resource_id
  http_method = aws_api_gateway_method.removebg-api-gateway-method-root.http_method

  type                    = "AWS_PROXY"
  integration_http_method = "POST"
  uri                     = aws_lambda_function.removebg-api-lambda.invoke_arn

}

resource "aws_api_gateway_method" "removebg-api-gateway-method-root" {

  rest_api_id = aws_api_gateway_rest_api.removebg-api-gateway.id
  resource_id = aws_api_gateway_rest_api.removebg-api-gateway.root_resource_id

  http_method   = "ANY"
  authorization = "NONE"

}

resource "aws_api_gateway_deployment" "removebg-api-gateway-deployment" {

  depends_on = [
    aws_api_gateway_integration.removebg-api-gateway-lambda,
    aws_api_gateway_integration.removebg-api-gateway-lambda-root
  ]

  rest_api_id = aws_api_gateway_rest_api.removebg-api-gateway.id
  stage_name  = local.stage

}

resource "aws_lambda_permission" "removebg-api-lambda-permission" {

  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.removebg-api-lambda.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.removebg-api-gateway.execution_arn}/*/*"

}
