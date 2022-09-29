"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Librería de archivos .bmp
Santiago Taracena Puga (20017)
"""

# Módulos necesarios
import struct

# Funciones lambda extra utilizadas.
color = lambda r, g, b: bytes([b, g, r])
char = lambda character: struct.pack("=c", character.encode("ascii"))
word = lambda word: struct.pack("=h", word)
dword = lambda dword: struct.pack("=l", dword)

# Constantes extra utilizadas.
BLACK: bytes = color(0, 0, 0)
WHITE: bytes = color(255, 255, 255)
RED: bytes = color(255, 0, 0)
GREEN: bytes = color(0, 255, 0)
BLUE: bytes = color(0, 0, 255)
