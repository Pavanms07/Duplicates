pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Duplicate status') {
      steps {
        sh 'python3 Duplicates.py'
      }
    }
  }
}
