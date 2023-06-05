import bpy

def hide_collection(collection_name, hide=True):
    collection = bpy.data.collections.get(collection_name)
    if collection:
        collection.hide_render = hide
        collection.hide_viewport = hide
