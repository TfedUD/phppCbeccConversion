
#Copyright (c) 2020, Trevor Fedyna, <unconstraineddevelopment.com> 
# This is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 3 of the License, 
# or (at your option) any later version. 
# 
# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# 
# For a copy of the GNU General Public License
# see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


# Innitial parsing of IDF into CBECC *ribd19 format:  work in progress



import sys 
import os
import eppy
from eppy import modeleditor as mE
from eppy.modeleditor import IDF

# eppy docs: https://eppy.readthedocs.io/en/latest/runningeplus.html
'''
To get a description of the options available, 
as well as the defaults you can call the Python built-in help function
on the IDF.run method and it will print a full description of the options to the console.
'''
# idd stays 
iddfile ="C:\\EnergyPlusV9-2-0\\Energy+.idd"
# input path to idf 
fileX = "C:\\EnergyPlusV9-2-0\\ExampleFiles\\BasicsFiles\\AdultEducationCenter.idf"
IDF.setiddname(iddfile)
# define weather file
epwfile = "C:\\EnergyPlusV9-2-0\\WeatherData\\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
# set IDF input data
idf1 = IDF(fileX, epwfile)

building = idf1.idfobjects['building'][0]
_maters = idf1.idfobjects["MATERIAL"]


for material in _maters:
    print('Mat  ', '"',material.Name,'"', '\n   ','Density =',material.Density,'\n   ','SpecHeat =',material.heatcapacity,
     '\n   ','Conductivity =',material.Conductivity,'\n   ..\n')


