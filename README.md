# MySQL Backup to S3 — Kubernetes + Terraform Project

This project automates the deployment and management of a MySQL database in a Kubernetes environment, with backups stored in AWS S3. Terraform provisions the necessary infrastructure, and Kubernetes manages stateful applications, secrets, and CronJob backups.

---

## 🚀 Key Features

* 🛠 **StatefulSet MySQL** → Persistent database deployment
* 🔐 **Secrets Management** → Secure MySQL & AWS credentials
* ⏰ **CronJob Backups** → Scheduled automated dumps
* ☁️ **AWS S3 Integration** → Cloud backup storage
* 📦 **Application Deployment** → Database connectivity validation

---

## Architecture Overview

| Component           | Type / Resource   | Role / Description                       |
| ------------------- | ----------------- | ---------------------------------------- |
| 🐬 MySQL Database   | StatefulSet + PVC | Persistent storage for database data     |
| 🔑 Database Secrets | Secret            | Secure MySQL and AWS credentials         |
| ⏰ Backup CronJob    | CronJob + PVC     | Dumps & compresses database every 2 mins |
| 📦 Application      | Deployment        | Verifies connectivity to database        |
| 🔗 MySQL Service    | ClusterIP Service | Stable internal endpoint for DB access   |
| ☁️ AWS S3 Bucket    | Cloud Storage     | Stores compressed backup files           |

![Architecture Diagram](diagrams/architecture.png)

---

## Project Structure

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

## Manifests Responsibilities

| Folder         | Responsibility                |
| -------------- | ----------------------------- |
| 00-namespace   | Isolate project resources     |
| 01-secrets     | Secure passwords and AWS keys |
| 02-storage     | Persistent volumes (PVC)      |
| 03-service     | MySQL service discovery       |
| 04-statefulset | Deploy MySQL StatefulSet      |
| 05-cronjob     | Automated backups to S3       |
| 06-cleanup     | Optional resource teardown    |

---

## Deployment Flow

1. **Create Namespace** → Isolates project resources
2. **Provision MySQL** → StatefulSet + PVC for persistent storage
3. **Store Credentials** → Secrets for MySQL & AWS
4. **Run CronJob** → Automatically backup & compress DB
5. **Deploy Application** → Connects to MySQL via ClusterIP

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

### Monitor Deployment

```bash
kubectl get all -n mysql-s3-backup

![service ok ](https://github.com/user-attachments/assets/c95ad7b8-de45-4474-bece-c7d980146349)


kubectl logs -f <cronjob-pod-name> -n mysql-s3-backup

![backup over](https://github.com/user-attachments/assets/96e41397-98af-4683-a9ee-de75b7a464f5)

```




* CronJob runs every 2 minutes (for testing).

* ![job 2 min](https://github.com/user-attachments/assets/24d6515c-fd7a-4c55-9d08-ffd55ebca4e2)


* S3 is provided

* 
*![resultat sql](https://github.com/user-attachments/assets/e9d015b9-4d9f-4e32-be20-bdf48ef072b2)





---

## Volumes & Persistence

* 🐬 MySQL Database → PVC attached to StatefulSet (`/var/lib/mysql`)
* ⏰ Backups → PVC attached to CronJob (`/backup`)
* 📦 Application → Stateless, no volume required

---

## Terraform Provisioning

Terraform handles AWS S3 bucket creation and IAM policy for backup uploads.

* S3 Bucket → Stores compressed backups
* IAM Policy → Permissions: `s3:PutObject`, `s3:GetObject`, `s3:ListBucket`

<img width="344" height="279" alt="image" src="https://github.com/user-attachments/assets/e359fff1-d79e-46ed-9b35-486897a24a1b" />




AWS credentials are validated via the `/scripts` Python script before deployment.


![aws keys ok ](https://github.com/user-attachments/assets/73d025e0-0186-4920-8b21-6b0ca681221a)


---

## Core Concepts

* **StatefulSet** → Stable network identity, storage, and ordered deployment
* **PersistentVolume / PVC** → Persistent storage for database & backups
* **Secret** → Stores credentials securely
* **CronJob** → Automates scheduled backups
* **Service (ClusterIP)** → Internal DB access
* **Application Connectivity** → Verifies end-to-end workflow

---

## Future Enhancements

* ☁️ Multi-cloud backups (AWS + Azure)
* 🔐 RBAC & NetworkPolicies
* 📊 Monitoring (Prometheus + Grafana)
* 🤖 GitOps / CI-CD automation (ArgoCD / Flux)

---

