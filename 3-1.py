from mcpi.minecraft import Minecraft
DD=Minecraft.create()

while True:
    hits=DD.events.pollBlockHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        bl=DD.getBlock(x,y,z)
        DD.postToChat("你打到"+str(bl))
        