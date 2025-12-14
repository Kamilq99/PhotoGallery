resource "aws_s3_bucket" "PhotoGalleryBucket" {
  bucket = "photo-gallery-bucket"

  # WAŻNE: ignorujemy tagi, żeby LocalStack nie wywalał błędu S3 Control
  lifecycle {
    ignore_changes = [tags, tags_all]
  }
}

resource "aws_s3_bucket_versioning" "PhotoGalleryBucket" {
  bucket = aws_s3_bucket.PhotoGalleryBucket.id

  versioning_configuration {
    status = "Enabled"
  }
}
