from mcpi.minecraft import Minecraft
DD=Minecraft.create()
import random,time


while True:
    x,y,z=DD.player.getTilePos()
    color=random.randrange(0,9)
    DD.setBlock(x,y,z-1,38,color)