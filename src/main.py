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
from shaders import plant_shader, rock_shader
import time
import math

# Código principal del programa.
if __name__ == "__main__":

  # Ancho y alto de la imagen creada.
  WIDTH = 1000
  HEIGHT = 1000

  # Valores de traslación, escala y rotación del modelo.
  TRANSLATE = (0, 0, 0)
  SCALE = (0.025, 0.025, 0.0025)
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

  """
  Fondo de pantalla de la escena.
  """

  # Fondo de la imagen o escena.
  jungle_background = Texture("./backgrounds/jungle.bmp")
  renderer.gl_load_background(jungle_background.pixels)

  """
  Modelos con texturas (5)
  """

  # Gato.
  cat_texture = Texture("./textures/cat_txs.bmp")
  renderer.gl_load_texture(cat_texture)
  renderer.gl_load_obj("./models/cat.obj", (0.6, -0.65, 0), (1, 1, 1), (0, (-1 * (math.pi / 4)), 0))

  # Máscara.
  mask_texture = Texture("./textures/mask_txs.bmp")
  renderer.gl_load_texture(mask_texture)
  renderer.gl_load_obj("./models/mask.obj", (-0.525, 0.35, 0), (1.5, 1.5, 1.5), (0, (math.pi / 6), 0))

  # Otra máscara.
  second_mask_texture = Texture("./textures/other_mask_txs.bmp")
  renderer.gl_load_texture(second_mask_texture)
  renderer.gl_load_obj("./models/other_mask.obj", (3.65, -0.35, 0), (1.5, 1.5, 1.5), ((math.pi / 9), (-1 * (math.pi / 6)), 0))

  # Piedra marrón.
  rocks_texture = Texture("./textures/rocks_txs.bmp")
  renderer.gl_load_texture(rocks_texture)
  renderer.gl_load_obj("./models/rocks.obj", (0.15, -0.9, 0), (0.00075, 0.00075, 0.00075), (0, 0, 0))

  # Calabazas.
  pumpkins_texture = Texture("./textures/pumpkins_txs.bmp")
  renderer.gl_load_texture(pumpkins_texture)
  renderer.gl_load_obj("./models/pumpkins.obj", (-0.45, -0.6, 0), (0.45, 0.45, 0.45), (0, 0, 0))

  # Monki :smiling_imp:.
  monki_texture = Texture("./textures/monki_txs.bmp")
  renderer.gl_load_texture(monki_texture)
  renderer.gl_load_obj("./models/monki.obj", (0, 0.05, 0), (0.004, 0.004, 0.004), ((math.pi), ((-1 * math.pi) / 2), (math.pi / 8)))

  """
  Modelos con shaders (5)
  """

  # Planta exótica.
  renderer.gl_load_shader(plant_shader)
  renderer.gl_load_obj("./models/plant.obj", (-0.6, -0.75, 0), (0.0045, 0.0045, 0.0045), (0, 0, 0))

  # Piedra con shaders.
  renderer.gl_load_shader(rock_shader)
  renderer.gl_load_obj("./models/rock.obj", (0.1, -0.3, 0), (0.003, 0.003, 0.003), ((math.pi / 6), 0, 0))

  # Finalización del renderizado.
  filename = renderer.gl_finish("./images/scene.bmp")

  # Impresión de resultados finales.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
