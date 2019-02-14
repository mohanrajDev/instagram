import json

from instagram_request import InstgaramRequest


class InstagramFactory:
    __instance = None

    def __init__(self, username):
        self.username = username

    @classmethod
    def handle(self, username):
        self.__instance = InstagramFactory(username)
        response = InstgaramRequest.profile(username)
        api_data = json.loads(response)
        self.raw_profile = api_data['graphql']['user']

        self.id = self.raw_profile['id']
        self.name = self.raw_profile['full_name']
        self.biography = self.raw_profile['biography']
        self.profile_pic_url = self.raw_profile['profile_pic_url']
        self.profile_pic_url_hd = self.raw_profile['profile_pic_url_hd']
        self.website_url = self.raw_profile['external_url']
        self.followers = self.raw_profile['edge_followed_by']['count']
        self.follow = self.raw_profile['edge_follow']['count']
        self.business_email = self.raw_profile['business_email']
        self.business_phone_number = self.raw_profile['business_phone_number']
        self.is_private = self.raw_profile['is_private']
        self.is_verified = self.raw_profile['is_verified']
        self.profile = {
            "id": self.id,
            "name": self.name,
            "biography": self.biography,
            "profile_pic_url": self.profile_pic_url,
            "profile_pic_url_hd": self.profile_pic_url_hd,
            "website_url": self.website_url,
            "followers": self.followers,
            "follow": self.follow,
            "business_email": self.business_email,
            "business_phone_number": self.business_phone_number,
            "is_private": self.is_private,
            "is_verified": self.is_verified
        }
            
        return self.__instance
