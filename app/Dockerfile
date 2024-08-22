#pthon 3.12 image
FROM python:3.12
#install pip
RUN pip install pandas
#set working directory to /app
WORKDIR /app
#copy pipeline.py from host to container (in /app directory)
COPY pipeline.py pipeline.py
#enter python with pipeline.py
ENTRYPOINT [ "python", "pipeline.py" ]