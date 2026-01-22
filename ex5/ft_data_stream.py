players = [{"name": "alice", "level": 0}, {"name": "bob", "level": 0}, {"name": "charlie", "level": 0}]
event_type = [{'txt': 'killed monster', 'count': 0}, {'txt': 'leveled up', 'count': 0}, {'txt': 'found treasure', 'count': 0}]

def event_generator(n: int):
	global players
	global event_type

	i = 0
	for i in range(n):
		iter_event = event_type[i % 3]
		iter_event["count"] += 1

		yield {
			"id": i + 1,
			"type": iter_event,
			"player": players[i % 3]
		}


def main()-> None:
	print("=== Game Data Stream Processor ===\n")

	n_events = 1000
	print(f"Processing {n_events} game events...\n")

	event_list = event_generator(n_events)
	for event in event_list:
		# if event["id"] == 4:
		# 	print("...\n")
		# 	break
		print(f"Event {event["id"]}: "
			  f"Player : {event["player"]["name"]} (level {event["player"]["level"]}) "
			  f"{event["type"]["txt"]}")

	global players
	global event_type

	print(players)
	print()
	print(event_type)


if __name__ == "__main__":
	main()
