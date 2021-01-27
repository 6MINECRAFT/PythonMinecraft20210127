from mcpi.minecraft import Minecraft
DD=Minecraft.create()

while True:
    x,y,z=DD.player.getPos()
    hits=DD.events.pollProjectileHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        DD.player.setTilePos(x,y,z)
        DD.spawnEntity(x,y,z,99)