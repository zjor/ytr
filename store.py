import requests as rq

BASE_URL = "https://api.airtable.com/v0/app1Nw2F1MCWi55W9/ytr"

class Store:
	def __init__(self, key):
		self.key = key

	def create(self, text, translation):
		data = {
			"records": [
				{
					"fields": {
						"text": text,
						"translation": translation
					}
				}
			]
		}
		res = rq.post(BASE_URL, params={"api_key": self.key}, json=data)		


	def list(self):
		res = rq.get(BASE_URL, params={"api_key": self.key})
		return res.json()




