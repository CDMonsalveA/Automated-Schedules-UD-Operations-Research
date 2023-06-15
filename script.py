import pandas as pd
import numpy as np
from pulp import *


class Base_Schedules:
    def __init__(self, Schedules, Classrooms, Timeslots):
        self.Schedules = Schedules
        self.Classrooms = Classrooms
        self.Timeslots = Timeslots
    def filter(self):
        

def main():
    Base_Schedules.Schedules = pd.read_excel('Base_Data/Horarios.xlsx', sheet_name='Horarios')
    Base_Schedules.Classrooms = pd.read_excel('Base_Data/Horarios.xlsx', sheet_name='Espacios_Fisicos')
    Base_Schedules.Timeslots = pd.read_excel('Base_Data/Horarios.xlsx', sheet_name='Tiempo')

if __name__ == "__main__":
    main()  

