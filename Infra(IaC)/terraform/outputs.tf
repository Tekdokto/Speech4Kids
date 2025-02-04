**`terraform/outputs.tf`**
```hcl```
output "vpc_id" {
  description = "VPC ID"
  value       = module.network.vpc_id
}

output "private_subnets" {
  description = "List of private subnets"
  value       = module.network.private_subnets
}

output "public_subnets" {
  description = "List of public subnets"
  value       = module.network.public_subnets
}

output "ecs_cluster_name" {
  description = "ECS Cluster Name"
  value       = module.ecs.cluster_name
}
