genome-feature-jupyter-widget
===============================

Genome Feature Jupyter Widget

Installation
------------

To install use pip:

    $ pip install genome-feature-jupyter-widget
    $ jupyter nbextension enable --py --sys-prefix genome-feature-jupyter-widget


For a development installation (requires npm),

    $ git clone https://github.com/bbop/genome-feature-jupyter-widget.git
    $ cd genome-feature-jupyter-widget
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix genome-feature-jupyter-widget
    $ jupyter nbextension enable --py --sys-prefix genome-feature-jupyter-widget


To run it:

    > from example import *
    > HelloWorld()
    > `Hello World`

