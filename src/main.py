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

  # Valores de escala y traslación del modelo.
  SCALE = (1000, 1000, 1000)
  TRANSLATE = (500, 100, 0)

  # Instancia y creación de valores básicos del renderer.
  renderer = Renderer()
  renderer.gl_create_window(WIDTH, HEIGHT)
  renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

  # Inicio del tiempo de renderización.
  start = time.time()

  # Proceso de renderización.
  renderer.gl_load_obj("./models/natsuki.obj", SCALE, TRANSLATE, (1, 0.6, 0.85))
  filename = renderer.gl_finish()

  # Impresión de resultados finales.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
