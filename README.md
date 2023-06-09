# Automated Schedules UD Operations Research

This repository contains the code for the automated schedules project. The project is a part of the [UD Operations Research] for the Universidad Distrital Francisco José de Caldas, Engineering Faculty.

Created by: [Cristian David Monsalve Alfonso](https://github.com/CDMonsalveA)

## Table of Contents

- [Introduction](#introduction)
- [How it works](#how-it-works)
- [How to use](#how-to-use)
- [Download The Solution](#download-the-solution)
- [License](#license)

## Introduction

The project is a part of the [UD Operations Research] for the Universidad Distrital Francisco José de Caldas, Engineering Faculty. The project is a part of the [UD Operations Research] for the Universidad Distrital Francisco José de Caldas, Engineering Faculty.

## How it works

The script is based on information on spreadsheets, which are read by the script and then the data is processed to generate the schedules.

1. The script reads the information from the spreadsheets.
2. The data is filtered and processed.
    - Filtered by 'Proyecto Curricular', so that only the data of INGENIERIA ELECTRONICA', 'INGENIERIA ELECTRICA', 'INGENIERIA INDUSTRIAL', 'INGENIERIA DE SISTEMAS', 'INGENIERIA CATASTRAL Y GEODESIA' are selected
    - Filtered by Sedes so only the buildings in charge of the Engineering Faculty are selected
    - Filtered by Salones so only the ones reported in the spreadsheet as 'Espacios_Fisicos' are selected
    - Finally, anything related to 'Trabajo de Grado' is filtered out so that the schedules represent the classes need a physical space.
3. The data is then processed to generate the schedules.
    - Create the information for Espacios Académicos (Materias)
        - Create a list of the unique values of the "Espacio Academico" column
        - Create a new column with the hours per week of the course
        - Create a new column with the number times the course is offered per week
        - Rename the column "Hora" to "Horas por semana" and "Dia" to "Dias por semana"
4. Create the information for available times, this is linearize the days information
5. Capacity analysis on Espacios_Fisicos and Espacios_Academicos
    - Where there are 7 categories based on Capacity, this is analyzed for both Espacios_Fisicos and Espacios_Academicos
        1. 0-15
        2. 16-20
        3. 21-25
        4. 26-30
        5. 31-35
        6. 36-40
        7. 41-200
    - The output will be a comparison of the capacity of the Espacios_Fisicos and Espacios_Academicos in form of a tables with rows as Proyecto Curricular and columns as the 7 categories
6. Create the information for the schedules

    - The model from Model_Explanation\MODEL.md is used to create the schedules
        - The solution is then read and the schedules are generated

## How to use

in progress

## Download The Solution

Dowload the solution [in the Github: Solution.xlsx file](https://github.com/CDMonsalveA/Automated-Schedules-UD-Operations-Research/raw/master/Solucion.xlsx)

## License

MIT License

Copyright (c) 2023 Cristian Monsalve

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[MIT](https://choosealicense.com/licenses/mit/)
