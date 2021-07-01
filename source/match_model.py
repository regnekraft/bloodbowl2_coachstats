class Match_model:
    def __init__(self, coach_name, CoachHomeName, LeagueName, CompetitionName):
        
        self.home_coach = CoachHomeName.lower() == coach_name.lower()
        self.LeagueName = LeagueName
        self.CompetitionName = CompetitionName
        self.races = {'1':'Human', '2':"Dwarf", '3':"Skaven", '4':"Orc", '5':"Lizardmen",
                    '6':"Goblin", '7':"Wood Elf", '8':"Chaos", '9':"Dark Elf", '10':"Undead",
                    '11':"Halfling", '12':"Norse", '13':"Amazon", '14':"Elven Union",
                    '15':"High Elf", '16':"Khemri", '17':"Necromantic", '18':"Nurgle",
                    '19':"Ogre", '20':"Vampire", '21':"Chaos Dwarf", '22':"Underworld",
                    '24':"Bretonians", '25':"Slann"}

    def set_overall_data(self, IdCoachHomeCompletionStatus, IdCoachAwayCompletionStatus,
                        IdRacesHome, IdRacesAway, HomeValue, AwayValue, HomeScore, 
                        AwayScore, HomeInflictedTouchdowns, AwayInflictedTouchdowns):
        self.own_conceed = IdCoachHomeCompletionStatus in ['true', 'True', 1] if self.home_coach else IdCoachAwayCompletionStatus in ['true', 'True', 1]
        self.opp_conceeded = IdCoachAwayCompletionStatus in ['true', 'True', 1] if not self.home_coach else IdCoachHomeCompletionStatus in ['true', 'True', 1] 
        self.own_race = self.races[IdRacesHome] if self.home_coach else self.races[IdRacesAway]
        self.opp_race = self.races[IdRacesAway] if not self.home_coach else self.races[IdRacesHome]
        self.own_tv = HomeValue if self.home_coach else AwayValue
        self.opp_tv = AwayValue if not self.home_coach else HomeValue
        self.own_score = HomeScore if self.home_coach else AwayScore
        self.opp_score = AwayScore if not self.home_coach else HomeScore
        self.own_tds = HomeInflictedTouchdowns if self.home_coach else AwayInflictedTouchdowns
        self.opp_tds = AwayInflictedTouchdowns if not self.home_coach else HomeInflictedTouchdowns

            


    def set_ball_data(self, HomeOccupationOwn, HomeOccupationTheir, HomePossessionBall, 
                    AwayOccupationOwn, AwayOccupationTheir, AwayPossessionBall,
                    HomeInflictedPasses, HomeInflictedCatches, AwayInflictedPasses, AwayInflictedCatches, 
                    HomeInflictedMetersPassing, AwayInflictedMetersPassing, HomeInflictedInterceptions, 
                    AwayInflictedInterceptions, HomeInflictedMetersRunning, AwayInflictedMetersRunning):
        x= 1

    def set_injury_data(self, HomeInflictedKO, AwaySustainedKO, AwayInflictedKO, HomeSustainedKO,
                        HomeInflictedInjuries, AwaySustainedInjuries, AwayInflictedInjuries, HomeSustainedInjuries,
                        HomeInflictedCasualties, AwaySustainedCasualties, AwayInflictedCasualties, HomeSustainedCasualties,
                        HomeInflictedDead, AwaySustainedDead, AwayInflictedDead, HomeSustainedDead):
        x = 1

    def set_surfing_beach_boy_data(self, HomeInflictedPushOuts, AwayInflictedPushOuts):
        x = 1


    def print(self):
        print(self.home_coach, self.own_race)


        '''
        1 = Human
        2 = dwarf
        3 = Skaven
        4 = Orc
        5 = Lizardmen
        6 = Goblin
        7 = Wood Elf
        8 = chaos
        9 = Dark Elf
        10 = Undead
        11 = Halfling
        12 = norse
        13 = Amazon
        14 = Elven Union
        15 = High Elf
        16 = khemri
        17 = necromantic
        18 = nurgle
        19 = Ogre
        20 = Vampire
        21 = Chaos Dwarf
        22 = Underworld
        23 = ?
        24 = Bretonia
        25 = Kislev
        '''
