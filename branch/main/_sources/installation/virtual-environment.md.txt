(venv)=

# Virtual environment

A virtual environment is an isolated software environment that is used to manage dependencies for a project
and you decide where it is located.

You will need a `requirements.txt` file that documents the dependencies:
```
black
click
flit
ipywidgets
isort
jupyterlab
jupyterlab-code-formatter
jupyterlab-git
matplotlib
myst-parser
nbdime
numpy
pandas
pytest
pytest-cov
scalene
seaborn
sphinx
sphinx-autoapi
sphinx-autobuild
sphinx_rtd_theme >= 2.0
vulture
scikit-image
```


## Before you create a virtual environment

1. Create a new directory for this course.
1. In this directory, create a `requirements.txt` file and copy-paste the dependencies above into it.


## Creating the virtual environment

Now create a virtual environment in this directory either using [pip and
venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
(more traditional and safer) or using [uv](https://docs.astral.sh/uv/) (more modern but also less tested):

:::::{tabs}

::::{group-tab} pip and venv
Create a new virtual environment and activate it:
```console
$ python3 -m venv coderefinery-environment
$ source coderefinery-environment/bin/activate
```

Install the dependencies into the environment:
```console
$ python3 -m pip install -r requirements.txt
```
::::


::::{group-tab} uv
Create a new virtual environment and activate it:
```console
$ uv venv coderefinery-environment
$ source coderefinery-environment/bin/activate
```

Install the dependencies into the environment:
```console
$ uv pip install -r requirements.txt
```
::::

:::::
