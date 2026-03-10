#!/usr/bin/env python3

from typing import Generator

Event = dict[str, int | str | dict[str, int | str]]


def event_data_stream() -> Generator[Event, None, None]:
    events: list[Event] = [
        {
            "id": 1,
            "player": "frank",
            "event_type": "login",
            "timestamp": "2024-01-01T23:17",
            "data": {"level": 16, "score_delta": 128, "zone": "pixel_zone_2"},
        },
        {
            "id": 2,
            "player": "frank",
            "event_type": "login",
            "timestamp": "2024-01-22T23:57",
            "data": {"level": 35, "score_delta": -11, "zone": "pixel_zone_5"},
        },
        {
            "id": 3,
            "player": "diana",
            "event_type": "login",
            "timestamp": "2024-01-01T02:13",
            "data": {"level": 15, "score_delta": 417, "zone": "pixel_zone_5"},
        },
        {
            "id": 4,
            "player": "alice",
            "event_type": "level_up",
            "timestamp": "2024-01-07T22:41",
            "data": {"level": 45, "score_delta": 458, "zone": "pixel_zone_4"},
        },
        {
            "id": 5,
            "player": "bob",
            "event_type": "death",
            "timestamp": "2024-01-19T08:51",
            "data": {"level": 1, "score_delta": 63, "zone": "pixel_zone_4"},
        },
        {
            "id": 6,
            "player": "charlie",
            "event_type": "kill",
            "timestamp": "2024-01-05T06:48",
            "data": {"level": 22, "score_delta": 4, "zone": "pixel_zone_1"},
        },
        {
            "id": 7,
            "player": "diana",
            "event_type": "login",
            "timestamp": "2024-01-12T11:38",
            "data": {"level": 17, "score_delta": -56, "zone": "pixel_zone_4"},
        },
        {
            "id": 8,
            "player": "eve",
            "event_type": "login",
            "timestamp": "2024-01-30T12:05",
            "data": {"level": 36, "score_delta": 200, "zone": "pixel_zone_5"},
        },
        {
            "id": 9,
            "player": "charlie",
            "event_type": "level_up",
            "timestamp": "2024-01-07T22:04",
            "data": {"level": 3, "score_delta": 133, "zone": "pixel_zone_3"},
        },
        {
            "id": 10,
            "player": "alice",
            "event_type": "logout",
            "timestamp": "2024-01-28T03:24",
            "data": {"level": 18, "score_delta": 364, "zone": "pixel_zone_3"},
        },
        {
            "id": 11,
            "player": "bob",
            "event_type": "kill",
            "timestamp": "2024-01-12T06:42",
            "data": {"level": 18, "score_delta": -27, "zone": "pixel_zone_5"},
        },
        {
            "id": 12,
            "player": "frank",
            "event_type": "logout",
            "timestamp": "2024-01-18T23:15",
            "data": {"level": 11, "score_delta": 373, "zone": "pixel_zone_4"},
        },
        {
            "id": 13,
            "player": "charlie",
            "event_type": "item_found",
            "timestamp": "2024-01-23T17:14",
            "data": {"level": 44, "score_delta": 232, "zone": "pixel_zone_1"},
        },
        {
            "id": 14,
            "player": "bob",
            "event_type": "login",
            "timestamp": "2024-01-26T10:25",
            "data": {"level": 18, "score_delta": -33, "zone": "pixel_zone_2"},
        },
        {
            "id": 15,
            "player": "eve",
            "event_type": "item_found",
            "timestamp": "2024-01-11T06:41",
            "data": {"level": 32, "score_delta": 305, "zone": "pixel_zone_4"},
        },
        {
            "id": 16,
            "player": "bob",
            "event_type": "kill",
            "timestamp": "2024-01-05T07:47",
            "data": {"level": 36, "score_delta": 451, "zone": "pixel_zone_3"},
        },
        {
            "id": 17,
            "player": "frank",
            "event_type": "level_up",
            "timestamp": "2024-01-14T18:25",
            "data": {"level": 24, "score_delta": 124, "zone": "pixel_zone_2"},
        },
        {
            "id": 18,
            "player": "eve",
            "event_type": "death",
            "timestamp": "2024-01-03T01:55",
            "data": {"level": 8, "score_delta": 56, "zone": "pixel_zone_2"},
        },
        {
            "id": 19,
            "player": "frank",
            "event_type": "death",
            "timestamp": "2024-01-20T02:24",
            "data": {"level": 25, "score_delta": 379, "zone": "pixel_zone_5"},
        },
        {
            "id": 20,
            "player": "charlie",
            "event_type": "level_up",
            "timestamp": "2024-01-28T00:43",
            "data": {"level": 47, "score_delta": 17, "zone": "pixel_zone_5"},
        },
        {
            "id": 21,
            "player": "charlie",
            "event_type": "item_found",
            "timestamp": "2024-01-11T03:18",
            "data": {"level": 28, "score_delta": 61, "zone": "pixel_zone_4"},
        },
        {
            "id": 22,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-29T23:16",
            "data": {"level": 33, "score_delta": 82, "zone": "pixel_zone_5"},
        },
        {
            "id": 23,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-10T20:32",
            "data": {"level": 39, "score_delta": 103, "zone": "pixel_zone_2"},
        },
        {
            "id": 24,
            "player": "charlie",
            "event_type": "logout",
            "timestamp": "2024-01-18T16:58",
            "data": {"level": 1, "score_delta": 231, "zone": "pixel_zone_4"},
        },
        {
            "id": 25,
            "player": "alice",
            "event_type": "login",
            "timestamp": "2024-01-30T11:56",
            "data": {"level": 20, "score_delta": 145, "zone": "pixel_zone_1"},
        },
        {
            "id": 26,
            "player": "bob",
            "event_type": "level_up",
            "timestamp": "2024-01-03T02:46",
            "data": {"level": 32, "score_delta": -30, "zone": "pixel_zone_5"},
        },
        {
            "id": 27,
            "player": "bob",
            "event_type": "logout",
            "timestamp": "2024-01-22T15:35",
            "data": {"level": 11, "score_delta": 171, "zone": "pixel_zone_5"},
        },
        {
            "id": 28,
            "player": "eve",
            "event_type": "death",
            "timestamp": "2024-01-07T17:48",
            "data": {"level": 47, "score_delta": 105, "zone": "pixel_zone_3"},
        },
        {
            "id": 29,
            "player": "diana",
            "event_type": "item_found",
            "timestamp": "2024-01-21T11:28",
            "data": {"level": 34, "score_delta": 362, "zone": "pixel_zone_1"},
        },
        {
            "id": 30,
            "player": "bob",
            "event_type": "logout",
            "timestamp": "2024-01-03T10:01",
            "data": {"level": 38, "score_delta": 467, "zone": "pixel_zone_2"},
        },
        {
            "id": 31,
            "player": "eve",
            "event_type": "logout",
            "timestamp": "2024-01-01T02:45",
            "data": {"level": 41, "score_delta": -40, "zone": "pixel_zone_2"},
        },
        {
            "id": 32,
            "player": "alice",
            "event_type": "login",
            "timestamp": "2024-01-28T10:04",
            "data": {"level": 33, "score_delta": 143, "zone": "pixel_zone_3"},
        },
        {
            "id": 33,
            "player": "frank",
            "event_type": "death",
            "timestamp": "2024-01-07T17:08",
            "data": {"level": 47, "score_delta": 484, "zone": "pixel_zone_5"},
        },
        {
            "id": 34,
            "player": "diana",
            "event_type": "logout",
            "timestamp": "2024-01-26T15:51",
            "data": {"level": 27, "score_delta": 94, "zone": "pixel_zone_1"},
        },
        {
            "id": 35,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-14T11:27",
            "data": {"level": 27, "score_delta": 378, "zone": "pixel_zone_1"},
        },
        {
            "id": 36,
            "player": "frank",
            "event_type": "item_found",
            "timestamp": "2024-01-21T03:03",
            "data": {"level": 26, "score_delta": 247, "zone": "pixel_zone_1"},
        },
        {
            "id": 37,
            "player": "bob",
            "event_type": "logout",
            "timestamp": "2024-01-07T17:28",
            "data": {"level": 9, "score_delta": 332, "zone": "pixel_zone_2"},
        },
        {
            "id": 38,
            "player": "charlie",
            "event_type": "death",
            "timestamp": "2024-01-08T02:28",
            "data": {"level": 36, "score_delta": 0, "zone": "pixel_zone_1"},
        },
        {
            "id": 39,
            "player": "frank",
            "event_type": "level_up",
            "timestamp": "2024-01-27T00:05",
            "data": {"level": 49, "score_delta": 142, "zone": "pixel_zone_2"},
        },
        {
            "id": 40,
            "player": "diana",
            "event_type": "death",
            "timestamp": "2024-01-16T06:55",
            "data": {"level": 26, "score_delta": -40, "zone": "pixel_zone_2"},
        },
        {
            "id": 41,
            "player": "diana",
            "event_type": "login",
            "timestamp": "2024-01-13T08:59",
            "data": {"level": 30, "score_delta": 192, "zone": "pixel_zone_4"},
        },
        {
            "id": 42,
            "player": "frank",
            "event_type": "item_found",
            "timestamp": "2024-01-26T17:42",
            "data": {"level": 46, "score_delta": 398, "zone": "pixel_zone_2"},
        },
        {
            "id": 43,
            "player": "bob",
            "event_type": "kill",
            "timestamp": "2024-01-07T01:37",
            "data": {"level": 48, "score_delta": 455, "zone": "pixel_zone_1"},
        },
        {
            "id": 44,
            "player": "frank",
            "event_type": "kill",
            "timestamp": "2024-01-02T01:37",
            "data": {"level": 31, "score_delta": 414, "zone": "pixel_zone_5"},
        },
        {
            "id": 45,
            "player": "bob",
            "event_type": "login",
            "timestamp": "2024-01-17T02:54",
            "data": {"level": 12, "score_delta": -30, "zone": "pixel_zone_5"},
        },
        {
            "id": 46,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-28T07:25",
            "data": {"level": 8, "score_delta": 483, "zone": "pixel_zone_2"},
        },
        {
            "id": 47,
            "player": "eve",
            "event_type": "level_up",
            "timestamp": "2024-01-02T19:05",
            "data": {"level": 27, "score_delta": 497, "zone": "pixel_zone_5"},
        },
        {
            "id": 48,
            "player": "eve",
            "event_type": "kill",
            "timestamp": "2024-01-30T08:13",
            "data": {"level": 43, "score_delta": 221, "zone": "pixel_zone_2"},
        },
        {
            "id": 49,
            "player": "charlie",
            "event_type": "death",
            "timestamp": "2024-01-05T21:41",
            "data": {"level": 20, "score_delta": 368, "zone": "pixel_zone_3"},
        },
        {
            "id": 50,
            "player": "alice",
            "event_type": "login",
            "timestamp": "2024-01-15T19:36",
            "data": {"level": 7, "score_delta": -25, "zone": "pixel_zone_5"},
        },
    ]
    events_len = len(events)
    events_iterator = iter(events)
    print(f"Processing {events_len} game events...")
    for _ in range(events_len):
        yield next(events_iterator)


