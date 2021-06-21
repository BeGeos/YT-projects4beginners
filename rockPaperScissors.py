import random


def is_winner(p1, p2):
    if p1 == "rock" and p2 == "scissors":
        return True
    if p1 == "paper" and p2 == "rock":
        return True
    if p1 == "scissors" and p2 == "paper":
        return True
    return False


def is_winner_rpsls(p1, p2):
    if p1 == "rock" and (p2 == "scissors" or p2 == "lizard"):
        return True
    if p1 == "paper" and (p2 == "rock" or p2 == "spock"):
        return True
    if p1 == "scissors" and (p2 == "paper" or p2 == "lizard"):
        return True
    if p1 == "lizard" and (p2 == "paper" or p2 == "spock"):
        return True
    if p1 == "spock" and (p2 == "scissors" or p2 == "rock"):
        return True
    return False


class Player:
    moves = ["rock", "paper", "scissors", "lizard", "spock"]
    rules = {
        "rock": ["paper", "spock"],
        "paper": ["scissors", "lizard"],
        "scissors": ["rock", "spock"],
        "lizard": ["scissors", "rock"],
        "spock": ["lizard", "paper"]
    }

    def __init__(self, name):
        self.name = name
        self.memory = []

    def pick(self):
        return random.choice(self.moves)

    def remember(self, move):
        if len(self.memory) >= 10:
            self.memory.remove(self.memory[0])
        self.memory.append(move)

    def _count(self):
        counter = {}

        for move in self.memory:
            counter[move] = counter.get(move, 0) + 1

        return counter

    def _calculate(self):
        count = self._count()

        lowest = ("dummy", 0)

        # Process the count
        processed = {
            "rock": 1 - (count.get("rock", 0.08) / 10),
            "paper": 1 - (count.get("paper", 0.08) / 10),
            "scissors": 1 - (count.get("scissors", 0.08) / 10),
            "lizard": 1 - (count.get("lizard", 0.08) / 10),
            "spock": 1 - (count.get("spock", 0.08) / 10)
        }

        for k, v in processed.items():
            if v > lowest[1]:
                lowest = (k, round(v, 2))
        return lowest

    def predict(self):
        probable_next_move = self._calculate()
        best_counter = random.choice(self.rules[probable_next_move[0]])
        return best_counter


class NormalPlayer:
    moves = ["rock", "paper", "scissors"]
    rules = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    def __init__(self, name):
        self.name = name
        self.memory = []

    def pick(self):
        return random.choice(self.moves)

    def remember(self, move):
        if len(self.memory) >= 10:
            self.memory.remove(self.memory[0])
        self.memory.append(move)

    def _count(self):
        counter = {}

        for move in self.memory:
            counter[move] = counter.get(move, 0) + 1

        return counter

    def _calculate(self):
        count = self._count()

        lowest = ("dummy", 0)

        # Process the count
        processed = {
            "rock": 1 - (count.get("rock", 0.08) / 10),
            "paper": 1 - (count.get("paper", 0.08) / 10),
            "scissors": 1 - (count.get("scissors", 0.08) / 10),
        }

        for k, v in processed.items():
            if v > lowest[1]:
                lowest = (k, round(v, 2))
        return lowest

    def predict(self):
        probable_next_move = self._calculate()
        return self.rules[probable_next_move[0]]


# Let's play

# p1_pick = p1.pick()
# p2_pick = p2.pick()
#
# if p1_pick == p2_pick:
#     print("It's a Tie!")
# elif is_winner(p1_pick, p2_pick):
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")


# Testing
def test_game(p1, p2, rounds):
    p1_score = 0
    p2_score = 0
    tie = 0

    for i in range(rounds):
        p1_pick = p1.pick()
        p2_pick = p2.pick()

        if p1_pick == p2_pick:
            tie += 1
        elif is_winner(p1_pick, p2_pick):
            p1_score += 1
        else:
            p2_score += 1

    print(f"{p1.name} has {round((p1_score / rounds) * 100)}% win rate. {p2.name} has "
          f"{round((p2_score / rounds) * 100)}% "
          f"win rate. And {round((tie / rounds) * 100)}% of the times it was a tie!")


