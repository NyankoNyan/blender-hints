import bpy
import os

ob = bpy.context.active_object
rename = {}

with open(bpy.path.abspath("//") + "mh_game_engine_to_def.csv", "r") as f:
    for line in f.readlines():
        vg_from, vg_to = line.split("\t")
        rename[vg_from] = vg_to

for v_group in bpy.context.active_object.vertex_groups:
    v_group.name = rename[v_group.name]
