# Automated Schedules UD Operations Research
This repository contains the code for the automated schedules project. The project is a part of the [UD Operations Research] for the Universidad Distrital Francisco José de Caldas, Engineering Faculty.

Created by: [Cristian David Monsalve Alfonso](https://github.com/CDMonsalveA)

## Table of Contents
- [Introduction](#introduction)
- [How it works](#how-it-works)
- [How to use](#how-to-use)
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
4. Create the information for available times linearize the 







