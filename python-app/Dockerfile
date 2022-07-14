# start by pulling the python image
FROM python:3.10.0-alpine3.15

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY requirements.txt .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# Expose Port for App
EXPOSE 5000

# Set Healthcheck details
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
            CMD curl -f http://localhost:5000/health || exit 1

# configure the container to run in an executed manner
ENTRYPOINT ["python3", "main.py" ]
