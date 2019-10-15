node{
    Stages{
        Stage('Get the code')
        {
          steps{
            git 'https://github.com/kesavanrangan/myrepo1.git'
            }
        }
        Stage('Build the Fib file')
        {
          steps{
            sh 'python Fib.py 20'
            }
       }
    }
   }
