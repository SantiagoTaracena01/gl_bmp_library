import struct
import utils
from renderer import Renderer
from vector import Vector
from obj import Obj

class Texture(object):
  def __init__(self, path):
    self.path = path
    self.read()
  
  def read(self):
    with open(self.path, "rb") as image:
      image.seek(2 + 4 + 2 + 2)
      header_size = struct.unpack("=l", image.read(4))[0]
      image.seek(2 + 4 + 2 + 2 + 4 + 4)
      self.width = struct.unpack("=l", image.read(4))[0]
      self.height = struct.unpack("=l", image.read(4))[0]
      image.seek(header_size)
      self.pixels = []
      for y in range(self.height):
        self.pixels.append([])
        for x in range(self.width):
          b = ord(image.read(1))
          g = ord(image.read(1))
          r = ord(image.read(1))
          self.pixels[y].append(
            utils.color(r, g, b)
          )

  def get_color(self, tx, ty):
    x = round(tx * self.width)
    y = round(ty * self.height)
    return self.pixels[y][x]

  def get_color_with_intensity(self, tx, ty, intensity):
    x = round(tx * self.width)
    y = round(ty * self.height)
    
    r = self.pixels[y][x][0] * intensity
    g = self.pixels[y][x][1] * intensity
    b = self.pixels[y][x][2] * intensity
    
    return utils.color(r, g, b)

r = Renderer(1024, 1024)
t = Texture("./textures/model_txs.bmp")
r.gl_reset_framebuffer(t.pixels)
r.gl_color(1, 1, 1)

object_file = Obj("./models/model.obj")

# Iteración sobre cada cara del archivo .obj.
for face in object_file.faces:
  # Dibujo de un triángulo.
  if (len(face) == 3):

    # Cálculo de las caras del triángulo.
    first_face = (face[0][1] - 1)
    second_face = (face[1][1] - 1)
    third_face = (face[2][1] - 1)

    vt1 = Vector(
      object_file.texture_vertices[first_face][0] * t.width,
      object_file.texture_vertices[first_face][1] * t.height,
    )
    vt2 = Vector(
      object_file.texture_vertices[second_face][0] * t.width,
      object_file.texture_vertices[second_face][1] * t.height,
    )
    vt3 = Vector(
      object_file.texture_vertices[third_face][0] * t.width,
      object_file.texture_vertices[third_face][1] * t.height,
    )

    # Dibujo de los polígonos necesarios para el triángulo.
    r.gl_vector_line(vt1, vt2)
    r.gl_vector_line(vt2, vt3)
    r.gl_vector_line(vt3, vt1)

r.gl_finish("./images/texture.bmp")
