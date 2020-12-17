pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.9-alpine'
                }
            }
            steps {
                sh 'python -m py_compile Sources/main.py'
                stash(name: 'compiled-results', includes: 'Sources/*.py*')
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'pip install pandas' 
                }
            }
            steps {
                sh 'python Sources/test.py' 
            }
            
        }
    }
}