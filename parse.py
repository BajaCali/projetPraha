#!/usr/bin/python3

import csv

def parse_file(filename):
	with open(filename) as afile:
		reader = csv.DictReader(afile,delimiter=",")
		rows = [r for r in reader]
	return rows

routes = (parse_file("routes.txt"))
print(routes[0]["route_id"])



