pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: 'c943865b-3d73-4cad-8e14-d7f223fc25d8', url: 'https://github.com/viswaradhyam/DevopsAI.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'c943865b-3d73-4cad-8e14-d7f223fc25d8', url: 'https://github.com/viswaradhyam/DevopsAI.git'
                bat 'python sort.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
