

# 🎬 Movie Ticket Booking Platform with CI/CD Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red?logo=jenkins\&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5)
![CI/CD](https://img.shields.io/badge/Jenkins-Pipeline-red)

A **production-ready Flask web application** for movie ticket booking integrated with a **CI/CD pipeline** using **Jenkins**, **Docker**, and **Kubernetes** for automated deployment and scalability.

---

## 🎯 Overview

This project demonstrates an end-to-end **DevOps workflow** for a Flask-based web application with:

* **Containerization** using Docker
* **Automated CI/CD** using Jenkins pipelines
* **Kubernetes orchestration** for scalable deployment
* **Continuous testing and deployment** for reliability

---

## 🌐 About the Application

The **Movie Ticket Booking Platform** allows users to:

* View currently running movies
* Check showtimes and seat availability
* Choose seats and book tickets
* Make secure payments

Designed for **responsiveness**, **real-time seat updates**, and a **smooth user experience**.

---

## ✨ Key Features

* **Flask Application** – Lightweight, modular backend
* **Dockerized Deployment** – Multi-stage builds for optimized images
* **Kubernetes Manifests** – Scalable pods and services
* **Jenkins CI/CD** – Automated build, test, deploy pipeline
* **Docker Hub Integration** – Auto push/pull of images
* **Health Checks & Monitoring** – Ensures uptime
* **Load Balancing** – Efficient traffic distribution via Kubernetes

---

## 🏗️ System Architecture

```text
             ┌──────────────────────────┐
             │      GitHub Repo          │
             │ gutthulamanikiran/Devops-Project │
             └──────────┬────────────────┘
                        │
                        ▼
             ┌────────────────────┐
             │      Jenkins        │
             │   CI/CD Pipeline    │
             └──────────┬──────────┘
                        │
                        ▼
             ┌──────────────────────────┐
             │       Docker Hub         │
             │ manikirangutthula2004    │
             └──────────┬───────────────┘
                        │
                        ▼
             ┌────────────────────┐
             │   Kubernetes        │
             │  Cluster (Pods)     │
             └──────────┬──────────┘
                        │
                        ▼
             ┌────────────────────┐
             │   LoadBalancer      │
             │   Service (External)│
             └──────────┬──────────┘
                        │
                        ▼
             ┌────────────────────┐
             │   End Users         │
             └────────────────────┘
```

---

## 📦 Prerequisites

* **Python 3.10+** → [Download](https://www.python.org/downloads/)
* **Docker** → [Install](https://docs.docker.com/get-docker/)
* **Kubernetes (kubectl)** → [Install](https://kubernetes.io/docs/tasks/tools/)
* **Minikube** → [Install](https://minikube.sigs.k8s.io/docs/start/)
* **Jenkins** → [Install](https://www.jenkins.io/doc/book/installing/)
* **Git** → [Install](https://git-scm.com/downloads/)

---

## 📁 Project Structure

```bash
DevOps-Assignment-2/
│
├── app.py                      # Flask app entry point
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker config
├── Jenkinsfile                  # CI/CD pipeline
├── README.md                    # Documentation
├── .gitignore                   # Git ignore rules
├── .dockerignore                # Docker ignore rules
│
├── templates/                   # HTML templates
│   ├── index.html
│   ├── movies.html
│   ├── seat_selection.html
│   └── payment.html
│
├── static/                      # CSS, JS, images
│   ├── css/
│   └── js/
│
├── k8s/                         # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
│
└── screenshots/                 # Pipeline and deployment screenshots
```

---

## 🚀 Local Development

```bash
# Clone repo
git clone https://github.com/gutthulamanikiran/Devops-Project.git
cd Devops-Project

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

---

## 🐳 Docker Deployment

```bash
# Build image
docker build -t manikirangutthula2004/ticket-booking-flask:latest .

# Run container
docker run -d -p 5000:5000 manikirangutthula2004/ticket-booking-flask:latest

# Stop & remove container
docker stop movie-app && docker rm movie-app
```

### Push to Docker Hub

```bash
docker tag movie-ticket-app manikirangutthula2004/ticket-booking-flask:latest
docker login
docker push manikirangutthula2004/ticket-booking-flask:latest
```

---

## ☸️ Kubernetes Deployment

```bash
# Start Minikube
minikube start

# Apply manifests
kubectl apply -f k8s/

# Verify pods & services
kubectl get pods
kubectl get services
```

**Scale replicas:**

```bash
kubectl scale deployment ticket-booking-flask --replicas=3
```

**Delete deployment:**

```bash
kubectl delete -f k8s/
```

---

## 🔄 CI/CD Pipeline

### Stages

1. **Checkout Code** – Pull latest code from GitHub
2. **Build Docker Image** – Build & tag image for Docker Hub
3. **Run Tests** – Basic health checks
4. **Push to Docker Hub** – Publish image
5. **Deploy to Kubernetes** – Apply manifests & expose service

---

### Jenkins Configuration

**Required Plugins:**

* Docker Pipeline
* Kubernetes CLI
* Git

**Credentials Setup:**

* **Docker Hub** → `docker-hub-cred`
* **Kubernetes Config** → `kubeconfig`

**Pipeline Variables:**

```groovy
DOCKERHUB_CREDENTIALS = credentials('docker-hub-cred')
DOCKER_IMAGE = 'manikirangutthula2004/ticket-booking-flask'
K8S_NAMESPACE = 'default'
```

**Steps:**

1. Create a Jenkins pipeline job
2. Connect to GitHub repo
3. Use `Jenkinsfile` from repo
4. Build & monitor from Jenkins Dashboard

---

## 👤 Author

**Name:** G. Manikiran
**Roll Number:** 160122771043

* **GitHub:** [github.com/gutthulamanikiran](https://github.com/gutthulamanikiran/Devops-Project)
* **Docker Hub:** [manikirangutthula2004](https://app.docker.com/accounts/manikirangutthula2004)

---

## 🙏 Acknowledgments

* Flask – Python web framework
* Docker – Containerization
* Jenkins – CI/CD automation
* Kubernetes – Deployment & scaling

---

