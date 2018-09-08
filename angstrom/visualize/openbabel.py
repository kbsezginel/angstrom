"""
--- Ångström ---
OpenBabel visualization adapter and configuration.
"""
import subprocess


class OpenBabel:
    """
    OpenBabel visualization adapter and configuration.
    """
    def __init__(self):
        """
        Initialize OpenBabel visualization adapter with default configuration.
        """
        self.executable = 'obabel'
        self.config = ['-xS', '-xd', 'xb', 'none']
        self.verbose = False

    def run(self, mol_file, img_file):
        """
        Render image file using OpenBabel.

        Parameters
        ----------
        mol_file : str
            Molecule file name to read.
        img_file : str
            Image file name to save ('svg' file format is recommended).

        Returns
        -------
        None
            Renders image file.

        """
        command = [self.executable, mol_file, '-O', img_file] + self.config
        obabel = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = obabel.stdout.decode(), obabel.stderr.decode()
        if self.verbose:
            print("Stdout:\n\n%s\nStderr:\n%s" % (stdout, stderr))
