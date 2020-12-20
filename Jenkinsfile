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
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml Sources/test.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
		stage('Deliver') { 
            agent any
            environment { 
                VOLUME = '$(pwd)/Sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python3'
            }
            steps {
                dir(path: env.BUILD_ID) { 
                    unstash(name: 'compiled-results') 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F main.py'" 
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/Sources/dist/main" 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
	}
		post{
            always{
                    mail to:"akshaysangar9@gmail.com", subject:"Status of pipeline: ${currentBuild.fullDisplayName}", 
                    body: "Bank Management System Application keeps the track of the books present in the library. \n ${env.BUILD_URL} has result ${currentBuild.result}."
                }
            }	
		 
}