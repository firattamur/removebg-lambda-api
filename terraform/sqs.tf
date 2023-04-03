resource "aws_sqs_queue" "removebg-api-sqs-queue" {
  name       = "removebg-api-queue.fifo"
  fifo_queue = true

  content_based_deduplication = true
  message_retention_seconds   = 345600
  visibility_timeout_seconds  = 600
  delay_seconds               = 0
  max_message_size            = 262144
}
