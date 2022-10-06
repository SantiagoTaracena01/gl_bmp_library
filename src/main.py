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
  SCALE = (0.75, 0.75, 0.75)
  TRANSLATE = (500, 550, 0)

  # Instancia y creación de valores básicos del renderer.
  renderer = Renderer()
  renderer.gl_create_window(WIDTH, HEIGHT)
  renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

  # Inicio del tiempo de renderización.
  start = time.time()

  # Proceso de renderización.
  renderer.gl_load_obj("./models/yoshi.obj", SCALE, TRANSLATE)
  filename = renderer.gl_finish("./images/yoshi.bmp")

  # Impresión de resultados finales.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
