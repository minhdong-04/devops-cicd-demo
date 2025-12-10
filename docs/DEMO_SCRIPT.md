# 🎬 Demo Script - Hướng Dẫn Demo Chi Tiết

> Script chi tiết để demo project DevOps & CI/CD trước lớp
> 
> **Thời gian**:  15-20 phút
> **Chuẩn bị**:  Mở sẵn các tabs/terminals trước khi demo

---

## 📋 Checklist Chuẩn Bị

### Trước Khi Demo (5 phút trước)

```
☐ Laptop đã sạc đầy, có backup charger
☐ Internet connection ổn định (test trước)
☐ Mở sẵn các tabs: 
  ☐ GitHub repository
  ☐ GitHub Actions
  ☐ Docker Hub
  ☐ Localhost: 5000 (app đang chạy)
☐ Terminal/IDE đã mở
☐ Presentation slides sẵn sàng
☐ Backup:  Screenshots/Video nếu demo fail
☐ Clicker hoặc mouse wireless (nếu có)
```

### Tabs Cần Mở Sẵn

```
Browser Tab 1: GitHub Repo
https://github.com/minhdong-04/devops-cicd-demo

Browser Tab 2: GitHub Actions
https://github.com/minhdong-04/devops-cicd-demo/actions

Browser Tab 3: Docker Hub
https://hub.docker.com/r/[username]/devops-cicd-demo

Browser Tab 4: Application
http://localhost:5000

Browser Tab 5: Presentation
(Google Slides/PowerPoint)

Terminal 1: Project directory
cd ~/devops-cicd-demo

Terminal 2: Docker commands
(Sẵn sàng run docker commands)
```

---

## 🎯 Demo Flow Overview

```
┌─────────────────────────────────────────────────┐
│ Part 1: Introduction (2 min)                   │
├─────────────────────────────────────────────────┤
│ Part 2: Application Demo (3 min)               │
├─────────────────────────────────────────────────┤
│ Part 3: Docker Demo (3 min)                    │
├─────────────────────────────────────────────────┤
│ Part 4: CI/CD Pipeline Demo (5 min)            │
├─────────────────────────────────────────────────┤
│ Part 5: Live Code Push (3 min)                 │
├─────────────────────────────────────────────────┤
│ Part 6: Wrap Up (2 min)                        │
└─────────────────────────────────────────────────┘

Total: ~18 minutes
```

---

## 📖 Part 1: Introduction (2 phút)

### Script: 

> "Xin chào thầy/cô và các bạn! 
> 
> Hôm nay nhóm em sẽ demo project **DevOps & CI/CD** với Python, Docker và GitHub Actions.
> 
> Project này minh họa **quy trình tự động hóa hoàn chỉnh** từ khi developer viết code, đến khi code được test, build thành Docker image, và cuối cùng deploy lên production.
> 
> Demo sẽ bao gồm:
> 1. ✅ Web application với Flask
> 2. ✅ Docker containerization
> 3. ✅ CI/CD pipeline với GitHub Actions
> 4. ✅ Live demo:  Push code và xem pipeline tự động chạy
> 
> Bắt đầu nào!"

---

## 📖 Part 2: Application Demo (3 phút)

### Step 1: Hiển thị Web Application

**Action**:  Switch sang tab `localhost:5000`

**Script**:
> "Đây là ứng dụng web của nhóm em, được viết bằng **Python Flask**. 
> 
> [Scroll trang chủ]
> 
> Giao diện được thiết kế với **Bootstrap 5**, có animations và responsive. 
> 
> Trang này giải thích các khái niệm:
> - DevOps là gì
> - CI/CD là gì
> - Quy trình pipeline của nhóm em"

**Pause 3 giây để audience nhìn UI**

---

### Step 2: Demo API Endpoints

**Action**: Click vào link `/api/health`

**Script**:
> "Application có 3 API endpoints:
> 
> Đầu tiên là **/api/health** - Health check endpoint"

**Expected Output**:
```json
{
  "status": "healthy",
  "timestamp": "2025-12-09T10:30:00",
  "version": "1.0.0"
}
```

