import os
from os.path import join, dirname
from dotenv import load_dotenv
import glob
from source.replay_reader import Replay_reader
from source.stats_service import Stats_service

#setup
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
xml_path = os.environ.get('xml_path')
csv_directory = os.environ.get('csv_directory')
coach_name = os.environ.get('coach_name')

rr = Replay_reader()
matches = rr.get_matches_from_coach_xml(xml_path, coach_name)
#for m in matches:
#    print(m.race, m.opponent_race, m.td_plus, m.td_minus, m.cas_plus, m.cas_minus)
rr.panda_magic(matches)
