from mana import Mana

STANDARD_STARTING_LIFE = 20
COMMANDER_STARTING_LIFE = 40

class Player:
    def __init__(self, deck):
        self.life = COMMANDER_STARTING_LIFE
        
        self.library = deck
        self.hand
        self.graveyard
        self.exile
        self.command_zone

        self.lands_per_turn = 1

        self.mana = {
            Mana['WHITE']: 0,
            Mana['RED']: 0,
            Mana['BLACK']: 0,
            Mana['RED']: 0,
            Mana['GREEN']: 0,
            Mana['COLORLESS']: 0
        }
    