import bpy
import os

with open(bpy.path.abspath("//") + "mesh_vertex_groups.txt", "w") as f:
    for v_group in bpy.context.active_object.vertex_groups:
        f.write(v_group.name + "\n")
