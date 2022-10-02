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
    if ((0 < x < self.__viewport_width) and (0 < y < self.__viewport_height)):
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
    
    # Redondeo de los puntos de la línea.
    x0, y0, x1, y1 = round(x0), round(y0), round(x1), round(y1)

    # Diferenciales de la línea.
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)

    # Pendiente mayor o menor a 45 grados.
    steep = (dy > dx)

    # Cambio de variables si la pendiente es muy empinada.
    if (steep):
      x0, y0 = y0, x0
      x1, y1 = y1, x1

    # Cambio de variables para el orden de dibujo de la línea.
    if (x0 > x1):
      x0, x1 = x1, x0
      y0, y1 = y1, y0

    # Nuevo cálculo de los diferenciales de la línea.
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)

    # Variables importantes para dibujar.
    offset = 0
    threshold = dx
    y = y0

    # Iteración sobre los puntos de la línea.
    for x in range(x0, (x1 + 1)):

      # Dibujo de la línea.
      if (steep):
        self.gl_vertex(x, y)
      else:
        self.gl_vertex(y, x)

      # Recálculo del offset.
      offset += (dy * 2)

      # Cambio del threshold cuando el offset es mayor.
      if (offset >= threshold):
        y += 1 if (y0 < y1) else -1
        threshold += dx * 2

  # Función que dibuja una linea con coordenadas relativas.
  def gl_relative_line(self, x0, y0, x1, y1):
    if ((-1 <= x0 <= 1) and (-1 <= y0 <= 1) and (-1 <= x1 <= 1) and (-1 <= y1 <= 1)):
      x0, y0 = self.__relative_to_absolute_conversion(x0, y0)
      x1, y1 = self.__relative_to_absolute_conversion(x1, y1)
      self.gl_line(x0, y0, x1, y1)

  def __is_inside(self, x, y, polygon):
    result = False
    vertices = len(polygon)
    x0, y0 = polygon[0]
    for i in range((vertices + 1)):
      x1, y1 = polygon[(i % vertices)]
      if ((min(y0, y1) < y < max(y0, y1)) and (x <= max(x0, x1))):
        if (y0 != y1):
          x_interior = (y - y0) * (x1 - x0) / (y1 - y0) + x0
        if (x_interior and ((x0 == x1) or (x <= x_interior))):
          result = not result
      x0, y0 = x1, y1
    return result

  def gl_fill_polygon(self, polygon):
    for x in range(self.__width):
      for y in range(self.__height):
        if (self.__is_inside(x, y, polygon)):
          self.gl_vertex(x, y)

  # Función que transforma un vértice con constantes de escala y traslación dadas.
  def __transform_vertex(self, vertex, scale, translate):
    return [(vertex[0] * scale[0]) + translate[0], (vertex[1] * scale[1]) + translate[1]]

  # Función que carga y dibuja un archivo .obj.
  def gl_load_obj(self, obj_file, scale_factor, translate_factor):

    # Carga y lectura del archivo .obj.
    object_file = Obj(obj_file)

    # Iteración sobre cada cara del archivo .obj.
    for face in object_file.faces:

      # Dibujo de un cuadrado.
      if (len(face) == 4):

        # Cálculo de las caras del cuadrado.
        first_face = (face[0][0] - 1)
        second_face = (face[1][0] - 1)
        third_face = (face[2][0] - 1)
        fourth_face = (face[3][0] - 1)

        # Vértices del cuadrado a dibujar.
        first_vertex = self.__transform_vertex(object_file.vertices[first_face], scale_factor, translate_factor)
        second_vertex = self.__transform_vertex(object_file.vertices[second_face], scale_factor, translate_factor)
        third_vertex = self.__transform_vertex(object_file.vertices[third_face], scale_factor, translate_factor)
        fourth_vertex = self.__transform_vertex(object_file.vertices[fourth_face], scale_factor, translate_factor)

        # Dibujo de las líneas necesarias para el cuadrado.
        self.gl_line(first_vertex[0], first_vertex[1], second_vertex[0], second_vertex[1])
        self.gl_line(second_vertex[0], second_vertex[1], third_vertex[0], third_vertex[1])
        self.gl_line(third_vertex[0], third_vertex[1], fourth_vertex[0], fourth_vertex[1])
        self.gl_line(fourth_vertex[0], fourth_vertex[1], first_vertex[0], first_vertex[1])

      # Dibujo de un triángulo.
      elif (len(face) == 3):

        # Cálculo de las caras del triángulo.
        first_face = (face[0][0] - 1)
        second_face = (face[1][0] - 1)
        third_face = (face[2][0] - 1)

        # Vértices del triángulo a dibujar.
        first_vertex = self.__transform_vertex(object_file.vertices[first_face], scale_factor, translate_factor)
        second_vertex = self.__transform_vertex(object_file.vertices[second_face], scale_factor, translate_factor)
        third_vertex = self.__transform_vertex(object_file.vertices[third_face], scale_factor, translate_factor)

        # Dibujo de las líneas necesarias para el triángulo.
        self.gl_line(first_vertex[0], first_vertex[1], second_vertex[0], second_vertex[1])
        self.gl_line(second_vertex[0], second_vertex[1], third_vertex[0], third_vertex[1])
        self.gl_line(third_vertex[0], third_vertex[1], first_vertex[0], first_vertex[1])

  # Método para renderizar la imagen creada.
  def gl_finish(self, filename="./images/image.bmp"):

    # Formateo del nombre del archivo para estar en la carpeta de imágenes.
    bmp_filename = filename if filename.endswith(".bmp") else f"{filename}.bmp"
    actual_filename = bmp_filename if bmp_filename.startswith("./images/") else f"./images/{bmp_filename}"

    # Apertura del archivo.
    file = open(actual_filename, "bw")

    # Escritura preliminar del header del archivo.
    file.write(utils.char("B"))
    file.write(utils.char("M"))
    file.write(utils.dword(self.__HEADER_SIZE + (self.__width * self.__height * self.__COLORS_PER_PIXEL)))
    file.write(utils.dword(0))
    file.write(utils.dword(self.__HEADER_SIZE))

    # Finalización de la escritura del header del archivo.
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

    # Escritura de cada pixel del archivo mediante los valores del framebuffer.
    for x in range(self.__width):
      for y in range(self.__height):
        file.write(self.__framebuffer[y][x])

    # Cierre del archivo.
    file.close()

    # Retorno del nombre del archivo para futuras operaciones.
    return actual_filename