**Script**:
> "Endpoint này dùng để monitoring.  Docker và load balancers sẽ check endpoint này để biết app có healthy không."

---

**Action**:  Quay lại trang chủ, click `/api/info`

**Script**:
> "Tiếp theo là **/api/info** - Thông tin về ứng dụng"

**Expected Output**:
```json
{
  "app_name": "DevOps CI/CD Demo",
  "version": "1.0.0",
  "environment": "development",
  "python_version": "3.11",
  "framework": "Flask",
  "features": [
    "CI/CD Pipeline với GitHub Actions",
    "Docker Containerization",
    "Automated Testing",
    "Health Monitoring"
  ]
}
```

---

**Action**: Click `/api/pipeline`

**Script**:
> "Cuối cùng là **/api/pipeline** - Mô tả các stages trong CI/CD pipeline"

**Expected Output**:
```json
{
  "stages": [
    {
      "name": "Test",
      "description": "Chạy unit tests và coverage",
      "tools": ["pytest", "pytest-cov"]
    },
    {
      "name": "Build",
      "description": "Build Docker image",
      "tools":  ["Docker", "docker-compose"]
    },
    {
      "name": "Deploy",
      "description": "Deploy lên production",
      "tools":  ["GitHub Actions", "Docker Hub"]
    }
  ]
}
```

**Script**:
> "OK, vậy là em đã demo xong phần application. Giờ chúng ta xem cách app này được containerize với Docker."

---

## 📖 Part 3: Docker Demo (3 phút)

### Step 1: Show Dockerfile

**Action**: Switch sang Terminal/IDE, mở file `Dockerfile`

**Script**:
> "Nhóm em sử dụng **multi-stage build** trong Dockerfile. 
> 
> [Scroll through Dockerfile]
> 
> **Stage 1** - Builder: 
> - Base image: `python:3.11-slim`
> - Install tất cả dependencies
> - Build packages
> 
> **Stage 2** - Production:
> - Base image: `python:3.11-alpine` (cực kỳ nhỏ gọn)
> - Chỉ copy kết quả từ stage 1
> - Không copy build tools
> 
> Kết quả:  Image size chỉ **50MB**, giảm **95%** so với cách build thông thường!"

---

### Step 2: Docker Commands Demo

**Action**: Terminal 2

**Command 1: Build Image**
```bash
docker build -t devops-cicd-demo:latest .
```

**Script**:
> "Đây là lệnh build Docker image. 
> 
> [Chờ build...  hoặc đã build sẵn]
> 
> Quá trình build mất khoảng 30-45 giây."

**If already built**:
```bash
docker images | grep devops-cicd-demo
```

**Expected Output**:
```
devops-cicd-demo   latest   abc123def456   50MB
```

**Script**:
> "Như các bạn thấy, image chỉ 50MB, rất nhỏ gọn!"

---

**Command 2: Run Container**
```bash
docker ps
```

**Script**:
> "App đang chạy trong container Docker.  Lệnh `docker ps` hiển thị các containers đang chạy."

**Expected Output**:
```
CONTAINER ID   IMAGE                    STATUS        PORTS
abc123         devops-cicd-demo: latest  Up 10 mins    0.0.0.0:5000->5000/tcp
```

---

**Command 3: Docker Logs**
```bash
docker logs <container_id> --tail 10
```

**Expected Output**:
```
[2025-12-09 10:30:00] INFO:  Starting gunicorn 21.2.0
[2025-12-09 10:30:00] INFO:  Listening at:  http://0.0.0.0:5000
[2025-12-09 10:30:00] INFO: Using worker: sync
[2025-12-09 10:30:00] INFO: Booting worker with pid: 8
```

**Script**:
> "Logs cho thấy Gunicorn WSGI server đang chạy với 4 workers, production-ready!"

---

### Step 3: Docker Compose

**Action**: Show `docker-compose.yml`

```bash
cat docker-compose.yml
```

**Script**:
> "Nhóm em cũng setup **Docker Compose** để dễ dàng chạy local. 
> 
> Chỉ cần một lệnh: `docker-compose up` là app chạy ngay! 
> 
> File này define: 
> - Service configuration
> - Port mapping
> - Environment variables
> - Volume mounts cho development
> - Health checks"

