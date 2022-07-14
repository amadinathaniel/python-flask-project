provider "aws" {
    region = "eu-west-2"
}

resource "aws_s3_bucket" "helm_central" {
   bucket = "nath-helm-central-bucket"
}

resource "aws_s3_bucket_acl" "helm_central_bucket_acl" {
   bucket = aws_s3_bucket.helm_central.id
   acl    = "private"
}

resource "aws_s3_object" "object" {
   bucket = aws_s3_bucket.helm_central.id
   key    = "charts/index.yaml"
   source = "/home/nathaniel/Devops_Projects/kubernetes/devops-task-swoon/index.yaml"
}