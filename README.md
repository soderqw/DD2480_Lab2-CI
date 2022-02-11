# DD2480_Lab2-CI

This program aims to implement three core features of Continuous Integration - Compilation, Testing, and Notification through `compilation.py`, `test.py` and `notification.py` respectively.


# Requirements

Below are the required packages:

1. ***Flask***
```bash
pip3 install Flask
```
2. ***os***
```bash
Requires import only
```
3. ***sys***
```bash
Requires import only
```
4. ***unittest***
```bash
Requires import only
```

5. ***requests***
```bash
pip3 install requests
```

# Usage

Step 1: Starting the Server
Starting the server requires fetching a token with access to the GitHub repository. The server takes that as an input through standard input.

```bash
python3 continousIntegration/main.py < TOKEN.txt
```

Step 2: Running the Continuous Integration tool
The server runs a check whenever a push to the repository has been made.

Step 3: Verifying Commit Status
GitHub displays the build status from the Continuous Integration tool using the GitHub commit status.

# Implementation

Compilation module
```bash
The compilation module grabs the clone URL and branch from the JSON payload then cloning the repository locally. It then looks for any file within the cloned repository with the relevant file extension '.py'. It then completes a static syntax check of any occurences of such files, returning an error code to the main server accordingly.

Unit tests have been implemented testing the functionality of the component. Files were added which compile and do not compile and the compilation component was then run locally on those files to evaluate the performance. If it could detect errors within a script.
```

Test module
```bash
The test module looks within the previously cloned repository for a /tests folder at a specified location. It then, similarly to the compilation module, look for any file with the extension '.py' and runs them. An error code is returned accordingly to the main server.

Unit tests have been implemented testing the functionality of the component. Files were added which compile and do not compile and the compilation component was then run locally on those files to evaluate the performance. If it could detect errors within a script.
```

Notification module
```bash
The notification module takes an error code, corresponding to success or any error. Using a token which is provided to the server it sends a POST request using the GitHub API for a commit status change of the status corresponding to the error code.

A pending status is sent before any other component is run in order to signify that a test is being run.

Unit testing for this has been run by providing different parameters to the component. Namely the TOKEN parameter as this is the one parameter that the program uses. An invalid input and a correct token was tested.
```

# Statement of Contribution

During this project, an effort was put towards distributing the workload equally amongst all members of the team. While some of the specified assignments were largely attributed to one person, a team effort was put into the group assignment, thus a plethora of the features were worked on as a group.
(As a sidenote - Adding any function to the project entails the addition of unit tests as well.)

A further detailed list of contributions follows:

Oscar

```
Initial project setup - Translating Java Skeleton to a Python skeleton.
Restructuring of the project into a comprehensible project structure.
Implementation of Core CI feature - notification.
Implementation of Core CI feature - compilation.
Implement Unit Test for compilation.
Creation of README file.

```

William

```
Implementation of Core CI feature - notification.
Implement Unit Test for notification.
```

Tim

```
Implementation of Core CI feature - testing.
Implement Unit Test for testing.
```

Jansen

```
Implementation of Core CI feature - testing.
Implement Unit Test for testing.
Creation of README file.
```

Mustafa
```
Implementation of Core CI feature - testing.
Implement Unit Test for testing.
Creation of Essence documentation.
Documentation of DocString.
```

# Properties Made to Achieve P+

1. The program logs previous status.

2. All of our Issues are linked to a commit.  

3. We have implemented a Continous Integration (CI) tool, using GitHub Actions. The tool is run every time someone pushes to or makes a Pull Request towards the main branch. It then runs a linter and our unit tests in order to spot errors within the code (syntax- or runtime errors) but also errors regarding assignment specifications. The tool runs Python 3.10 and Ubuntu Linux.