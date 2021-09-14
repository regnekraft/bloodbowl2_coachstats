class Match_model:
    def __init__(self, p1_race, p2_race, td_plus, td_minus, cas_plus, cas_minus):
        self.races = {'1':'Human', '2':"Dwarf", '3':"Skaven", '4':"Orc", '5':"Lizardmen",
                    '6':"Goblin", '7':"Wood Elf", '8':"Chaos", '9':"Dark Elf", '10':"Undead",
                    '11':"Halfling", '12':"Norse", '13':"Amazon", '14':"Elven Union",
                    '15':"High Elf", '16':"Khemri", '17':"Necromantic", '18':"Nurgle",
                    '19':"Ogre", '20':"Vampire", '21':"Chaos Dwarf", '22':"Underworld",
                    '24':"Bretonians", '25':"Slann"}
        self.race = self.races[p1_race]
        self.opponent_race = self.races[p2_race]
        self.td_plus = int(td_plus)
        self.td_minus = int(td_minus)
        self.cas_plus = int(cas_plus)
        self.cas_minus = int(cas_minus)
        #self.res = int(td_plus) - int(td_minus)

    def as_dict(self):
        return {'race': self.race, 'opponent_race': self.opponent_race, 'td_plus': self.td_plus, 
                'td_minus': self.td_minus, 'cas_plus': self.cas_plus, 'cas_minus': self.cas_minus}
                #,'res': self.res}