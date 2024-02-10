import requests
import json

API = ""

class HiruNews:
  def New():
    info = requests.get(API).json()
    title = info["title"]
    description = info["description"]
    date = info["date"]
    image = info["image"]
    return image, title, description, date
