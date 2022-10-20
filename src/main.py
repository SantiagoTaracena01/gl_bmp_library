"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos/librerías importadas para el desarrollo de main.py.
from renderer import Renderer
from texture import Texture
from vector import Vector
import time
import math

# Código principal del programa.
if __name__ == "__main__":

  # Ancho y alto de la imagen creada.
  WIDTH = 1000
  HEIGHT = 1000

  # Valores de traslación, escala y rotación del modelo.
  TRANSLATE = (0, 0, 0)
  SCALE = (7.5, 7.5, 7.5)
  ROTATE = (0, (math.pi / 6), 0)

  # Instancia y creación de valores básicos del renderer.
  renderer = Renderer()
  renderer.gl_create_window(WIDTH, HEIGHT)
  renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

  # Inicio del tiempo de renderización.
  start = time.time()

  # Proceso de renderización.
  renderer.gl_look_at(Vector(0, 0, 10), Vector(0, 0, 0), Vector(0, 1, 0))
  model_texture = Texture("./textures/mask_txs.bmp")
  renderer.gl_load_texture(model_texture)
  renderer.gl_load_obj("./models/mask.obj", TRANSLATE, SCALE, ROTATE)
  filename = renderer.gl_finish()

  # Impresión de resultados finales.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
