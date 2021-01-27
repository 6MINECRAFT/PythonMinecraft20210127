from mcpi.minecraft import Minecraft
DD=Minecraft.create()

x,y,z=DD.player.getPos()

number=1

for i in range(8):
    for i in range(number):
        DD.spawnEntity(x,y,z,60)
    number=number*2
    DD.postToChat("已召喚:"+stre(number)+"隻")  