"""
--- Ångström ---
Squence a list of images and render a movie using Blender.
"""
import pickle
import bpy
import sys
import os
from PIL import Image


def sequence_images(settings):
    """
    Create a video of a list of images using Blender video sequencer.

    Parameters
    ----------
    settings : dict
        Blender sequencer settings.

    Returns
    -------
    None
        This function is called by the Blender Python installation.

    """
    # Create scene and sequence editor
    scene = bpy.context.scene
    scene.sequence_editor_create()

    # Add background
    background = scene.sequence_editor.sequences.new_effect(name='background', frame_start=1, frame_end=len(settings['images']) + 1, channel=1, type='COLOR')
    background.color = settings['background_color']

    # Add images
    seq = scene.sequence_editor.sequences.new_image(name='img_strip', filepath=settings['images'][0], channel=2, frame_start=1)
    seq.blend_type = 'ALPHA_OVER'
    for f in settings['images'][1:]:
        seq.elements.append(os.path.basename(f))

    # Video settings
    scene.render.fps = settings['fps']
    scene.render.image_settings.file_format = settings['file_format']
    scene.render.image_settings.quality = 100
    scene.frame_end = len(settings['images'])
    scene.render.resolution_x, scene.render.resolution_y = settings['resolution']
    scene.render.resolution_percentage = 100

    # Save .blend file
    if settings['save'] != '':
        bpy.ops.wm.save_as_mainfile(filepath=settings['save'])

    if settings['render']:
        scene.render.filepath = os.path.join(os.path.dirname(settings['images'][0]), 'angstrom')
        bpy.ops.render.render(animation=True)


if __name__ == '__main__':
    argv = sys.argv[sys.argv.index("--") + 1:]  # get all args after "--"
    with open(argv[0], 'rb') as handle:
        settings = pickle.load(handle)
    print(settings)
    sequence_images(settings)
