from instagram_factory import InstagramFactory
from instagram_followers_factory import InstagramFollowersFactory

class Instagram:
    
    @classmethod
    def getProfile(self, username):
        return InstagramFactory.handle(username)

    @classmethod
    def getFollowers(self, profile, cursor):
        if not isinstance(profile, int):
           profile = InstagramFactory.handle(profile).id 

        return InstagramFollowersFactory.get(profile, cursor)





    