# wheels storage repository

Unofficial wheels for OpenMC, MOAB, NJOY2016 and FEniCSx (DOLFINx, Basix, FFCx, UFL, with PETSc) packages.

These are particularly useful to have available as wheels for various workflows as a temporary measure until official wheels are distributed on PyPI.

This is particularly enabling for a few places where I need an easy install for these packages (e.g. https://fusion-energy.github.io/neutronics-workshop/html/docs/install_pip.html).

Longer term there are efforts for these packages to distribute wheels on PyPI but in the meantime this repository might be of use, I am also supporting these efforts (either directly of via developer sponsorship). These temporary wheels also serve as a test of the future PyPI wheels.

There are two benefits of using this wheel over the Conda distribution of OpenMC
- The wheel contains OpenMC compiled with Embree enabled DAGMC while the Conda package does not have the Embree acceleration. The inclusion of Embree can in the some cases accelerate the DAGMC CAD based simulations by up to 8 times faster.
- The wheel contains a recent version of the develop branch that contains improvements and bug fixes compared to the last stable release available on Conda

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

You can install `moab`, `openmc` or `njoy2016` directly from this repository using pip's `--extra-index-url` option, which works with the [GitHub Pages index](https://shimwell.github.io/wheels):

To install `openmc`
```
python -m pip install --extra-index-url https://shimwell.github.io/wheels openmc
```

To install `moab`
```
python -m pip install --extra-index-url https://shimwell.github.io/wheels moab
```

To install `njoy2016`
```
python -m pip install --extra-index-url https://shimwell.github.io/wheels njoy2016
```

This makes the `njoy` executable available on your PATH, reading its input deck from stdin exactly as a source build does
```
njoy < my_input_deck
```
The bundled executable can also be located from Python, which is useful for pointing OpenMC's `openmc.data.njoy` helpers at it
```python
import njoy
njoy.executable()   # path to the bundled njoy binary
```

Using the above pip install method will automatically select the correct wheel for your Python version and platform, if available (please let us know if additional builds would be desirable).

## Installing FEniCSx with PETSc

DOLFINx needs PETSc, which has historically been the hard part of a pip install. These wheels let the whole stack install without compiling anything

```
python -m pip install --pre --extra-index-url https://shimwell.github.io/wheels mpich fenics-dolfinx[petsc4py] petsc
```

`--pre` is required. These are development versions, and without it pip skips them and falls back to building PETSc from the source distribution on PyPI.

`mpich` comes from PyPI and supplies the MPI runtime. The PETSc wheels here are built against it, so it needs to be the MPI in use.

Linux x86_64 and aarch64, Python 3.12, 3.13 and 3.14. Verified by installing into a clean `python:3.13` container and running the DOLFINx test suite under `mpiexec -n 2`, 2381 passed. macOS is not published yet.

Some things worth knowing about these PETSc builds
- They are built Fortran free with SuperLU_DIST rather than MUMPS as the parallel direct solver, because the MPI wheels on PyPI ship no Fortran bindings.
- They are built from PETSc `main` rather than a release, to pick up [petsc!9573](https://gitlab.com/petsc/petsc/-/merge_requests/9573), without which a prebuilt petsc4py wheel records the `PETSC_DIR` of the machine that built it and DOLFINx cannot find `libpetsc`. That fix is in the 3.26 milestone, so these will be rebuilt against the release once it lands.
- Intel MPI will not work with them. PETSc built against MPICH references `MPIX_Irecv_enqueue`, and Intel MPI is MPICH ABI compatible but does not implement the enqueue extensions.

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
NJOY2016 on Linux. Note that the NJOY2016 wheels are tagged `py3-none-<platform>` rather than per Python version, because the wheel ships a Fortran executable and no Python extension module, so one wheel per platform works on every supported Python
```
python -m pip install https://shimwell.github.io/wheels/njoy2016/njoy2016-2016.79.post8-py3-none-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl
```

## Reproduce the wheels

You can build the OpenMC, MOAB and NJOY2016 wheels yourself from source code if you prefere.

- OpenMC wheels can be built with [this branch and with these commands](https://github.com/shimwell/openmc/pull/70#issue-3013447666)
- MOAB wheels can be built using the ```python -m build``` command on the [develop branch](https://bitbucket.org/fathomteam/moab/branch/develop)
- NJOY2016 wheels can be built with ```python -m build``` on the [feature/python-wheel branch](https://github.com/shimwell/NJOY2016/tree/feature/python-wheel), or for all platforms by the [Build wheels workflow](https://github.com/shimwell/NJOY2016/actions/workflows/wheels.yml) on that branch. [This issue](https://github.com/shimwell/NJOY2016/issues/1) documents what the packaging changes are and why

## A note on the NJOY2016 package name

NJOY2016 is distributed here as `njoy2016` rather than `njoy` because the [`njoy` name on PyPI](https://pypi.org/project/njoy/) is already taken by an unrelated unofficial upload, which ships a Linux binary under a `py3-none-any` tag and exposes a different command line interface (it takes the input deck as a positional argument rather than reading stdin). Since `--extra-index-url` pools candidates across PyPI and this index and picks the highest version, sharing the name would make resolution depend on staying ahead of that upload. Using a distinct name keeps it deterministic.

NJOY2016's licence permits binary redistribution provided the copyright notice and disclaimer accompany the distribution; the `LICENSE` file is included inside each wheel. These wheels are an unofficial build and are not endorsed by LANL.
