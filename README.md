# wheels storage repositoy

Unoffical wheels for OpenMC and MOAB packages.

These particularly useful to have available as wheels for various workflows

Longer term there are effrots for these packages to distribute wheels on PyPI but in the meantime this repository might be of use.

There are lots of wheels for different versions of python and also opperating systems available on this repository, please browser the folder structure.

For my use case I tend to install on Linux with Python 3.12 so I use these commands

```bash
python -m pip install https://github.com/shimwell/wheels/raw/refs/heads/main/moab/moab-wheels-ubuntu-latest/moab-5.5.1-cp312-cp312-manylinux_2_28_x86_64.whl
python -m pip install https://github.com/shimwell/wheels/raw/refs/heads/main/openmc/openmc-0.15.1.dev0-cp312-cp312-manylinux_2_28_x86_64.whl
```
