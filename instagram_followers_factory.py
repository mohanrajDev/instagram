from instagram_request import InstgaramRequest
import json

class InstagramFollowersFactory:

    __instance = None

    def __init__(self, profile_id):
        self.profile_id = profile_id   
     
    @classmethod
    def get(self, profile_id, end_cursor):
        self.__instance = InstagramFollowersFactory(profile_id)
        # response = InstgaramRequest.followers(profile_id, end_cursor)
        response = InstgaramRequest.follows(profile_id, end_cursor)
        api_data = json.loads(response)
        # self.raw_followers = api_data['data']['user']['edge_followed_by']
        self.raw_followers = api_data['data']['user']['edge_follow']

        self.next = self.raw_followers['page_info']['has_next_page']
        self.cursor = self.raw_followers['page_info']['end_cursor']
        self.followers = []
        self.follower_ids = []
        self.follower_names = []
        follower = {}
        for current_page_follower in self.raw_followers['edges']:
            node = current_page_follower['node']
            follower['id'] = node['id']
            follower['username'] = node['username']
            follower['full_name'] = node['full_name']
            follower['profile_pic_url'] = node['profile_pic_url']

            self.followers.append(follower)
            self.follower_ids.append(node['id'])
            self.follower_names.append(node['username'])
             
        return self.__instance