"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

"""
Posibles argumentos de un shader:
- x: Coordenada en x.
- y: Coordenada en y.
- width: Ancho de la imagen.
- height: Alto de la imagen.
- light: Vector de luz.
- coords: Coordenadas baricéntricas del punto.
- texture_coords: Coordenadas de texturas del modelo.
- normal_coords: Coordenadas normales del modelo.
"""

import utils

def my_first_shader(**kwargs):
  y = kwargs["y"]
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

def planet_shader(**kwargs):
  x = kwargs["x"]
  y = kwargs["y"]
  width = kwargs["width"]
  height = kwargs["height"]

  relative_x, relative_y = utils.absolute_to_relative_conversion(x, y, width, height)
  distance = ((((relative_x ** 2) + (relative_y ** 2)) ** 0.5))

  factor = (1 - distance)

  if ((175 <= y <= 200) or (300 <= y <= 325) or (425 <= y <= 450) or (550 <= y <= 575) or (675 <= y <= 700) or (800 <= y <= 825)):
    r, g, b = round(60 * factor), round(80 * factor), round(215 * factor)
  elif ((200 <= y <= 225) or (275 <= y <= 300) or (450 <= y <= 475) or (525 <= y <= 550) or (700 <= y <= 725) or (775 <= y <= 800)):
    r, g, b = round(50 * factor), round(70 * factor), round(190 * factor)
  elif ((225 <= y <= 275) or (475 <= y <= 525) or (725 <= y <= 775)):
    r, g, b = round(50 * factor), round(60 * factor), round(160 * factor)
  else:
    r, g, b = round(60 * factor), round(100 * factor), round(255 * factor)

  return utils.color(r, g, b)

def model_shader():
  return 0
