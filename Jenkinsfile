pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3-alpine' 
                }
            }
            steps {
                sh 'python3 -m py_compile Sources/main.py' 
                stash(name: 'compiled-results', includes: 'Sources/*.py*') 
            }
        }
    }
}
