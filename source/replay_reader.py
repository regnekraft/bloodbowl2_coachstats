import xml.etree.ElementTree as ET
import pandas as pd
from source.models.match_model import Match_model
from source.models.coach_model import Coach_model

class Replay_reader:
        
    def get_matches_from_coach_xml(self, xmlpath, coach_name):
        tree = ET.parse(xmlpath)
        root = tree.getroot()
        # gets <matches> from the ElementTree that has the root of <ReplayIndex.xml>
        xml_matches = root.find('Matches').getchildren()
        result = []
        for match in xml_matches:
            # If the match was not played for some reason, it is likely the data is incomplete.
            if match.find('Played').text in ['false', 'False', '0', 0]:
                continue
            
            is_home_coach =  match.find('CoachHomeName').text.lower() == coach_name.lower()
            
            p1_race =  match.find('IdRacesHome').text if is_home_coach else match.find('IdRacesAway').text
            p2_race = match.find('IdRacesAway').text if is_home_coach else match.find('IdRacesHome').text
            td_plus = match.find('HomeInflictedTouchdowns').text if is_home_coach else match.find('AwayInflictedTouchdowns').text
            td_minus = match.find('AwayInflictedTouchdowns').text if is_home_coach else match.find('HomeInflictedTouchdowns').text
            cas_plus = match.find('HomeInflictedCasualties').text if is_home_coach else match.find('AwayInflictedCasualties').text
            cas_minus = match.find('AwayInflictedCasualties').text if is_home_coach else match.find('HomeInflictedCasualties').text
            mm = Match_model(p1_race, p2_race, td_plus, td_minus, cas_plus, cas_minus)
            result.append(mm)
        return result

                            
            

    def get_coach_object_from_coach_xml(self):
        '''
        '''
        # gets <matches> from the ElementTree that has the root of <ReplayIndex.xml>
        xml_matches = self.root.find('Matches').getchildren()
        coach = Coach_model()
        for match in xml_matches:
            # If the match was not played for some reason, it is likely the data is incomplete.
            if match.find('Played').text in ['false', 'False', '0', 0]:
                continue

            mm = Match_model(self.coach_name, match.find('CoachHomeName').text, match.find('LeagueName').text,
                            match.find('CompetitionName').text)
                            
            mm.set_overall_data(match.find('IdCoachHomeCompletionStatus').text, match.find('IdCoachAwayCompletionStatus').text,
                         match.find('IdRacesHome').text, match.find('IdRacesAway').text, match.find('HomeValue').text,
                         match.find('AwayValue').text, match.find('HomeScore').text, match.find('AwayScore').text,
                         match.find('HomeInflictedTouchdowns').text, match.find('AwayInflictedTouchdowns').text)

            mm.set_ball_data(match.find('HomeOccupationOwn').text, match.find('HomeOccupationTheir').text, match.find('HomePossessionBall').text,
                            match.find('AwayOccupationOwn').text, match.find('AwayOccupationTheir').text, match.find('AwayPossessionBall').text,
                            match.find('HomeInflictedPasses').text, match.find('AwayInflictedPasses').text, match.find('HomeInflictedMetersPassing').text,
                            match.find('AwayInflictedMetersPassing').text, match.find('HomeInflictedInterceptions').text,
                            match.find('AwayInflictedInterceptions').text, match.find('HomeInflictedMetersRunning').text,
                            match.find('AwayInflictedMetersRunning').text)
            
            mm.set_injury_data(match.find('HomeInflictedKO').text, match.find('AwaySustainedKO').text, match.find('HomeSustainedKO').text,
                            match.find('AwayInflictedKO').text, match.find('HomeInflictedInjuries').text, match.find('AwayInflictedInjuries').text,
                            match.find('HomeSustainedInjuries').text, match.find('AwaySustainedInjuries').text, match.find('HomeInflictedCasualties').text,
                            match.find('AwayInflictedCasualties').text, match.find('HomeSustainedCasualties').text, match.find('AwaySustainedCasualties').text,
                            match.find('HomeInflictedDead').text, match.find('AwayInflictedDead').text, match.find('HomeSustainedDead').text,
                            match.find('AwaySustainedDead').text)

            mm.set_surfing_beach_boy_data(match.find('HomeInflictedPushOuts').text, match.find('AwayInflictedPushOuts').text)
            coach.add_match(mm.race, mm)
        #coach.print_top_stats()
        return coach

    def panda_magic(self, matches):
        print(len(matches))
        alt = pd.DataFrame(matches)
        print(alt.head())