# test_game(p1, p2, 100)


def new_test_game(p1, p2, rounds):
    p1_score = 0
    p2_score = 0
    tie = 0

    for i in range(rounds):
        if i >= 10:
            p1_pick = p1.predict()
            p2_pick = p2.predict()
        else:
            p1_pick = p1.pick()
            p2_pick = p2.pick()

        p1.remember(p2_pick)
        p2.remember(p1_pick)

        # Check which player won
        if p1_pick == p2_pick:
            tie += 1
        elif is_winner(p1_pick, p2_pick):
            p1_score += 1
        else:
            p2_score += 1

    p1.memory = []
    p2.memory = []

    print(f"{p1.name} has {round((p1_score / rounds) * 100)}% win rate. {p2.name} has "
          f"{round((p2_score / rounds) * 100)}% "
          f"win rate. And {round((tie / rounds) * 100)}% of the times it was a tie!")

    return round((p1_score / rounds) * 100), round((p2_score / rounds) * 100), round((tie / rounds) * 100)


# new_test_game(p1, p2, 100)


p1 = Player("jack")
p2 = Player("john")


def new_test_game_rpsls(p1, p2, rounds):
    p1_score = 0
    p2_score = 0
    tie = 0

    for i in range(rounds):
        if i >= 10:
            p1_pick = p1.predict()
            p2_pick = p2.predict()
        else:
            p1_pick = p1.pick()
            p2_pick = p2.pick()

        p1.remember(p2_pick)
        p2.remember(p1_pick)

        # Check which player won
        if p1_pick == p2_pick:
            tie += 1
        elif is_winner_rpsls(p1_pick, p2_pick):
            p1_score += 1
        else:
            p2_score += 1

    p1.memory = []
    p2.memory = []

    print(f"{p1.name} has {round((p1_score / rounds) * 100)}% win rate. {p2.name} has "
          f"{round((p2_score / rounds) * 100)}% "
          f"win rate. And {round((tie / rounds) * 100)}% of the times it was a tie!")

    return round((p1_score / rounds) * 100), round((p2_score / rounds) * 100), round((tie / rounds) * 100)


new_test_game_rpsls(p1, p2, 100)


def test_total(rounds):
    normal_player = NormalPlayer("jack")
    normal_other = NormalPlayer("john")

    super_player = Player("sheldon")
    super_other = Player("raj")

    # Stats of normal Rock, Paper, Scissors
    p1_stats = []
    p2_stats = []
    tie_stats = []

    # Stats of Rock, Paper, Scissors, Lizard, Spock
    p1_mem_stats = []
    p2_mem_stats = []
    tie_mem_stats = []

    for i in range(rounds):
        rps_result = new_test_game(normal_player, normal_other, 100)
        rpsls_result = new_test_game_rpsls(super_player, super_other, 100)

        p1_stats.append(rps_result[0])
        p2_stats.append(rps_result[1])
        tie_stats.append(rps_result[2])

        p1_mem_stats.append(rpsls_result[0])
        p2_mem_stats.append(rpsls_result[1])
        tie_mem_stats.append(rpsls_result[2])

    p1_average = sum(p1_stats) // len(p1_stats)
    p2_average = sum(p2_stats) // len(p2_stats)
    tie_average = sum(tie_stats) // len(tie_stats)

    p1_average_mem = sum(p1_mem_stats) // len(p1_mem_stats)
    p2_average_mem = sum(p2_mem_stats) // len(p2_mem_stats)
    tie_average_mem = sum(tie_mem_stats) // len(tie_mem_stats)

    print(f"The averages for the normal game are:\n* Player 1 --> {p1_average}%"
          f"\n* Player 2 --> {p2_average}%\n* Tie --> {tie_average}%\n\n")

    print(f"The averages for the hyper game are:\n* Player 1 --> {p1_average_mem}%"
          f"\n* Player 2 --> {p2_average_mem}%\n* Tie --> {tie_average_mem}%")
    return


# test_total(100)
