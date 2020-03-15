"""
--- Ångström ---
Command line interface for molecular visualization.
This is a temporary CLI for video usage. It will be merged with the
image visualizer CLI in the future.

Funtionalities:
    - render images from xyz | pdb file
    - render xyz trajectory videos
    - create rotation animation from xyz molecule file
"""
import os
import argparse

import numpy as np

from angstrom.visualize import render
from angstrom import Molecule, Trajectory
from angstrom.visualize.blender import Blender
from angstrom.cli.tools import rotation, search_blender_executable


def main():
    parser = argparse.ArgumentParser(
        description="""
    =================================================
         __    __  ---- Ångström ----  __    __
      __/  \__/  \__      ╔═╗       __/  \__/  \__
     /  \__/  \__/  \     ╚═╝      /  \__/  \__/  \\
     \__/  \__/  \__/   ███████╗   \__/  \__/  \__/
     /  \__/  \__/  \  ██╔════██╗  /  \__/  \__/  \\
     \__/  \__/  \__/  ██║    ██║  \__/  \__/  \__/
     /  \__/  \__/  \  ██║██████║  /  \__/  \__/  \\
     \__/  \__/  \__/  ██║    ██║  \__/  \__/  \__/
        \__/  \__/     ██╝    ██╝     \__/  \__/
    =================================================
    Command-line molecular visualization.............
    =================================================
        """,
        epilog="""
    Example:
    > angstrom my_molecule.pdb
    would generate my_molecule.png file.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Positional arguments
    parser.add_argument('molecule', type=str, help='Molecule file (pdb / xyz) to read')

    # Optional arguments
    parser.add_argument('--read-config', '-conf', default='', type=str, metavar='',
                        help="Read config yaml file.")
    parser.add_argument('--exe', '-x', default='', type=str, metavar='',
                        help="Blender executable path")
    parser.add_argument('--video', '-vid', action='store_true', default=False,
                        help="Render video.")
    parser.add_argument('--rotate', '-rot', default=[0], type=int, metavar='', nargs=5,
                        help="Rotate molecule -> degrees x y z (axis) frames. (ex: 360 0 0 1 50)")
    parser.add_argument('--no-center', action='store_true', default=False,
                        help="Center molecule to origin.")
    parser.add_argument('--model', '-m', default='default', type=str, metavar='',
                        help="Molecular representation model ([default] | ball_and_stick | space_filling | stick | surface)")
    parser.add_argument('--zoom', '-z', default=20, type=int, metavar='',
                        help="Image zoom, molecule gets smaller as zoom gets bigger (default: 20)")
    parser.add_argument('--view', default='xy', type=str, metavar='',
                        help="Camera view plane ([xy] | xz | yx | yz | zx | zy)")
    parser.add_argument('--distance', '-d', default=10, type=int, metavar='',
                        help="Camera distance from origin (default: 10)")
    parser.add_argument('--camera', '-c', default='ORTHO', type=str, metavar='',
                        help="Camera type ([ORTHO] | PERSP)")
    parser.add_argument('--light', '-l', default=2000.0, type=float, metavar='',
                        help="Light energy (default: 2000 W)")
    parser.add_argument('--resolution', '-r', default='1920x1080', type=str, metavar='',
                        help="Image resolution (WIDTHxHEIGHT) (default: 1920x1080)")
    parser.add_argument('--bcolor', '-bc', default=None, type=float, metavar='', nargs='+',
                        help="Background color in RGBA (ex: 1.0 1.0 1.0 1.0 for white | default: transparent)")
    parser.add_argument('--no-render', '-nr', action='store_true', default=False,
                        help="Don't render the image (default: False)")
    parser.add_argument('--save', '-s', default='', type=str, metavar='',
                        help="Save .blend file [ex: molecule.blend] (default: don't save)")
    parser.add_argument('--verbose', '-v', action='store_true', default=False,
                        help="Verbosity  (default: False)")

    args = parser.parse_args()
    # Set options --------------------------------------------------------------------------------------
    # Search for Blender executable if not given
    if args.exe == '':
        args.exe = search_blender_executable()

    blend = Blender()
    if args.read_config != '':
        print('Reading config file -> %s' % args.read_config)
        blend.read_config(args.read_config)
        blend.config['pdb']['filepath'] = args.molecule
        blend.config['img_file'] = '%s.png' % os.path.splitext(args.molecule)[0]
    else:
        img_file = os.path.join(os.getcwd(), '%s.png' % os.path.splitext(os.path.basename(args.molecule))[0])
        blend.configure(mol_file=args.molecule, img_file=img_file, executable=args.exe,
                        model=args.model, save=args.save, render=(not args.no_render), verbose=args.verbose,
                        camera_zoom=args.zoom, camera_type=args.camera.upper(), camera_view=args.view,
                        camera_distance=args.distance, background_color=args.bcolor,
                        light=args.light, resolution=[int(i) for i in args.resolution.split('x')])
    blend.config['pdb']['use_center'] = (not args.no_center)
    blend.print_config()
    if args.video:
        blend.config['pdb']['use_center'] = False
        if len(args.rotate) == 5:
            mol = Molecule(read=args.molecule)
            rot_axis = ([0, 0, 0], args.rotate[1:4])
            traj = rotation(mol, args.rotate[4], args.rotate[0], rot_axis, interpolation='linear')
        else:
            traj = Trajectory(read=args.molecule)
        render(traj, os.path.splitext(args.molecule)[0], renderer=blend, verbose=args.verbose)
    else:
        if os.path.splitext(args.molecule)[1] == '.pdb':
            blend.run()
        elif os.path.splitext(args.molecule)[1] == '.xyz':
            mol = Molecule(read=args.molecule)
            render(mol, os.path.splitext(args.molecule)[0], renderer=blend, verbose=args.verbose)
        else:
            print('File format not supported for -> %s' % args.molecule)


if __name__ == '__main__':
    main()
