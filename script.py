"""Module for interacting with the base data"""
import pandas as pd



class BaseSchedules:
    '''
    Class for interacting with the base data
    '''
    def __init__(self, schedules, classrooms, timeslots):
        self.schedules = schedules
        self.classrooms = classrooms
        self.timeslots = timeslots

    def filter_by(self, column, _filter_array):
        '''
        Filter a dataset by a list of filters
        '''
        return self[self[column].isin(filter)].copy()

def main():
    '''
    Main function for testing the module
    '''
    BaseSchedules.Schedules = pd.read_excel(r'Base_Data\Horarios.xlsx',
        sheet_name='Horarios')
    BaseSchedules.Classrooms = pd.read_excel(r'Base_Data\Horarios.xlsx',
        sheet_name='Espacios_Fisicos')
    BaseSchedules.Timeslots = pd.read_excel(r'Base_Data\Horarios.xlsx',
        sheet_name='Tiempo')

if __name__ == "__main__":
    main()
