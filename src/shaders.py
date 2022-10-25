"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

import utils

def my_first_shader(y):
  if (y < 100):
    return utils.color(255, 0, 0)
  elif (y < 150):
    return utils.color(200, 50, 50)
  elif y < 200:
    return utils.color(150, 100, 100)
  elif (y < 250):
    return utils.color(100, 200, 200)
  else:
    return utils.color(0, 255, 255)
