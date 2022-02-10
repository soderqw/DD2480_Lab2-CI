from datetime import datetime
import os

def logger(PATH_REPO, name, message, sender, sha):

    #Checks if the file exist
    file_exists = os.path.exists('../../../logging.txt') #will hold a True or False value

    #Creates the file if it does not exist
    if(file_exists == False):
        f = open("../../../logging.txt", "x")

    # Append-adds at last of the file
    time = datetime.now()
    path = PATH_REPO + '/' + name

    file1 = open("../../../logging.txt", "a")  #append mode
    file1.write("Push event from: " + sender + "\n" + "Path: " + path + "\n" + "Compiled at:" + str(time) + "\n" + "Status: " + message + "\n" + "Sha: " + sha + "\n\n")
    file1.close()