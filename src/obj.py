"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

class Obj(object):
  
  def __init__(self, filename):
    
    with open(filename) as file:
      self.__lines = file.read().splitlines()
    
    self.__vertices = []
    self.__faces = []
    
    for line in self.__lines:
      prefix, value = line.split(" ", 1)
      if (prefix == "v"):
        self.__vertices.append(list(map(float, value.split(" "))))
      elif (prefix == "f"):
        self.__faces.append([list(map(int, face.split("/"))) for face in value.split(" ")])

  def get_vertices(self):
    return self.__vertices

  def get_faces(self):
    return self.__faces
