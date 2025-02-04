### READMEs

#### GitHub Actions: `ci_cd/github_actions/README.md`

```markdown
# GitHub Actions CI/CD Workflow

This workflow automates the build, test, and deployment process.

### Key Features
- Runs on `push` and `pull_request` to the `main` branch.
- Tests the application using `pytest`.
- Deploys to staging if tests pass.

### Usage
1. Place the `workflow.yml` in `.github/workflows/`.
2. Push changes to trigger the workflow.
```

#### CircleCI: `ci_cd/circleci/README.md`

```markdown
# CircleCI CI/CD Pipeline

This configuration defines the build and test process using CircleCI.

### Key Features
- Runs tests using `pytest` in a Docker container.
- Stores test results as artifacts.

### Usage
1. Place the `config.yml` in `.circleci/`.
2. Commit and push changes to trigger the pipeline.
```

#### Jenkins: `ci_cd/jenkins/README.md`

```markdown
# Jenkins CI/CD Pipeline

This `Jenkinsfile` defines a pipeline for building, testing, and deploying the application.

### Key Features
- Executes stages for checkout, dependency installation, testing, and deployment.
- Publishes test results to Jenkins.

### Usage
1. Create a new Jenkins pipeline job.
2. Point the job to the repository containing this `Jenkinsfile`.
```

---