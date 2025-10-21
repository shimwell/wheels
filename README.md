# wheels storage repository

Unofficial wheels for OpenMC and MOAB packages.

These particularly useful to have available as wheels for various workflows as a temporary measure until official wheels are distributed on PyPI.

This is particularly enabling for a few places where I need an easy install for these two packages (e.g. https://fusion-energy.github.io/neutronics-workshop/html/docs/install_pip.html).

Longer term there are efforts for these packages to distribute wheels on PyPI but in the meantime this repository might be of use, I am also supporting these efforts (either directly of via developer sponsorship). These temporary wheels also serve as a test of the future PyPI wheels.

There are lots of wheels for different versions of python and also operating systems available on this repository, please browser the folder structure.

Feedback welcome.

## Prerequisites for installing

Install Python and pip if you don't already have these installed.
```
sudo apt install python3 python3-pip
```
Optionally create and activate a new virtual environment
```
sudo apt-get --yes install python3-venv
python3 -m venv .new_env
source .new_env/bin/activate
```


## Installing with pip from this custom index (recommended)

You can install `moab` or `openmc` directly from this repository using pip's `--extra-index-url` option, which works with the [GitHub Pages index](https://shimwell.github.io/wheels):

To install `openmc`
```
python -m pip install --extra-index-url https://shimwell.github.io/wheels openmc
```

To install `moab`
```
python -m pip install --extra-index-url https://shimwell.github.io/wheels moab
```

Using the above pip install method will automatically select the correct wheel for your Python version and platform, if available (please let us know if additional builds would be desirable).

## Installing from file

If you know what version of Python you have and your opperating system then you can install a specific wheel using the direct link to the file, for example:

Moab Python 3.12 on Linux
```
python -m pip install https://shimwell.github.io/wheels/moab/moab-5.5.1-cp312-cp312-manylinux_2_28_x86_64.whl
```
OpenMC for Python 3.12 on Linux
```
python -m pip install https://shimwell.github.io/wheels/openmc/openmc-0.15.3-cp312-cp312-manylinux_2_28_x86_64.whl
```

## Reproduce the wheels

You can build the OpenMC and MOAB wheels yourself from source code if you prefere.

- OpenMC wheels can be built with [this branch and with these commands](https://github.com/shimwell/openmc/pull/70#issue-3013447666)
- MOAB wheels can be built using the ```python -m build``` command on the [develop branch](https://bitbucket.org/fathomteam/moab/branch/develop)
