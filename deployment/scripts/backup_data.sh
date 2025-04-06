#!/bin/bash
echo "Backing up PostgreSQL and MongoDB data..."
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
mkdir -p backups/$TIMESTAMP

# PostgreSQL backup
pg_dump -U postgres -h localhost -F c -b -v -f backups/$TIMESTAMP/postgres_backup.dump mydatabase

# MongoDB backup
mongodump --uri="mongodb://localhost:27017/mydatabase" --out=backups/$TIMESTAMP/mongodb_backup

echo "Backup completed and saved to backups/$TIMESTAMP"
