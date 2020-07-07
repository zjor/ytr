#!/usr/bin/env python3

from settings import YATR_KEY
from ytr_client import YtrClient

client = YtrClient(YATR_KEY)


print(client.translate("hello world"))
