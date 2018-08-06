from ._version import version_info, __version__

from .example import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'genome-feature-jupyter-widget',
        'require': 'genome-feature-jupyter-widget/extension'
    }]
