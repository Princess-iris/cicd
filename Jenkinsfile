pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Deploy to Apache') {  // <-- UNAHIN ANG DEPLOY
            steps {
                sh '''
                sudo rsync -av --delete --exclude='venv/' --exclude='.git/' ./ /var/www/html/
                sudo chown -R www-data:www-data /var/www/html/
                '''
            }
        }
        
        stage('Run Selenium Test') {  // <-- TEST PAGKATAPOS MAG-DEPLOY
            steps {
                sh '''
                . venv/bin/activate
                python test.py
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD SUCCESS ✔ Deployment completed"
        }
        failure {
            echo "CI/CD FAILED ❌ Check logs"
        }
        always {
            cleanWs()
        }
    }
}
