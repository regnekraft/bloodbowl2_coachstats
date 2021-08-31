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
        self.own_race = self.races[IdRacesHome] if self.home_coach else self.races[IdRacesAway]
        self.opp_race = self.races[IdRacesAway] if not self.home_coach else self.races[IdRacesHome]
        self.own_tv = HomeValue if self.home_coach else AwayValue
        self.opp_tv = AwayValue if not self.home_coach else HomeValue
        self.own_score = HomeScore if self.home_coach else AwayScore
        self.opp_score = AwayScore if not self.home_coach else HomeScore
        self.own_tds = HomeInflictedTouchdowns if self.home_coach else AwayInflictedTouchdowns
        self.opp_tds = AwayInflictedTouchdowns if not self.home_coach else HomeInflictedTouchdowns
        self.result = Match_model.set_result(self, HomeScore, AwayScore)
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
            self.own_conceed = 0
            self.opp_conceeded = 0
        else:
            if self.home_coach:
                self.own_conceed = 0 if IdCoachHomeCompletionStatus == 0 else 1
                self.opp_conceeded = 0 if IdCoachAwayCompletionStatus == 0 else 1
            else:
                self.opp_conceeded = 0 if IdCoachHomeCompletionStatus == 0 else 1
                self.own_conceed = 0 if IdCoachAwayCompletionStatus == 0 else 1
        

    def set_ball_data(self, HomeOccupationOwn, HomeOccupationTheir, HomePossessionBall, 
                    AwayOccupationOwn, AwayOccupationTheir, AwayPossessionBall, HomeInflictedPasses,
                    AwayInflictedPasses, HomeInflictedMetersPassing, AwayInflictedMetersPassing, 
                    HomeInflictedInterceptions, AwayInflictedInterceptions, HomeInflictedMetersRunning,
                    AwayInflictedMetersRunning):
        # the game can regrister HomeInflictedPasses + HomeInflictedCatches and AwayInflictedPasses + AwayInflictedCatches
        # but they will always be the same number for some reason, so incomplete passes and handoffs aren't regristered.
        
        self.own_occupation_own = HomeOccupationOwn if self.home_coach else AwayOccupationOwn
        self.opp_occupation_own = AwayOccupationOwn if not self.home_coach else HomeOccupationOwn
        self.own_occupation_their = HomeOccupationTheir if self.home_coach else AwayOccupationTheir
        self.opp_occupation_their = AwayOccupationTheir if not self.home_coach else HomeOccupationTheir
        self.own_ball_possession = HomePossessionBall if self.home_coach else AwayInflictedPasses
        self.opp_ball_possession = AwayPossessionBall if not self.home_coach else HomePossessionBall
        self.own_pass_attempts = HomeInflictedPasses if self.home_coach else AwayInflictedPasses
        self.opp_pass_attempts = AwayInflictedPasses if not self.home_coach else HomeInflictedPasses
        self.own_passing_meters = HomeInflictedMetersPassing if self.home_coach else AwayInflictedInterceptions
        self.opp_passing_meters = AwayInflictedMetersPassing if not self.home_coach else HomeInflictedMetersPassing
        self.own_interceptions = HomeInflictedInterceptions if self.home_coach else AwayInflictedInterceptions
        self.opp_interceptions = AwayInflictedInterceptions if not self.home_coach else HomeInflictedInterceptions
        self.own_running_meters = HomeInflictedMetersRunning if self.home_coach else AwayInflictedMetersRunning
        self.opp_running_meters = AwayInflictedMetersRunning if not self.home_coach else HomeInflictedMetersRunning
        

    def set_injury_data(self, HomeInflictedKO, AwaySustainedKO, HomeSustainedKO, AwayInflictedKO,
                        HomeInflictedInjuries, AwayInflictedInjuries, HomeSustainedInjuries, AwaySustainedInjuries,
                        HomeInflictedCasualties, AwayInflictedCasualties, HomeSustainedCasualties, AwaySustainedCasualties,
                        HomeInflictedDead, AwayInflictedDead, HomeSustainedDead, AwaySustainedDead):
        self.own_ko_caused = HomeInflictedKO if self.home_coach else AwayInflictedKO
        self.opp_ko_caused = AwayInflictedKO if not self.home_coach else HomeInflictedKO
        self.own_ko_sustained = HomeSustainedKO if self.home_coach else AwaySustainedKO
        self.opp_ko_sustained = AwaySustainedKO if not self.home_coach else HomeSustainedKO
        self.own_injuries_caused = HomeInflictedInjuries if self.home_coach else AwayInflictedInjuries
        self.opp_injuries_caused = AwayInflictedInjuries if not self.home_coach else HomeInflictedInjuries
        self.own_injuries_sustained = HomeSustainedInjuries if self.home_coach else AwaySustainedInjuries
        self.opp_injuries_sustained = AwaySustainedInjuries if not self.home_coach else HomeSustainedInjuries
        self.own_casualties_caused = HomeInflictedCasualties if self.home_coach else AwayInflictedCasualties
        self.opp_casualties_caused = AwayInflictedCasualties if not self.home_coach else HomeInflictedCasualties
        self.own_casualties_sustained = HomeSustainedCasualties if self.home_coach else AwaySustainedCasualties
        self.opp_casualties_sustained = AwaySustainedCasualties if not self.home_coach else HomeSustainedCasualties
        self.own_murders_caused = HomeInflictedDead if self.home_coach else AwayInflictedDead
        self.opp_murders_caused = AwayInflictedDead if not self.home_coach else HomeInflictedDead
        self.own_deaths_sustained =HomeSustainedDead if self.home_coach else AwaySustainedDead
        self.opp_deaths_sustained = AwaySustainedDead if not self.home_coach else HomeSustainedDead

    def set_surfing_beach_boy_data(self, HomeInflictedPushOuts, AwayInflictedPushOuts):
        self.own_surfs = HomeInflictedPushOuts if self.home_coach else AwayInflictedPushOuts
        self.opp_surfs = AwayInflictedPushOuts if not self.home_coach else HomeInflictedPushOuts

