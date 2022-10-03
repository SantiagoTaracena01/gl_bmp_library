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

first_polygon = [
  (195, 380), (215, 360), (210, 330), (237, 345), (263, 330), 
  (260, 360), (280, 380), (250, 385), (235, 410), (223, 383)
]

second_polygon = [(321, 335), (288, 286), (339, 251), (374, 302)]

third_polygon = [(377, 249), (411, 197), (436, 249)]

fourth_polygon = [
  (413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
  (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
  (597, 215), (552, 214), (517, 144), (466, 180)
]

fifth_polygon = [(682, 175), (708, 120), (735, 148), (739, 170)]

renderer.gl_color(1, 0.85, 0)
renderer.gl_fill_polygon([tuple(reversed(point)) for point in first_polygon])

renderer.gl_color(0, 1, 0)
renderer.gl_fill_polygon([tuple(reversed(point)) for point in second_polygon])

renderer.gl_color(0, 0, 1)
renderer.gl_fill_polygon([tuple(reversed(point)) for point in third_polygon])

renderer.gl_color(0.5, 0.5, 0.5)
renderer.gl_fill_polygon([tuple(reversed(point)) for point in fourth_polygon])

renderer.gl_color(1, 0, 0)
renderer.gl_fill_polygon([tuple(reversed(point)) for point in fifth_polygon])

filename = renderer.gl_finish("./images/polygons.bmp")
print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {filename}!\n")
