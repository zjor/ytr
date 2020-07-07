#!/usr/bin/env python3

import requests as rq

from settings import YATR_KEY


def get_languages():
	res = rq.get("https://translate.yandex.net/api/v1.5/tr.json/getLangs", {"key": YATR_KEY})
	return res.json()


def translate(text, lang="en-ru"):
	res = rq.get("https://translate.yandex.net/api/v1.5/tr.json/translate", {"key": YATR_KEY, "text": text, "lang": lang})
	return res.json()["text"]

print(translate("hello world"))
