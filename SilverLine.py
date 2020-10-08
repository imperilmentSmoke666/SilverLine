import requests
from requests.exceptions import HTTPError

with open("sites.txt") as fp:
    Lines = fp.readlines() 

for line in Lines:
    try:
        response = requests.get(line, timeout=0.09)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success! >' + response.url)
        with open("working.txt", "a") as fp:
            fp.writelines(line)
            fp.close()
