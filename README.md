## Deploying Python Application using Docker, Kubernetes and Helm

- Installing Python 3.X
- Creating Python Virtual Environments
- Installing Python VS Code Extension
- Sample Flask Application
- Jinja templating for Dynamic Web Pages
- Using Pip to Freeze Python Dependencies
- Building the docker image using Dockerfile
- Writing Docker Compose file
- Writing Kubernetes Manifest files for the application
- Setting Up s3 bucket as helm repository using Terraform
- Creating Helm Chart



# Python-flask-project 

This repository contains the code for setting up a simple DevOps App Deployment Workflow 

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [ ] [AWS CLI Tool](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- [ ] [Git](https://git-scm.com/downloads)
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/amadinathaniel/python-flask-project .git
```

2. Check into the cloned repository
```
$ cd python-flask-project
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Configure AWS CLI
```
$ aws configure
```

5. Create a bucket on AWS using Terraform in the  and update it on the `main.py` file.

6. Run the application
```
$ python main.py
```

7. Navigate to http://localhost:5000/storage to display contents of the s3 bucket as json response
