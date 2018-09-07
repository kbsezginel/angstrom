"""
--- Ångström ---
Render molecular images and animations.
"""
from .blender import Blender
from .openbabel import OpenBabel
from angstrom.molecule.write import write_pdb
from angstrom import Molecule, Trajectory
import subprocess
import tempfile
import pickle
import os


def render(render_obj, output='angstrom', renderer='blender', verbose=False):
    """
    Render Molecule object.

    Parameters
    ----------
    render_obj : Molecule or Trajectory
        Ångström Molecule (for image) or Trajectory (for video) object.
    output : str
        File name for the render without extension.
    renderer : str or object
        The renderer can be either a string ('blender' | 'openbabel') or a renderer object.
        Using a string would select default configuration for each renderer.
        To configure renderer settings the renderer object should be initialized separately
        and used here as an argument.
    verbose : bool
        Verbosity.

    Returns
    -------
    None
        Saves image / video file.

    Notes
    -----
    Image renderers:
        Blender: 'png' image format is recommended.
        OpenBabel: 'svg' image format is recommended.

    Video renderers:
        Blender: Background color is white by default. See Blender configuration for more options.

    """
    output = os.path.abspath(output)
    if isinstance(renderer, str):
        renderer = {'blender': Blender(), 'openbabel': OpenBabel()}[renderer]
    if isinstance(render_obj, Molecule):
        render_image(render_obj, output, renderer=renderer, verbose=verbose)
    elif isinstance(render_obj, Trajectory):
        render_video(render_obj, output, renderer=renderer, verbose=verbose)



def render_image(molecule, img_file, renderer, verbose=False):
    """
    Renders image of a Molecule object.

    Parameters
    ----------
    molecule : Molecule
        Ångström Molecule object.
    img_file : str
        File name for the image file to be saved (use .svg for OpenBabel and .png for Blender).
    renderer : object
        Renderer object (blender | openbabel).
    verbose : bool
        Verbosity.

    Returns
    -------
    None
        Saves image file.

    Notes
    -----
    Blender: 'png' image format is recommended.
    OpenBabel: 'svg' image format is recommended.

    """
    if not hasattr(molecule, 'bonds'):
        molecule.get_bonds()
    temp_pdb_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.pdb')
    write_pdb(temp_pdb_file, molecule.atoms, molecule.coordinates, bonds=molecule.bonds)
    if renderer.__class__.__name__ == 'Blender':
        print('Rendering %s image with Blender -> %s' % (molecule.name, img_file))
        renderer.config['pdb']['filepath'] = temp_pdb_file.name
        renderer.config['img_file'] = img_file
        renderer.config['verbose'] = verbose
        renderer.run()
    elif renderer.__class__.__name__ == 'OpenBabel':
        print('Rendering %s image with OpenBabel -> %s' % (molecule.name, img_file))
        renderer.verbose = verbose
        renderer.run(temp_pdb_file.name, img_file)
    else:
        print('Rendering engine not detected!')
    temp_pdb_file.close()


def render_video(trajectory, vid_file, renderer, verbose=False):
    """
    Renders video of a Trajectory object.

    Parameters
    ----------
    trajectory : Trajectory
        Ångström Trajectory object.
    vid_file : str
        File name for the video file to be saved (no extension required).
    renderer : object
        Renderer object (blender).
    verbose : bool
        Verbosity.

    Returns
    -------
    None
        Saves video file.

    Notes
    -----
    Blender: Background color is white by default. See Blender configuration for more options.

    """
    if renderer.__class__.__name__ == 'Blender':
        vid_dir = os.path.dirname(vid_file)
        print('Rendering %i images with Blender -> %s' % (len(trajectory), vid_dir))
        images = []
        for idx, mol in enumerate(trajectory):
            img_file = os.path.join(vid_dir, '%i.png' % idx)
            render_image(mol, img_file, renderer)
            images.append(img_file)
        renderer.configure(images=images, vid_file=vid_file, script='seq', verbose=verbose, background_color=(1, 1, 1))
        print('Rendering %s video with Blender -> %s' % (trajectory.name, vid_file))
        renderer.run()
        # Remove all images
        for img in images:
            if os.path.exists(img):
                os.remove(img)
        renderer.configure()
