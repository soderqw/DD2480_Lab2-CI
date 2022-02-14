from datetime import datetime
import os



def logger(PATH_REPO, name, message, sender, sha, commit_url):
    ''' Logs the activity when a webhook is activated.
                   Parameters
                   ----------
                   PATH: The path to the project.
                   name: name of the repo
                   message: Status of the build
                   sender: The person who created the webhook
                   Returns
                   -------
                   none
                   See Also
                   -------
                   main : Functions that calls this logger function
           '''


    #Checks if the file exist
    p = f"../../commit_logs/logs{sha}.txt"
    file_exists = os.path.exists(p) #will hold a True or False value
    print(file_exists)
    #Creates the file if it does not exist
    if (file_exists == False):
        f = open(p, "w")

    print(file_exists)
    # Append-adds at last of the file
    time = datetime.now()
    path = PATH_REPO + '/' + name
    print("RUNNING")
    file1 = open(p, "w")  #append mode
    file1.write("Push event from: " + sender + "\n" + "Path: " + path + "\n" + "Compiled at:" + str(time) + "\n" + "Status: " + message + "\n" + "Sha: " + sha + "\n" +commit_url + "\n\n")
    file1.close()

    p = f"../../commit_logs/logs.txt"
    file_exists = os.path.exists(p)  # will hold a True or False value
    print(file_exists)
    # Creates the file if it does not exist
    if (file_exists == False):
        f = open(p, "w")

    file1 = open(p, "a")  # append mode
    file1.write("Push event from: " + sender + "\n" + "Path: " + path + "\n" + "Compiled at:" + str(
        time) + "\n" + "Status: " + message + "\n" + "Sha: " + sha + "\n" + commit_url + "\n\n")
    file1.close()

def main():
    logger("Musse/Tim/wille", "ISSUE#33", "FAIL", "MUSSE", "MDSADA", "HTTP://github.bajs.com")

if __name__ == "__main__":
    main()