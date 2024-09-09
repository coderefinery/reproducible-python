(conda)=

# Conda environment

A Conda environment is an isolated software environment that is used to manage dependencies for a project
and you decide where it is located.

You will need a `environment.yml` file that documents the dependencies:
```yaml
name: coderefinery
channels:
  - conda-forge
  - bioconda
dependencies:
  - python >= 3.10
  - black
  - click
  - flit
  - ipywidgets
  - isort
  - jupyterlab
  - jupyterlab_code_formatter
  - jupyterlab-git
  - matplotlib
  - myst-parser
  - nbdime
  - numpy
  - pandas
  - pytest
  - pytest-cov
  - scalene
  - seaborn
  - snakemake-minimal
  - sphinx
  - sphinx-autoapi
  - sphinx-autobuild
  - sphinx_rtd_theme >= 2.0
  - vulture
  - scikit-image
```


## Before you create a virtual environment

1. Create a new directory for this course.
1. In this directory, create an `environment.yml` file and copy-paste the dependencies above into it.


## Choose the tool to manage the environment

If you are already using one of these tools, please continue using the tool that you like and know.
If you are new to this, **we recommend using Miniconda or Miniforge**.

- [Anaconda](https://docs.anaconda.com/anaconda/install/)
  - Advantages: easy to install, easy to use, good for beginners
  - Disadvantages: large download, installs more than we will need, license restrictions
- [Miniconda](https://docs.anaconda.com/miniconda/)
  - Advantages: small size, installs only what you need
  - Disadvantages: no graphical interface, license restrictions
- [Miniforge](https://github.com/conda-forge/miniforge)
  - Advantages: small size, no license restrictions
  - Disadvantages: no graphical interface
- [Micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)
  - Advantages: fast, small size
  - Disadvantages: no graphical interface
- [Pixi](https://pixi.sh/latest/)
  - Advantages: fast and new
  - Disadvantages: new and less tested and not documented here


## Creating the virtual environment

1. Open your terminal shell (e.g. Bash or Zsh).
2. Activate `conda` using `conda activate` or `source ~/miniconda3/bin/activate`.
3. Run the following command:
   ```console
   $ conda env create --file environment.yml
   ```
4. Make sure that you see "coderefinery" in the output when you ask for a list of all available environments:
   ```console
   $ conda env list
   ```


## How to verify that this worked

(this will be added)
