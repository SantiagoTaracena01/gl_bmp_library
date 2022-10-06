"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos necesarios.
from obj import Obj
from vector import Vector
import utils
import random
import math

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
    self.__background_color = utils.BLACK
    self.__current_color = utils.WHITE
    self.__framebuffer = []
    self.__z_buffer = [[-999999 for x in range(self.__width)] for y in range(self.__height)]
    self.gl_clear()

  # Función que limpia la ventana a un sólo color.
  def gl_clear(self):
    self.__framebuffer = [[(self.__background_color) for x in range(self.__width)] for y in range(self.__height)]

  # Función que cambia el color de gl_clear().
  def gl_clear_color(self, r, g, b):
    self.__background_color = utils.color(
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
        self.__framebuffer[self.__viewport_y_coordinate + h][self.__viewport_x_coordinate + w] = self.__background_color

  # Función que permite intercambiar o crear un framebuffer personalizado.
  def gl_reset_framebuffer(self, new_framebuffer=[]):
    self.__framebuffer = new_framebuffer

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

  # Función que dibuja una línea con coordenadas relativas.
  def gl_relative_line(self, x0, y0, x1, y1):
    if ((-1 <= x0 <= 1) and (-1 <= y0 <= 1) and (-1 <= x1 <= 1) and (-1 <= y1 <= 1)):
      x0, y0 = self.__relative_to_absolute_conversion(x0, y0)
      x1, y1 = self.__relative_to_absolute_conversion(x1, y1)
      self.gl_line(x0, y0, x1, y1)

  # Función que dibuja una línea dados dos puntos p y q.
  def gl_vector_line(self, P, Q):
    x0, y0 = P.x, P.y
    x1, y1 = Q.x, Q.y
    self.gl_line(x0, y0, x1, y1)

  # Función que calcula si un punto está dentro de un polígono.
  def __is_inside(self, x, y, polygon):

    # Variables útiles para el proceso.
    result = False
    vertices = len(polygon)
    value = (vertices - 1)

    # Iteración sobre cada vértice del polígono.
    for i in range(vertices):

      # Descarte de puntos que sean parte de las líneas fronterizas del polígono.
      if ((x == polygon[i][0]) and (y == polygon[i][1])):
        return True

      # Evaluación de la elevación de cada punto del polígono.
      if ((polygon[i][1] > y) != (polygon[value][1] > y)):

        # Cálculo de la pendiente entre los dos puntos.
        upper_slope_component = ((x - polygon[i][0]) * (polygon[value][1] - polygon[i][1]))
        lower_slope_component = ((polygon[value][0] - polygon[i][0]) * (y - polygon[i][1]))
        slope = (upper_slope_component - lower_slope_component)

        # Si la pendiente es cero, el punto está dentro.
        if (slope == 0):
          return True

        # Si las pendientes siguen siendo diferentes, recalculamos el resultado.
        elif ((slope < 0) != (polygon[value][1] < polygon[i][1])):
          result = not result

      # Cambio de vértice actual.
      value = i

    # Retorno del resultado.
    return result

  # Función que dibuja y colorea un polígono de puntos dados.
  def gl_fill_polygon(self, polygon):
    for x in range(self.__width):
      for y in range(self.__height):
        if (self.__is_inside(x, y, polygon)):
          self.gl_vertex(x, y)

  # Función que carga y dibuja un archivo .obj.
  def gl_load_obj(self, obj_file, scale_factor, translate_factor, color=None):

    # Nueva definición del color del modelo.
    if (color is None):
      color = (1, 1, 1)

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
        first_vertex = utils.transform_vertex(object_file.vertices[first_face], scale_factor, translate_factor)
        second_vertex = utils.transform_vertex(object_file.vertices[second_face], scale_factor, translate_factor)
        third_vertex = utils.transform_vertex(object_file.vertices[third_face], scale_factor, translate_factor)
        fourth_vertex = utils.transform_vertex(object_file.vertices[fourth_face], scale_factor, translate_factor)

        # Dibujo de los polígonos necesarios para pintar el modelo.
        self.gl_draw_triangle(Vector(*first_vertex), Vector(*second_vertex), Vector(*third_vertex), color)
        self.gl_draw_triangle(Vector(*first_vertex), Vector(*third_vertex), Vector(*fourth_vertex), color)

      # Dibujo de un triángulo.
      elif (len(face) == 3):

        # Cálculo de las caras del triángulo.
        first_face = (face[0][0] - 1)
        second_face = (face[1][0] - 1)
        third_face = (face[2][0] - 1)

        # Vértices del triángulo a dibujar.
        first_vertex = utils.transform_vertex(object_file.vertices[first_face], scale_factor, translate_factor)
        second_vertex = utils.transform_vertex(object_file.vertices[second_face], scale_factor, translate_factor)
        third_vertex = utils.transform_vertex(object_file.vertices[third_face], scale_factor, translate_factor)

        if (self.texture):

          # Cálculo de las caras del triángulo.
          first_texture_face = (face[0][1] - 1)
          second_texture_face = (face[1][1] - 1)
          third_texture_face = (face[2][1] - 1)

          # Vértices del triángulo a dibujar.
          first_texture_vertex = Vector(
            object_file.vertices[first_texture_face][0] * self.texture.width,
            object_file.vertices[first_texture_face][1] * self.texture.height
          )
          second_texture_vertex = Vector(
            object_file.vertices[second_texture_face][0] * self.texture.width,
            object_file.vertices[second_texture_face][1] * self.texture.height
          )
          third_texture_vertex = Vector(
            object_file.vertices[third_texture_face][0] * self.texture.width,
            object_file.vertices[third_texture_face][1] * self.texture.height
          )

        else:

          # Dibujo de los polígonos necesarios para el triángulo.
          self.gl_draw_triangle(Vector(*first_vertex), Vector(*second_vertex), Vector(*third_vertex), color)

  # Función que halla los límites de un triángulo a pintar.
  def __bounding_box(self, A, B, C):

    # Coordenadas de los vértices del triángulo.
    coords = [(A.x, A.y), (B.x, B.y), (C.x, C.y)]

    # Valores mínimos y máximos exagerados.
    xmin = 9999
    xmax = -9999
    ymin = 9999
    ymax = -9999

    # Cálculo de los nuevos máximos y mínimos.
    for (x, y) in coords:
      if (x < xmin):
        xmin = x
      if (x > xmax):
        xmax = x
      if (y < ymin):
        ymin = y
      if (y > ymax):
        ymax = y

    # Retorno de los vectores mínimos y máximos del triángulo.
    return Vector(xmin, ymin), Vector(xmax, ymax)

  # Función que calcula coordenadas baricéntricas.
  def __barycentric_coords(self, A, B, C, P):

    # Vector creado para el cálculo de las coordenadas.
    V = (Vector((B.x - A.x), (C.x - A.x), (A.x - P.x)) * Vector((B.y - A.y), (C.y - A.y), (A.y - P.y)))

    # Cálculo de los valores u, v y w resultantes.
    try:
      u = (V.x / V.z)
      v = (V.y / V.z)
      w = (1 - ((V.x + V.y) / V.z))
    except:
      u, v, w = -1, -1, -1

    # Retorno de los valores w, v y u.
    return (w, v, u)

  # Función que dibuja un triángulo dados tres puntos A, B y C.
  def gl_draw_triangle(self, A, B, C, color=None):

    # Luz, vector normal e intensidad del triángulo.
    light = Vector(0, 0, -1)
    normal = ((C - A) * (B - A))
    intensity = (light.norm() @ normal.norm())

    # Si la intensidad es menor a cero, no dibujamos nada.
    if (intensity < 0):
      return

    # Cambio de color para colorear un modelo.
    if (color is not None):
      self.gl_color(color[0] * intensity, color[1] * intensity, color[2] * intensity)

    # Coloración en blanco y negro del modelo.
    else:
      self.gl_color(intensity, intensity, intensity)

    # Puntos mínimos y máximos sobre los cuáles dibujar.
    min_point, max_point = self.__bounding_box(A, B, C)
    min_point.round_coords()
    max_point.round_coords()

    # Iteración sobre el triángulo a pintar.
    for x in range(min_point.x, (max_point.x + 1)):
      for y in range(min_point.y, (max_point.y + 1)):

        # Coordenadas a pintar.
        w, v, u = self.__barycentric_coords(A, B, C, Vector(x, y))

        # Casos en los que el punto no se encuentra en el triángulo.
        if (w < 0 or v < 0 or u < 0):
          continue

        # Cálculo de la coordenada z del triángulo a pintar.
        z = ((A.z * w) + (B.z * v) + (C.z * u))

        # Si el valor a pintar está frente al último valor del z-buffer, lo pintamos.
        if (self.__z_buffer[x][y] < z):
          self.__z_buffer[x][y] = z
          self.gl_vertex(y, x)

  # Función para renderizar la imagen creada.
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
    for y in range(self.__height):
      for x in range(self.__width):
        file.write(self.__framebuffer[y][x])

    # Cierre del archivo.
    file.close()

    # Retorno del nombre del archivo para futuras operaciones.
    return actual_filename
