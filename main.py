import json
from random import randint
from datetime import datetime
import argparse


parser = argparse.ArgumentParser(description='''Giveway Random Comment. This is an idea of morrolinux''',
    epilog="""All's well that ends well.""")
parser.add_argument('--time', type=int, default=42, help='FOO!')
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
args=parser.parse_args()


with open("comments.json") as json_file:
	time_limit = datetime.strptime("2020-08-08T23:59:59Z", "%Y-%m-%dT%H:%M:%SZ")
	comments = json.load(json_file)
	while True:
		comment = comments[randint(0, len(comments) - 1)]
		comment_date = comment["publishedAt"]
		if datetime.strptime(comment_date, "%Y-%m-%dT%H:%M:%SZ") > time_limit:
			continue
		if "#babbonatalenonesiste" not in comment["textOriginal"]:
			continue
		print("The WINNER IS: ", comment["authorDisplayName"], "\n", "\"%s\"" % comment["textOriginal"], "\n", comment["authorChannelUrl"])
		break 				
