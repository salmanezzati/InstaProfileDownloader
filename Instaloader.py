import instaloader

l = instaloader.Instaloader()
l.login('salmanezzati', '123456789') # Instagram user and password
profile = instaloader.Profile.from_username(l.context, 'salmanezzati')

print(profile.followers)
print(profile.followees)
print(profile.get_profile_pic_url())
print(profile.is_private)
print(profile.is_verified)
print(profile.biography)

for post in profile.get_posts():
    print(post.caption)
    print('----------')

for i in profile.get_similar_accounts():
    print(i.username)


