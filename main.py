from api import Instagram

if __name__== "__main__":
  instagram = Instagram.details('amazon')
  print instagram.business_email

#   instagram = Instagram.posts('mohanraj12mca14')
#   print instagram.get()

#   instagram = Instagram.followers('mohanraj12mca14')
#   print instagram.get()