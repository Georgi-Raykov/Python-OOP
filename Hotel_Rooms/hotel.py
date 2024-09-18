from Hotel_Rooms.room import Room


class Hotel:

    def __init__(self, name):

        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):

        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):

        room = self.find_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.find_room_by_number(room_number)
        result = room.free_room
        if result:
            return result
        self.guests -= room.guests

    def find_room_by_number(self, number):

        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def status(self):
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken]
        free_rooms = [str(x.number) for x in self.rooms if not x.is_taken]

        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 + f"Free rooms: {', '.join(free_rooms)}\n" + f"Taken rooms: {', '.join(taken_rooms)}"
        return result
