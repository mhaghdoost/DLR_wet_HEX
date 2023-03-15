# -*- coding: utf-8 -*-
"""
Created on Tue May  3 11:38:24 2022

@author: reza_ma
"""

v = 50 #m/s Climb DO228
A = 0.85 * 0.85  # m² Hex Querschnitt

V_dot = v * A
print('Volumenstrom HEX Do228  = {:.1f} m³/s'.format(V_dot))

# Windkanäle
# TU Berlin FG Regelungstechnik (paper)
v = 20 # m/s
A = 0.7 * 0.5 # m²
V_dot = v * A
print('Volumenstrom TU Windkanal  = {:.1f} m³/s'.format(V_dot))

# Thomas Verdichter
V_dot = 2.7 # m³/s
print('Volumenstrom BTU (Thomas) Windkanal  = {:.1f} m³/s'.format(V_dot))