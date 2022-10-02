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
renderer.gl_color(0, 0, 0)
renderer.gl_create_window(WIDTH, HEIGHT)
renderer.gl_viewport(0, 0, WIDTH, HEIGHT)

renderer.gl_color(0, 0.5, 1)

scale_factor = (25, 25)
translate_factor = (500, 500)

renderer.gl_load_obj("./models/hylian_shield.obj", scale_factor, translate_factor)

# renderer.gl_color(1, 0, 0)
# renderer.gl_fill_polygon([
#   (165, 380), (185, 360), (180, 330), (207, 345), (233, 330), 
#   (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)
# ])

# renderer.gl_color(0, 1, 0)
# renderer.gl_fill_polygon([(321, 335), (288, 286), (339, 251), (374, 302)])

# renderer.gl_color(0, 0, 1)
# renderer.gl_fill_polygon([(377, 249), (411, 197), (436, 249)])

# renderer.gl_color(0, 1, 1)
# renderer.gl_fill_polygon([
#   (413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
#   (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
#   (597, 215), (552, 214), (517, 144), (466, 180)
# ])

# renderer.gl_color(1, 1, 0)
# renderer.gl_fill_polygon([(682, 175), (708, 120), (735, 148), (739, 170)])

start = time.time()
filename = renderer.gl_finish()
print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
