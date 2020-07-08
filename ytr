#!/usr/bin/env python3

import click

from settings import YATR_KEY
from ytr_client import YtrClient

client = YtrClient(YATR_KEY)

@click.command()
@click.argument('text')
def main(text):
	ts = client.translate(text)
	if len(ts) > 0:
		print(f"{text} - {ts[0]}")
	else:
		print("No translation available")


if __name__ == "__main__":
	main()
