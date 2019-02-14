import requests
import json

class Instagram:

    @classmethod
    def details(self, username):
        return InstagramFactory(username)

    @classmethod
    def posts(self, username):
        return InstagramPostFactory(username)

    @classmethod
    def followers(self, username):
        return InstagramFollowersFactory(username)



class InstagramFactory:

    global business_phone_number
    global business_email

    def __init__(self, username):
        self.username = username 

     
    def get(self):
        api_data = InstgaramRequest.handle(self.username)
        api_data =  json.loads(api_data)
        api_data =  api_data['graphql']['user']
        business_phone_number = api_data['business_phone_number']
        business_email = api_data['business_email']
        return api_data


class InstagramPostFactory:

    def __init__(self, username):
        self.username = username   
     
    def get(self):
        return InstgaramRequest.handle(self.username)


class InstagramFollowersFactory:

    def __init__(self, username):
        self.username = username   
     
    def get(self):
        return InstgaramRequest.handle(self.username)

class InstgaramRequest:

    headers = {
        'Host': 'www.instagram.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'mid=XElpBwAEAAHVvXZ9-bmABmGC-_4r; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=cEeKYyXwwTtPAejF6rsTYNVy1EZOnWcz; ds_user_id=10880533397; sessionid=10880533397%3AVzOaopAVn5BxNi%3A15; rur=ASH; urlgen="{\"171.61.79.229\": 24560\054 \"122.179.34.235\": 24560\054 \"122.171.212.137\": 24560}:1guGz6:tRUNYasgVnyaTn-AObx8ve34JY4"',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

    @classmethod
    def handle(self, username):
        url = 'https://www.instagram.com/%s/?__a=1' % username
        response =  requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.content
        else:
            return None

    