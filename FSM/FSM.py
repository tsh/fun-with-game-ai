class Locations:
    GOLDMINE = 0
    BANK = 10
    SHACK = 20
    SALOON = 30

class BaseGameEntity:
    def update(self):
        raise NotImplementedError


class State:
    def enter(self, miner):
        raise NotImplementedError

    def execute(self, miner):
        raise NotImplementedError

    def exit(self, miner):
        raise NotImplementedError


class EnterMineAndDigForNugget(State):
    def enter(self, miner):
        if miner.location != Locations.GOLDMINE:
            print("Walkin' to the goldmine")
            miner.location = Locations.GOLDMINE

    def execute(self, miner):
        miner.gold_carried += 1
        miner.fatigue += 1
        print("Pickin' up a nugget")
        if miner.is_pockets_full():
            miner.change_state(VisitBankAndDepositGold())
        elif miner.is_thirsty():
            miner.change_state(QuenchThirst())

    def exit(self, miner):
        print("Ah'm leavin' the goldmine with mah pockets full o' sweet gold")


class VisitBankAndDepositGold(State):
    def enter(self, miner):
        print("Goin' to the bank. Yes siree")
        miner.location = Locations.BANK

    def execute(self, miner):
        miner.money_in_bank += miner.gold_carried
        miner.gold_carried = 0
        print("Depositing gold. Total savings now: ", miner.money_in_bank)

        if miner.money_in_bank >= miner.MONEY_COMFORT_LEVEL:
            print("WooHoo! Rich enough for now. Back home to mah li'lle lady")
            miner.change_state(GoHomeSleepTillRested())
        else:
            miner.change_state(EnterMineAndDigForNugget())

    def exit(self, miner):
        print("Leavin' the bank")


class GoHomeSleepTillRested(State):
    def enter(self, miner):
        print("Walkin' home")
        miner.location = Locations.SHACK

    def execute(self, miner):
        if not miner.is_fatigued():
            print("What a God darn fantastic nap! Time to find more gold")
            miner.change_state(EnterMineAndDigForNugget())
        else:
            miner.fatigue -= 1
            print("Zzzz...")

    def exit(self, miner):
        print("Leaving the house")


class QuenchThirst(State):
    def enter(self, miner):
        miner.location = Locations.SALOON
        print("Boy, ah sure is thusty! Walking to the saloon")

    def execute(self, miner):
        if (miner.is_thirsty()):
            miner.thirst = 0
            print("That's mighty fine sippin liquer")
            miner.change_state(EnterMineAndDigForNugget())

    def exit(self, miner):
        print("Leaving the saloon, feelin' good")


class Miner(BaseGameEntity):
    THIRST_LEVEL = 10
    FATIGUE_LEVEL = 10
    MONEY_COMFORT_LEVEL = 12
    POCKET_CAPACITY = 6

    def __init__(self):
        self.current_state = GoHomeSleepTillRested()
        self.location = Locations.SHACK
        self.gold_carried = 0
        self.money_in_bank = 0
        self.thirst = 0
        self.fatigue = 0

    def change_state(self, state: State):
        self.current_state.exit(self)
        self.current_state = state
        self.current_state.enter(self)

    def is_thirsty(self):
        return self.thirst >= self.THIRST_LEVEL

    def is_fatigued(self):
        return self.fatigue >= self.FATIGUE_LEVEL

    def is_pockets_full(self):
        return self.gold_carried >= self.POCKET_CAPACITY

    def update(self):
        self.thirst += 1
        self.current_state.execute(self)


if __name__ == "__main__":
    miner = Miner()
    for _ in range(20):
        miner.update()

