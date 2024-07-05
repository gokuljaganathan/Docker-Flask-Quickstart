from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True)


# docker image build -t flask-test ./flask_sample
# docker images
# docker run flask-test --> It will run but not work in public env because it is only accessible inside the docker container
# docker run -d -p 5000:5000 flask-test --> to work in public we can run in the detach mode like to call the docker usng
# 5000 port from outside.