# blender --background --python run.py
import bpy

# 清除场景中现有的所有对象
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 加载 GLB 文件
bpy.ops.import_scene.gltf(filepath="mesh.glb")

# 遍历所有网格对象并进行处理
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        # 设置当前对象为活动对象并选中
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        # 进入编辑模式
        bpy.ops.object.mode_set(mode='EDIT')
        
        # 选择所有面
        bpy.ops.mesh.select_all(action='SELECT')
        
        # 如果需要手动设置缝线（seams），可以先运行下面这一行（可选）
        # bpy.ops.uv.seams_from_islands()
        
        # 使用智能 UV 投影，支持 angle_limit 参数
        bpy.ops.uv.smart_project(
            angle_limit=89.0,         # 设置接近90度的角度限制
            island_margin=0.001,        # UV 岛之间的间距
        )
        
        # 可选：对生成的 UV 岛进行平均缩放、对齐旋转以及打包处理
        bpy.ops.uv.average_islands_scale()
        bpy.ops.uv.align_rotation()
        bpy.ops.uv.pack_islands(
            margin=0.001,
            rotate=True,
            rotate_method='AXIS_ALIGNED'
        )
        
        # 返回对象模式
        bpy.ops.object.mode_set(mode='OBJECT')
        obj.select_set(False)

# 导出为新的 GLB 文件
bpy.ops.export_scene.gltf(filepath="optimized_model.glb")
