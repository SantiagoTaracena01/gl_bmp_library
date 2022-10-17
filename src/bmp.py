"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el archivo bmp.py.
import utils

# Función que escribe un archivo .bmp.
def write_bmp(filename, framebuffer, width, height, constants):
  
  # Constantes teóricas utilizadas para escribir un .bmp.
  HEADER_SIZE, IMAGE_HEADER_SIZE, COLORS_PER_PIXEL = constants
  
  # Formateo del nombre del archivo para estar en la carpeta de imágenes.
  bmp_filename = filename if filename.endswith(".bmp") else f"{filename}.bmp"
  actual_filename = bmp_filename if bmp_filename.startswith("./images/") else f"./images/{bmp_filename}"

  # Apertura del archivo.
  file = open(actual_filename, "bw")

  # Escritura preliminar del header del archivo.
  file.write(utils.char("B"))
  file.write(utils.char("M"))
  file.write(utils.dword(HEADER_SIZE + (width * height * COLORS_PER_PIXEL)))
  file.write(utils.dword(0))
  file.write(utils.dword(HEADER_SIZE))

  # Finalización de la escritura del header del archivo.
  file.write(utils.dword(IMAGE_HEADER_SIZE))
  file.write(utils.dword(width))
  file.write(utils.dword(height))
  file.write(utils.word(1))
  file.write(utils.word(24))
  file.write(utils.dword(0))
  file.write(utils.dword(width * height * COLORS_PER_PIXEL))
  file.write(utils.dword(0))
  file.write(utils.dword(0))
  file.write(utils.dword(0))
  file.write(utils.dword(0))

  # Escritura de cada pixel del archivo mediante los valores del framebuffer.
  for y in range(height):
    for x in range(width):
      file.write(framebuffer[y][x])

  # Cierre del archivo.
  file.close()

  # Retorno del nombre del archivo para futuras operaciones.
  return actual_filename

# Función que lee un archivo .bmp.
def read_bmp(path):
  with open(path, "rb") as image:
    image.seek(2 + 4 + 2 + 2)
    header_size = utils.unpack(image.read(4))
    image.seek(2 + 4 + 2 + 2 + 4 + 4)
    width = utils.unpack(image.read(4))
    height = utils.unpack(image.read(4))
    image.seek(header_size)
    pixels = []
    for y in range(height):
      pixels.append([])
      for x in range(width):
        b = ord(image.read(1))
        g = ord(image.read(1))
        r = ord(image.read(1))
        pixels[y].append(
          utils.color(r, g, b)
        )
  return width, height, pixels
