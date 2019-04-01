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

