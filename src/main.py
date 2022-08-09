"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

from render import Render

WIDTH: int = 500
HEIGHT: int = 500

my_render = Render()
my_render.gl_create_window(WIDTH, HEIGHT)
my_render.gl_viewport_color(0.9, 0.9, 1)
my_render.gl_viewport(0, 0, WIDTH, HEIGHT)

"""
(-0.70, -0.40)
(-0.25, -0.70)
(-0.25, -0.30)
(-0.70, +0.00)
"""

# Pared izquierda de la casa.
my_render.gl_relative_line(-0.70, -0.40, -0.25, -0.70)
my_render.gl_relative_line(-0.25, -0.70, -0.25, -0.30)
my_render.gl_relative_line(-0.25, -0.30, -0.70, 0)
my_render.gl_relative_line(-0.70, 0, -0.70, -0.40)

# Pared frontal de la casa.
my_render.gl_relative_line(-0.25, -0.70, 0.05, -0.60)
my_render.gl_relative_line(0.05, -0.60, 0.05, -0.35)
my_render.gl_relative_line(0.05, -0.35, 0.25, -0.25)

my_render.gl_finish("output.bmp")
