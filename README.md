
## **Project Overview**

> This project automates the deployment and management of a MySQL database in a Kubernetes environment. It includes database initialization, backups, and access by an application. The goal is to demonstrate **best practices in deploying stateful applications, data persistence, and automated backups**.

**Key Features**
🛠 StatefulSet MySQL → Persistent database deployment

🔐 Secrets Management → Secure credentials for MySQL & AWS

⏰ CronJob Backups → Scheduled automatic backups

☁️ AWS S3 Integration → Backup uploads to cloud storage

📦 Application Deployment → Verify database connectivity

                     --- Architecture Overview ---
| Component           | Type / Resource   | Role / Description                           |
| ------------------- | ----------------- | -------------------------------------------- |
| 🐬 MySQL Database   | StatefulSet + PVC | Persistent storage for database data         |
| 🔑 Database Secrets | Secret            | Secure MySQL and AWS credentials             |
| ⏰ Backup CronJob    | CronJob + PVC     | Dumps & compresses the database every 2 mins |
| 📦 Application      | Deployment        | Verifies connectivity to database            |
| 🔗 MySQL Service    | ClusterIP Service | Stable internal endpoint for database access |
| ☁️ AWS S3 Bucket    | Cloud Storage     | Stores compressed backup files               |


## **Project Structure**

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
📌 Responsibilities / Roles
Manifest Folder	Responsibility
00-namespace	Isolate the project from other resources
01-secrets	Secure passwords and keys
02-storage	Persist MySQL data
03-service	Allow MySQL pod discovery
04-statefulset	Ensure MySQL identity and ordered deployment
05-cronjob	Automate backups to S3
06-cleanup	Cleanup resources (optional)
## **Architecture / Project Components**

| Component             | Type / Resource   | Role / Description                              |
| --------------------- | ----------------- | ----------------------------------------------- |
| MySQL Database        | StatefulSet + PVC | Persistent storage of database data             |
| Database Secrets      | Secret            | Stores database username/password securely      |
| Database Init Scripts | ConfigMap         | Initializes DB schema and tables on first start |
| Backup CronJob        | CronJob + PVC     | Dumps the database every 5 minutes              |
| Application           | Deployment        | Accesses database to confirm users              |
| Database Service      | ClusterIP Service | Internal endpoint for DB access                 |

---🚀 Deployment Flow

Create namespace → Isolates project resources

Provision MySQL → StatefulSet + PVC for persistent storage

Store credentials → Secrets for MySQL & AWS

Run CronJob → Automatically backup and compress the database

Deploy application → Connects to MySQL via ClusterIP to verify data

💾 Volumes & Persistence

🐬 MySQL Database → PVC attached to StatefulSet (/var/lib/mysql)

⏰ Backups → PVC attached to CronJob (/backup)

📦 Application → Stateless; no volume required

🔧 Core Concepts
1️⃣ StatefulSet

Stable network identity, storage, and ordered deployment.

2️⃣ PersistentVolume / PVC

Persistent storage for database and backup files.

3️⃣ Secret

Stores sensitive credentials securely.

4️⃣ CronJob

Automates scheduled backups every 2 minutes (for testing).

5️⃣ Service

ClusterIP service exposes MySQL for internal access.

6️⃣ Application Connectivity

Application reads data from MySQL to demonstrate end-to-end workflow.

✨ Enhancements / Future Improvements

☁️ Multi-cloud backups (AWS + Azure)

🔐 RBAC, Network Policies, and TLS for security

📊 Monitoring & alerting (Prometheus + Grafana)

🤖 CI/CD automation for manifest deployments

⚡ Quickstart / Prerequisites

🖥 Kubernetes cluster running

🛠 kubectl installed and configured

☁️ AWS S3 bucket for backups

git clone git@github.com:epierret/k8s-mysql-migration-backup.git
cd k8s-mysql-migration-backup

Apply manifests:

kubectl apply -f manifests/00-namespace/
kubectl apply -f manifests/01-secrets/
kubectl apply -f manifests/02-storage/
kubectl apply -f manifests/03-service/
kubectl apply -f manifests/04-statefulset/
kubectl apply -f manifests/05-cronjob/

Monitor pods:

kubectl get pods -n mysql-s3-backup
kubectl logs -f <cronjob-pod-name> -n mysql-s3-backup

Verify backups in AWS S3:

aws s3 ls s3://sql-backup-nrik/mysql/ --region eu-west-3
👤 Author

Enrique Pierret – DevOps & Kubernetes enthusiast

If you want, I can also re-make the architecture diagram with emojis/visual style so the README looks even more portfolio-ready.

Do you want me to do that next?
