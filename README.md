# wheels storage repositoy

Unoffical wheels for OpenMC and MOAB packages.

These particularly useful to have available as wheels for various workflows

Longer term there are efforts for these packages to distribute wheels on PyPI but in the meantime this repository might be of use.

There are lots of wheels for different versions of python and also opperating systems available on this repository, please browser the folder structure.

Linux with Python 3.12 commands
```bash
python -m pip install https://github.com/shimwell/wheels/raw/refs/heads/main/moab/moab-wheels-ubuntu-latest/moab-5.5.1-cp312-cp312-manylinux_2_28_x86_64.whl
python -m pip install https://github.com/shimwell/wheels/raw/refs/heads/main/openmc/openmc-0.15.3-cp312-cp312-manylinux_2_28_x86_64.whl
```

Linux with Python 3.11 commands
```bash
python -m pip install https://github.com/shimwell/wheels/raw/refs/heads/main/moab/moab-wheels-ubuntu-latest/moab-5.5.1-cp311-cp311-manylinux_2_28_x86_64.whl
python -m pip install https://github.com/shimwell/wheels/raw/refs/heads/main/openmc/openmc-0.15.3-cp311-cp311-manylinux_2_28_x86_64.whl
```

If you would like to reproduce these from source that can be donw from [this branch with these commands](https://github.com/shimwell/openmc/pull/70#issue-3013447666)

Feedback  welcome.