---

## 📖 Part 4: CI/CD Pipeline Demo (5 phút)

### Step 1: Show GitHub Repository

**Action**: Switch sang Browser Tab 1 (GitHub Repo)

**Script**:
> "Đây là repository của nhóm em trên GitHub.
> 
> [Scroll files]
> 
> Cấu trúc project rất organized:
> - `app. py` - Flask application
> - `test_app.py` - Unit tests
> - `Dockerfile` - Docker configuration
> - `.github/workflows/` - CI/CD pipeline
> - `docs/` - Documentation
> 
> Tất cả documentation đều bằng **Tiếng Việt** để dễ hiểu!"

---

### Step 2: Show Workflow File

**Action**: Navigate to `.github/workflows/ci-cd.yml`

```
Click:  . github → workflows → ci-cd.yml
```

**Script**:
> "Đây là file workflow định nghĩa CI/CD pipeline.
> 
> [Scroll through file]
> 
> Pipeline có **4 jobs**:
> 
> 1. **Test Job**: Chạy pytest, check coverage
> 2. **Build Job**: Build Docker image, push lên Docker Hub
> 3. **Deploy Job**: Deploy lên production (nếu branch = main)
> 4. **Security Job**: Scan vulnerabilities với Trivy
> 
> Tất cả đều **tự động** khi push code!"

---

### Step 3: Show GitHub Actions

**Action**: Switch sang Browser Tab 2 (GitHub Actions)

**Script**:
> "Đây là GitHub Actions tab, nơi chúng ta xem các workflow runs.
> 
> [Click vào latest workflow run]
> 
> Workflow này chạy khi em push code lúc [time].
> 
> Xem chi tiết..."

**Action**: Click vào workflow run

**Expected View**:
```
✅ Test (23s)
✅ Build (49s)
✅ Deploy (8s)
✅ Security (18s)

Total: 2m 15s
```

---

### Step 4: Deep Dive vào Test Job

**Action**: Click vào "Test" job

**Script**:
> "Click vào Test job để xem chi tiết.
> 
> [Expand các steps]
> 
> Các bước: 
> 1. ✅ Checkout code
> 2. ✅ Setup Python 3.11
> 3. ✅ Install dependencies
> 4. ✅ Run pytest
> 
> [Click vào 'Run pytest' step]
> 
> Output cho thấy **7 tests passed**, coverage **95%+**!"

**Expected Output in logs**:
```
======================== test session starts ========================
test_app.py::test_index_page PASSED                          [ 14%]
test_app.py::test_health_endpoint PASSED                     [ 28%]
test_app.py:: test_info_endpoint PASSED                       [ 42%]
test_app.py::test_pipeline_endpoint PASSED                   [ 57%]
test_app.py::test_404_error PASSED                           [ 71%]
test_app.py::test_api_response_format PASSED                 [ 85%]

======================== 7 passed in 0.23s ==========================

---------- coverage: platform linux, python 3.11 -----------
Name      Stmts   Miss  Cover
-----------------------------
app.py       45      2    95%
-----------------------------
```

**Script**:
> "Perfect! All tests passed với high coverage!"

---

### Step 5: Deep Dive vào Build Job

**Action**: Back, click vào "Build" job

**Script**:
> "Build job thực hiện: 
> 
> [Expand steps]
> 
> 1. ✅ Setup Docker Buildx
> 2. ✅ Login to Docker Hub (với secrets)
> 3. ✅ Build multi-stage image
> 4. ✅ Tag với commit SHA và 'latest'
> 5. ✅ Push lên Docker Hub
> 
> [Click vào 'Build and push' step]
> 
> Output cho thấy image được build và push thành công!"

---

### Step 6: Show Docker Hub

**Action**: Switch sang Browser Tab 3 (Docker Hub)

