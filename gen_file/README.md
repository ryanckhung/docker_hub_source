# Virtual Environment
> python3 -m venv <env-name>
> source <env-name>/bin/activate
> pip freeze > requirements.txt
> pip install -r requirement.txt

# Linuc Command
> ps aux | grep python
> kill <process_id>

# Docker Build and Run
> docker build -t ryanckhung/gen_file .
> docker run -d --mount type=bind,source=/home/ryanhung/Desktop/temp/,target=/usr/src/app/data --name gen_file ryanckhung/gen_file
> docker exec -it <container ID> bash


# Login into Docker Hub
Reference: https://jsta.github.io/r-docker-tutorial/04-Dockerhub.html
> docker login -u your_user_name
> docker tag <image id> ryanckhung/gen_file
> docker push ryanckhung/gen_file:latest