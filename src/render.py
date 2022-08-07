"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos necesarios.
import math
import utils

# Definición de la clase Render.
class Render(object):

  # Propiedades variables del Render.
  __width: int = 0
  __height: int = 0
  __framebuffer: list[list[int]] = []
  __viewport_width: int = 0
  __viewport_height: int = 0
  __viewport_x_coordinate: int = 0
  __viewport_y_coordinate: int = 0

  # Constantes del render.
  __MAX_DIMENSION: int = 2147483647 # MAX WIDTH/HEIGHT 23169
  __FILE_HEADER_SIZE: int = 14
  __IMAGE_HEADER_SIZE: int = 40
  __HEADER_SIZE: int = (__FILE_HEADER_SIZE + __IMAGE_HEADER_SIZE)
  __COLORS_PER_PIXEL: int = 3

  # Constructor de la clase Render.
  def __init__(self) -> None:

    self.__current_color: bytes = utils.BLACK
    self.__viewport_color: bytes = utils.WHITE
    self.__vertex_color: bytes = utils.RED

  # Función que se encarga de crear una ventana.
  def gl_create_window(self, width: int, height: int) -> None:

    if ((width > 0) and (height > 0) and ((4 * width * (height + 1)) <= self.__MAX_DIMENSION)):
      self.__width = width
      self.__height = height
      self.gl_clear()
    else:
      raise Exception(f"Window dimensions are out of range [1, {self.__MAX_DIMENSION}].")

  # Función que cambia el color de gl_viewport().
  def gl_viewport_color(self, r: float, g: float, b: float) -> None:

    if ((0 <= r <= 1) or (0 <= g <= 1) or (0 <= b <= 1)):
      self.__viewport_color = utils.color(
        math.ceil(r * 255),
        math.ceil(g * 255),
        math.ceil(b * 255),
      )
    else:
      raise Exception("Color is out of range (0, 1).")

  # Función que crea un viewport sobre el cuál dibujar.
  def gl_viewport(self, x: int, y: int, width: int, height: int) -> None:

    if ((x < width) and (y < height) and (width < self.__width) and (height < self.__height)):

      self.__viewport_x_coordinate = x
      self.__viewport_y_coordinate = y
      self.__viewport_width = width
      self.__viewport_height = height

      for w in range(self.__viewport_width + 1):
        for h in range(self.__viewport_height + 1):
          self.__framebuffer[self.__viewport_y_coordinate + h][self.__viewport_x_coordinate + w] = self.__viewport_color

    else:
      raise Exception(f"Viewport dimensions are out of range [0, {self.__MAX_DIMENSION}].")

  # Función que limpia la ventana a un sólo color.
  def gl_clear(self) -> None:

    self.__framebuffer = [[(self.__current_color) for x in range(self.__width)] for y in range(self.__height)]

  # Función que cambia el color de gl_clear().
  def gl_clear_color(self, r: float, g: float, b: float) -> None:

    if ((0 <= r <= 1) or (0 <= g <= 1) or (0 <= b <= 1)):
      self.__current_color = utils.color(
        math.ceil(r * 255),
        math.ceil(g * 255),
        math.ceil(b * 255),
      )
    else:
      raise Exception("Color is out of range (0, 1).")

  # Función que coloca un punto en la pantalla con coordenadas absolutas.
  def gl_vertex(self, x: int, y: int) -> None:

    if (((-1 * self.__viewport_width) <= x <= self.__viewport_width) and ((-1 * self.__viewport_height) <= y <= self.__viewport_height)):
      self.__framebuffer[y + self.__viewport_y_coordinate][x + self.__viewport_x_coordinate] = self.__vertex_color
    else:
      raise Exception(f"Drawing is out of range [[0, {self.__width}], [0, {self.__height}]].")

  # Función que convierte coordenadas absolutas a relativas.
  def __relative_to_absolute_conversion(self, x, y) -> tuple[int, int]:

    cx, cy = (self.__viewport_width // 2), (self.__viewport_height // 2)
    return (((cx * x) + cx + self.__viewport_x_coordinate), ((cy * y) + cy + self.__viewport_y_coordinate))

  # Función que coloca un punto en la pantalla con coordenadas relativas.
  def gl_relative_vertex(self, x, y):

    if ((-1 <= x <= 1) and (-1 <= y <= 1)):
      px, py = self.__relative_to_absolute_conversion(x, y)
      self.__framebuffer[round(px)][round(py)] = self.__vertex_color
    else:
      raise Exception(f"Drawing is out of range [[-1, 1], [-1, 1]].")

  # Función que cambia el color de gl_point() y gl_vertex().
  def gl_color(self, r, g, b):

    if ((0 <= r <= 1) or (0 <= g <= 1) or (0 <= b <= 1)):
      self.__vertex_color = utils.color(
        math.ceil(r * 255),
        math.ceil(g * 255),
        math.ceil(b * 255),
      )
    else:
      raise Exception("Color is out of range (0, 1).")

  # Función que escribe el archivo .bmp con la imagen finalizada.
  def gl_finish(self, filename: str = "./images/image.bmp") -> None:

    bmp_filename: str = filename if filename.endswith(".bmp") else f"{filename}.bmp"
    actual_filename: str = bmp_filename if bmp_filename.startswith("./images/") else f"./images/{bmp_filename}"

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
