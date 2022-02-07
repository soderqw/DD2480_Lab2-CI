##### IMPORTS #####

from flask import Flask, request, json
import os
import sys

from modules.compilation import compile

##### SETTINGS #####

STATUS_DEBUG = True
HOST = "127.0.0.1"
PORT = 8080

PATH_REPO = str(os.getcwd()) # Folder within CWD to run the code.

##### PROGRAM #####

app = Flask(__name__) # Variable for flask server application, to be called upon.

# Create an endpoint which receives requests from the GitHub API.
@app.route('/', methods=['POST']) # Triggered by URL localhost:5000/
def handler_Push():

    data = request.json # Request the data from the event.

    print("Received PUSH event from webhook!") # Debug print.

    # TODO: Extract Repository.
    # TODO: Save relevant parts of repo into variables to send to the other scripts.

    # Here you do all the continuous integration tasks
    # For example:
    # 1st clone your repository DONE
    # 2nd compile the code DONE

    # Step 1: Clone the repository.
    repo = data["repository"]["clone_url"] # Fetches the clone URL from the payload.
    name = data["repository"]["name"]
    branch = data["ref"].split('/')[2]

    #os.chdir(str(os.getcwd) + PATH_REPO) # Changes current directory to where the cloned repository is to be located.
    os.chdir(PATH_REPO)
    os.system("git clone " + '-b ' + branch + ' ' + repo) # Runs command to clone the repository.

    # Run module that compiles.

    print(str(os.getcwd()) + '/' + name)

    message, code = compile(PATH_REPO + '/' + name)

    if code > 0 or code < 0: # Error occured!
        return message + ' ' + str(code)

    # TODO: Run module that tests.

    #Flask.Response(status=200)

    return "OK " + message + ' ' + str(code)

    #return "OK" # Defaults to 200 response code.


# Start the Flask web server.
if __name__ == '__main__':
    app.run(debug=STATUS_DEBUG, host=HOST, port=PORT)