# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:42:42 2022

@author: reza_ma
Quelle:
#https://www.engineeringtoolbox.com/water-vapor-saturation-pressure-air-d_689.html
https://www.engineeringtoolbox.com/humidity-ratio-air-d_686.html
"""
# https://afim-dehumidifier.com/en/mollier-chart-air-calculator/
# With air temperature 25 oC and 50% relative humidity the humidity ratio in the air is 0.0098 kg/kg - check Mollier diagram.
# T = 15; Hum = 50%; Absolute Moisture kg/kg = 5.274E-3
# T = 15; Hum = 20%; Absolute Moisture kg/kg = 2.099E-3
# T = 35; Hum = 50; Absolute Moisture kg/kg = 17.747E-3
# T = 35; Hum = 20; Absolute Moisture kg/kg = 6.979E-3
# Das ist das x in untere Rechnung!
# x = 0.0098 # bsp
x = 2.099E-3


import numpy as np
# Ambient (air) temperature 
# T_w_in_C = 20 #C # bsp
T_w_in_C = 80 #C
# Air velocity
# v = 0.5 #m/s
v = 50 #m/s
# Air Temperature
# T_a_in_C = 25

#Surface Area
# A = 1000 #m² # bsp
A = 121.5

T_w = 273 + T_w_in_C
# T_a = 273 + T_a_in_C
#+++++++++++++++++
# Wiki: https://de.wikipedia.org/wiki/Verdampfungsenthalpie
# Heat of evaporation for water in kJ/kg
h_we = (50.09 - 0.9298 * T_w/1000 - 65.19*(T_w/1000)**2) / 18.02 * 1000
#+++++++++++++++++
#Engineeringtoolbox.com

# saturation pressure water vapor
p_ws = np.exp(77.3450 + 0.0057 * T_w - 7235 / T_w ) / (T_w**8.2)

# Humidity Ratio of Moist Air (Maximum Saturation Humidity Ratio of Air)
p_a = 101325
x_s = 0.62198 * p_ws / (p_a - p_ws) # kg/kg

# Θ = (25 + 19 v) = evaporation coefficient (kg/m²h)
beta = 25 + 19*v

#gs = amount of evaporated water per second (kg/s)
gs = beta * A * (x_s - x) / 3600

# Required heat to cover evaporatio: q = h_we * g_s ;
q = h_we * gs

print('q - heat supply = {:.1f} kw'.format(q))
print('gs - evaporated water per second = {:.3f} kg/s'.format(gs))
print('gs - evaporated water per second = {:.3f} kg/h'.format(gs*3600))
#######################################################################
# #https://www.physicsforums.com/threads/evaporation-of-water-error-in-formula.242677/
# Pw = 23.71 # Pw@25 C = 23.71 mmHG
# # Pw = 354.58 # Pw@80 C = 23.71 mmHG 
# Ps = 15.46 #Ps@ 18 C = 15.46 mmHG ( 25 C air temp, 50% RH)
# # Ps = 42.05 #Ps@ 35 C
# A = 9
# V = 0.5
# M_dot= A*(42.6+37.6*v)*(Pw-Ps)/h_we/3600
# # m-dot= evaporation rate, kg/hr 
# # A= surface area, m^2 
# # V= air velocity over water surface, m/s 
# # Pw= saturation vapor pressure at water temperature, mm Hg
# # Ps= saturation vapor pressure of air dew point, mm Hg
# # Hv= latent heat of vaporization of water at pool temperature, about 2270 KJ/Kg
# print('M_dot = {:.3f} kg/s'.format(M_dot))