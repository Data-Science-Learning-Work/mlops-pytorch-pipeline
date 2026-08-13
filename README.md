# mlops-pytorch-pipeline
In this assignment, you will take a PyTorch image classification model through the full deployment lifecycle: from local development with proper Git workflows, to containerized training with Docker, to orchestrated deployment on Kubernetes. By the end, you will have a production-style ML pipeline that can train and serve predictions at scale.

# project directory
mlops-pytorch-pipeline/
··· README.md
··· .gitignore
··· .github/
· ··· workflows/
· ··· ci.yml
··· src/
· ··· train.py
· ··· model.py
· ··· dataset.py
· ··· serve.py
··· configs/
· ··· training_config.yaml
··· docker/
· ··· Dockerfile.train
· ··· Dockerfile.serve
··· k8s/
· ··· namespace.yaml
· ··· training-job.yaml
· ··· serving-deployment.yaml
· ··· serving-service.yaml
· ··· configmap.yaml
· ··· hpa.yaml
··· requirements/
· ··· train.txt
· ··· serve.txt
··· tests/
··· test_model.py