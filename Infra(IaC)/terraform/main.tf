**`terraform/main.tf`**
```hcl```
provider "aws" {
  region = var.region
}

module "network" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.2"

  name            = "speech4kids-vpc"
  cidr            = var.vpc_cidr
  azs             = var.availability_zones
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets

  enable_nat_gateway = true
  tags = {
    Project = "Speech4Kids"
  }
}

module "ecs" {
  source  = "terraform-aws-modules/ecs/aws"
  version = "1.4.0"

  cluster_name = "speech4kids-cluster"
  vpc_id       = module.network.vpc_id
  subnets      = module.network.private_subnets

  tags = {
    Project = "Speech4Kids"
  }
}
