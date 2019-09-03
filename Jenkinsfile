pipeline {
    agent any
    triggers {
        pollSCM ('H/15 * * * *')
    }
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                branch 'lab'
            }
            steps {
                echo 'Deploying'
                echo ' in lab '
                echi ' Sep 2 , 2019 , test'
            }
        }
    }
}
