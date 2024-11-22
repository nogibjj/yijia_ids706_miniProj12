DOCKER_USERNAME=yijia123
DOCKER_IMAGE_NAME=mini12

login:
	docker login -u ${DOCKER_USERNAME}

build:
	docker build -t ${DOCKER_IMAGE_NAME} .

# Run the Docker container
run:
	docker run -p 8080:5000 $(DOCKER_IMAGE_NAME)

# Remove the Docker image
clean:
	docker rmi $(DOCKER_IMAGE_NAME)

show_local_images:
	docker images

show_running_containers:
	docker ps

push:
	docker login
	docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_USERNAME}/${DOCKER_IMAGE_NAME}
	docker push ${DOCKER_USERNAME}/${DOCKER_IMAGE_NAME}:latest
