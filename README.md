# docker_python
Get a docker container up and run a python script accepting passed arguments

1. install docker
2. run docker
3. open powershell / (git) bash
4. navigate to the app's folder using powershell / (git) bash
5. run command: docker build -t <desired_image_name:desired_tag> . (this will read the Dockerfile and run its commands)
6. run command: docker run -it <chosen_image_name:chosen_tag> <desired_argument_passed_1 desired_arguments_passed_2>
