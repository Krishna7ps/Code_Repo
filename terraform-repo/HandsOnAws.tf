provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "master" {
  key_name      = "Puppet_oregon"
  ami           = "ami-aa5ebdd2"
  instance_type = "t2.micro"
  subnet_id     = "${aws_subnet.test_subnet.id}"
}

resource "aws_instance" "slave" {
  key_name      = "Puppet_oregon"
  ami           = "ami-aa5ebdd2"
  instance_type = "t2.micro"
  subnet_id     = "${aws_subnet.test_subnet.id}"
  depends_on    = ["aws_instance.master"]
 
  lifecycle{
      ignore_changes=["tags"]
  }
}

#tags {
#    Name = "test Instance"
#  }
#}

resource "aws_vpc" "testVpc" {
  cidr_block = "10.3.0.0/16"
}

resource "aws_subnet" "test_subnet" {
  vpc_id     = "${aws_vpc.testVpc.id}"
  cidr_block = "10.3.1.0/24"
}
