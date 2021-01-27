from mcpi.minecraft import Minecraft
DD=Minecraft.create()
x,y,z=DD.player.getTilePos()
for i in range(0,66):
    DD.setBlock(x,y-1,z+i,57)