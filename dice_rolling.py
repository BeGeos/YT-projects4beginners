import random
from scipy import stats


class Dice:

    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)


class Game:
    all_dices = []
    throw_log = {}

    def __init__(self, dices, faces):
        self.dices = dices
        self.faces = faces

    def _create_dice(self):
        if self.dices == 0:
            return "You can't play with no dice"

        for i in range(0, self.dices):
            dice = Dice(self.faces)
            self.all_dices.append(dice)

    def play(self):
        self._create_dice()
        output = 0
        counter = 0

        for i in self.all_dices:
            throw = i.roll()
            output += throw
            counter += 1
            self.throw_log[f"Dice {counter}"] = throw

        print(self.throw_log)
        return output


def log_dice_throws(throws):
    if throws == 0:
        return 0

    dice = Dice(6)
    dice_count = {}

    for i in range(throws):
        throw = dice.roll()
        dice_count[throw] = dice_count.get(throw, 0) + 1

    return dice_count


def chi_squared(throw_log, n_throws):

    expected_value = n_throws / len(throw_log)
    alpha_value = 0.05
    DF = 5

    CHI_SQUARED = 0

    for number, frequency in throw_log.items():
        differential = ((frequency - expected_value)**2) / expected_value
        CHI_SQUARED += differential

    p_value = 1 - stats.chi2.cdf(CHI_SQUARED, DF)

    if p_value <= alpha_value:
        return f"The p-value is {p_value}. There is 95% chance the dice is biased"
    else:
        return f"The p-value is {p_value}. There is no evidence to reject the null hypothesis"


log = log_dice_throws(100)
print(chi_squared(log, 100))



