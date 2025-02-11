# blender --background --python run.py
# 优化模型的UV映射
import bpy

# 清除场景中现有的所有对象
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 加载GLB文件
bpy.ops.import_scene.gltf(filepath="mesh.glb")

# 选择所有网格对象并进行处理
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        # 设置当前对象为活动对象
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        # 进入编辑模式
        bpy.ops.object.mode_set(mode='EDIT')
        # 启动UV展开操作
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
        # 返回对象模式
        bpy.ops.object.mode_set(mode='OBJECT')
        
        obj.select_set(False)

# 导出为新的GLB文件
bpy.ops.export_scene.gltf(filepath="optimized_model.glb")
