
# Contents of `usage_guides/setup.md`

## Setup Guide

### Prerequisites
1. Install Docker and Docker Compose.
2. Ensure Python 3.9+ is installed.
3. Install Kubernetes (kubectl) and Helm for deployment.

### Local Development

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-org/speech4kids.git
cd speech4kids
```

#### Step 2: Set Up Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### Step 3: Run Docker Compose
```bash
docker-compose up --build
```

---