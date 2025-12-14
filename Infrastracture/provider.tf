provider "aws" {
  region = "us-east-1"

  # Credentials dla LocalStack
  access_key = var.use_localstack ? "test" : null
  secret_key = var.use_localstack ? "test" : null

  # LocalStack wymaga path-style i pomijania weryfikacji
  s3_use_path_style           = var.use_localstack
  skip_credentials_validation = var.use_localstack
  skip_metadata_api_check     = var.use_localstack
  skip_requesting_account_id  = var.use_localstack

  # Endpointy tylko dla LocalStack
  dynamic "endpoints" {
    for_each = var.use_localstack ? [1] : []
    content {
      s3        = "http://localhost:4566"
      s3control = "http://localhost:4566"
    }
  }
}
