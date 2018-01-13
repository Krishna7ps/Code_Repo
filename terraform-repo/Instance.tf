/*
#variable "welcomeNote"{
#    description     = "thsi is the test of terraform"
#}
provider "aws"{
#    access_key  = $AWS_
#    secret_key  = ""
    region      = "us-west-2"
#   region      = "us-east-1"
#   description     = "This is test EC2 from terraform"
}

resource "aws_instance" "terraform_instance"{
    
 #     description     = "This is test EC2 from terraform"
    ami             = "ami-80861296"
    instance_type   = "t2.micro"
    key_name        = "Puppet_oregon.pem"  
#    security_groups = ["xyz"]

    tags = {
        identity    =   "...."
        client         =   "posti"        
    }


}

output "Public_ip"{
   value = "${aws_instance.terraform_instance.public_ip}"
}


output "private_ip"{
    value = ["${aws_instance.terraform_instance.private_ip}", "${aws_instance.terraform_instance.public_ip}"]
}







*/

