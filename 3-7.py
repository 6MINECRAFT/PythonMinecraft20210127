def plantTree(x,y,z):
    DD.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    DD.setBlocks(x,y,z,x,y+4,z,17)

from mcpi.minecraft import Minecraft
DD=Minecraft.create()
x,y,z=DD.player.getTilePos()
for i in range(10):
    plantTree(x+i*5,y,z)