**Script**:
> "Đây là Docker Hub - nơi lưu trữ images. 
> 
> [Show repository]
> 
> Repository của nhóm em có nhiều tags:
> - `latest` - Bản mới nhất
> - `main` - Từ main branch
> - `main-abc1234` - Với commit SHA
> 
> Tất cả đều được **tự động push** bởi CI/CD pipeline! 
> 
> [Click vào tag để show details]
> 
> Image size: **50.2 MB** - rất nhỏ gọn!"

---

## 📖 Part 5: Live Code Push (3 phút) ⭐ HIGHLIGHT

**Script**:
> "Bây giờ phần thú vị nhất - nhóm em sẽ **push code mới** và các bạn sẽ thấy **pipeline tự động chạy** real-time!"

---

### Step 1: Make Code Change

**Action**: Terminal 1, mở editor

```bash
code app.py
# Or:  vim app.py
```

**Script**:
> "Em sẽ thay đổi version number từ 1.0.0 lên 1.0.1"

**Action**: Edit line
```python
# Before
app.config['VERSION'] = '1.0.0'

# After
app.config['VERSION'] = '1.0.1'
```

**Script**:
> "Đây là một thay đổi nhỏ, nhưng sẽ trigger toàn bộ CI/CD pipeline!"

---

### Step 2: Git Commit & Push

**Action**: Terminal 1

```bash
git status
```

**Expected Output**:
```
On branch main
Changes not staged for commit:
  modified:   app.py
```

**Script**:
> "Git status cho thấy file app.py đã được modified."

---

```bash
git add app.py
git commit -m "Update version to 1.0.1"
```

**Expected Output**:
```
[main abc1234] Update version to 1.0.1
 1 file changed, 1 insertion(+), 1 deletion(-)
```

---

```bash
git push origin main
```

**Expected Output**:
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 315 bytes | 315.00 KiB/s, done. 
Total 3 (delta 2), reused 0 (delta 0)
To github.com:minhdong-04/devops-cicd-demo.git
   abc1234.. def5678  main -> main
