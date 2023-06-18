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

    def load_data(self, baselink, schedule_sheetname, classroom_sheetname, timeslot_sheetname):
        '''
        Loads the data from the excel file
        '''
        self.schedules = pd.read_excel(baselink, sheet_name=schedule_sheetname)
        self.classrooms = pd.read_excel(baselink, sheet_name=classroom_sheetname)
        self.timeslots = pd.read_excel(baselink, sheet_name=timeslot_sheetname)

    def filter_isin_array(self, array, column_name):
        '''
        Filters the data from the base data
        '''
        return self.schedules[self.schedules[column_name].isin(array)].copy()

    def filter_isnotin_array(self, array, column_name):
        '''
        Filters the data from the base data
        
        Parameters
        ----------
        array : array
            Array of values to filter
        column_name : string
            Name of the column to filter
        '''
        return self.schedules[~self.schedules[column_name].isin(array)].copy()
    def filter_apply(self, array, column_name, function):
        '''
        Apply a filter to the data

        Parameters
        ----------
        array : array
            array of values to filter
        column_name : string
            name of the column to filter
        function : function
            isin or isnotin
        '''
        if function == 'isin':
            return self.filter_isin_array(array, column_name)
        elif function == 'isnotin':
            return self.filter_isnotin_array(array, column_name)
        else:
            raise ValueError('Function not found')
    def filter_apply_all(self):
        '''
        Apply all the filters
        '''
        # Check only the carrers
        filter1 = ['INGENIERIA ELECTRONICA',
                    'INGENIERIA ELECTRICA',
                    'INGENIERIA INDUSTRIAL',
                    'INGENIERIA DE SISTEMAS',
                    'INGENIERIA CATASTRAL Y GEODESIA']
        col_1 = 'Proyecto Curricular'
        # Check only the Sedes
        filter2 = ['CALLE 34 - CALLE 34',
                'CALLE 40 - SABIO CALDAS',
                'ASISTIDO POR TIC - ASISTIDO POR TIC',
                'CALLE 40 - ADMINISTRATIVO', 'CALLE 42 - CALLE 42',
                'POR ASIGNAR - POR ASIGNAR']
        col_2 = 'Sede'
        # Check only the classrooms
        filter3 = self.classrooms['Salon'].tolist()
        filter3 += ['VIRT000000 - ASISTIDO POR TIC', 'PAS0000000 - POR ASIGNAR']
        col_3 = 'Salon'
        # Take Out the Espacio Academico on filters
        filter4 = ['TRABAJO DE GRADO I',
                'TRABAJO DE GRADO I: METODOLOGIA DE LA INVESTIGACION',
                'TRABAJO DE GRADO II',
                'TRABAJO DE GRADO',
                'PRACTICA EMPRESARIAL',
                'PRACTICA  EMPRESARIAL']
        col_4 = 'Espacio Academico'
        self.schedules = self.filter_apply(filter1, col_1, 'isin')
        self.schedules = self.filter_apply(filter2, col_2, 'isin')
        self.schedules = self.filter_apply(filter3, col_3, 'isin')
        self.schedules = self.filter_apply(filter4, col_4, 'isnotin')

Data = BaseSchedules(None, None, None)
Data.load_data('Base_Data/Horarios.xlsx', 'Horarios', 'Espacios_Fisicos', 'Tiempo')
Data.filter_apply_all()
print(Data.schedules)
print(Data.classrooms)
print(Data.timeslots)
