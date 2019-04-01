#!/usr/bin/python3


from parse import parse_file

trips = parse_file("trips.txt")
calendar = parse_file("calendar.txt")


def filter_day(day,calendar,trips):
	services = list(map(lambda x: x["service_id"], filter(lambda x: x[day] == '1', calendar)))
	return list(filter(lambda t: t["service_id"] in services, trips))

print(len(trips))
trips = (filter_day('monday',calendar,trips))
print(len(trips))
print(trips[0])
