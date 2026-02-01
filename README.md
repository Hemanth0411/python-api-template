# 🐍 Production-Ready Python REST API Template

[![CI/CD Pipeline](https://github.com/Hemanth0411/python-api-template/actions/workflows/ci.yml/badge.svg)](https://github.com/Hemanth0411/python-api-template/actions/workflows/ci.yml)
[![Docker Image on Docker Hub](https://img.shields.io/docker/pulls/hemanth0411/python-api-template.svg)](https://hub.docker.com/r/hemanth0411/python-api-template)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

A **senior-adjacent, production-ready blueprint** for building enterprise-grade REST APIs with FastAPI. This template goes beyond basic tutorials by implementing real-world patterns used in production systems: Clean Architecture, fail-fast configuration, distributed tracing, and automated quality enforcement.

---

## 📋 Table of Contents

- [Why This Template?](#-why-this-template)
- [Key Features](#-key-features)
- [Architecture & Design Decisions](#-architecture--design-decisions)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Development Workflow](#-development-workflow)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Configuration](#-configuration)
- [Testing Strategy](#-testing-strategy)
- [Docker & Deployment](#-docker--deployment)
- [Best Practices Implemented](#-best-practices-implemented)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## 🎯 Why This Template?

### The Problem
Most API templates focus on "getting started" but ignore the challenges you'll face in production:
- How do you trace a single user's request through thousands of log entries?
- How do you prevent deployments with missing environment variables?
- How do you maintain code quality as your team grows?
- How do you ensure your Docker containers are secure?

### The Solution
This template addresses **"Day 2" operational concerns** from Day 1:

| Challenge | Solution in This Template |
|-----------|--------------------------|
| **Debugging in Production** | Request ID middleware + Structured JSON logging |
| **Configuration Errors** | Pydantic-Settings with fail-fast validation |
| **Code Quality Drift** | Automated Ruff linting + Pytest in CI/CD |
| **Security Vulnerabilities** | Non-root Docker user + Multi-stage builds |
| **Scaling Complexity** | Clean Architecture with separated concerns |

---

## 🚀 Key Features

### 🏗️ Architecture
- **Clean Architecture**: Strict separation between API, Business Logic, Data Models, and Infrastructure
- **API Versioning**: Built-in `/api/v1/` structure for backward compatibility
- **Dependency Injection**: Service layer pattern for testable, maintainable code

### 🔒 Security
- **Non-Root Docker Execution**: Runs as dedicated `app` user with minimal permissions
- **Environment Validation**: Pydantic-Settings ensures no secrets are missing
- **Security Headers**: Ready for Helmet-style middleware integration

### 📊 Observability
- **Structured Logging**: JSON-ready logs via Loguru for ELK/Datadog integration
- **Request Tracing**: Unique `X-Request-ID` attached to every log entry
- **Health Checks**: `/` endpoint for Kubernetes liveness/readiness probes

### 🧪 Quality Assurance
- **Ruff Integration**: 10-100x faster than Flake8/Black/Isort combined
- **Pytest Suite**: Integration tests using `httpx` with zero network overhead
- **Async Testing**: Full support for FastAPI's async endpoints
- **CI/CD Enforcement**: Build fails on linting errors or test failures

### 🐳 DevOps
- **Multi-Stage Docker**: Optimized production images (~150MB)
- **Docker Compose**: One-command development environment with hot-reload
- **GitHub Actions**: Automated testing, linting, and Docker Hub deployment

---

## 🏛️ Architecture & Design Decisions

### 1. Layered Clean Architecture

**Decision**: Refactored from a monolithic `main.py` into distinct layers.

```
┌─────────────────────────────────────┐
│   API Layer (FastAPI Routes)       │  ← HTTP/Transport
├─────────────────────────────────────┤
│   Service Layer (Business Logic)   │  ← Pure Python
├─────────────────────────────────────┤
│   Schema Layer (Pydantic Models)   │  ← Data Validation
├─────────────────────────────────────┤
│   Core Layer (Config, Logging)     │  ← Infrastructure
└─────────────────────────────────────┘
```

**Why?**
- **Testability**: Business logic can be tested without HTTP mocking
- **Flexibility**: Swap FastAPI for GraphQL without touching business logic
- **Maintainability**: Each layer has a single responsibility

### 2. Fail-Fast Configuration

**Decision**: Use `Pydantic-Settings` to validate environment variables at startup.

```python
# src/core/config.py
class Settings(BaseSettings):
    APP_TITLE: str          # Required - app crashes if missing
    DEBUG: bool             # Required
    APP_VERSION: str = "1.0.0"  # Optional with default
```

**Why?**
- **90% of production outages** are caused by misconfiguration
- Crashes immediately with a clear error message
- Prevents "zombie deployments" that fail silently

### 3. Structured Observability

**Decision**: Replace `print()` with `Loguru` and implement Request ID middleware.

**Before** (Standard Logging):
```
INFO: Request received
ERROR: Database connection failed
INFO: Response sent
```
*Problem: Which request failed? Impossible to tell with 1000 req/sec*

**After** (This Template):
```json
{"time": "2026-02-01 11:00:00", "level": "INFO", "request_id": "a1b2c3", "message": "Request received"}
{"time": "2026-02-01 11:00:01", "level": "ERROR", "request_id": "a1b2c3", "message": "DB failed"}
```
*Solution: Search logs for `request_id: a1b2c3` to see the entire journey*

**Why?**
- Essential for distributed systems and microservices
- Compatible with Datadog, ELK, CloudWatch
- Makes debugging 10x faster

### 4. Zero-Network Testing

**Decision**: Use `httpx.ASGITransport` instead of `TestClient`.

**Why?**
- **10x faster**: No TCP/IP overhead
- **No port conflicts**: Doesn't bind to localhost:8000
- **More reliable**: Eliminates network-related flakiness in CI/CD

### 5. Security-First Docker

**Decision**: Multi-stage build with non-root user.

```dockerfile
# Stage 1: Build dependencies
FROM python:3.11-slim AS builder
# ... install packages ...

# Stage 2: Production runtime
FROM python:3.11-slim
RUN useradd -m -u 1000 app  # ← Non-root user
USER app  # ← Run as app, not root
```

**Why?**
- **Attack Surface Reduction**: If compromised, attacker has limited permissions
- **Compliance**: Many security audits require non-root containers
- **Best Practice**: Recommended by Docker, NIST, and OWASP

---

## 📁 Project Structure

```
python-api-template/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions pipeline
│
├── src/
│   ├── api/
│   │   ├── middleware.py          # Request ID injection
│   │   └── v1/
│   │       ├── api.py             # Router aggregation
│   │       └── endpoints/
│   │           └── items.py       # Item CRUD endpoints
│   │
│   ├── core/
│   │   ├── config.py              # Pydantic Settings
│   │   └── logging_config.py     # Loguru setup
│   │
│   ├── schemas/
│   │   └── item.py                # Pydantic models
│   │
│   ├── services/
│   │   └── item_service.py        # Business logic
│   │
│   └── main.py                    # FastAPI app initialization
│
├── tests/
│   ├── conftest.py                # Pytest fixtures
│   └── test_api_v1/
│       └── test_items.py          # Integration tests
│
├── .dockerignore                  # Docker build exclusions
├── .env.example                   # Environment template
├── .gitignore                     # Git exclusions
├── 3RD-PARTY-LICENSES.md         # Dependency licenses
├── docker-compose.yml             # Local dev orchestration
├── Dockerfile                     # Production image
├── LICENSE                        # MIT License
├── pyproject.toml                 # Ruff configuration
├── pytest.ini                     # Pytest configuration
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

---

## 🏁 Getting Started

### Prerequisites

- **Docker Desktop** ([Download](https://www.docker.com/products/docker-desktop/))
- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/))

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/Hemanth0411/python-api-template.git
cd python-api-template

# Create environment file
cp .env.example .env

# Start the application
docker-compose up --build
```

**Access Points:**
- **API Health Check**: http://localhost:8000/
- **Interactive Docs (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

### Option 2: Local Development (Venv)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Run the application
cd src
uvicorn main:app --reload
```

---

## 💻 Development Workflow

### Running Tests

```bash
# Run all tests
PYTHONPATH=src APP_TITLE=Test DEBUG=True pytest

# Run with coverage
PYTHONPATH=src APP_TITLE=Test DEBUG=True pytest --cov=src

# Run specific test file
PYTHONPATH=src APP_TITLE=Test DEBUG=True pytest tests/test_api_v1/test_items.py
```

### Code Quality Checks

```bash
# Lint and auto-fix issues
ruff check . --fix

# Format code
ruff format .

# Check formatting without changes
ruff format --check .
```

### Docker Commands

```bash
# Build the image
docker build -t python-api-template .

# Run container
docker run -p 8000:8000 --env-file .env python-api-template

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

---

## 🤖 CI/CD Pipeline

### GitHub Actions Workflow

The `.github/workflows/ci.yml` file defines a 3-stage pipeline:

#### Stage 1: Lint and Test
```yaml
- Install Python 3.11
- Install Ruff
- Run: ruff check .
- Run: ruff format --check .
- Install dependencies
- Run: pytest tests
```
**Purpose**: Ensure code quality and functionality before building

#### Stage 2: Build for PR (Pull Requests Only)
```yaml
- Checkout code
- Build Docker image
- Tag with commit SHA
```
**Purpose**: Verify Dockerfile is valid before merging

#### Stage 3: Build and Push (Main Branch Only)
```yaml
- Login to Docker Hub
- Build production image
- Push to hemanth0411/python-api-template
- Tag with 'latest' and commit SHA
```
**Purpose**: Automated deployment to Docker Hub

### Required Secrets

Configure these in GitHub Settings → Secrets:
- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Application Settings
APP_TITLE=My Production API
APP_VERSION=1.0.0
DEBUG=False

# Future: Database
# DATABASE_URL=postgresql://user:pass@localhost/db

# Future: Authentication
# JWT_SECRET=your-secret-key
# JWT_ALGORITHM=HS256
```

### Validation Rules

The app validates configuration on startup:
- `APP_TITLE`: **Required** - Application name
- `DEBUG`: **Required** - Boolean (True/False)
- `APP_VERSION`: Optional - Defaults to "0.2.0"

**If validation fails**, the app crashes with a clear error:
```
pydantic_core._pydantic_core.ValidationError: 1 validation error for Settings
APP_TITLE
  Field required [type=missing, input_value={}, input_type=dict]
```

---

## 🧪 Testing Strategy

### Test Architecture

```
tests/
├── conftest.py              # Shared fixtures
└── test_api_v1/
    └── test_items.py        # Endpoint tests
```

### Key Testing Patterns

#### 1. Async Test Client (conftest.py)
```python
@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac
```
**Why**: No network overhead, 10x faster tests

#### 2. Integration Tests (test_items.py)
```python
async def test_read_item(client):
    response = await client.get("/api/v1/items/1")
    assert response.status_code == 200
    assert response.json()["item_id"] == 1
```
**Why**: Tests the full request/response cycle

### Running Tests in Docker

```bash
docker-compose run --rm -u root api sh -c "pip install pytest pytest-asyncio httpx && export PYTHONPATH=src && export APP_TITLE=test && export DEBUG=True && pytest tests"
```

---

## 🐳 Docker & Deployment

### Multi-Stage Build Explained

```dockerfile
# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
RUN useradd -m -u 1000 app
COPY --from=builder /root/.local /home/app/.local
COPY src /app
USER app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Benefits**:
- **Smaller Image**: ~150MB vs ~900MB
- **Security**: Non-root execution
- **Speed**: Cached dependency layer

### Deployment Options

#### 1. Docker Hub
```bash
docker pull hemanth0411/python-api-template:latest
docker run -p 8000:8000 --env-file .env hemanth0411/python-api-template
```

#### 2. Kubernetes
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-api
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: api
        image: hemanth0411/python-api-template:latest
        ports:
        - containerPort: 8000
        env:
        - name: APP_TITLE
          value: "Production API"
        - name: DEBUG
          value: "False"
```

#### 3. Cloud Run / App Engine
The template is compatible with:
- Google Cloud Run
- AWS App Runner
- Azure Container Instances

---

## ✅ Best Practices Implemented

### Code Quality
- ✅ **PEP 8 Compliance**: Enforced by Ruff
- ✅ **Import Sorting**: Alphabetical, grouped by type
- ✅ **Type Hints**: Pydantic models provide runtime validation
- ✅ **Docstrings**: All public functions documented

### Security
- ✅ **Non-Root Containers**: Principle of least privilege
- ✅ **No Hardcoded Secrets**: All config via environment
- ✅ **Dependency Scanning**: (Future: Dependabot integration)
- ✅ **CORS Ready**: Middleware structure in place

### Operations
- ✅ **Health Checks**: `/` endpoint for load balancers
- ✅ **Structured Logs**: JSON format for log aggregation
- ✅ **Request Tracing**: Correlation IDs for debugging
- ✅ **Graceful Shutdown**: (Future: Signal handling)

### Development
- ✅ **Hot Reload**: Docker Compose with volume mounts
- ✅ **Pre-commit Hooks**: (Future: Husky equivalent)
- ✅ **API Documentation**: Auto-generated Swagger/ReDoc
- ✅ **Version Control**: Semantic versioning ready

---

## 🔧 Troubleshooting

### Common Issues

#### 1. `ValidationError: Field required`
**Problem**: Missing environment variable

**Solution**:
```bash
cp .env.example .env
# Edit .env and add required values
```

#### 2. `Port 8000 already in use`
**Problem**: Another process is using port 8000

**Solution**:
```bash
# Find process
lsof -i :8000  # Mac/Linux
netstat -ano | findstr :8000  # Windows

# Kill process or change port in docker-compose.yml
ports:
  - "8001:8000"
```

#### 3. Tests fail with `ModuleNotFoundError`
**Problem**: PYTHONPATH not set

**Solution**:
```bash
export PYTHONPATH=src  # Linux/Mac
$env:PYTHONPATH="src"  # Windows PowerShell
```

#### 4. Docker build fails on Windows
**Problem**: Line ending issues (CRLF vs LF)

**Solution**:
```bash
git config --global core.autocrlf input
git rm --cached -r .
git reset --hard
```

---

## 📚 Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Pydantic Settings**: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- **Loguru**: https://loguru.readthedocs.io/
- **Ruff**: https://docs.astral.sh/ruff/
- **Docker Best Practices**: https://docs.docker.com/develop/dev-best-practices/

---

## 🤝 Contributing

This is a template repository. To use it:

1. Click "Use this template" on GitHub
2. Clone your new repository
3. Update `README.md`, `LICENSE`, and `docker-compose.yml` with your details
4. Start building!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Third-party dependency licenses are documented in [3RD-PARTY-LICENSES.md](3RD-PARTY-LICENSES.md).

---

## 🙏 Acknowledgments

Built with:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Loguru](https://loguru.readthedocs.io/) - Simplified logging
- [Ruff](https://docs.astral.sh/ruff/) - Lightning-fast linter
- [Pytest](https://docs.pytest.org/) - Testing framework

---

**Made with ❤️ for production-ready Python APIs**
