# wheels storage repository

Unofficial wheels for OpenMC and MOAB packages.

These particularly useful to have available as wheels for various workflows as a temporary measure until official wheels are distributed on PyPI.

This is particularly enabling for a few places where I need an easy install for these two packages (e.g. https://fusion-energy.github.io/neutronics-workshop/html/docs/install_pip.html).

Longer term there are efforts for these packages to distribute wheels on PyPI but in the meantime this repository might be of use, I am also supporting these efforts (either directly of via developer sponsorship). These temporary wheels also serve as a test of the future PyPI wheels.

There are lots of wheels for different versions of python and also operating systems available on this repository, please browser the folder structure.

Feedback welcome.


## Installing with pip from this custom index

Optionally create a new virtual environment
```
sudo apt-get --yes install python3-venv
python3 -m venv .new_env
source .new_env/bin/activate
```

You can install `moab` or `openmc` directly from this repository using pip's `--extra-index-url` option, which works with the [GitHub Pages index](https://shimwell.github.io/wheels):

```
python -m pip install --extra-index-url https://shimwell.github.io/wheels moab
python -m pip install --extra-index-url https://shimwell.github.io/wheels openmc
```

This will automatically select the correct wheel for your Python version and platform, if available (please let us know if additional builds would be desirable).

If you know what wheel you want to install you can also use the direct link to the file, for example:

```
python -m pip install https://shimwell.github.io/wheels/moab/moab-5.5.1-cp312-cp312-manylinux_2_28_x86_64.whl
python -m pip install https://shimwell.github.io/wheels/openmc/openmc-0.15.3-cp312-cp312-manylinux_2_28_x86_64.whl
```

If you would like to reproduce OpenMC wheels from source that can be downloaded from [this branch with these commands](https://github.com/shimwell/openmc/pull/70#issue-3013447666) and MOAB wheels can be build using the ```python -m build``` command on the [develop branch](https://bitbucket.org/fathomteam/moab/branch/develop)
