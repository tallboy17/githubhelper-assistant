---
repo: ageitgey/face_recognition
readme_filename: ageitgey_face_recognition_README.md
stars: 54971
forks: 13620
watchers: 54971
contributors_count: 49
license: MIT
Header 1: Face Recognition
Header 2: <a name="deployment">Deployment to Cloud Hosts (Heroku, AWS, etc)</a>
---
Since `face_recognition` depends on `dlib` which is written in C++, it can be tricky to deploy an app
using it to a cloud hosting provider like Heroku or AWS.  
To make things easier, there's an example Dockerfile in this repo that shows how to run an app built with
`face_recognition` in a Docker container. With that, you should be able to deploy
to any service that supports Docker images.  
You can try the Docker image locally by running: `docker-compose up --build`  
There are also several prebuilt Docker images.  
Linux users with a GPU (drivers >= 384.81) and Nvidia-Docker installed can run the example on the GPU: Open the docker-compose.yml file and uncomment the `dockerfile: Dockerfile.gpu` and `runtime: nvidia` lines.