'''
            <LeagueName>Kartoffelbowl</LeagueName>
            <CompetitionName>Den Moste XIV T4</CompetitionName>

            <IdCoachHomeCompletionStatus>0</IdCoachHomeCompletionStatus>
            <IdCoachAwayCompletionStatus>0</IdCoachAwayCompletionStatus>
            

            <CoachHomeName>CBraw</CoachHomeName>
            <CoachAwayName>Usnugnu</CoachAwayName>

            <IdRacesAway>16</IdRacesAway>
            <IdRacesHome>10</IdRacesHome>
            <HomeValue>1000</HomeValue>
            <AwayValue>1000</AwayValue>


            # score
            <HomeScore>1</HomeScore>
            <AwayScore>0</AwayScore>
            <HomeInflictedTouchdowns>1</HomeInflictedTouchdowns>
            <AwayInflictedTouchdowns>0</AwayInflictedTouchdowns>

            # bold hold
            <HomeOccupationOwn>25</HomeOccupationOwn>
            <HomePossessionBall>43</HomePossessionBall>
            <AwayOccupationOwn>37</AwayOccupationOwn>
            <HomeOccupationTheir>18</HomeOccupationTheir>
            <AwayPossessionBall>37</AwayPossessionBall>
            <AwayOccupationTheir>0</AwayOccupationTheir>

            # passing
            <AwayInflictedPasses>0</AwayInflictedPasses>
            <AwayInflictedCatches>0</AwayInflictedCatches>

            <HomeInflictedPasses>0</HomeInflictedPasses>
            <HomeInflictedCatches>0</HomeInflictedCatches>

            <HomeInflictedMetersPassing>0</HomeInflictedMetersPassing>
            <AwayInflictedMetersPassing>0</AwayInflictedMetersPassing>
            <AwayInflictedInterceptions>0</AwayInflictedInterceptions>
            <HomeInflictedInterceptions>0</HomeInflictedInterceptions>

            # running
            <HomeInflictedMetersRunning>54</HomeInflictedMetersRunning>
            <AwayInflictedMetersRunning>16</AwayInflictedMetersRunning>

            # skader
            <HomeInflictedKO>3</HomeInflictedKO>
            <AwaySustainedKO>3</AwaySustainedKO>
            <AwayInflictedKO>0</AwayInflictedKO>
            <HomeSustainedKO>0</HomeSustainedKO>
            
            <HomeInflictedInjuries>11</HomeInflictedInjuries>
            <AwaySustainedInjuries>13</AwaySustainedInjuries>
            <AwayInflictedInjuries>10</AwayInflictedInjuries>
            <HomeSustainedInjuries>10</HomeSustainedInjuries>

            <HomeInflictedCasualties>0</HomeInflictedCasualties>
            <AwaySustainedCasualties>1</AwaySustainedCasualties>
            <AwayInflictedCasualties>3</AwayInflictedCasualties>
            <HomeSustainedCasualties>3</HomeSustainedCasualties>

            <HomeInflictedDead>0</HomeInflictedDead>
            <AwaySustainedDead>0</AwaySustainedDead>
            <AwayInflictedDead>0</AwayInflictedDead>
            <HomeSustainedDead>0</HomeSustainedDead>
            

            # beach boys
            <HomeInflictedPushOuts>1</HomeInflictedPushOuts>
            <AwayInflictedPushOuts>0</AwayInflictedPushOuts>
            <AwaySustainedExpulsions>1</AwaySustainedExpulsions>
            <HomeSustainedExpulsions>0</HomeSustainedExpulsions>


            <HomeInflictedTackles>49</HomeInflictedTackles>
            <AwayInflictedTackles>44</AwayInflictedTackles>
            <AwayWinningsDice>1</AwayWinningsDice>
            <HomeWinningsDice>3</HomeWinningsDice>
            

'''




