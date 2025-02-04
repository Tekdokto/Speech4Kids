# Contents of `usage_guides/deployment.md`

## Deployment Guide

### Prerequisites
1. Kubernetes cluster (e.g., GKE, EKS, or AKS).
2. Helm installed locally.
3. CI/CD tool configured (e.g., GitHub Actions).

### Steps

#### Step 1: Build Docker Images
```bash
docker build -t speech4kids/gateway:latest ./gateway
```

#### Step 2: Push to Container Registry
```bash
docker tag speech4kids/gateway:latest gcr.io/your-project-id/speech4kids/gateway:latest
docker push gcr.io/your-project-id/speech4kids/gateway:latest
```

#### Step 3: Deploy Using Helm
```bash
helm install speech4kids ./infra/kubernetes/helm/speech4kids -f ./infra/kubernetes/helm/speech4kids/values.yaml
```

---