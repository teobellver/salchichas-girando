from ursina import *
app=Ursina()
model="paquete.stl"
cube=Entity(model=model,color=hsv(300,1,1), scale=0.3, collider=True)
def spin():
    cube.animate("rotation_x", cube.rotation_x+60, duration=5, curve=curve.in_out_expo)
    cube.animate("rotation_z", cube.rotation_z+30, duration=5, curve=curve.in_out_expo)
    cube.animate("rotation_y", cube.rotation_y+360, duration=20, curve=curve.in_out_expo)
cube.onclick = spin()
EditorCamera()
app.run()