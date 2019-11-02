import requests
import os

apiKey = os.environ.get("NBAKEY")

def getJson(url):
    #https://api.sportsdata.io/v3/nba/stats/json/Players/TEAM?key=KEY
    try:
        response = requests.get(
            url=url,
            headers={'Ocp-Apim-Subscription-Key':apiKey}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    
    try:
        jSonResp = response.json()
        return jSonResp
    except ValueError:
        # no jSon returned
        print ("Error, empty json response")
        return 'E'