import requests
from requests.exceptions import HTTPError

with open("sites.txt") as fp:
    Lines = fp.readlines()

for line in Lines:
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0'
        }

        response = requests.get(line, timeout=2.5, headers=headers)

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
