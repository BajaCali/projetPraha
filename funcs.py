def get_stop_id_by_name(name, stops): # returns <stop_id> from name of the stop
	for stop in stops:
		if (stop["stop_name"] == name):
			return stop["stop_id"]
	return None

def get_trip_ids_by_stop_id(stop_id, stop_times): # returns list of <trip_id>s which stops at the stop with given stop_id
	trip_ids = []
	for trip in trips:
		if (stop_id == trip["stop_id"]):
			trip_ids.append(trip["trip_id"])
	if (trip_ids == []):
		return None
	return trip_ids

def get_route_id_by_trip_id(trip_id, trips): # returns <route_id> of given trip_id
	for trip in trips:
		if (trip_id == trip['trip_id']):
			return trip['route_id']
	return None

def get_stop_ids_with_times_by_trip_id(trip_id, stop_times): # returns dics, where value is list with times and keys are <stop_id>s
	stop_ids_with_times = {}
	for i in range(len(stop_times)):
		if stop_times[i+1]['trip_id'] == trip_id:
			if stop_times[i+1]['stop_id'] not in stop_ids_with_times.keys():
				stop_ids_with_times[stop_times[i+1]['stop_id']] = []
			stop_ids_with_times[stop_times[i+1]['stop_id']].append(stop_times[i+1]['departure_time'])
	if not stop_ids_with_times:
		return None
	return stop_ids_with_times

def get_time(trip_id, stop_id, stop_times): # returns (arrival_time, departure_time) on given <stop_id> and <trip_id>
	for time in stop_times:
		if (time['stop_id'] == stop_id and time['trip_id'] == trip_id):
			return (time['arrival_time'], time['departure_time'])
	return None

def get_times(trip_ids, stop_id, stop_times): # retruns list of tuples of times on given <stop_id> and list of trip_ids
	return [get_time(trip, stop_id, stop_times) for trip in trip_ids]

def get_stop_with_times(trips_ids, stop_id, stop_times): # returns (stop_id, [times])
	return (stop_id, get_times(trip_ids, stop_id, stop_times))

def get_list_of_next_stops_with_times(trips_ids, next_stop_ids, stop_times):
	return [get_stop_with_times(trips_ids, stop_id, stop_times) for stop_id in next_stop_ids]

def get_dict_of_lines_stopsAndTimes(lines, ):
	return {}


# create_struct(stop_id, data):
#	routes, trips = get_route_ids_and_trip_ids(stop_id, stop_times)
#	next_stops = get_next_stops(stop_id, trips)
#	out = {}
#	for route in routes:
#		for stop in next_stops:
#			out[route].append((stop, get_times(route, stop, trips)
#	return out

