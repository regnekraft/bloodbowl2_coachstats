from typing import Match


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
        self.race = self.races[IdRacesHome] if self.home_coach else self.races[IdRacesAway]
        self.race_opp = self.races[IdRacesAway] if self.home_coach else self.races[IdRacesHome]
        self.tv = HomeValue if self.home_coach else AwayValue
        self.tv_opp = AwayValue if self.home_coach else HomeValue
        self.score = HomeScore if self.home_coach else AwayScore
        self.score_opp = AwayScore if self.home_coach else HomeScore
        self.tds = HomeInflictedTouchdowns if self.home_coach else AwayInflictedTouchdowns
        self.tds_opp = AwayInflictedTouchdowns if self.home_coach else HomeInflictedTouchdowns
        self.match_result = Match_model.set_result(self, HomeScore, AwayScore)
        Match_model.set_conceed_status(self, int(IdCoachHomeCompletionStatus), int(IdCoachAwayCompletionStatus))
        

    def set_result(self, HomeScore, AwayScore):
        if HomeScore > AwayScore:
            return 'Won'
        elif HomeScore < AwayScore:
            return 'Lost'
        else:
            return 'Draw'

    def set_conceed_status(self, IdCoachHomeCompletionStatus, IdCoachAwayCompletionStatus):
        if IdCoachAwayCompletionStatus == 0 and IdCoachHomeCompletionStatus == 0:
            self.conceed = 0
            self.conceed_opp = 0
        else:
            if self.home_coach:
                self.conceed = 0 if IdCoachHomeCompletionStatus == 0 else 1
                self.conceed_opp = 0 if IdCoachAwayCompletionStatus == 0 else 1
            else:
                self.conceed_opp = 0 if IdCoachHomeCompletionStatus == 0 else 1
                self.conceed = 0 if IdCoachAwayCompletionStatus == 0 else 1
        

    def set_ball_data(self, HomeOccupationOwn, HomeOccupationTheir, HomePossessionBall, 
                    AwayOccupationOwn, AwayOccupationTheir, AwayPossessionBall, HomeInflictedPasses,
                    AwayInflictedPasses, HomeInflictedMetersPassing, AwayInflictedMetersPassing, 
                    HomeInflictedInterceptions, AwayInflictedInterceptions, HomeInflictedMetersRunning,
                    AwayInflictedMetersRunning):
        # the game can regrister HomeInflictedPasses + HomeInflictedCatches and AwayInflictedPasses + AwayInflictedCatches
        # but they will always be the same number for some reason, so incomplete passes and handoffs aren't regristered.
        
        self.occupation_ownhalf = HomeOccupationOwn if self.home_coach else AwayOccupationOwn
        self.occupation_ownhalf_opp = AwayOccupationOwn if self.home_coach else HomeOccupationOwn
        self.occupation_theirhalf = HomeOccupationTheir if self.home_coach else AwayOccupationTheir
        self.occupation_theirhalf_opp = AwayOccupationTheir if self.home_coach else HomeOccupationTheir
        self.ball_possession = HomePossessionBall if self.home_coach else AwayInflictedPasses
        self.ball_possession_opp = AwayPossessionBall if self.home_coach else HomePossessionBall
        self.pass_attempts = HomeInflictedPasses if self.home_coach else AwayInflictedPasses
        self.pass_attempts_opp = AwayInflictedPasses if self.home_coach else HomeInflictedPasses
        self.passing_meters = HomeInflictedMetersPassing if self.home_coach else AwayInflictedInterceptions
        self.passing_meters_opp = AwayInflictedMetersPassing if self.home_coach else HomeInflictedMetersPassing
        self.interceptions = HomeInflictedInterceptions if self.home_coach else AwayInflictedInterceptions
        self.interceptions_opp = AwayInflictedInterceptions if self.home_coach else HomeInflictedInterceptions
        self.running_meters = HomeInflictedMetersRunning if self.home_coach else AwayInflictedMetersRunning
        self.running_meters_opp = AwayInflictedMetersRunning if self.home_coach else HomeInflictedMetersRunning
        

    def set_injury_data(self, HomeInflictedKO, AwaySustainedKO, HomeSustainedKO, AwayInflictedKO,
                        HomeInflictedInjuries, AwayInflictedInjuries, HomeSustainedInjuries, AwaySustainedInjuries,
                        HomeInflictedCasualties, AwayInflictedCasualties, HomeSustainedCasualties, AwaySustainedCasualties,
                        HomeInflictedDead, AwayInflictedDead, HomeSustainedDead, AwaySustainedDead):
        self.ko_caused = HomeInflictedKO if self.home_coach else AwayInflictedKO
        self.ko_caused_opp = AwayInflictedKO if self.home_coach else HomeInflictedKO
        self.ko_sustained = HomeSustainedKO if self.home_coach else AwaySustainedKO
        self.ko_sustained_opp = AwaySustainedKO if self.home_coach else HomeSustainedKO
        self.injuries_caused = HomeInflictedInjuries if self.home_coach else AwayInflictedInjuries
        self.injuries_caused_opp = AwayInflictedInjuries if self.home_coach else HomeInflictedInjuries
        self.injuries_sustained = HomeSustainedInjuries if self.home_coach else AwaySustainedInjuries
        self.injuries_sustained_opp = AwaySustainedInjuries if self.home_coach else HomeSustainedInjuries
        self.casualties_caused = HomeInflictedCasualties if self.home_coach else AwayInflictedCasualties
        self.casualties_caused_opp = AwayInflictedCasualties if self.home_coach else HomeInflictedCasualties
        self.casualties_sustained = HomeSustainedCasualties if self.home_coach else AwaySustainedCasualties
        self.casualties_sustained_opp = AwaySustainedCasualties if self.home_coach else HomeSustainedCasualties
        self.murders_caused = HomeInflictedDead if self.home_coach else AwayInflictedDead
        self.murders_caused_opp = AwayInflictedDead if self.home_coach else HomeInflictedDead
        self.deaths_sustained =HomeSustainedDead if self.home_coach else AwaySustainedDead
        self.deaths_sustained_opp = AwaySustainedDead if self.home_coach else HomeSustainedDead

    def set_surfing_beach_boy_data(self, HomeInflictedPushOuts, AwayInflictedPushOuts):
        self.surfs = HomeInflictedPushOuts if self.home_coach else AwayInflictedPushOuts
        self.surfs_opp = AwayInflictedPushOuts if self.home_coach else HomeInflictedPushOuts

