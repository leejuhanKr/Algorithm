from sys import stdin

from operator import attrgetter


def preprocess_input():
    N, M = map(int, stdin.readline().split())
    room_names = [stdin.readline().rstrip() for _ in range(N)]
    reservations = []
    for _ in range(M):
        name, start, end = stdin.readline().split()
        reservations.append((name, int(start), int(end)))
    return room_names, reservations


def solution():
    room_names, reservations = preprocess_input()

    rooms = {name: Room(name) for name in room_names}

    for name, start, end in reservations:
        rooms[name].reserve(start, end)

    return "\n-----\n".join(
        (str(room) for room in sorted(rooms.values(), key=attrgetter("name")))
    )


class Room:
    def __init__(self, name, start=9, end=18):
        self.name = name
        self.start = start
        self.end = end
        self.status = [True] * 24

    def reserve(self, start, end):
        for i in range(start, end):
            self.status[i] = False

    def _group_time(self):
        status, start_idx, end_idx = self.status, self.start, self.end

        time_group = []
        time = []
        for i, available in enumerate(status[start_idx:end_idx], start_idx):
            if available:
                if not time:
                    time.extend([i, i])
                else:
                    time[1] = i
            else:
                if time:
                    time_group.append(time)
                    time = []
        if time:
            time_group.append(time)

        return time_group

    @staticmethod
    def _pretty_time_delta(time_tuple):
        start, end = time_tuple
        return f"{start:0>2}-{end+1:0>2}"

    def __str__(self):
        time_group = self._group_time()
        room_info = (
            "\n".join(
                [
                    f"{len(time_group)} available:",
                    *map(self._pretty_time_delta, time_group),
                ]
            )
            if time_group
            else "Not available"
        )

        return f"Room {self.name}:\n{room_info}"


answer = solution()
print(answer)
