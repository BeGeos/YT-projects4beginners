class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1


class Room:

    def __init__(self, name, corners, door):
        self.name = name
        self.bl = corners[0]
        self.tl = corners[1]
        self.tr = corners[2]
        self.br = corners[3]
        self.door = door


class House:

    def __init__(self, rooms, door):
        self.rooms = rooms
        self.door = door

    def can_move(self, x, y):
        if [x, y] == self.door:
            print("This is the main door!")
            return True

        for room in self.rooms:
            if [x, y] == room.door:
                print("There is a door! You may go in")
                return True
            if (room.bl[0] < x < room.tr[0]) and (room.bl[1] < y < room.tr[1]):
                print(f"You are in {room.name}")
                return True
            if ((x == room.bl[0] or x == room.br[0]) and y in range(room.bl[1], room.tl[1] + 1)) \
                    or ((y == room.bl[1] or y == room.tl[1]) and x in range(room.bl[0], room.br[0] + 1)):
                print("There is a wall in front of you!")
                return False
        print("You are in a corridor!")
        return True


kitchen = Room("kitchen", [[0, 0], [0, 4], [4, 4], [4, 0]], [4, 3])
living_room = Room("living room", [[6, 0], [6, 4], [8, 4], [8, 0]], [6, 2])
gaming_room = Room("gaming room", [[4, 6], [4, 10], [8, 10], [8, 6]], [7, 6])
bathroom = Room("bathroom", [[0, 8], [0, 10], [3, 10], [3, 8]], [1, 8])

house = House([kitchen, living_room, gaming_room, bathroom], [5, 0])

player = Player(house.door[0], house.door[1])

while True:
    move = input("Select your move: W (up), A (left), S (down), D (right)\n")
    if move.lower() == "w":
        if house.can_move(player.x, player.y + 1):
            player.move_up()
    if move.lower() == "s":
        if house.can_move(player.x, player.y - 1):
            player.move_down()
    if move.lower() == "a":
        if house.can_move(player.x - 1, player.y):
            player.move_left()
    if move.lower() == "d":
        if house.can_move(player.x + 1, player.y):
            player.move_right()