```

**Script**:
> "Code đã được push lên GitHub!  
> 
> Giờ chúng ta xem pipeline tự động chạy..."

---

### Step 3: Watch Pipeline Run

**Action**:  NHANH switch sang Browser Tab 2 (GitHub Actions)

**Script**:
> "Refresh trang...  
> 
> [Click refresh hoặc F5]
> 
> Và đây!  Một workflow run mới đã được trigger!
> 
> [Point vào workflow run mới nhất]
> 
> Status: **In progress** ⏳
> 
> Commit message: 'Update version to 1.0.1'
> 
> Các bạn thấy không, **hoàn toàn tự động**!"

---

**Action**: Click vào workflow run

**Expected View**:
```
⏳ Test (running...)
⏸️  Build (queued)
⏸️  Deploy (queued)
⏸️  Security (queued)
```

**Script**:
> "Test job đang chạy... 
> 
> [Wait 10-15 seconds hoặc refresh]
> 
> [Test completes]
> 
> ✅ Test job passed!
> 
> Build job bắt đầu chạy..."

---

**Wait another 20-30 seconds**

**Script while waiting**:
> "Trong khi chờ, em xin giải thích: 
> 
> - **Test job** vừa chạy 7 unit tests
> - **Build job** đang build Docker image từ source code mới
> - Sau đó sẽ push lên Docker Hub
> - Cuối cùng **Deploy job** sẽ deploy lên production
> 
> Tất cả điều này **hoàn toàn tự động**, không cần human intervention!"

---

**Action**: Refresh page

**Expected View**:
```
✅ Test (23s)
✅ Build (49s)
⏳ Deploy (running...)
✅ Security (18s)
```

**Script**:
> "Perfect! Test và Build đã pass!
> 
> Deploy đang chạy... 
> 
> [Wait for deploy to complete]
> 
> ✅ **All jobs passed!**
> 
> Vậy là code mới đã được: 
> 1. ✅ Test tự động
> 2. ✅ Build thành Docker image
> 3. ✅ Deploy lên production
> 
> Tất cả chỉ trong **~2 phút**! 
> 
> Đây chính là sức mạnh của **CI/CD**!"

---

### Step 4: Verify New Version

**Action**: Switch sang Browser Tab 4 (localhost:5000)

```bash
# Or refresh the page
# Or curl
curl http://localhost:5000/api/info | jq . version
```

**Expected Output**:
```json
{
  "version": "1.0.1",
  ... 
}
```

**Script**:
> "Và khi check lại API endpoint... 
> 
> Version đã được update thành **1.0.1**! 
> 
> Code đã được deploy thành công!  🎉"

---

## 📖 Part 6: Wrap Up (2 phút)

### Summary

**Script**:
> "Tóm lại, trong demo vừa rồi, nhóm em đã show:
> 
> ✅ **Flask Web Application**
>    - UI đẹp, responsive
>    - RESTful API endpoints
>    - Production-ready với Gunicorn
> 
> ✅ **Docker Containerization**
>    - Multi-stage build
>    - Image size chỉ 50MB
>    - Chạy được ở bất kỳ đâu
> 
> ✅ **CI/CD Pipeline**
>    - Automated testing
>    - Docker build & push
>    - Auto deployment
>    - Security scanning
> 
> ✅ **Live Demo**
>    - Push code → Tự động test → Build → Deploy
>    - Tất cả trong ~2 phút
> 
> Đây là quy trình DevOps thực tế mà các công ty lớn đang sử dụng!
> 
> Project code và documentation đầy đủ tại: 
> **github.com/minhdong-04/devops-cicd-demo**"

---

### Highlight Key Achievements

**Script**:
> "Một số con số đáng chú ý: 
> 
> 📊 **Metrics**: 
> - 95%+ test coverage
> - 50MB Docker image (giảm 95%)
> - ~2 phút từ commit đến production
> - 4 CI/CD jobs tự động
> - 100% automated pipeline
> 
> 📚 **Documentation**:
> - README đầy đủ
> - Docker Guide chi tiết
> - CI/CD Guide
> - Presentation & Demo script
> - Tất cả bằng Tiếng Việt!"

---

### Call to Action

**Script**: 
> "Nếu các bạn quan tâm: 
> 
> 🔗 GitHub:  github.com/minhdong-04/devops-cicd-demo
> ⭐ Cho project một star nếu thấy hữu ích!
> 📖 Đọc documentation để hiểu sâu hơn
> 🐳 Pull Docker image và thử ngay
> 
> Mọi contribution đều welcome!"

---

### Q&A Prep

**Script**:
> "Vậy là kết thúc phần demo. Giờ em xin mở phần hỏi đáp. 
> 
> Thầy/cô và các bạn có câu hỏi nào không ạ?"

---

## 🆘 Backup Plan (Nếu Demo Fail)

### Scenario 1: Internet Down

**Plan A**: Dùng mobile hotspot

**Plan B**: Demo offline
```bash
# All locally
docker-compose up
# Show app running
# Show pre-recorded video of pipeline
```

**Script**:
> "Internet hiện tại không ổn định, nên em sẽ demo phần pipeline qua video đã record trước..."

---

### Scenario 2: App Không Start

**Plan A**: Check logs
```bash
docker logs <container_id>
# Fix issue nhanh
```

**Plan B**:  Dùng screenshots
```
Show:  docs/images/screenshot-app. png
```

**Script**:
> "App đang gặp issue nhỏ, em xin show qua screenshots..."

---

### Scenario 3: Pipeline Fail

**Plan A**: Show previous successful run

**Script**:
> "Run hiện tại đang pending do GitHub queuing, em xin show run trước đó..."

**Plan B**:  Explain based on logs

---

### Scenario 4: Port Conflict

**Quick Fix**:
```bash
# Kill process on port 5000
lsof -ti: 5000 | xargs kill -9

