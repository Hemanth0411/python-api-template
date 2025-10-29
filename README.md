# Python REST API Template

A professional, modern template for building robust and containerized Python REST APIs. This project provides a generic blueprint for structuring, containerizing, documenting, and automating a web service.

---

## Status

![CI/CD Pipeline](https://github.com/Hemanth0411/python-api-template/actions/workflows/ci.yml/badge.svg)

[![Docker Image on Docker Hub](https://img.shields.io/docker/pulls/hemanth0411/python-api-template.svg)](https://hub.docker.com/r/hemanth0411/python-api-template)

---

## Features

- **FastAPI**: A modern, high-performance web framework for building APIs.
- **Docker Ready**: Fully containerized with a multi-stage `Dockerfile` and `docker-compose` for easy development and deployment.
- **CI/CD Automation**: GitHub Actions workflow that automatically builds, tests, and pushes the image to Docker Hub.
- **Professional Structure**: Clear project layout and version control practices.
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
    This command will build the image and start the container.
    ```bash
    docker-compose up --build
    ```

3.  **Access the API:**
    The API will be available at `http://localhost:8000`. You can access the health check endpoint to verify it's running.

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

## Contributing

This project follows an issue-driven workflow. All changes are managed via GitHub Issues and submitted via Pull Requests. Please open an issue to discuss a change before submitting a PR.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. The licenses for third-party dependencies are documented in the [3RD-PARTY-LICENSES.md](3RD-PARTY-LICENSES.md) file.


