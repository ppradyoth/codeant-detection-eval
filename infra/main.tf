provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "attachments" {
  bucket = "orders-service-attachments"
  acl    = "public-read"
}

resource "aws_security_group" "app" {
  name = "orders-app-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "orders" {
  identifier          = "orders-db"
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  username            = "admin"
  password            = "Postgres123!"
  storage_encrypted   = false
  publicly_accessible = true
  skip_final_snapshot = true
}
