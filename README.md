# 3-Tier Docker App with GitHub Actions CI/CD to Azure Container Instances

This project demonstrates a complete **3-tier architecture** (Frontend, Backend, and Database) using **Docker containers**, orchestrated with **Docker Compose**, and **automatically deployed to Azure Container Instances (ACI)** using **GitHub Actions CI/CD pipeline**.

---

## 🏗 Architecture
<pre>
+-------------+ +---------------+ +-------------+
| | | | | |
| Frontend +------->+ Backend +------->+ MySQL |
| (NGINX) | | (Flask App) | | Database |
| | | | | |
+-------------+ +---------------+ +-------------+
:80 :5000 :3306
</pre>

---

## 🧰 Tech Stack

- **Frontend:** NGINX serving static HTML
- **Backend:** Python Flask API
- **Database:** MySQL 5.7
- **Containerization:** Docker & Docker Compose
- **Cloud:** Azure (ACI + ACR)
- **CI/CD:** GitHub Actions

---

## 📂 Project Structure
<pre>
├── backend/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── db/
│ └── Dockerfile (optional if using official mysql)
├── frontend/
│ ├── index.html
│ └── Dockerfile
├── docker-compose.yml
└── .github/
└── workflows/
└── deploy.yml
</pre>

---

## 🚀 How It Works

### 1. **Code Push to GitHub**

Every push to the `main` branch triggers the GitHub Actions workflow.

### 2. **CI/CD Workflow**

- Logs in to Azure and Azure Container Registry (ACR)
- Builds Docker images for frontend, backend, and DB using `docker-compose`
- Pushes images to ACR
- Deploys each container to Azure Container Instances (ACI)

---

## 🔧 GitHub Actions Workflow Breakdown

```yaml
on:
  push:
    branches: [main]
- Login to Azure & ACR
- Build images with docker-compose build
- Tag & push to ACR
- Deploy to ACI using az container create
Includes separate ACI containers for each tier with dns-name-labels for public access.

🛠 Setup Instructions
✅ Prerequisites
- Azure subscription
- Azure CLI installed
- Docker installed
- A GitHub repo
- Azure Container Registry (ACR) created

📌 1. Clone the Repo
git clone https://github.com/af1nzr/3-tier-docker-app-Actions.git
cd 3-tier-docker-app-Actions

📌 2. Create GitHub Secrets
In your GitHub repo:
- AZURE_CREDENTIALS: JSON from az ad sp create-for-rbac
- ACR_USERNAME: Your ACR login username
- ACR_PASSWORD: Your ACR login password

📌 3. Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

This triggers the pipeline and deploys your app to Azure!

🌐 Access URLs
After deployment, you’ll get DNS URLs like:
http://frontend-<run_number>.eastus.azurecontainer.io
http://backend-<run_number>.eastus.azurecontainer.io

🧹 Clean Up Resources
To delete the resource group and stop billing:
az group delete --name my-resource-group --yes --no-wait

📖 License
MIT License — feel free to fork and improve!

🤝 Contributing
PRs are welcome! For major changes, open an issue first to discuss.

✍️ Author
Made with ❤️ by af1nzr

---

Let me know if you want:
- A badge for GitHub Actions status
- ASCII logo
- Public demo URL
- Azure CLI command helper script

I'll enhance this further if needed!
