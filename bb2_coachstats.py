import os
from os.path import join, dirname
from dotenv import load_dotenv
import glob
from source.xml_reader import XML_reader_sevice

#setup
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
xml_path = os.environ.get('xml_path')
csv_directory = os.environ.get('csv_directory')
coach_name = os.environ.get('coach_name')

reader = XML_reader_sevice(xml_path, coach_name)
reader.get_matches_from_coach_xml()
