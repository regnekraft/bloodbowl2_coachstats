import xml.etree.ElementTree as ET

class XML_reader_sevice:
    def __init__(self, xmlpath):
        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()

    def get_matches_from_coach_xml(self):
        '''
        '''
        matches = {}
        for match in self.root.findall('MatchRecord'):
            los_id = match.get('HomeOccupationOwn')
            longname = match.find('HomeOccupationOwn').text
            print(los_id, longname)