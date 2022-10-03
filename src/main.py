"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos/librerías importadas para el desarrollo de main.py.
from renderer import Renderer
import time

# Ancho y alto de la imagen creada.
WIDTH = 200
HEIGHT = 200

renderer = Renderer()
renderer.gl_create_window(WIDTH, HEIGHT)
renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

start = time.time()

renderer.gl_draw_triangle((10, 70), (50, 160), (70, 80), (1, 0, 0))
renderer.gl_draw_triangle((180, 50), (150, 10), (70, 180), (1, 1, 1))
renderer.gl_draw_triangle((180, 150), (120, 160), (130, 180), (0, 1, 0))

filename = renderer.gl_finish()
print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
