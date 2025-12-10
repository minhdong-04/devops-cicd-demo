# 🔄 CI/CD Guide - Hướng Dẫn CI/CD Chi Tiết

> Tài liệu này giải thích chi tiết về CI/CD và GitHub Actions trong project DevOps CI/CD Demo

---

## 📑 Mục Lục

- [CI/CD là gì?](#cicd-là-gì)
- [GitHub Actions Overview](#github-actions-overview)
- [Workflow Chi Tiết](#workflow-chi-tiết)
- [Setup Guide](#setup-guide)
- [Best Practices](#best-practices)
- [Monitoring & Debugging](#monitoring--debugging)
- [Advanced Topics](#advanced-topics)

---

## 🔄 CI/CD là gì? 

### Continuous Integration (CI)

**Định nghĩa**: Thực hành tích hợp code thường xuyên vào repository chung, tự động test và build. 

```
Developer 1 ──┐
Developer 2 ──┼──→ Git Push ──→ Auto Test ──→ Auto Build ──→ Feedback
Developer 3 ──┘
```

**Quy trình CI**:
1. Developer commit code lên branch
2. Trigger automated tests
3. Run linters, formatters
4. Build application
5. Report results (pass/fail)

**Lợi ích**:
- ✅ Phát hiện bugs sớm
- ✅ Giảm integration conflicts
- ✅ Tăng chất lượng code
- ✅ Faster feedback loop

---

### Continuous Delivery (CD)

**Định nghĩa**:  Code luôn trong trạng thái sẵn sàng deploy, nhưng cần approval thủ công.

```
CI Pass ──→ Deploy to Staging ──→ Manual Approval ──→ Deploy to Production
```

---

### Continuous Deployment (CD)

**Định nghĩa**:  Tự động deploy lên production sau khi pass tất cả tests.

```
CI Pass ──→ Auto Deploy Staging ──→ Auto Tests ──→ Auto Deploy Production
```

**Sự khác biệt**: 
```
Continuous Delivery    :  CI → Staging → [MANUAL] → Production
Continuous Deployment  : CI → Staging → [AUTO]   → Production
```

---

## 🎯 GitHub Actions Overview

### GitHub Actions là gì?

GitHub Actions là CI/CD platform tích hợp sẵn trong GitHub, cho phép:
- 🔄 Tự động hóa workflows
- 🧪 Run tests
- 🐳 Build Docker images
- 🚀 Deploy applications
- 📊 Generate reports

### Core Concepts

#### 1. **Workflow**
```yaml
name: CI/CD Pipeline  # Tên workflow

on:                   # Events trigger workflow
  push:
  pull_request: 

jobs:                 # Các jobs cần chạy
  test:
    runs-on: ubuntu-latest
    steps:
      - ... 
```

#### 2. **Events** (Triggers)
```yaml
on:
  push:                     # Khi push code
    branches: [main]
  pull_request:             # Khi tạo PR
  schedule:                # Chạy theo lịch
    - cron: '0 0 * * *'
  workflow_dispatch:       # Trigger thủ công
```

#### 3. **Jobs**
```yaml
jobs:
  test:                    # Job name
    runs-on: ubuntu-latest # Runner OS
    steps:                 # Các bước thực hiện
      - uses:  actions/checkout@v4
      - run: npm test
```

#### 4. **Steps**
```yaml
steps:
  - name: Checkout code          # Step name
    uses: actions/checkout@v4    # Dùng action có sẵn
  
  - name: Run tests
    run: pytest test_app.py      # Chạy command
```

#### 5. **Runners**
- **GitHub-hosted**: Ubuntu, Windows, macOS
- **Self-hosted**:  Tự setup server

#### 6. **Actions**
- Reusable units of code
- Từ Marketplace hoặc tự viết
- Example: `actions/checkout@v4`, `docker/build-push-action@v5`

---

## 📝 Workflow Chi Tiết

### Project Workflow Architecture

```yaml
Trigger (Push/PR)
    │
    ▼
┌─────────────────────────────────────────┐
│           GITHUB ACTIONS                │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────────────────────────────┐  │
│  │   JOB 1: TEST                    │  │
│  │   - Checkout code                │  │
│  │   - Setup Python 3.11            │  │
│  │   - Install dependencies         │  │
│  │   - Run pytest + coverage        │  │
│  │   - Upload coverage report       │  │
│  └──────────────┬───────────────────┘  │
│                 │ (success)             │
│                 ▼                       │
│  ┌──────────────────────────────────┐  │
│  │   JOB 2: BUILD                   │  │
│  │   - Setup Docker Buildx          │  │
│  │   - Login to Docker Hub          │  │
│  │   - Build multi-stage image     │  │
│  │   - Tag with SHA + latest        │  │
│  │   - Push to Docker Hub           │  │
│  └──────────────┬───────────────────┘  │
│                 │ (success + main)      │
│                 ▼                       │
│  ┌──────────────────────────────────┐  │
│  │   JOB 3: DEPLOY                  │  │
│  │   - Pull latest image            │  │
│  │   - Deploy to production         │  │
│  │   - Health check                 │  │
│  │   - Comment on commit            │  │
│  └──────────────────────────────────┘  │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │   JOB 4: SECURITY (parallel)     │  │
│  │   - Run Trivy scanner            │  │
│  │   - Scan vulnerabilities         │  │
│  │   - Upload to Security tab       │  │
│  └──────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

---

### Job 1: Test - Giải Thích Chi Tiết

```yaml
test:
  name: 🧪 Run Tests
  runs-on: ubuntu-latest
  # Chạy trên Ubuntu runner (GitHub-hosted)
  
  steps:
  - name: 📥 Checkout code
    uses: actions/checkout@v4
    # Clone repository vào runner
    # @v4 = version 4 của action
  
  - name: 🐍 Set up Python
    uses: actions/setup-python@v4
    with:
      python-version: ${{ env.PYTHON_VERSION }}
      cache: 'pip'
    # Install Python 3.11
    # cache: 'pip' → cache pip packages để build nhanh
  
  - name: 📦 Install dependencies
    run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    # Chạy shell commands
    # | = multi-line string
  
  - name: 🧪 Run tests with pytest
    run: |
      pytest test_app.py -v \
        --cov=app \
        --cov-report=term-missing \
        --cov-report=xml
    # -v = verbose
    # --cov = coverage
    # --cov-report=xml → để upload lên codecov
  
  - name: 📊 Upload coverage reports
    uses: codecov/codecov-action@v3
    with:
      file: ./coverage.xml
      flags: unittests
      name: codecov-umbrella
      fail_ci_if_error:  false
    # Upload coverage lên codecov. io
    # fail_ci_if_error: false → không fail job nếu upload lỗi
  
  - name: ✅ Test Summary
    if: always()
    run: |
      echo "### 🧪 Test Results" >> $GITHUB_STEP_SUMMARY
      echo "✅ Tests completed successfully!" >> $GITHUB_STEP_SUMMARY
    # if: always() → chạy dù job pass hay fail
    # $GITHUB_STEP_SUMMARY → hiển thị summary trong GitHub UI
```

**Output Example**:
```
🧪 Run Tests
  ✓ Checkout code (1s)
  ✓ Set up Python (3s)
  ✓ Install dependencies (12s)
  ✓ Run tests with pytest (5s)
    ======================== test session starts ========================
    test_app.py::test_index_page PASSED                          [ 14%]
    test_app. py::test_health_endpoint PASSED                     [ 28%]
    ... 
    ======================== 7 passed in 0.23s =======================
  ✓ Upload coverage reports (2s)
  ✓ Test Summary (0s)

Total time: 23s
```

---

### Job 2: Build - Giải Thích Chi Tiết

```yaml
build:
  name: 🐳 Build Docker Image
  runs-on: ubuntu-latest
  needs: test
  # needs: test → chỉ chạy khi test job success
  if: github.event_name == 'push'
  # Chỉ build khi push (không build cho PR)
  
  steps:
  - name: 📥 Checkout code
    uses:  actions/checkout@v4
  
  - name: 🔧 Set up Docker Buildx
    uses: docker/setup-buildx-action@v3
    # Buildx = Docker CLI plugin để build advanced
    # Hỗ trợ:  multi-platform, caching, ... 
  
  - name: 🔑 Login to Docker Hub
    uses: docker/login-action@v3
    with:
      username: ${{ secrets.DOCKER_USERNAME }}
      password: ${{ secrets.DOCKER_PASSWORD }}
    # Login để push image
    # secrets = environment variables được mã hóa
  
  - name: 🏷️ Extract metadata
    id: meta
    uses: docker/metadata-action@v5
    with:
      images: ${{ env.DOCKER_IMAGE }}
      tags: |
        type=ref,event=branch
        type=sha,prefix={{branch}}-
        type=raw,value=latest,enable={{is_default_branch}}
    # Tự động generate tags: 
    # - main (branch name)
    # - main-abc1234 (branch-sha)
    # - latest (nếu là main branch)
  
  - name: 🐳 Build and push Docker image
    uses: docker/build-push-action@v5
    with:
      context: . 
      push: true
      tags: ${{ steps.meta.outputs.tags }}
      labels: ${{ steps. meta.outputs.labels }}
      cache-from: type=registry,ref=${{ env.DOCKER_IMAGE }}:buildcache
      cache-to: type=registry,ref=${{ env.DOCKER_IMAGE }}:buildcache,mode=max
    # context: .  → build từ root directory
    # push:  true → push lên Docker Hub sau khi build
    # cache → lưu layers để build lần sau nhanh hơn
  
  - name: 📝 Build Summary
    run: |
      echo "### 🐳 Docker Build Results" >> $GITHUB_STEP_SUMMARY
      echo "✅ Image built and pushed successfully!" >> $GITHUB_STEP_SUMMARY
      echo "**Tags:**" >> $GITHUB_STEP_SUMMARY
      echo "${{ steps.meta.outputs.tags }}" >> $GITHUB_STEP_SUMMARY
    # Hiển thị summary với các tags đã build
```

**Output Example**:
```
🐳 Build Docker Image
  ✓ Checkout code (1s)
  ✓ Set up Docker Buildx (2s)
  ✓ Login to Docker Hub (1s)
  ✓ Extract metadata (0s)
  ✓ Build and push Docker image (45s)
    #1 [internal] load build definition
    #2 [internal] load .dockerignore
    #3 [stage-0 1/4] FROM python:3.11-slim
    #4 [stage-0 2/4] WORKDIR /app
    #5 [stage-0 3/4] COPY requirements.txt .
    #6 [stage-0 4/4] RUN pip install... 
    #7 [stage-1 1/5] FROM python:3.11-alpine
    ... 
    Successfully tagged myuser/devops-cicd-demo:latest
    Successfully tagged myuser/devops-cicd-demo:main
    Successfully tagged myuser/devops-cicd-demo:main-abc1234
  ✓ Build Summary (0s)

Total time: 49s
```

---

### Job 3: Deploy - Giải Thích Chi Tiết

```yaml
deploy:
  name: 🚀 Deploy Application
  runs-on: ubuntu-latest
  needs: build
  # Chỉ chạy sau khi build success
  if: github.ref == 'refs/heads/main'
  # Chỉ deploy khi push vào main branch
  
  steps:
  - name: 📥 Checkout code
    uses: actions/checkout@v4
  
  - name: 🚀 Deploy to Production (Simulation)
    run: |
      echo "🎯 Deploying to production environment..."
      echo "📦 Pulling latest Docker image..."
      # docker pull ${{ env.DOCKER_IMAGE }}:latest
      # docker stop myapp || true
      # docker rm myapp || true
      # docker run -d -p 80:5000 --name myapp ${{ env. DOCKER_IMAGE }}:latest
      echo "✅ Deployment completed successfully!"
    # Đây là simulation
    # Thực tế:  SSH vào server, pull image, restart container
    # Hoặc dùng:  AWS ECS, Kubernetes, etc. 
  
  - name: 💬 Comment on commit
    uses: actions/github-script@v7
    with:
      script: |
        github.rest.repos.createCommitComment({
          owner: context.repo.owner,
          repo: context.repo.repo,
          commit_sha: context.sha,
          body: '🚀 **Deployment Status**: Successfully deployed to production!\n\n✅ All CI/CD stages passed.'
        })
    # Tự động comment lên commit với deployment status
    # github-script = chạy JavaScript code với GitHub API
  
  - name: 📝 Deployment Summary
    run: |
      echo "### 🚀 Deployment Results" >> $GITHUB_STEP_SUMMARY
      echo "✅ Application deployed successfully!" >> $GITHUB_STEP_SUMMARY
      echo "**Environment:** Production" >> $GITHUB_STEP_SUMMARY
      echo "**Image:** ${{ env.DOCKER_IMAGE }}:latest" >> $GITHUB_STEP_SUMMARY
      echo "**Commit:** ${{ github.sha }}" >> $GITHUB_STEP_SUMMARY
```

---

### Job 4: Security - Giải Thích Chi Tiết

```yaml
security:
  name: 🔒 Security Scan
  runs-on:  ubuntu-latest
  needs: test
  # Chạy parallel với build job
  
  steps:
  - name: 📥 Checkout code
    uses: actions/checkout@v4
  
  - name: 🔍 Run Trivy vulnerability scanner
    uses: aquasecurity/trivy-action@master
    with:
      scan-type: 'fs'
      # fs = filesystem scan
      # Scan:  dependencies, source code
      scan-ref: '.'
      format: 'sarif'
      # SARIF = Static Analysis Results Interchange Format
      # Format để upload lên GitHub Security
      output: 'trivy-results.sarif'
  
  - name: 📤 Upload Trivy results to GitHub Security
    uses: github/codeql-action/upload-sarif@v2
    if: always()
    with:
      sarif_file: 'trivy-results.sarif'
    # Upload lên Security tab trong GitHub repo
    # Có thể xem vulnerabilities trong UI
```

**Output Example**:
```
🔒 Security Scan
  ✓ Checkout code (1s)
  ✓ Run Trivy vulnerability scanner (15s)
    2023-12-09T10:30:00.000Z	INFO	Vulnerability scanning is enabled
    2023-12-09T10:30:00.000Z	INFO	Detected OS: alpine
    2023-12-09T10:30:02.000Z	INFO	Detecting Alpine vulnerabilities...
    
    Total: 3 (UNKNOWN: 0, LOW: 1, MEDIUM: 2, HIGH: 0, CRITICAL: 0)
  ✓ Upload Trivy results to GitHub Security (2s)

Total time: 18s
```

---

## 🛠️ Setup Guide

### Bước 1: Tạo GitHub Repository

```bash
# Local
git init
git add .
git commit -m "Initial commit"

# GitHub
# Tạo repo trên github.com
git remote add origin https://github.com/minhdong-04/devops-cicd-demo.git
git push -u origin main
```

---

### Bước 2: Setup GitHub Secrets

**Đi tới**:  Repository → Settings → Secrets and variables → Actions → New repository secret

Cần setup:
```
DOCKER_USERNAME    # Docker Hub username
DOCKER_PASSWORD    # Docker Hub password hoặc access token
```

**Cách lấy Docker Hub token**:
1. Login vào hub.docker.com
2. Account Settings → Security → New Access Token
3. Copy token
4. Paste vào GitHub Secret

---

### Bước 3: Tạo Workflow File

```bash
mkdir -p .github/workflows
touch .github/workflows/ci-cd.yml
```

Copy nội dung workflow đã cung cấp vào file. 

---

### Bước 4: Push và Test

```bash
git add .github/workflows/ci-cd.yml
git commit -m "Add CI/CD pipeline"
git push origin main
```

**Kiểm tra**:
- Đi tới:  Repository → Actions tab
- Xem workflow đang chạy
- Click vào workflow để xem details

---

### Bước 5: Monitor Results

```
Actions tab
  ├─ CI/CD Pipeline
      ├─ Test ✅ (23s)
      ├─ Build ✅ (49s)
      ├─ Deploy ✅ (8s)
      └─ Security ✅ (18s)

Total time: ~2 minutes
```

---

## 🏆 Best Practices

### 1. **Job Dependencies**

```yaml
# ✅ Good:  Sequential với dependencies
jobs:
  test:
    runs-on: ubuntu-latest
  
  build:
    needs: test          # Chờ test pass
    runs-on: ubuntu-latest
  
  deploy:
    needs:  build         # Chờ build pass
    runs-on: ubuntu-latest

# ✅ Good: Parallel jobs
jobs:
  test: 
    runs-on: ubuntu-latest
  
  lint:
    runs-on: ubuntu-latest  # Chạy song song với test
  
  security:
    needs: [test, lint]     # Chờ cả 2 pass
```

---

### 2. **Caching**

```yaml
# ✅ Cache pip packages
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version:  '3.11'
    cache: 'pip'

# ✅ Cache Docker layers
- name: Build and push
  uses: docker/build-push-action@v5
  with:
    cache-from: type=registry,ref=myimage:buildcache
    cache-to: type=registry,ref=myimage:buildcache
```

**Lợi ích**: Build nhanh hơn 3-5x

---

### 3. **Secrets Management**

```yaml
# ❌ Don't:  Hardcode secrets
- name:  Deploy
  run: |
    docker login -u myuser -p mypassword123

# ✅ Do: Use GitHub Secrets
- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets. DOCKER_PASSWORD }}
```

---

### 4. **Conditional Execution**

```yaml
# Deploy chỉ khi: 
# - Build success
# - Branch = main
# - Event = push (không phải PR)
deploy:
  needs: build
  if: |
    github.ref == 'refs/heads/main' &&
    github.event_name == 'push'
  steps:
    - ... 
```

---

### 5. **Matrix Builds**

```yaml
# Test trên nhiều versions
test:
  strategy: 
    matrix:
      python-version: [3.9, 3.10, 3.11]
      os: [ubuntu-latest, windows-latest]
  runs-on: ${{ matrix.os }}
  steps:
    - uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
```

**Result**: 6 jobs (3 Python × 2 OS)

---

### 6. **Artifacts**

```yaml
# Upload test results
- name: Upload test results
  uses: actions/upload-artifact@v3
  with:
    name: test-results
    path: test-reports/

# Download trong job khác
- name: Download test results
  uses: actions/download-artifact@v3
  with:
    name: test-results
```

---

### 7. **Notifications**

```yaml
# Slack notification
- name:  Slack Notification
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: 'Deployment completed!'
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
  if: always()
```

---

## 🔍 Monitoring & Debugging

### 1. **Xem Logs**

```
Actions tab → Workflow run → Job → Step
```

Mỗi step hiển thị:
- ✅/❌ Status
- ⏱️ Duration
- 📝 Logs chi tiết

---

### 2. **Re-run Jobs**

```
Actions tab → Workflow run → Re-run all jobs
```

Options:
- Re-run failed jobs only
- Re-run all jobs
- Enable debug logging

---

### 3. **Debug Mode**

Enable debug logs: 

**Repository Secrets**:
```
ACTIONS_RUNNER_DEBUG = true
ACTIONS_STEP_DEBUG = true
```

**Output**:
```
##[debug]Evaluating condition for step: 'Run tests'
##[debug]Evaluating:  success()
##[debug]Evaluating success: 
##[debug]=> true
##[debug]Result: true
```

---

### 4. **SSH Debugging**

```yaml
# Debug bằng SSH
- name: Setup tmate session
  uses: mxschmitt/action-tmate@v3
  if: failure()
```

Khi job fail → tạo SSH session → debug trực tiếp trên runner

---

### 5. **Status Checks**

```yaml
# Require status checks trước khi merge PR
# Settings → Branches → Branch protection rules
# ✓ Require status checks to pass before merging
#   ✓ test
#   ✓ build
```

---

## 🚀 Advanced Topics

### 1. **Reusable Workflows**

```yaml
# . github/workflows/reusable-test.yml
name: Reusable Test Workflow

on:
  workflow_call:
    inputs: 
      python-version:
        required: true
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses:  actions/setup-python@v4
        with:
          python-version: ${{ inputs.python-version }}
      - run: pytest

# . github/workflows/main.yml
jobs:
  test-39:
    uses: ./.github/workflows/reusable-test.yml
    with:
      python-version:  '3.9'
  
  test-311:
    uses: ./.github/workflows/reusable-test.yml
    with:
      python-version: '3.11'
```

---

### 2. **Composite Actions**

```yaml
# .github/actions/setup-app/action.yml
name: 'Setup Application'
description: 'Setup Python and install dependencies'

runs:
  using: 'composite'
  steps:
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - run: pip install -r requirements.txt
      shell: bash

# Usage
jobs:
  test:
    steps:
      - uses: . /.github/actions/setup-app
```

---

### 3. **Dynamic Matrix**

```yaml
jobs:
  setup:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run:  echo "::set-output name=matrix::{\"version\":[\"3.9\",\"3.11\"]}"
  
  test:
    needs: setup
    strategy:
      matrix:  ${{fromJson(needs.setup.outputs.matrix)}}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testing Python ${{ matrix.version }}"
```

---

### 4. **Environment Protection**

```yaml
jobs:
  deploy-production:
    runs-on:  ubuntu-latest
    environment: 
      name: production
      url: https://myapp.com
    steps:
      - run: echo "Deploying to production"
```

**Settings → Environments → production**: 
- ✓ Required reviewers (phê duyệt thủ công)
- ✓ Wait timer (đợi X phút)
- ✓ Deployment branches (chỉ main)

---

### 5. **Self-Hosted Runners**

```bash
# Setup self-hosted runner
# Settings → Actions → Runners → New self-hosted runner

# Download và setup
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux. tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
tar xzf ./actions-runner-linux.tar. gz
./config.sh --url https://github.com/minhdong-04/devops-cicd-demo --token YOUR_TOKEN
./run.sh
```

**Usage**:
```yaml
jobs:
  build:
    runs-on: self-hosted  # Thay vì ubuntu-latest
```

---

## 📊 Metrics & Analytics

### Workflow Insights

**Actions tab → Insights**:
- Success rate
- Average duration
- Job success rate
- Runner usage

### Example Metrics: 
```
CI/CD Pipeline
├─ Success rate: 95%
├─ Average duration: 2m 15s
├─ Runs last 7 days: 42
└─ Top failing job: deploy (3 failures)
```

---

## 📚 Resources

### Official Documentation
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Actions Marketplace](https://github.com/marketplace? type=actions)

### Best Practices
- [GitHub Actions Best Practices](https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions)
- [CI/CD Best Practices](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)

### Tools
- [Act](https://github.com/nektos/act) - Run GitHub Actions locally
- [Actionlint](https://github.com/rhysd/actionlint) - Lint workflow files

---

## 🎯 Summary

### CI/CD trong Project: 

```
Push code
    ↓
[TEST] → pytest, coverage (23s)
    ↓
[BUILD] → Docker multi-stage (49s)
    ↓
[DEPLOY] → Production (8s)
    ↓
[SECURITY] → Trivy scan (18s) [parallel]
    ↓
✅ Done (Total: ~2 minutes)
```

### Key Takeaways: 

- ✅ CI/CD tự động hóa quy trình từ code đến production
- ✅ GitHub Actions dễ setup và powerful
- ✅ Secrets management cho security
- ✅ Caching để tăng tốc builds
- ✅ Conditional execution để control workflow
- ✅ Monitoring và debugging tools

---

**[⬆ Back to top](#-cicd-guide---hướng-dẫn-cicd-chi-tiết)**