# Run on different port
docker run -p 8000:5000 devops-cicd-demo
```

---

## 📊 Common Q&A

### Q1: "Tại sao chọn Flask thay vì Django?"

**Answer**:
> "Flask nhẹ hơn, đơn giản hơn, phù hợp cho demo và microservices.  Django quá nặng cho một API đơn giản như này.  Trong thực tế, cả 2 đều OK, tùy use case."

---

### Q2: "Docker image 50MB có nhỏ không?"

**Answer**:
> "Rất nhỏ! So sánh: 
> - Python base image: 900MB
> - Sau optimization: 50MB
> - Giảm 95%! 
> 
> Trong production, image nhỏ = faster deployment, ít bandwidth, tiết kiệm storage."

---

### Q3: "CI/CD có chạy cho mọi commit không?"

**Answer**:
> "Có!  Mỗi push/PR đều trigger pipeline. Nhưng: 
> - Test job:  Chạy cho tất cả
> - Build job: Chỉ khi push (không phải PR)
> - Deploy job: Chỉ khi push vào main branch
> 
> Điều này được config trong workflow file với `if` conditions."

---

### Q4: "Project có deploy production thật không?"

**Answer**: 
> "Deploy job hiện tại là simulation.  Trong thực tế, có thể deploy lên: 
> - AWS (ECS, EKS, EC2)
> - Google Cloud (GKE, Cloud Run)
> - Azure (AKS, Container Instances)
> - Heroku, DigitalOcean, etc. 
> 
> Nhóm em chưa deploy production vì giới hạn về tài nguyên và chi phí."

---

### Q5: "Test coverage 95% có đủ không?"

**Answer**: 
> "Rất tốt! Industry standard: 
> - 80%+ = Good
> - 90%+ = Excellent
> - 100% = Không cần thiết (diminishing returns)
> 
> Quan trọng là test các critical paths, edge cases, và business logic."

---

### Q6: "Nhóm gặp khó khăn gì khi làm?"

**Answer**: 
> "Một số khó khăn: 
> 1. Docker image ban đầu quá lớn → giải quyết bằng multi-stage build
> 2. GitHub Secrets confusing → đọc docs kỹ
> 3. Test coverage thấp → viết thêm tests
> 4. Merge conflicts → git workflow tốt hơn
> 
> Nhưng đó là quá trình học tập quý giá!"

---

### Q7: "Có dùng Kubernetes không?"

**Answer**: 
> "Chưa.  Project này focus vào: 
> - Docker (containerization)
> - CI/CD pipeline
> 
> Kubernetes là bước tiếp theo (orchestration), phức tạp hơn.  Trong roadmap future của nhóm em có Kubernetes."

---

### Q8: "Monitoring và logging như thế nào?"

**Answer**:
> "Hiện tại: 
> - Health check endpoint:  /api/health
> - Docker logs: `docker logs`
> - GitHub Actions logs
> 
> Production nên có: 
> - Prometheus + Grafana (metrics)
> - ELK Stack (logs)
> - Sentry (error tracking)
> - PagerDuty (alerts)"

---

## ✅ Post-Demo Checklist

```
☐ Trả lời hết questions
☐ Share GitHub link với audience
☐ Share Docker Hub link
☐ Commit/push demo changes (nếu có)
☐ Screenshot/record demo (để sau này reference)
☐ Thank audience
☐ Collect feedback
```

---

## 📝 Notes

### Timing Tips: 

- ⏰ **Practice trước 3-5 lần** để quen flow
- ⏰ **Set timer** để track time
- ⏰ **Có backup plan** cho mỗi phần
- ⏰ **Không rush**, nói rõ ràng

### Presentation Tips:

- 😊 **Smile và confident**
- 👀 **Eye contact với audience**
- 🗣️ **Speak clearly**, không quá nhanh
- ✋ **Use gestures** để emphasize points
- 🎯 **Focus vào key achievements**

### Technical Tips:

- 💻 **Close unnecessary apps** để máy chạy mượt
- 🔋 **Full battery + charger**
- 📶 **Stable internet** (test trước)
- 🖱️ **Wireless mouse/clicker** (nếu có)
- 📱 **Mobile hotspot backup**

---

## 🎬 Final Words

> "Demo DevOps/CI/CD không chỉ là show code, mà là show **mindset** và **culture**: 
> 
> - Automation over manual work
> - Fast feedback loops
> - Continuous improvement
> - Collaboration between teams
> 
> Good luck với presentation! 🚀"

---

**[⬆ Back to top](#-demo-script---hướng-dẫn-demo-chi-tiết)**