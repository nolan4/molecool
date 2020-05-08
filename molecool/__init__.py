"""
molecool
A python package for analyzing and visualizing pdb and xyz files. for MolSSI May webinar series.
"""

# Add imports here
from .functions import *
#from .functions import canvas
#import molecool.functions # changes external function call (molecool.functions.canvas())

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
