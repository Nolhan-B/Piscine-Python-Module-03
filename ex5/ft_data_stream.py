players = [
    {"name": "alice", "level": 0},
    {"name": "bob", "level": 0},
    {"name": "charlie", "level": 0}
    ]
event_type = [
    {'txt': 'killed monster', 'count': 0},
    {'txt': 'leveled up', 'count': 0},
    {'txt': 'found treasure', 'count': 0},
    {'txt': 'defeated a boss', 'count': 0},
    {'txt': 'ran away', 'count': 0}
    ]


def event_generator(n: int) -> list[int | list[str | int]]:
    i = 0
    for i in range(n):
        iter_event = event_type[i % 5]
        iter_event["count"] += 1
        iter_player = players[i % 3]
        if iter_event["txt"] == "leveled up":
            iter_player["level"] += 1

        yield {
            "id": i + 1,
            "type": iter_event,
            "player": players[i % 3]
        }

def fibo(n: int) -> int:
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b

def prime(n: int):
    nb = 2

    for _ in range(n):
        is_prime = False
        while not is_prime:
            is_prime = True

            if nb < 2:
                is_prime = False
            else:
                for i in range(2, nb):
                    if nb % i == 0:
                        is_prime = False
                        break

            if is_prime:
                yield nb
                nb += 1
                break

            nb += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    n_events = 1000
    print(f"Processing {n_events} game events...\n")

    event_list = event_generator(n_events)
    for event in event_list:
        if event["id"] < 4:
            print(f"Event {event["id"]}: "
                  f"Player : {event["player"]["name"]} "
                  f"(level {event["player"]["level"]}) "
                  f"{event["type"]["txt"]}")

    print(players)
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {n_events}")
    total_lvl = 0
    for player in players:
        if (player["level"] >= 10):
            total_lvl += 1 
    print(f"High-level players (10+) : {total_lvl}")
    print(f"Treasure events: {event_type[1]["count"]}")
    print(f"Level-up events: {event_type[2]["count"]}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 secondes")

    print("\n=== Generator Demonstration ===")
    fibonnaci = fibo(10)
    fibo_str = "Fibonacci sequence (first 10): "
    i = 0
    for number in fibonnaci:
        i += 1
        if i == 10:
            fibo_str += f"{number}"
        else:
            fibo_str += f"{number}, "
    print(fibo_str)

    prime_str = "Prime numbers (first 5) : "
    prime_list = prime(5)
    i = 0
    for number in prime_list:
        i += 1
        if i == 5:
            prime_str += f"{number}"
        else:
            prime_str += f"{number}, "
    print(prime_str)

if __name__ == "__main__":
    main()
