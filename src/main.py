"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos/librerías importadas para el desarrollo de main.py.
from renderer import Renderer
# from obj import Obj

# Ancho y alto de la imagen creada.
WIDTH = 1000
HEIGHT = 1000

renderer = Renderer()
renderer.gl_create_window(WIDTH, HEIGHT)
renderer.gl_color(0, 0.25, 0.5)
renderer.gl_viewport(0, 0, WIDTH, HEIGHT)
renderer.gl_color(1, 1, 1)

"""
(-0.70, -0.40)
(-0.25, -0.70)
(-0.25, -0.30)
(-0.70, +0.00)
"""

# Pared izquierda de la casa.
renderer.gl_relative_line(-0.70, -0.40, -0.25, -0.70)
renderer.gl_relative_line(-0.25, -0.70, -0.25, -0.30)
renderer.gl_relative_line(-0.25, -0.30, -0.70, 0)
renderer.gl_relative_line(-0.70, 0, -0.70, -0.40)

# Pared frontal de la casa.
renderer.gl_relative_line(-0.25, -0.70, 0.05, -0.60)
renderer.gl_relative_line(0.05, -0.60, 0.05, -0.35)
renderer.gl_relative_line(0.05, -0.35, 0.25, -0.30)
renderer.gl_relative_line(0.25, -0.30, 0.25, -0.50)
renderer.gl_relative_line(0.25, -0.50, 0.55, -0.40)
renderer.gl_relative_line(0.55, -0.40, 0.55, 0.00)
renderer.gl_relative_line(0.55, 0.00, 0.10, 0.30)
renderer.gl_relative_line(0.10, 0.30, -0.25, -0.30)

# Techo de la casa.
renderer.gl_relative_line(-0.35, 0.45, -0.70, 0.00)
renderer.gl_relative_line(-0.35, 0.45, 0.10, 0.30)

# Chimenea de la casa.
renderer.gl_relative_line(-0.15, 0.385, -0.15, 0.55)
renderer.gl_relative_line(-0.15, 0.55, -0.10, 0.55)
renderer.gl_relative_line(-0.10, 0.55, -0.10, 0.3675)

renderer.gl_finish("./images/house.bmp")

# square = [(250, 250), (750, 250), (750, 750), (250, 750)]
# right_square = [(450, 250), (950, 250), (950, 750), (450, 750)]

# last_point = right_square[-1]

# for point in right_square:
#   my_render.gl_line(*last_point, *point)
#   last_point = point

# my_render.gl_load_obj("./models/cube.obj")
