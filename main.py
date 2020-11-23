import requests

API_TOKEN = "<Your VK Token>"
API_VERSION = "5.126"

class User:

  def __init__(self, user_id):
    self.user_id = user_id

  def __and__(self, other):
    result = requests.get(
      "https://api.vk.com/method/friends.getMutual",
      params={
        "source_uid": self.user_id,
        "target_uid": other.user_id,
        "access_token": API_TOKEN,
        "v": API_VERSION
      }
    )
    response = result.json()["response"]
    return [User(user_id) for user_id in response]

  def __str__(self):
    user_page = "https://vk.com/id" + str(self.user_id)
    return user_page

  def __repr__(self):
     return "<User {} >".format(self)

vk_test = User('<Your VK ID>')
vk_test2 = User('<Vk ID>')
print(vk_test & vk_test2)
print(vk_test)