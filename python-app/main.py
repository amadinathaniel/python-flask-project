from flask import Flask, render_template, jsonify
from flask.cli import load_dotenv
import socket
import boto3
import os


app = Flask(__name__)
BUCKET = "nath-helm-central-bucket"
load_dotenv()


# Function to list files in a given S3 bucket
def list_files(bucket):
    s3 = boto3.client('s3',
                      aws_access_key_id=os.getenv("ACCESS_KEY"),
                      aws_secret_access_key=os.getenv("SECRET_KEY"))
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            print(item)
            contents.append(item)
    except Exception as e:
        pass

    return contents


# Function to get hostname and IP Address
def fetch_details():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)

    return str(hostname), str(host_ip)


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/storage")
def storage():
    contents = list_files(BUCKET)
    return jsonify(contents)


@app.route('/health')
def health():
    return jsonify(
        status="UP"
    )


@app.route('/details')
def get_details():
    hostname, ip = fetch_details()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
