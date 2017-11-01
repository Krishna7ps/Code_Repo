variable region {
  description = "Enter region for infrastructure"
  default     = "us-west-2"
}

variable "environment" {
  default = "dev"
}

variable "instance_type" {
  type = "map"

  default = {
    dev   = "t2.micro"
    prod  = "t2.small"
    stage = "t2.micro"
  }
}
