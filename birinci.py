from lib2to3.pgen2 import pgen
import pygame as pg
import sys

pg.init()

en , boy = 800 , 600

siyah = 0 , 0 , 0 , # RGB 0- 25
beyaz = 255 ,255, 255
kırmızı = 255 ,0, 0
gri = 190 ,190,190
cyan = 0 ,255, 255
pink = 255 ,105, 180
purple = 160 ,32, 240

ekran = pg.display.set_mode( (en,boy) )
x , y = 20 , 20
x_speed = y_speed = 1
y_cap = 20

while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)
    pg.draw.circle(ekran,purple,( x , y ),y_cap)

    x += x_speed
    y += y_speed
    if x >= en - y_cap : 
        x_speed *= -1
    if x <= 0 +y_cap : 
        x_speed *= -1

    if y >= boy - y_cap:
        y_speed *= -1
    if y <=0 + y_cap :
        y_speed *= -1







    pg.display.flip()