**`kubernetes/README.md`**
```markdown
# Kubernetes Configuration for Speech4Kids

This directory contains Kubernetes manifests and Helm charts for deploying Speech4Kids services.

### Usage
1. Apply manifests:
   ```bash
   kubectl apply -f manifests/
   ```

2. Use Helm for advanced deployments:
   ```bash
   helm install speech4kids ./helm/speech4kids
   ```

3. Verify the services are running:
   ```bash
   kubectl get all
   ```
```