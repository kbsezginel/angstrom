"""
--- Ångström ---
Squence a list of images and render a movie using Blender.
"""
import pickle
import bpy
import sys


def sequence_images(settings):
    pass


if __name__ == '__main__':
    argv = sys.argv[sys.argv.index("--") + 1:]  # get all args after "--"
    with open(argv[0], 'rb') as handle:
        settings = pickle.load(handle)
    print(settings)
    sequence_images(settings)