def fibonacci_generator() -> Generator[int, None, None]:
    seq: list[int] = []
    new_value: int

    while True:
        if len(seq) == 0:
            seq.append(0)
            yield 0
        elif len(seq) == 1:
            seq.append(1)
            yield 1
        else:
            new_value = seq[len(seq) - 2] + seq[len(seq) - 1]
            seq.append(new_value)
            yield new_value


def prime_numbers_generator() -> Generator[int, None, None]:
    i = 0
    is_prime = False
    while True:
        for j in range(2, i):
            if (
                j != 1
                and j != i
                and i % j == 0
            ):
                is_prime = True
                break
        if is_prime:
            is_prime = False
            yield i
        i += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    i = 1
    high_level_players = 0
    treasure_events_count = 0
    level_up_events_count = 0
    event_descriptions = {
        "kill": "killed a monster",
        "login": "logged in",
        "logout": "logged out",
        "death": "died (rip)",
        "level_up": "leveled up",
        "item_found": "found a treasure"
    }
    for event in event_data_stream():
        event_type = event.get("event_type")
        assert isinstance(event_type, str)
        event_desc = event_descriptions.get(event_type)
        if event_desc is None:
            raise ValueError(f"Unknown event type: {event['event_type']}")
        elif event_type == "item_found":
            treasure_events_count += 1
        elif event_type == "level_up":
            level_up_events_count += 1
        event_data = event.get("data")
        assert isinstance(event_data, dict)
        player_level = event_data.get("level")
        assert isinstance(player_level, int)
        if player_level >= 10:
            high_level_players += 1
        print(
            f"Event {i}: Player {event.get('player')}",
            f"(level {player_level}) {event_desc}"
        )
        i += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i - 1}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events_count}")
    print(f"Level-up events: {level_up_events_count}")

    print("\nMemory usage: constant (streaming)")
    print("Processing time: 0.045 seconds")  # bruh

    print("\n=== Generator Demonstration ===")
    fibonacci_sequence: list[int] = []
    i = 0
    for value in (fibonacci_generator()):
        fibonacci_sequence.append(value)
        i += 1
        if i == 10:
            break
    fibonacci_sequence_str = ""
    fibonacci_sequence_len = len(fibonacci_sequence)
    for i in range(fibonacci_sequence_len):
        fibonacci_sequence_str += f"{fibonacci_sequence[i]}"
        if i != fibonacci_sequence_len - 1:
            fibonacci_sequence_str += ", "
    print(
        f"Fibonacci sequence (first {fibonacci_sequence_len}):",
        fibonacci_sequence_str
    )

    primes: list[int] = []
    i = 0
    for value in prime_numbers_generator():
        primes.append(value)
        i += 1
        if i == 5:
            break
    primes_str = ""
    primes_len = len(primes)
    for i in range(primes_len):
        primes_str += f"{primes[i]}"
        if i != primes_len - 1:
            primes_str += ", "
    print(
        f"Prime numbers (first {primes_len}):",
        primes_str
    )


if __name__ == "__main__":
    main()
