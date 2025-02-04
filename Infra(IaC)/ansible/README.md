**`ansible/README.md`**
```markdown
# Ansible Playbooks for Speech4Kids

This directory contains Ansible playbooks to configure and deploy Speech4Kids services.

### Features
- Installs Docker on target machines
- Pulls service images from a registry
- Deploys services as Docker containers

### Usage
1. Run the playbook:
   ```bash
   ansible-playbook -i inventory deploy.yml
   ```

2. Ensure all services are running using `docker ps`.
```