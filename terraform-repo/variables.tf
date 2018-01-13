variable "environment" {
  default = "prod"
}

variable "region" {
  description = "Enter the region for infrastructure"
  default     = "us-west-2"
}

/*
variable "instance_type" {
  type = "map"

  default = {
    dev   = "t2.small"
    prod  = "t2.micro"
    stage = "t2.micro"
  }
}
*/