import requests as rq

class YtrClient:
	def __init__(self, key):
		self.key = key


	def get_languages(self):
		res = rq.get("https://translate.yandex.net/api/v1.5/tr.json/getLangs", {"key": self.key})
		return res.json()


	def translate(self, text, lang="en-ru"):
		res = rq.get("https://translate.yandex.net/api/v1.5/tr.json/translate", {"key": self.key, "text": text, "lang": lang})
		return res.json()["text"]

