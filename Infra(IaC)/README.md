# Infrastructure as Code (IaC) for Speech4Kids

This directory contains all the configuration files and automation scripts needed to provision and manage the infrastructure for the Speech4Kids application.

## Directory Structure

```plaintext
infra/                        # Infrastructure as Code (IaC)
├── terraform/                # Terraform for provisioning cloud infrastructure
│   ├── main.tf               # Main configuration file
│   ├── variables.tf          # Input variables for Terraform
│   ├── outputs.tf            # Outputs from Terraform modules
│
├── ansible/                  # Ansible for configuration management and deployment
│   └── playbooks/
│       └── deploy.yml        # Playbook for deploying application services
│
├── kubernetes/               # Kubernetes manifests and Helm charts
│   ├── manifests/            # Kubernetes YAML files for direct deployment
│   │   ├── gateway-deployment.yml  # Deployment for gateway service
│   │   └── gateway-service.yml     # Service for gateway deployment
│   └── helm/                 # Helm charts for managing Kubernetes deployments
│       └── speech4kids/
│           ├── values.yaml   # Default configuration values
│           └── templates/    # Templated Kubernetes YAML files
│               ├── deployment.yaml
│               └── service.yaml
```

## Components Overview

### Terraform
Terraform is used to provision cloud resources for the Speech4Kids application. This includes VPCs, subnets, load balancers, and other required infrastructure.

#### Files:
- `main.tf`: Defines the resources to be created.
- `variables.tf`: Contains input variables for flexible configurations.
- `outputs.tf`: Exports key resource attributes for integration with other systems.

#### Usage:
```bash
# Initialize Terraform
terraform init

# Plan the infrastructure changes
terraform plan -var-file="path/to/variables.tfvars"

# Apply the changes
terraform apply -var-file="path/to/variables.tfvars"
```

### Ansible
Ansible is used for provisioning and configuring servers, installing dependencies, and deploying application services.

#### Files:
- `playbooks/deploy.yml`: Automates the deployment of Docker and application containers.

#### Usage:
```bash
# Run the Ansible playbook
ansible-playbook -i inventory playbooks/deploy.yml
```

### Kubernetes
Kubernetes manages container orchestration for Speech4Kids services.

#### Files:
- `manifests/`: Contains YAML files for deploying the gateway service.
- `helm/`: Helm charts for templated and scalable deployments.

#### Usage:
```bash
# Apply Kubernetes manifests directly
kubectl apply -f kubernetes/manifests/

# Use Helm to deploy
helm install speech4kids kubernetes/helm/speech4kids
```

## Deployment Workflow
1. Use **Terraform** to provision the required cloud infrastructure.
2. Use **Ansible** to configure servers and deploy application services.
3. Use **Kubernetes** (with or without Helm) for container orchestration.

## Future Enhancements
- Add CI/CD pipelines for automated deployments.
- Integrate monitoring tools (e.g., Prometheus, Grafana).
- Add secret management using tools like HashiCorp Vault or AWS Secrets Manager.

---

For detailed documentation on each component, see the respective `README.md` files within each subdirectory.
