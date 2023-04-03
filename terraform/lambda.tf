resource "aws_lambda_function" "removegb-api-lambda" {

  function_name = local.lambda_name

  s3_bucket = local.lambda_s3_bucket
  s3_key    = local.lambda_s3_key

  handler = local.lambda_handler
  runtime = local.lambda_runtime

  timeout     = local.lambda_timeout
  description = local.lambda_description

  role = aws_iam_role.removebg-api-lambda-role.arn

  environment {
    variables = {
      STAGE                     = local.stage
      APP_VERSION               = var.APP_VERSION
      APP_AWS_DEFAULT_REGION    = var.APP_AWS_DEFAULT_REGION
      APP_AWS_ACCESS_KEY_ID     = var.APP_AWS_ACCESS_KEY_ID
      APP_AWS_SECRET_ACCESS_KEY = var.APP_AWS_SECRET_ACCESS_KEY
      APP_AWS_S3_BUCKET         = var.APP_AWS_S3_BUCKET
      APP_AWS_SQS_QUEUE_URL     = var.APP_AWS_SQS_QUEUE_URL
      APP_AWS_SNS_TOPIC_ARN     = var.APP_AWS_SNS_TOPIC_ARN
    }
  }

  tags = {
    name        = local.lambda_name
    environment = local.stage
  }

}

resource "aws_iam_role" "removebg-api-lambda-role" {

  name = "removebg-api-lambda-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

}


resource "aws_iam_role_policy_attachment" "removebg-api-lamda-role-dynamodb" {

  role       = aws_iam_role.removebg-api-lambda-role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"

}

resource "aws_iam_role_policy_attachment" "removebg-api-lamda-role-s3" {

  role       = aws_iam_role.removebg-api-lambda-role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"

}

resource "aws_iam_role_policy_attachment" "removebg-api-lamda-role-sqs" {

  role       = aws_iam_role.removebg-api-lambda-role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSQSFullAccess"

}

resource "aws_iam_role_policy_attachment" "removebg-api-lamda-role-sns" {

  role       = aws_iam_role.removebg-api-lambda-role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSNSFullAccess"

}

resource "aws_iam_role_policy_attachment" "removebg-api-lamda-role-cloudwatch" {

  role       = aws_iam_role.removebg-api-lambda-role.name
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchFullAccess"

}

resource "aws_iam_role_policy_attachment" "removebg-api-lamda-role-logs" {

  role       = aws_iam_role.removebg-api-lambda-role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"

}
