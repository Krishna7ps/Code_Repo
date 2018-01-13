resource "aws_instance" "server1" {
  key_name      = "tech"
  ami           = "ami-e689729e"
  instance_type = "${lookup(var.instance_type, var.environment)}"
}