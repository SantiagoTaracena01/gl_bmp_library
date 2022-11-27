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

# Librerías importantes para el desarrollo del archivo.
import random
import utils

# Primer shader realizado en clase.
def my_first_shader(**kwargs):

  # Altura y en la que se ubica el renderer.
  y = kwargs["y"]

  # Colores a retornar por el shader.
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

# Shader desarrollado para el laboratorio 02.
def planet_shader(**kwargs):

  # Parámetros necesarios para el shader.
  x = kwargs["x"]
  y = kwargs["y"]
  width = kwargs["width"]
  height = kwargs["height"]

  # Coordenadas relativas en las que se encuentra el renderer.
  relative_x, relative_y = utils.absolute_to_relative_conversion(x, y, width, height)
  distance = (((relative_x ** 2) + (relative_y ** 2)) ** 0.5)

  # Factor para determinar la claridad/oscuridad del punto a colorear.
  factor = (1 - distance)

  # Colores a asignar por el shader.
  if ((175 <= y <= 200) or (300 <= y <= 325) or (425 <= y <= 450) or (550 <= y <= 575) or (675 <= y <= 700) or (800 <= y <= 825)):
    r, g, b = round(60 * factor), round(80 * factor), round(215 * factor)
  elif ((200 <= y <= 225) or (275 <= y <= 300) or (450 <= y <= 475) or (525 <= y <= 550) or (700 <= y <= 725) or (775 <= y <= 800)):
    r, g, b = round(50 * factor), round(70 * factor), round(190 * factor)
  elif ((225 <= y <= 275) or (475 <= y <= 525) or (725 <= y <= 775)):
    r, g, b = round(50 * factor), round(60 * factor), round(160 * factor)
  else:
    r, g, b = round(60 * factor), round(100 * factor), round(255 * factor)

  # Retorno del color del shader.
  return utils.color(r, g, b)

# Shader para la planta del proyecto.
def plant_shader(**kwargs):

  # Parámetros necesarios para el shader.
  y = kwargs["y"]

  # Factor para el gradiente de la planta.
  y_factor = (1 - abs((160 - y) / 160))

  # Retorno del color con el gradiente incluido.
  return utils.color(30, round(150 * y_factor), 100)

# Shader para la roca gris del proyecto.
def rock_shader(**kwargs):

  # Parámetros necesarios para el shader.
  y = kwargs["y"]

  # Factor vertical del color de la roca.
  y_factor = (1 - abs((400 - y) / 100))
  actual_factor = max(min(y_factor, 1), 0)

  # Valor aleatorio para poner puntos blancos en la roca.
  random_value = random.random()

  # Puntos aleatorios en la roca.
  if (random_value <= 0.05):
    return utils.color(10, 10, 10)
  elif ((0.05 < random_value <= 0.1) and (y > 360)):
    return utils.color(200, 200, 200)

  # Retorno del gris del gradiente vertical de la roca.
  return utils.color(round(75 * actual_factor), round(75 * actual_factor), round(75 * actual_factor))

# Shader para el pino del proyecto.
def spruce_shader(**kwargs):

  # Parámetros necesarios para el shader.
  y = kwargs["y"]

  # Factor vertical del color del pino.
  y_factor = (1 - abs((425 - y) / 350))

  # Selección de un color aleatorio para frondosidad.
  if (random.random() < 0.1):
    return random.choice((
      utils.color(45, 145, 170),
      utils.color(50, 150, 175),
      utils.color(55, 155, 180),
      utils.color(60, 160, 185),
    ))

  # Color del pino según la gradiente vertical.
  return utils.color(50, round(150 * y_factor), round(175 * y_factor))
