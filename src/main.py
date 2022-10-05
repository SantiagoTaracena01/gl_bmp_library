"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos/librerías importadas para el desarrollo de main.py.
from renderer import Renderer
import time

# Código principal del programa.
if __name__ == "__main__":

  # Ancho y alto de la imagen creada.
  WIDTH = 1000
  HEIGHT = 1000

  SCALE = (35, 35, 35)
  TRANSLATE = (500, 550, 0)

  renderer = Renderer()
  renderer.gl_create_window(WIDTH, HEIGHT)
  renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

  start = time.time()

  renderer.gl_load_obj("./models/hylian_shield.obj", SCALE, TRANSLATE)

  filename = renderer.gl_finish()
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
