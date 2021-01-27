from mcpi.minecraft import Minecraft
DD=Minecraft.create()

while True:
    hits=DD.events.pollProjectileHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        DD.createExplosion(x,y,z,power=200)