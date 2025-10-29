# Production-Ready Python REST API Template

This repository provides a comprehensive, professional blueprint for building robust, containerized, and production-ready REST APIs in Python using FastAPI. Its primary purpose is to allow any developer to clone or template this project and immediately start building business logic, without worrying about setup, containerization, or CI/CD.

---

## Status

![CI/CD Pipeline](https://github.com/Hemanth0411/python-api-template/actions/workflows/ci.yml/badge.svg)

[![Docker Image on Docker Hub](https://img.shields.io/docker/pulls/hemanth0411/python-api-template.svg)](https://hub.docker.com/r/hemanth0411/python-api-template)

---

## Features

- **FastAPI**: A modern, high-performance web framework for building APIs.
- **Docker Ready**: Fully containerized with a multi-stage `Dockerfile` and `docker-compose` for easy development and deployment.
- **CI/CD Automation**: GitHub Actions workflow that automatically builds, tests, and pushes the image to Docker Hub.
- **API Auto-Documentation**: Interactive API documentation served at `/docs` (Swagger UI) and `/redoc` (ReDoc).
- **Professional Structure**: Clear project layout and a proven, issue-driven workflow.
- **Legal Compliance**: Includes `LICENSE` and a generated `3RD-PARTY-LICENSES.md` file.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)

### Running Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Hemanth0411/python-api-template.git
    cd python-api-template
    ```

2.  **Launch the application using Docker Compose:**
    This command will build the image and start the container with live-reloading enabled.
    ```bash
    docker-compose up --build
    ```

3.  **Access the Service:**
    Once the container is running, the following endpoints are available:
    - **Health Check**: `http://localhost:8000/`
    - **Interactive API Docs (Swagger)**: `http://localhost:8000/docs`
    - **Alternative API Docs (ReDoc)**: `http://localhost:8000/redoc`

## How to Use This Template

To use this project as the foundation for your own API, follow these steps:

1.  **Create Your Repository:**
    Click the "**Use this template**" button at the top of the GitHub repository page to create a new repository with a copy of this project's files.

2.  **Update the `README.md`:**
    Edit this `README.md` file to describe your new project. Change the title, description, and Docker Hub username.

3.  **Update the CI/CD Workflow:**
    - Open `.github/workflows/ci.yml`.
    - On line 58, change `hemanth0411/python-api-template` to your Docker Hub username and desired image name.
    - Configure the `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets in your new repository's settings.

4.  **Update Application Metadata:**
    - Open `src/main.py`.
    - Change the `title`, `description`, and `version` in the `FastAPI` app instance to match your project.

5.  **Update the `LICENSE`:**
    - Open the `LICENSE` file and change the `[year]` and `[fullname]` to your own.

6.  **Start Developing!**
    You are now ready to add your own Pydantic models and API endpoints in the `src/` directory.

## Project Structure

```
.
├── .github/workflows/      # GitHub Actions CI/CD pipeline
├── src/                    # Application source code
│   └── main.py
├── .dockerignore           # Specifies files to ignore in the Docker build
├── .gitignore              # Specifies files to ignore for Git
├── 3RD-PARTY-LICENSES.md   # Licenses of third-party dependencies
├── docker-compose.yml      # Defines services for local development
├── Dockerfile              # Instructions for building the application image
├── LICENSE                 # Project's software license
├── README.md               # This file
└── requirements.txt        # Python package dependencies
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. The licenses for third-party dependencies are documented in the [3RD-PARTY-LICENSES.md](3RD-PARTY-LICENSES.md) file.
```

