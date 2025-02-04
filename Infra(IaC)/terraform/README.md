**`terraform/README.md`**
```markdown
# Terraform Configuration for Speech4Kids Infrastructure

This directory contains Terraform configurations to provision the necessary AWS infrastructure for Speech4Kids.

### Features
- VPC with public and private subnets
- ECS Cluster for microservices
- NAT Gateway for internet connectivity in private subnets

### Usage
1. Initialize Terraform:
   ```bash
   terraform init
   ```

2. Apply the configuration:
   ```bash
   terraform apply -var-file="variables.tfvars"
   ```

3. Review the outputs to get resource details.
```
