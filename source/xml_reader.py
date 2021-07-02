import xml.etree.ElementTree as ET
from source.models.match_model import Match_model

class XML_reader_sevice:
    def __init__(self, xmlpath, coach_name):
        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
        self.coach_name = coach_name

    def get_matches_from_coach_xml(self):
        '''
        '''
        # gets <matches> from the ElementTree that has the root of <ReplayIndex.xml>
        xml_matches = self.root.find('Matches').getchildren()
        #print(len(xml_matches))
        matches = []
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
            matches.append(mm)
        #print(len(matches))
        return matches