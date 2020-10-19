import requests
from requests.exceptions import HTTPError

with open("sites.txt") as fp:
    Lines = fp.readlines() #reads URLS from file 


for line in Lines:
    try:

        headers = {

            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0'

        }

        response = requests.get(line, timeout=2.5, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success! >' + response.url)
        with open("working.txt", "a") as fp:  #Puts working proxies into a file

            # If you fancy getting the response headers & encoding :/ 
#            fp.writelines(line)
#            fp.writelines("-----------Start--------")
#            fp.writelines("\n")
#            fp.writelines("Headers: ")
#            fp.writelines(str(response.headers))
#            fp.writelines("\n")
#            fp.writelines("Encoding: ")
#            fp.writelines(response.encoding)
#            fp.writelines("\n")
#            fp.writelines("-----------End------------")
#            fp.writelines("\n")
#            fp.writelines("\n")
