# 1. Launch EC2 instance on AWS Console
#   - Choose Ubuntu Server 20.04 LTS AMI (or latest version).
#   - Choose an instance type (e.g., t2.micro).
#   - Create a new key pair for SSH access and download the .pem file.

# 2. SSH into EC2 instance
# Get the Public IP of the EC2 instance and use the SSH command:
ssh -i /path/to/your-key.pem ubuntu@<ec2-public-ip>

# 3. Update system packages
sudo apt-get update -y
sudo apt-get upgrade -y

# 4. Install Docker
sudo apt-get install -y docker.io

# 5. Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 6. Clone your repository
git clone https://github.com/your-username/book-summary-app.git
cd book-summary-app

# 7. Create `.env` file in backend directory
# backend/.env
echo "DB_NAME=bookdb" >> backend/.env
echo "DB_USER=bookuser" >> backend/.env
echo "DB_PASSWORD=bookpass" >> backend/.env

# 8. Build Docker containers with Docker Compose
sudo docker-compose up --build -d

