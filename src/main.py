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
from shaders import planet_shader
import time
import math

# Código principal del programa.
if __name__ == "__main__":

  # Ancho y alto de la imagen creada.
  WIDTH = 1000
  HEIGHT = 1000

  # Valores de traslación, escala y rotación del modelo.
  TRANSLATE = (0, 0, 0)
  SCALE = (0.0025, 0.0025, 0.0025)
  ROTATE = (0, 0, 0)

  # Instancia y creación de valores básicos del renderer.
  renderer = Renderer()
  renderer.gl_create_window(WIDTH, HEIGHT)
  renderer.gl_viewport(0, 0, WIDTH, HEIGHT)
  renderer.gl_look_at(Vector(0, 0, 10), Vector(0, 0, 0), Vector(0, 1, 0))
  renderer.gl_clear_color(0, 0, 0.02)
  renderer.gl_clear()

  # Inicio del tiempo de renderización.
  start = time.time()

  # # Fondo de la imagen o escena.
  # jungle_background = Texture("./backgrounds/jungle.bmp")
  # renderer.gl_load_background(jungle_background.pixels)

  # # Gato.
  # cat_texture = Texture("./textures/cat_txs.bmp")
  # renderer.gl_load_texture(cat_texture)
  # renderer.gl_load_obj("./models/cat.obj", (0.6, -0.65, 0), (1, 1, 1), (0, (-1 * (math.pi / 4)), 0))

  # # Máscara.
  # mask_texture = Texture("./textures/mask_txs.bmp")
  # renderer.gl_load_texture(mask_texture)
  # renderer.gl_load_obj("./models/mask.obj", (-0.525, 0.35, 0), (1, 1, 1), (0, (math.pi / 6), 0))

  # # Otra máscara lol.
  # second_mask_texture = Texture("./textures/other_mask_txs.bmp")
  # renderer.gl_load_texture(second_mask_texture)
  # renderer.gl_load_obj("./models/other_mask.obj", (0, 0, 0), (100, 100, 100), (0, (-1 * (math.pi / 6)), 0))

  # Proceso de renderización.
  renderer.gl_load_shader(planet_shader)
  model_texture = Texture("./textures/model_txs.bmp")
  renderer.gl_load_texture(model_texture)
  renderer.gl_load_obj("./models/earth.obj", TRANSLATE, SCALE, ROTATE)
  filename = renderer.gl_finish("./images/neptune.bmp")

  # Impresión de resultados finales.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
