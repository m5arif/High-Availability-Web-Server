# main.tf
module "vpc" {
  source = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
}

module "web_server" {
  source = "./modules/ec2"
  subnet_id = module.vpc.public_subnet_id
  instance_type = "t3.micro"
  
  # User data to install Nginx automatically (Self-healing concept)
  user_data = <<-EOF
              #!/bin/bash
              yum install -y nginx
              systemctl start nginx
              EOF
}
