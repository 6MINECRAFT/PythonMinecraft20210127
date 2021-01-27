from mcpi.minecraft import Minecraft
DD=Minecraft.create()
import random,time

while True:
    x,y,z=DD.player.getPos()
    a=random.uniform(-19,20)
    b=random.uniform(-19,20)
    y=y+15
    DD.spawnEntity(x+a,y,z+b,45)
    time.sleep(0.00000001)