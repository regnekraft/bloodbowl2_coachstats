class Coach_model:
    def __init__(self):
        self.matches = {'Human':[], "Dwarf":[], "Skaven":[], "Orc":[], "Lizardmen":[],
                    "Goblin":[], "Wood Elf":[], "Chaos":[], "Dark Elf":[], "Undead":[],
                    "Halfling":[], "Norse":[], "Amazon":[], "Elven Union":[],
                    "High Elf":[], "Khemri":[], "Necromantic":[], "Nurgle":[],
                    "Ogre":[], "Vampire":[], "Chaos Dwarf":[], "Underworld":[],
                    "Bretonians":[], "Slann":[]}
        self.results = {'Human':[0, 0, 0, 0, 0], "Dwarf":[0, 0, 0, 0, 0], "Skaven":[0, 0, 0, 0, 0], "Orc":[0, 0, 0, 0, 0], "Lizardmen":[0, 0, 0, 0, 0],
                    "Goblin":[0, 0, 0, 0, 0], "Wood Elf":[0, 0, 0, 0, 0], "Chaos":[0, 0, 0, 0, 0], "Dark Elf":[0, 0, 0, 0, 0], "Undead":[0, 0, 0, 0, 0],
                    "Halfling":[0, 0, 0, 0, 0], "Norse":[0, 0, 0, 0, 0], "Amazon":[0, 0, 0, 0, 0], "Elven Union":[0, 0, 0, 0, 0],
                    "High Elf":[0, 0, 0, 0, 0], "Khemri":[0, 0, 0, 0, 0], "Necromantic":[0, 0, 0, 0, 0], "Nurgle":[0, 0, 0, 0, 0],
                    "Ogre":[0, 0, 0, 0, 0], "Vampire":[0, 0, 0, 0, 0], "Chaos Dwarf":[0, 0, 0, 0, 0], "Underworld":[0, 0, 0, 0, 0],
                    "Bretonians":[0, 0, 0, 0, 0], "Slann":[0, 0, 0, 0, 0]}

    def add_match(self, race, match):
        matches_list = self.matches[race]
        matches_list.append(match)
        result = self.results[race]
        if match.result == "Won":
            result[0] += 1
        elif match.result == "Draw":
            result[1] += 1
        else:
            result[2] += 1

        if match.own_conceed == 1:
            result[3] += 1
        if match.opp_conceeded == 1:
            result[4] += 1

    def print_top_stats(self):
        totales = 0
        for key in self.results:
            race_name = key
            match_stats = self.results[key]
            w = match_stats[0]
            d = match_stats[1]
            l = match_stats[2]
            t = w + d + l
            totales += t
            win_percentage = "{:.2%}".format((w + (d / 2)) / t)
            conceeds_with = "{:.2%}".format(match_stats[3] / t)
            conceed_against = "{:.2%}".format(match_stats[4] / t)
            print(race_name, 'Matches:', t, "-", win_percentage, "| Times conceeded:", conceeds_with, " - times opponents conceeded:", conceed_against)
        print(totales)



