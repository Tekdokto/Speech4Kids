**`terraform/variables.tf`**
```hcl```
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "private_subnets" {
  description = "Private subnets for the application"
  type        = list(string)
}

variable "public_subnets" {
  description = "Public subnets for NAT gateways"
  type        = list(string)
}