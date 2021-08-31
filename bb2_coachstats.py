import os
from os.path import join, dirname
from dotenv import load_dotenv
import glob
from source.replay_reader import Replay_reader

#setup
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
xml_path = os.environ.get('xml_path')
csv_directory = os.environ.get('csv_directory')
coach_name = os.environ.get('coach_name')

rr = Replay_reader(xml_path, coach_name)
matches = rr.get_coach_object_from_coach_xml()
#rr.panda_magic(matches)
