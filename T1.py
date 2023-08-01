#Grabs a random quote from quotable.io API - User simply need to run the script and it will generate it anytime - Maybe a daily quote a day bot?
import argparse
import math
import requests


#Research API details without CHATBOT or Mentor
def call_api():
    #Endpoint features
    url = "https://api.quotable.io/random"

    #Use requests to GET data - Learn what redirects do
    response = requests.get(url, allow_redirects=True)

    #Check if response is valid
    if response.status_code == 200:
        return response.json()
    else:
        print("The Quote of The Day:\n\nGod is dead...")
        exit()
    

dic = call_api()
print("The Quote of The Day:\n" + dic["content"])