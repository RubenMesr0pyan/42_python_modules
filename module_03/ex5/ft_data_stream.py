import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
               "release", "use"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(event_list: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event
        

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(stream))
    print(f"Built list of 10 events: {ten_events}")
    consumer = consume_event(ten_events)
    for event in consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")
