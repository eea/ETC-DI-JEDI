"""
Constant settings that can be recycled among most of the scripts and notebooks
"""

import os
import geopandas as gpd
from pathlib import WindowsPath

# Some default settings

# the network drive name on which all the data is stored
# TODO adapt to work also on Unix-like systems
dir_signature = WindowsPath('//cwsfileserver/projects/lulucf/f02_data')