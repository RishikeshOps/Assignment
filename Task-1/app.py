import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World :) "

@app.route('/What is Your Name')
def hello():
    return 'My Name is Rushikesh Mashidkar'

if __name__ == "__main__":
    app.run()
