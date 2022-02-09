import requests
import json

def notify(data, STATUS, TOKEN):
    ''' Will set commit status to 'pending', 'success' or 'failure' based on STATUS input. The status set will be visible on GitHub in the commit history after a push.

        Parameters
        ----------
        data: JSON file containing webhook payload.
        STATUS: Set by caller to 'pending', 'success', 'failure' or other valid statuses.
        TOKEN: Set by caller to authenticate in order to make GitHub API calls.
        
    '''
    SHA = str(data["after"])
    REPO = str(data["repository"]["full_name"])

    # Not a valid token
    if not TOKEN:
        return ('ERROR: No authentication token provided', -1)

    # Create a commit status using curl
    api_url = f"https://api.github.com/repos/{REPO}/statuses/{SHA}"
    paramters = {
            "state": f'{STATUS}',
            "description": 'Indicates CI build results',
        }
    header = {'Authorization': f'token {TOKEN}','Accept': 'application/vnd.github.v3+json'}
    response = requests.post(api_url, headers=header, data=json.dumps(paramters))
    
    # API call failed
    if response.status_code != 201:
        return ('ERROR: ', response.status_code)
    
    # API call successfull
    return ('SUCCESS', 0)
