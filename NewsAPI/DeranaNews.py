import requests
import json

API = ""

class DeranaNews:
  def New():
    info = requests.get(API).json()
    title = info["title"]
    description = info["description"]
    date = info["date"]
    image = info["image"]
    if image == "None" or image == None:
      image = None
    return image, title, description, date
