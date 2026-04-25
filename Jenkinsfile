pipeline {
    agent any
 
    environment {
        JAVA_HOME = "/usr/lib/jvm/java-17-openjdk-amd64"
        DEPLOY = "/var/www/html"
    }
 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Princess-iris/cicd.git',
                    credentialsId: 'github-pat'
            }
        }
 
        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
 
        stage('Start Apache') {
            steps {
                sh 'sudo systemctl start apache2'
            }
        }
 
        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                python test.py
                '''
            }
        }
 
        stage('Deploy') {
            steps {
                sh '''
                sudo cp index.php ${DEPLOY}/
                sudo chown -R www-data:www-data ${DEPLOY}
                sudo chmod -R 755 ${DEPLOY}
                '''
            }
        }
    }
}
