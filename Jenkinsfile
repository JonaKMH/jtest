pipeline {
  agent any
  stages {
    stage('publish') {
      steps {
        sh '''	#!/bin/bash
	export WORKSPACE=`pwd`

	# Create/Activate virtualenv
	virtualenv venv
	source venv/bin/activate

	# Install Requirements
	pip install -r requirements.txt

	# Run tests
	python manage.py test'''
      }
    }
  }
}