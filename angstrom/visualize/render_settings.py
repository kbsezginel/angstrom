"""
--- Ångström ---
Render settings for molecular visualization.
"""
import os

"""
----------------------------------- OPENBABEL SETTINGS ---------------------------------------------
"""
openbabel_settings = ['-xS', '-xd', 'xb', 'none']  # OpenBabel command line arguments for rendering


"""
----------------------------------- BLENDER SETTINGS -----------------------------------------------
"""
default_model = {'use_center': True,               # Position object to origin
                 'use_camera': False,              # Add camera
                 'use_lamp': False,                # Add lamp
                 'ball': '0',                      # Type of ball -> 0: NURBS | 1: Mesh | 2: Meta
                 'mesh_azimuth': 32,               # Number of sectors (azimuth)
                 'mesh_zenith': 32,                # Number of sectors (zenith)
                 'scale_ballradius': 0.5,          # Scale factor for all atom radii
                 'scale_distances': 1,             # Scale factor for all distances
                 'atomradius': '2',                # Type of radius -> 0: Pre-defined | 1: Atomic radius | 2: van der Waals
                 'use_sticks': True,               # Use bonds as cylinders
                 'use_sticks_type': '0',           # Sticks type -> 0: Dupliverts | 1: Skin | 2: Normal
                 'sticks_subdiv_view': 2,          # Number of subdivisions (view)
                 'sticks_subdiv_render': 2,        # Number of subdivisions (render)
                 'sticks_sectors': 20,             # Number of sectors of a stick
                 'sticks_radius': 0.25,            # Radius of a stick
                 'sticks_unit_length': 0.05,       # Length of the unit of a stick in Angstrom
                 'use_sticks_color': True,         # The sticks appear in the color of the atoms
                 'use_sticks_smooth': True,        # The sticks are round (sectors are not visible)
                 'use_sticks_bonds': False,        # Show double and tripple bonds.
                 'sticks_dist': 1.1,               # Distance between sticks measured in stick diameter (min:1 / max:3)
                 'use_sticks_one_object': True,    # All sticks are one object
                 'use_sticks_one_object_nr': 200   # Number of sticks to be grouped at once
                 }

ball_and_stick = {'scale_ballradius': 0.5,
                  'scale_distances': 1,
                  'sticks_radius': 0.25}

space_filling = {'scale_ballradius': 1,            # Scale factor for all atom radii
                 'scale_distances': 1,             # Scale factor for all distances
                 'atomradius': '2',                # Type of radius -> 0: Pre-defined | 1: Atomic radius | 2: van der Waals
                 'use_sticks': False,              # Use bonds as cylinders
                 }

MODELS = {'default': default_model,
          'ball-and-stick': ball_and_stick,
          'space-filling': space_filling
          }

COLORS = {'Carbon': (0.05, 0.05, 0.05),
          'Hydrogen': (1.00, 1.00, 1.00),
          'Nitrogen': (0.18, 0.34, 0.95),
          'Oxygen': (0.70, 0.00, 0.00)}

PI = 3.14159265359
IMG_SCRIPT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'blender_image.py')


def get_blender_settings(executable='blender', render=True, save='', model='default',
                         camera_zoom=20, camera_distance=10, camera_view='xy', camera_type='ORTHO',
                         resolution=(1920, 1080), brightness=1.0, lamp=2.0, colors=COLORS,
                         verbose=False, script=IMG_SCRIPT, pickle='temp-settings.pkl'):
    """
    Get Blender image rendering settings.

    Parameters
    ----------
    executable : str
        Path to blender executable (depends on OS).
    render : bool
        Render image switch.
    save : str
        Saves .blend file to given filename.
    model : str
        Molecule model (default | ball-and-stick | space_filling).
    camera_zoom : float
        Camera zoom / focal length (default: 20).
    camera_distance : float
        Distance between the camera and the molecule (default: 10).
    camera_view : str
        Camera view plane (xy | xz | yx | yz | zx | zy).
    camera_type : str
        Camera type (ORTHO | PERSP).
    resolution : tuple
        Image resolution (default: 1920 x 1080).
    brightness : float
        Image brighness (environmental lightning).
    lamp : float
        Lamp strength (default: 2).
    colors : dict
        Atom colors in RGB | ex: {'Carbon': (0.1, 0.1, 0.1), 'Oxygen': (0.7, 0.0, 0.0)}.
    verbose : bool
        Blender subprocess verbosity.
    script : str
        Python script to render the image.
    pickle : str
        Pickle file for communicating settings with Blender.

    Returns
    -------
    dict
        Blender render settings.
    """
    d = camera_distance
    VIEW = {'xy': dict(location=[0, 0, d], rotation=[0, 0, 0]),
            'xz': dict(location=[0, -d, 0], rotation=[PI / 2, 0, 0]),
            'yx': dict(location=[0, 0, -d], rotation=[0, PI, -PI / 2]),
            'yz': dict(location=[d, 0, 0], rotation=[PI / 2, 0, PI / 2]),
            'zx': dict(location=[0, d, 0], rotation=[PI / 2, -PI / 2, PI]),
            'zy': dict(location=[-d, 0, 0], rotation=[PI / 2, -PI / 2, -PI / 2])}

    settings = {'camera': dict(location=VIEW[camera_view]['location'],
                               rotation=VIEW[camera_view]['rotation'],
                               type=camera_type, zoom=camera_zoom),
                'brightness': brightness, 'lamp': lamp, 'resolution': resolution,
                'pdb': MODELS[model], 'colors': colors, 'verbose': verbose, 'render': render,
                'executable': executable, 'script': script, 'pickle': pickle, 'save': save}
    return settings
