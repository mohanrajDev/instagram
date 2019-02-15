from api import Instagram

if __name__== "__main__":
  
  profiles = ['mohanraj12mca14', 'cyb3rs4k1', 'ramnath_sesaya', 'mohanrajmrrp', 'chinmayidash']

  # profiles = [6909766576, 7777225224, 1615882500, 8310027871, 4398363219]  

  # instagram = Instagram.getProfile('mohanraj12mca14')
  # print(instagram.profile)

  for profile in profiles:  
    print('//////////////////////////////////////////////')
    print(profile)
    print('//////////////////////////////////////////////')
    next = True
    cursor = ''
    # profile = 1615882500
    i = 1
    followers = []
    while(next):
      instagram = Instagram.getFollows(profile=profile, cursor=cursor)
      followers = followers + instagram.follower_ids
      next = instagram.next
      cursor = instagram.cursor
      print('*****%d*****' % i)
      i = i + 1

    print(len(followers))


  # instagram = Instagram.getFollows(profile='mohanraj12mca14', cursor="")
  # print(instagram)

  