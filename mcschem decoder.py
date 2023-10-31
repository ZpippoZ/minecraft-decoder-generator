import mcschematic
import time

schem = mcschematic.MCSchematic()

bits=int(input("Input the number of bits of the decoder: "))

for i in range(2**bits):
    for e in range(bits):
        value=bin(i)[2:].zfill(6)[::-1]
        if value[e]=='0':
            #wool
            schem.setBlock((i*2+1,e*2,-1), "minecraft:gray_wool")
            schem.setBlock((i*2,e*2,-1), "minecraft:gray_wool")
            #redstone dust
            schem.setBlock((i*2+1,e*2+1,-1), "minecraft:redstone_wire")
            schem.setBlock((i*2,e*2+1,-1), "minecraft:redstone_wire")
            #repeater every 15 blocks
            #for j in range(1,8):
                #if i == 15*j:
                    #for k in range(1,8):
                        #schem.setBlock((15*k+k-1,e*2+1,-1), "minecraft:repeater[facing=west]")
            #glass
            schem.setBlock((i*2,e*2-1,0), "minecraft:gray_stained_glass")
            #repeater
            schem.setBlock((i*2,e*2,0), "minecraft:repeater")
            
        if value[e]=='1':
            #wool
            schem.setBlock((i*2+1,e*2,-1), "minecraft:gray_wool")
            schem.setBlock((i*2,e*2,-1), "minecraft:gray_wool")
            #redstone dust
            schem.setBlock((i*2+1,e*2+1,-1), "minecraft:redstone_wire")
            schem.setBlock((i*2,e*2+1,-1), "minecraft:redstone_wire")
            #repeater every 15 blocks
            #for j in range(1,8):
                #if i == 15*j:
                    #for k in range(1,8):
                        #schem.setBlock((15*k+k-1,e*2+1,-1), "minecraft:repeater[facing=west]")
            #torch
            schem.setBlock((i*2,e*2,0),"minecraft:redstone_wall_torch[facing=south]")
            
    

schem.save("C:/Users/zPippo/curseforge/minecraft/Instances/Server brutto/config/worldedit/schematics", str(bits) + "bitDecoder", mcschematic.Version.JE_1_18_2)
print("Schematic saved")
time.sleep(5)