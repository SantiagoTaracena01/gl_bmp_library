"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos/librerías importadas para el desarrollo de main.py.
from renderer import Renderer
from texture import Texture
import time

# Código principal del programa.
if __name__ == "__main__":

  # Ancho y alto de la imagen creada.
  WIDTH = 1000
  HEIGHT = 1000

  # Valores de escala y traslación del modelo.
  SCALE = (2400, 2400, 2400)
  TRANSLATE = (500, 500, 0)

  # Instancia y creación de valores básicos del renderer.
  renderer = Renderer()
  renderer.gl_create_window(WIDTH, HEIGHT)
  renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

  # Inicio del tiempo de renderización.
  start = time.time()

  # Proceso de renderización.
  model_texture = Texture("./textures/mask_txs.bmp")
  renderer.gl_load_texture(model_texture)
  renderer.gl_load_obj("./models/mask.obj", SCALE, TRANSLATE, (1, 0.6, 0.85))
  filename = renderer.gl_finish()

  # Impresión de resultados finales.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
