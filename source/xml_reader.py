import xml.etree.ElementTree as ET
from source.match_model import Match_model

class XML_reader_sevice:
    def __init__(self, xmlpath, coach_name):
        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
        self.coach_name = coach_name

    def get_matches_from_coach_xml(self):
        '''
        '''
        # gets <matches> from the ElementTree that has the root of <ReplayIndex.xml>
        xml_matches = self.root[0]
        matches = {}
        for match in xml_matches.findall('MatchRecord'):
            mm = Match_model(self.coach_name, match.find('CoachHomeName').text, match.find('LeagueName').text,
                            match.find('CompetitionName').text)
                            
            mm.set_overall_data( match.find('IdCoachHomeCompletionStatus').text,  match.find('IdCoachAwayCompletionStatus').text,
                         match.find('IdRacesHome').text, match.find('IdRacesAway').text, match.find('HomeValue').text,
                         match.find('AwayValue').text,  match.find('HomeScore').text, match.find('AwayScore').text,
                         match.find('HomeInflictedTouchdowns').text, match.find('AwayInflictedTouchdowns').text)
            mm.print()