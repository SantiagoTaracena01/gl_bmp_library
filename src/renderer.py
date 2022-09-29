"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos necesarios.
from obj import Obj
import math
import utils

# Definición de la clase Render.
class Renderer(object):

  # Constantes del render.
  __FILE_HEADER_SIZE = 14
  __IMAGE_HEADER_SIZE = 40
  __HEADER_SIZE = (__FILE_HEADER_SIZE + __IMAGE_HEADER_SIZE)
  __COLORS_PER_PIXEL = 3

  # Constructor de la clase Render.
  def __init__(self, width=1000, height=1000):
    self.__width = width
    self.__height = height
    self.__viewport_width = 0
    self.__viewport_height = 0
    self.__viewport_x_coordinate = 0
    self.__viewport_y_coordinate = 0
    self.__clear_color = utils.BLACK
    self.__current_color = utils.WHITE
    self.__framebuffer = []
    self.gl_clear()

  # Función que limpia la ventana a un sólo color.
  def gl_clear(self):
    self.__framebuffer = [[(self.__clear_color) for x in range(self.__width)] for y in range(self.__height)]

  # Función que cambia el color de gl_clear().
  def gl_clear_color(self, r, g, b):
    self.__clear_color = utils.color(
      math.ceil(r * 255),
      math.ceil(g * 255),
      math.ceil(b * 255),
    )
  
  # Función que cambia el color de los dibujos realizados.
  def gl_color(self, r, g, b):
    self.__current_color = utils.color(
      math.ceil(r * 255),
      math.ceil(g * 255),
      math.ceil(b * 255),
    )

  # Función que se encarga de crear una ventana.
  def gl_create_window(self, width, height):
    self.__width = width
    self.__height = height
    self.gl_clear()

  # Función que crea un viewport sobre el cuál dibujar.
  def gl_viewport(self, x, y, width, height):
    self.__viewport_x_coordinate = x
    self.__viewport_y_coordinate = y
    self.__viewport_width = width
    self.__viewport_height = height
    for w in range(self.__viewport_width):
      for h in range(self.__viewport_height):
        self.__framebuffer[self.__viewport_y_coordinate + h][self.__viewport_x_coordinate + w] = self.__current_color

  # Función que convierte coordenadas absolutas a relativas.
  def __relative_to_absolute_conversion(self, x, y) -> tuple[int, int]:
    cx, cy = (self.__viewport_width // 2), (self.__viewport_height // 2)
    px, py = (round((x + 1) * cx) + self.__viewport_x_coordinate), (round((y + 1) * cy) + self.__viewport_y_coordinate)
    return (px, py)

  # Función que coloca un punto en la pantalla con coordenadas absolutas.
  def gl_vertex(self, x, y):
    if ((0 <= x <= self.__viewport_width) and (0 <= y <= self.__viewport_height)):
      self.__framebuffer[y][x] = self.__current_color

  # Función que coloca un punto en cualquier parte de la pantalla.
  def gl_absolute_vertex(self, x, y):
    if ((0 <= x <= self.__width) and (0 <= y <= self.__height)):
      self.__framebuffer[y + self.__viewport_y_coordinate][x + self.__viewport_x_coordinate] = self.__current_color

  # Función que coloca un punto en la pantalla con coordenadas relativas.
  def gl_relative_vertex(self, x, y):
    if ((-1 <= x <= 1) and (-1 <= y <= 1)):
      px, py = self.__relative_to_absolute_conversion(x, y)
      self.__framebuffer[px][py] = self.__current_color

  # Función que dibuja una línea en la pantalla.
  def gl_line(self, x0, y0, x1, y1):

    dy = abs(y1 - y0)
    dx = abs(x1 - x0)

    steep = (dy > dx)

    if (steep):
      x0, y0 = y0, x0
      x1, y1 = y1, x1

    if (x0 > x1):
      x0, x1 = x1, x0
      y0, y1 = y1, y0

    dy = abs(y1 - y0)
    dx = abs(x1 - x0)

    offset = 0
    threshold = dx
    y = y0

    for x in range(x0, (x1 + 1)):

      if (steep):
        self.gl_vertex(x, y)
      else:
        self.gl_vertex(y, x)

      offset += (dy * 2)

      if (offset >= threshold):
        y += 1 if (y0 < y1) else -1
        threshold += dx * 2

  # Función que dibuja una linea con coordenadas relativas.
  def gl_relative_line(self, x0, y0, x1, y1):
    if ((-1 <= x0 <= 1) and (-1 <= y0 <= 1) and (-1 <= x1 <= 1) and (-1 <= y1 <= 1)):
      x0, y0 = self.__relative_to_absolute_conversion(x0, y0)
      x1, y1 = self.__relative_to_absolute_conversion(x1, y1)
      self.gl_line(x0, y0, x1, y1)

  # Función que carga y dibuja un archivo .obj.
  def gl_load_obj(self, obj_file):
    
    object_file = Obj(obj_file)
    
    for face in object_file.get_faces():
      
      first_face = (face[0][0] - 1)
      second_face = (face[1][0] - 1)
      third_face = (face[2][0] - 1)
      fourth_face = (face[3][0] - 1)
      
      vertices = object_file.get_vertices()
      
      first_vertex = vertices[first_face]
      second_vertex = vertices[second_face]
      third_vertex = vertices[third_face]
      fourth_vertex = vertices[fourth_face]
      
      self.gl_relative_line(first_vertex[0], first_vertex[1], second_vertex[0], second_vertex[1])
      self.gl_relative_line(second_vertex[0], second_vertex[1], third_vertex[0], third_vertex[1])
      self.gl_relative_line(third_vertex[0], third_vertex[1], fourth_vertex[0], fourth_vertex[1])
      self.gl_relative_line(fourth_vertex[0], fourth_vertex[1], first_vertex[0], first_vertex[1])

  # Función que escribe el archivo .bmp con la imagen finalizada.
  def gl_finish(self, filename="./images/image.bmp"):

    bmp_filename = filename if filename.endswith(".bmp") else f"{filename}.bmp"
    actual_filename = bmp_filename if bmp_filename.startswith("./images/") else f"./images/{bmp_filename}"

    file = open(actual_filename, "bw")

    file.write(utils.char("B"))
    file.write(utils.char("M"))
    file.write(utils.dword(self.__HEADER_SIZE + (self.__width * self.__height * self.__COLORS_PER_PIXEL)))
    file.write(utils.dword(0))
    file.write(utils.dword(self.__HEADER_SIZE))

    file.write(utils.dword(self.__IMAGE_HEADER_SIZE))
    file.write(utils.dword(self.__width))
    file.write(utils.dword(self.__height))
    file.write(utils.word(1))
    file.write(utils.word(24))
    file.write(utils.dword(0))
    file.write(utils.dword(self.__width * self.__height * self.__COLORS_PER_PIXEL))
    file.write(utils.dword(0))
    file.write(utils.dword(0))
    file.write(utils.dword(0))
    file.write(utils.dword(0))

    for x in range(self.__width):
      for y in range(self.__height):
        file.write(self.__framebuffer[y][x])

    file.close()
