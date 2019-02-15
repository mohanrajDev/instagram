import requests

class InstgaramRequest:

    headers1 = {
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

    headers2 = {
        'Host': 'www.instagram.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'mid=XF73AAAEAAFHkoCzqWUVZAXJXFY5; csrftoken=W6iMgtUbDS0OVZcwhgpTWcwGanWaqsDk; mcd=3; ds_user_id=10712799216; sessionid=10712799216%3AMiPKQDa16D5Ewh%3A22; rur=FRC; urlgen="{\"103.253.168.197\": 133011}:1guL8x:A-fImrgEVX_1jDccDRd2h_m_UwU"',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers'
    }

    @classmethod
    def profile(self, username):
        url = 'https://www.instagram.com/%s/?__a=1' % username
        response =  requests.get(url, headers=self.headers1)
        if response.status_code == 200:
            return response.content
        else:
            return None

    @classmethod
    def followers(self, profile_id, end_cursor):
        url = 'https://www.instagram.com/graphql/query/?query_hash=56066f031e6239f35a904ac20c9f37d9&variables={"id":"' + str(profile_id) +'","include_reel":true,"fetch_mutual":false,"first":50,"after":"' + end_cursor + '"}'
        print(url)
        response =  requests.get(url, headers=self.headers1)
        print(response)
        if response.status_code == 200:
            return response.content
        else:
            return None

    
    @classmethod
    def follows(self, profile_id, end_cursor):
        url = 'https://www.instagram.com/graphql/query/?query_hash=c56ee0ae1f89cdbd1c89e2bc6b8f3d18&variables={"id":"' + str(profile_id) +'","include_reel":true,"fetch_mutual":false,"first":50,"after":"' + end_cursor + '"}'
        print(url)
        response =  requests.get(url, headers=self.headers1)
        print(response)
        if response.status_code == 200:
            return response.content
        else:
            return None


# https://www.instagram.com/graphql/query/?query_hash=c56ee0ae1f89cdbd1c89e2bc6b8f3d18&variables={"id":"' + str(profile_id) +'","include_reel":true,"fetch_mutual":false,"first":50,"after":"' + + '"}