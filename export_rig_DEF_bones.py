import bpy
import os

ob = bpy.context.active_object
bpy.ops.object.mode_set(mode='OBJECT')

with open(bpy.path.abspath("//") + "rig_DEF_bones.txt", "w") as f:
    for bone in ob.data.bones:
        if bone.name[0:4] == 'DEF-':
            f.write(bone.name + "\n")
