resource "aws_sns_topic" "removebg-api-sns-topic" {
  name = "removebg-api-sns-topic"
}

resource "aws_sns_topic_subscription" "removebg-api-sns-topic-subscription-https" {
  topic_arn = aws_sns_topic.removebg-api-sns-topic.arn
  protocol  = "https"
  endpoint  = "${aws_api_gateway_deployment.removebg-api-gateway-deployment.invoke_url}/api/v1/removebg/sns"
}
