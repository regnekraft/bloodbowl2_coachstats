class Race_model:
    def __init__(self, race):
        self.race = race
        self.total_matches = 0
        self.total_tds = 0
        self.total_cas = 0
        self.running_meters = 0
        self.passing_meters = 0
        self.results = {'Human':[0, 0, 0, 0, 0], "Dwarf":[0, 0, 0, 0, 0], "Skaven":[0, 0, 0, 0, 0], "Orc":[0, 0, 0, 0, 0], "Lizardmen":[0, 0, 0, 0, 0],
                        "Goblin":[0, 0, 0, 0, 0], "Wood Elf":[0, 0, 0, 0, 0], "Chaos":[0, 0, 0, 0, 0], "Dark Elf":[0, 0, 0, 0, 0], "Undead":[0, 0, 0, 0, 0],
                        "Halfling":[0, 0, 0, 0, 0], "Norse":[0, 0, 0, 0, 0], "Amazon":[0, 0, 0, 0, 0], "Elven Union":[0, 0, 0, 0, 0],
                        "High Elf":[0, 0, 0, 0, 0], "Khemri":[0, 0, 0, 0, 0], "Necromantic":[0, 0, 0, 0, 0], "Nurgle":[0, 0, 0, 0, 0],
                        "Ogre":[0, 0, 0, 0, 0], "Vampire":[0, 0, 0, 0, 0], "Chaos Dwarf":[0, 0, 0, 0, 0], "Underworld":[0, 0, 0, 0, 0],
                        "Bretonians":[0, 0, 0, 0, 0], "Slann":[0, 0, 0, 0, 0]}

    def add_result(self, race, match):
        result = self.results[race]
        if match.match_result == "Won":
            result[0] += 1
        elif match.match_result == "Draw":
            result[1] += 1
        else:
            result[2] += 1

        if match.conceed == 1:
            result[3] += 1
        if match.conceed_opp == 1:
            result[4] += 1