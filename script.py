from TikTokApi import TikTokApi
api = TikTokApi()

results = 10

trending = api.discoverMusic()
print(trending[0]['cardItem']['id'])
print(api.getMusicObject(id=trending[0]['cardItem']['id']))
print(len(trending))
