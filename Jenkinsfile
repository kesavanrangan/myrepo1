pipeline {
    stages {
    stage('Get the code')
        {
          steps {
            git 'https://github.com/kesavanrangan/myrepo1.git'
            }
        }
    stage('Build the Fib file') {
          steps {
            sh 'python Fib.py 20'
            }
       }
    }
    }
   
