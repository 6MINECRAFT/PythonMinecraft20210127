from mcpi.minecraft import Minecraft
DD=Minecraft.create()
x,y,z=DD.player.getTilePos()
for i in range(0,66):
        DD.setBlock(x+i,y,z+i,46)
        DD.setBlock(x+i+1,y,z+i,46)
        DD.setBlock(x+i+2,y,z+i,46)