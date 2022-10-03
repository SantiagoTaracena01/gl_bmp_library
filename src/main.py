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
WIDTH = 1000
HEIGHT = 1000

renderer = Renderer()
renderer.gl_create_window(WIDTH, HEIGHT)
renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

start = time.time()

renderer.gl_color(1, 0, 0)
renderer.gl_point_line((200, 200), (800, 800))
renderer.gl_draw_triangle((200, 800), (400, 800), (200, 600))

filename = renderer.gl_finish()
print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
