import utils
import bmp

class Texture(object):
  def __init__(self, path):
    self.path = path
    self.width, self.height, self.pixels = bmp.read_bmp(path)

  def get_color(self, tx, ty):
    x = round(tx * self.width)
    y = round(ty * self.height)
    return self.pixels[y][x]

  def get_color_with_intensity(self, tx, ty, intensity):
    x = round(tx * self.width)
    y = round(ty * self.height)
    
    b = round(self.pixels[y][x][0] * intensity)
    g = round(self.pixels[y][x][1] * intensity)
    r = round(self.pixels[y][x][2] * intensity)
    
    return utils.color(r, g, b)
