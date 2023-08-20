# Makehuman to Blender complete guide
1) Выгрузить пустой меш со скелетом из Makehuman как fbx
2) Загрузить меш в Blender
3) (один раз)Выгрузить группы вершин через скрипт \
https://github.com/NyankoNyan/blender-hints/blob/main/export_mesh_vertex_groups.py \
Все файлы выгружаются в папку с текущим файлом .blend
4) Всеми правдами и неправдами сделать модельку в Blender
5) Подготовить арматуру для рига с Rigify, чтобы существовали DEF-кости
6) (один раз)Выгрузить DEF-кости через скрипт\
https://github.com/NyankoNyan/blender-hints/blob/main/export_rig_DEF_bones.py\
7) (один раз)Создать CSV-файл мэппинга для переименования костей. Здесь скрипта нет, так что вперёд, ручками. У нас в организме всего 200 костей.\
Вот файл с примером\
https://github.com/NyankoNyan/blender-hints/blob/main/mh_game_engine_to_def.csv
8) Переименовать скриптом группы вершин по файлу меппинга\
Здесь скрипт\
https://github.com/NyankoNyan/blender-hints/blob/main/rename_vetex_groups_by_mapping_file.py \
Так как, меш из Makehuman немного странный, меш должен "упасть". Этого можно избежать, если предварительно применить модификатор арматуры.
9) Руками пофиксить мелкие косяки с группами вершин.\
В примере образуется группа вершин DEF-spine.001.tmp\
С помощью модификатора Vertex Weight Mix можно добавить её вес к группе DEF-spine.001, после чего удалить.
10) Переносим веса вершин с клёвого меша из Makehuman на наш меш. Теперь он тоже клёвый.\
Как это делается, можно посмотреть вот на этом видео:\
https://youtu.be/arXf5EV3H1c
 
