# 🤝 Contributing Guide

> Hướng dẫn contribute cho thành viên nhóm và community

---

## 🎯 Quy Trình Contribute

### 1. Fork & Clone

```bash
# Fork repo trên GitHub (click Fork button)

# Clone về local
git clone https://github.com/YOUR_USERNAME/devops-cicd-demo.git
cd devops-cicd-demo

# Add upstream remote
git remote add upstream https://github.com/minhdong-04/devops-cicd-demo.git
```

---

### 2. Tạo Branch Mới

```bash
# Sync với upstream
git checkout main
git pull upstream main

# Tạo feature branch
git checkout -b feature/your-feature-name

# Naming convention: 
# - feature/add-xxx :  Thêm feature mới
# - fix/bug-xxx     : Fix bugs
# - docs/update-xxx : Update documentation
# - test/add-xxx    :  Thêm tests
```

---

### 3. Make Changes

```bash
# Code your changes
# ... 

# Run tests local
make test

# Check code quality
make lint
```

---

### 4. Commit Changes

```bash
# Stage changes
git add .

# Commit với message rõ ràng
git commit -m "feat: add new feature X"

# Commit message format:
# - feat: Thêm feature mới
# - fix: Fix bug
# - docs: Update docs
# - test:  Thêm tests
# - refactor: Refactor code
# - style: Format code
# - chore: Update config, dependencies
```

---

### 5. Push & Create PR

```bash
# Push lên fork của bạn
git push origin feature/your-feature-name

# Tạo Pull Request trên GitHub
# Base:  minhdong-04/devops-cicd-demo: main
# Compare: YOUR_USERNAME/devops-cicd-demo:feature/your-feature-name
```

---

## ✅ Checklist Trước Khi Submit PR

```
☐ Code chạy được local
☐ Tests pass (make test)
☐ Coverage không giảm
☐ Code quality OK (make lint)
☐ Documentation updated (nếu cần)
☐ Commit messages rõ ràng
☐ Branch updated với main
☐ No merge conflicts
```

---

## 📝 PR Template

```markdown
## Description
[Mô tả ngắn gọn về changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] Manual testing done

## Screenshots (if applicable)
[Add screenshots]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added where needed
- [ ] Documentation updated
```

---

## 🎨 Code Style Guidelines

### Python (PEP 8)

```python
# ✅ Good
def calculate_total(items:  list) -> float:
    """
    Calculate total price of items. 
    
    Args:
        items: List of items with prices
        
    Returns:
        Total price as float
    """
    return sum(item.price for item in items)


# ❌ Bad
def calc(i):
    return sum([x. p for x in i])
```

### Naming Conventions

```python
# Variables & functions:  snake_case
user_name = "John"
def get_user_info():
    pass

# Classes: PascalCase
class UserProfile:
    pass

# Constants: UPPER_CASE
MAX_RETRY = 3
API_KEY = "xxx"
```

---

## 🧪 Testing Guidelines

```python
# Test file:  test_*.py
# Test function: test_*

def test_health_endpoint():
    """Test health check endpoint returns 200"""
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'
```

**Requirements**:
- Mỗi function public cần có test
- Coverage target: 80%+
- Test cả happy path và edge cases

---

## 📖 Documentation Guidelines

```python
def process_data(data:  dict, validate: bool = True) -> dict:
    """
    Process input data and return result.
    
    Args:
        data (dict): Input data to process
        validate (bool): Whether to validate data.  Defaults to True.
        
    Returns:
        dict:  Processed data
        
    Raises:
        ValueError: If data is invalid and validate=True
        
    Example:
        >>> process_data({"name": "John"})
        {"name": "JOHN", "processed": True}
    """
    pass
```

---

## 🔍 Code Review Process

### Reviewer Checklist

```
☐ Code logic correct? 
☐ Tests adequate?
☐ Security issues? 
☐ Performance concerns?
☐ Documentation clear?
☐ Style consistent?
```

### Review Comments

```markdown
# ✅ Good feedback
"Consider using list comprehension here for better performance: 
`return [x*2 for x in items]`"

# ❌ Bad feedback
"This is wrong"
```

---

## 🚀 Release Process

### Version Numbering

**Semantic Versioning**:  `MAJOR.MINOR.PATCH`

- `MAJOR`: Breaking changes
- `MINOR`: New features (backward compatible)
- `PATCH`: Bug fixes

Example: `1.2.3` → `1.3.0` (new feature)

---

### Release Checklist

```
☐ All tests passing
☐ Documentation updated
☐ CHANGELOG. md updated
☐ Version bumped
☐ Tag created
☐ Docker image built & pushed
☐ Release notes written
```

---

## 🐛 Bug Reports

### Template

```markdown
**Bug Description**
[Clear description of the bug]

**Steps to Reproduce**
1. Go to... 
2. Click on...
3. See error

**Expected Behavior**
[What should happen]

**Actual Behavior**
[What actually happens]

**Environment**
- OS: [e.g. Ubuntu 22.04]
- Python: [e.g. 3.11]
- Docker: [e.g. 24.0.0]

**Screenshots**
[If applicable]

**Additional Context**
[Any other info]
```

---

## 💡 Feature Requests

### Template

```markdown
**Feature Description**
[Clear description of proposed feature]

**Use Case**
[Why is this feature needed?]

**Proposed Solution**
[How should it work?]

**Alternatives Considered**
[Other approaches you thought about]

**Additional Context**
[Mockups, examples, etc.]
```

---

## 📞 Contact

- **GitHub Issues**: [Link](https://github.com/minhdong-04/devops-cicd-demo/issues)
- **Email**: [your-email@example.com]
- **Discussions**: [Link](https://github.com/minhdong-04/devops-cicd-demo/discussions)

---

## 🙏 Thank You! 

Cảm ơn bạn đã contribute!  Every contribution makes this project better!  🎉

---

**[⬆ Back to top](#-contributing-guide)**
