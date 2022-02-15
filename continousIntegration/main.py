##### IMPORTS #####

from tkinter import W
from flask import Flask, request, json, abort, render_template, send_file
import os
import sys
import shutil

from modules.compilation import compile
from modules.notification import notify
from modules.test import test
from modules.logger import logger

##### SETTINGS #####

STATUS_DEBUG = False
HOST = "127.0.0.1"
PORT = 8080
RELOAD = False

PATH_REPO = str(os.getcwd()) # Folder within CWD to run the code.

##### PROGRAM #####

app = Flask(__name__, template_folder="resources") # Variable for flask server application, to be called upon.

@app.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = os.getcwd()

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        with open(abs_path, "r") as f:
            return render_template("file.html", file=f.read())

    else:
        # Show directory contents
        files = os.listdir(abs_path)
        if '.DS_Store' in files:
            files.remove('.DS_Store')
        return render_template('files.html', files=files)



# Create an endpoint which receives requests from the GitHub API.
@app.route('/', methods=['POST']) # Triggered by URL localhost:5000/
def handler_Push():

    TOKEN = '';

    if not os.path.isfile('.TOKEN.txt'):
        TOKEN = sys.stdin.readline()
        with open('.TOKEN.txt', 'w') as f:
            f.write(TOKEN)
    else:
        with open('.TOKEN.txt', 'r') as f:
            TOKEN = f.read()
            print(TOKEN)

    data = request.json # Request the data from the event.

    message, code = notify(data, "pending", TOKEN)
    
    if code > 0 or code < 0: # Error occured!
        # Set github status.
        notify(data, "failure", TOKEN)
        return message + ' ' + str(code)

    print("Received PUSH event from webhook!") # Debug print.

    # Step 1: Clone the repository.
    repo = data["repository"]["clone_url"]  # Fetches the clone URL from the payload.
    name = data["repository"]["name"]
    sender = data["sender"]["login"]
    sha = data["after"]
    branch = data["ref"].split('/')[2]
    commit_url = data["commits"][0]["url"]

    if os.path.isdir(name):
            # Remove the cloned repo.
        shutil.rmtree(name)

    os.chdir(PATH_REPO)
    os.system("git clone " + '-b ' + branch + ' ' + repo) # Runs command to clone the repository.

    # Run module that compiles.

    print(str(os.getcwd()) + '/' + name)

    message, code = compile(PATH_REPO + '/' + name)

    if code > 0 or code < 0: # Error occured!
        # Set github status.
        notify(data, "failure", TOKEN)
        logger(PATH_REPO, name, message, sender, sha, commit_url)
        return message + ' ' + str(code)

    # Run module that tests.

    message, code = test(PATH_REPO + '/' + name)

    if code > 0 or code < 0: # Error occured!
        # Set github status.
        notify(data, "failure", TOKEN)
        logger(PATH_REPO, name, message, sender, sha, commit_url)
        return message + ' ' + str(code)

    print("test")
    logger(PATH_REPO, name, message, sender, sha, commit_url)
    notify(data, "success", TOKEN)

    return "OK " + message + ' ' + str(code)


# Start the Flask web server.
if __name__ == '__main__':
    app.run(debug=STATUS_DEBUG, host=HOST, port=PORT, use_reloader=RELOAD)
    
