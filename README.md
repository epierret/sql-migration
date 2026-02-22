# MySQL Backup to S3 — Kubernetes + Terraform Project

This project demonstrates an end-to-end cloud-native backup workflow where:

• **Terraform** provisions AWS infrastructure
• **Kubernetes** runs a stateful MySQL workload
• **CronJob** automates backups
• **AWS S3** stores compressed dumps

The objective is to showcase practical DevOps and cloud-native skills: stateful deployments, persistence, secrets management, automation, and cloud integration.

---

## 🧭 Architecture Diagram

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/af16a0c7-50b4-424c-ae38-3bb2c8d8cde2" />



---

## 🚀 Key Features

• 🛠 **StatefulSet MySQL** → Persistent database deployment
• 🔐 **Secrets Management** → Secure MySQL & AWS credentials
• ⏰ **CronJob Backups** → Automated scheduled dumps
• ☁️ **AWS S3 Integration** → Durable cloud storage
• 📦 **Application Deployment** → Connectivity validation

---

## 🏗 Architecture Overview

| Component           | Type / Resource   | Role / Description                       |
| ------------------- | ----------------- | ---------------------------------------- |
| 🐬 MySQL Database   | StatefulSet + PVC | Persistent storage for database data     |
| 🔑 Database Secrets | Secret            | Secure MySQL and AWS credentials         |
| ⏰ Backup CronJob    | CronJob + PVC     | Dumps & compresses database every 2 mins |
| 📦 Application      | Deployment        | Verifies connectivity to database        |
| 🔗 MySQL Service    | ClusterIP Service | Stable internal endpoint for DB access   |
| ☁️ AWS S3 Bucket    | Cloud Storage     | Stores compressed backup files           |

---

## 📁 Project Structure

```
k8s-mysql-migration-backup/
│
├── README.md
├── LICENSE
│
├── manifests/
│   ├── secrets/
│   ├── configmaps/
│   ├── pvc/
│   ├── deployments/
│   ├── services/
│   └── cronjobs/
│
├── diagrams/
│   └── architecture.png
│
├── scripts/
│   └── deploy.sh
│
└── terraform-s3/
    ├── main.tf
    └── variables.tf
```

---

## ⚙️ Terraform Provisioning (AWS)

Terraform is responsible for creating the cloud resources required by the backup workflow:

• ☁️ **AWS S3 Bucket** → Backup destination
• 🔐 **IAM Policy** → Permissions for uploads

**Permissions used:**

• `s3:PutObject` → Required for backups
• `s3:GetObject` → Optional verification
• `s3:ListBucket` → Bucket visibility

![IAM Policy](https://github.com/user-attachments/assets/e359fff1-d79e-46ed-9b35-486897a24a1b)

AWS credentials are validated beforehand using the Python script located in `/scripts`.

![AWS Keys Validation](https://github.com/user-attachments/assets/73d025e0-0186-4920-8b21-6b0ca681221a)

---

## 🚀 Deployment Flow

1️⃣ **Provision Infrastructure (Terraform)**
2️⃣ **Create Namespace** → Resource isolation
3️⃣ **Deploy MySQL** → StatefulSet + PVC
4️⃣ **Create Secrets** → MySQL & AWS credentials
5️⃣ **Run CronJob** → Backup automation
6️⃣ **Deploy Application** → Connectivity check

---

## ☸️ Kubernetes Deployment

### Apply Manifests

```bash
kubectl apply -f manifests/00-namespace/
kubectl apply -f manifests/01-secrets/
kubectl apply -f manifests/02-storage/
kubectl apply -f manifests/03-service/
kubectl apply -f manifests/04-statefulset/
kubectl apply -f manifests/05-cronjob/
# or use deploy.sh
```

---

## 📦 Monitoring & Validation

### Check Resources

```bash
kubectl get all -n mysql-s3-backup
```

![Service Running](https://github.com/user-attachments/assets/c95ad7b8-de45-4474-bece-c7d980146349)

---

### CronJob Execution

CronJob runs every **2 minutes** (testing interval).

![CronJob](https://github.com/user-attachments/assets/24d6515c-fd7a-4c55-9d08-ffd55ebca4e2)

---

### Backup Logs

```bash
kubectl logs -f <cronjob-pod-name> -n mysql-s3-backup
```

![Backup Logs](https://github.com/user-attachments/assets/96e41397-98af-4683-a9ee-de75b7a464f5)

---

### Verify Backups in S3

![S3 Backups](https://github.com/user-attachments/assets/e9d015b9-4d9f-4e32-be20-bdf48ef072b2)

---

## 💾 Volumes & Persistence

• 🐬 **MySQL Database** → PVC (`/var/lib/mysql`)
• ⏰ **Backups** → PVC (`/backup`)
• 📦 **Application** → Stateless

---

## 🔧 Core Concepts Demonstrated

• **StatefulSet** → Stable identity & storage
• **PersistentVolume / PVC** → Data durability
• **Secret** → Credential protection
• **CronJob** → Scheduled automation
• **Service (ClusterIP)** → Internal discovery
• **Cloud Integration (S3)** → Backup destination

---

## ✨ Future Enhancements

• ☁️ Multi-cloud backups (AWS + Azure)
• 🔐 RBAC & NetworkPolicies
• 📊 Monitoring (Prometheus + Grafana)
• 🤖 GitOps / CI-CD (ArgoCD / Flux)

---

## 🧹 Cleanup

```bash
kubectl delete namespace mysql-s3-backup
terraform destroy
```
