from data_processing.scrapers_check import *
import pandas as pd
from datetime import datetime

class DataTransformer:
    def __init__(self):
        self.crawler_dict = crawler_check()

    def get_scheduled(self):
        try:
            scheduled = self.crawler_dict['scheduled']['df']
            scheduled['Date'] = pd.to_datetime(scheduled['Date'], format='mixed', dayfirst=True)
            scheduled['ETA'] = pd.to_datetime(scheduled['ETA'], format='mixed', dayfirst=True)
            scheduled['UPDATED_AT'] = datetime.now()
            return scheduled
        except Exception as err:
            return err

    def get_foreseen_cargo(self):
        try:
            foreseen_cargo = self.crawler_dict['foreseen_cargo']['df']
            foreseen_cargo.drop(columns=['P'], axis=1, inplace=True)
            foreseen_cargo['Arrival'] = pd.to_datetime(foreseen_cargo['Arrival'], format='mixed', dayfirst=True)
            foreseen_cargo['UPDATED_AT'] = datetime.now()
            return foreseen_cargo
        except Exception as err:
            return err

    def get_foreseen_cruise(self):
        try:
            foreseen_cruise = self.crawler_dict['foreseen_cruise']['df']
            foreseen_cruise['Arrival'] = pd.to_datetime(foreseen_cruise['Arrival'], format='mixed', dayfirst=True)
            foreseen_cruise['UPDATED_AT'] = datetime.now()
            return foreseen_cruise
        except Exception as err:
            return err

    def get_berthage_ships(self):
        try:
            berthage_ships = self.crawler_dict['berthage_ships']['df']
            berthage_ships['Arrival'] = pd.to_datetime(berthage_ships['Arrival'], format='mixed', dayfirst=True)
            berthage_ships['Ship'] = berthage_ships['Ship'].str.replace(r'PROGRAMADO', '', case=False, regex=True)
            berthage_ships['UPDATED_AT'] = datetime.now()
            return berthage_ships
        except Exception as err:
            return err

    def get_berthed_ships(self):
        try:
            berthed_ships = self.crawler_dict['berthed_ships']['df']
            berthed_ships['Load'] = berthed_ships['Load'].astype(int)
            berthed_ships['Unload'] = berthed_ships['Unload'].astype(int)
            berthed_ships['UPDATED_AT'] = datetime.now()
            return berthed_ships
        except Exception as err:
            return err
