# DevOps Sandbox & CI/CD Prototyping

## 📌 Overview
Welcome to the **DevOps Sandbox**. This repository serves as a dedicated R&D environment for exploring, building, and refining Continuous Integration and Continuous Deployment (CI/CD) pipelines. 

The primary goal of this project is to provide a safe, reproducible space to understand how modern build tools, containerization, and automation servers fit together. While it currently serves as a learning opportunity for Jenkins and Docker, it is designed to scale into a multi-language monorepo for evaluating various DevOps patterns.

---

## 🏗️ Architecture & Repository Structure
This repository is structured to support multiple languages and technology stacks independently. 

```text
devops-sandbox/
├── python/
│   └── simple-math-uv/      # Active: Modern Python packaging with uv and hatchling
├── csharp/                  # Planned: .NET build and test pipelines
├── cpp/                     # Planned: C++ compilation and testing
└── README.md