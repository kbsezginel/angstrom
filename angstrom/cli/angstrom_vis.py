"""
--- Ångström ---
Command line interface for molecular visualization.
"""
import os
import yaml
import argparse
from angstrom.visualize.blender import Blender


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
    > python angstrom.py my_molecule.pdb
    would generate my_molecule.png file.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Positional arguments
    parser.add_argument('molecule', type=str, help='Molecule file (pdb) to read')

    # Optional arguments
    parser.add_argument('--model', '-m', default='default', type=str, metavar='',
                        help="Molecular representation model ([default] | ball_and_stick | space_filling | stick | surface)")
    parser.add_argument('--zoom', '-z', default=20, type=int, metavar='',
                        help="Image zoom. (default: 20)")
    parser.add_argument('--view', default='xy', type=str, metavar='',
                        help="Camera view plane ([xy] | xz | yx | yz | zx | zy)")
    parser.add_argument('--distance', '-d', default=10, type=int, metavar='',
                        help="Camera distance from origin (default: 10)")
    parser.add_argument('--camera', '-c', default='ORTHO', type=str, metavar='',
                        help="Camera type ([ORTHO] | PERSP)")
    parser.add_argument('--brightness', '-b', default=1.0, type=float, metavar='',
                        help="Brightness [environment lightning] (default: 1.0)")
    parser.add_argument('--lamp', '-l', default=2.0, type=float, metavar='',
                        help="Lamp energy (default: 2.0)")
    parser.add_argument('--resolution', '-r', default='1920x1080', type=str, metavar='',
                        help="Image resolution (WIDTHxHEIGHT) (default: 1920x1080)")
    parser.add_argument('--bcolor', '-bc', default=None, type=float, metavar='', nargs='+',
                        help="Background color in RGB (ex: 1.0 1.0 1.0 for white | default: transparent)")
    parser.add_argument('--no-render', '-nr', action='store_true', default=False,
                        help="Don't render the image (default: False)")
    parser.add_argument('--save', '-s', default='', type=str, metavar='',
                        help="Save .blend file [ex: molecule.blend] (default: don't save)")
    parser.add_argument('--verbose', '-v', action='store_true', default=False,
                        help="Verbosity  (default: False)")

    args = parser.parse_args()
    # Set options --------------------------------------------------------------------------------------
    blend = Blender()
    blend.configure(mol_file=args.molecule, img_file='%s.png' % os.path.splitext(args.molecule)[0],
                    model=args.model, save=args.save, render=(not args.no_render), verbose=args.verbose,
                    camera_zoom=args.zoom, camera_type=args.camera.upper(), camera_view=args.view,
                    camera_distance=args.distance, background_color=args.bcolor,
                    brightness=args.brightness, lamp=args.lamp, resolution=[int(i) for i in args.resolution.split('x')])
    blend.render_image()


if __name__ == '__main__':
    main()
