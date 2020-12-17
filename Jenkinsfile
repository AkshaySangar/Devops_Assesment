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
        stage('test') {
			steps {
				sh 'python test.py'
				}
			post {
				always {
					junit 'test-reports/*.xml'
					}
				}	    
		}
    }
}