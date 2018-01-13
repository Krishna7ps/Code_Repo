/*
*/
provider "aws" {
  region = "${var.region}"
}



module "source_module" {
  source      = "./modules/application"
#  environment = "${var.environment}"
}


