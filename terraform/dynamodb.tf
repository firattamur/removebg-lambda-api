resource "aws_dynamodb_table" "removebg-api-dynamodb-table" {

  name         = local.dynamodb_removebg_table_name
  billing_mode = local.dynamodb_removebg_table_billing_mode
  hash_key     = local.dynamodb_removebg_table_hash_key

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    name        = local.dynamodb_removebg_table_name
    environment = local.stage
  }

}
