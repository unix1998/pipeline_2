pipeline {
         agent any
         stages {
                 stage('One') {
                 steps {
                     echo 'Hi, this is a test from me'
                 }
                 }
                 stage('Two') {
                 steps {
                    script {
                     env.GO_or_NO_GO = input message: 'User input required',
                     parameters: [choice(name: 'GO or no go today ', choices: 'YES\nNO', \
                      description: 'Choose "yes" if we get signed off from manager')]
                       } 
                 
                 steps          when {
        environment name: 'GO_or_NO_GO', value: 'YES'
      }
                script {
                    echo " we are going next steps "
                } 
                 }
                 }
                 stage('Three') {
                 when {
                       not {
                            branch "master"
                       }
                 }
                 steps {
                       echo "Hello"
                 }
                 }
                 stage('Four') {
                 parallel { 
                            stage('Unit Test') {
                           steps {
                                echo "Running the unit test..."
                           }
                           }
                            stage('Integration test') {
                              agent {
                                    docker {
                                            reuseNode true
                                            image 'ubuntu'
                                           }
                                    }
                              steps {
                                echo "Running the integration test..."
                              }
                           }
                           }
                           }
              }
}
