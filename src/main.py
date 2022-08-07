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
my_render.gl_viewport_color(0.8, 0.8, 1)
my_render.gl_viewport(125, 125, 250, 250)
my_render.gl_vertex(125, 125)
my_render.gl_color(0.25, 0.25, 0.8)
my_render.gl_relative_vertex(0.75, -0.75)
my_render.gl_finish("./images/output.bmp")
