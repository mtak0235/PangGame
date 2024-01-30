from ursina import *
app = Ursina()
cube = Entity(model='cube', color=color.green, texture='white_cube', scale=2)
def update():
    cube.rotation_x += 0.5
    cube.rotation_y += 0.15
app.run()