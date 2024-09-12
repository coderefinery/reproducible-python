(documentation)=

# Code documentation

- 15 min: What makes good documentation? Also https://diataxis.fr/
- 15 min: Writing good README files
- 30 min: Exercise: Set up a Sphinx documentation and add API documentation
- 15 min: Building documentation with GitHub Actions


requirements.txt:
```
sphinx
sphinx_rtd_theme >= 2.0
sphinx_autobuild
sphinx_autoapi
myst_parser
```


conf.py:
```python
extensions = [
    "myst_parser",
    "autoapi.extension",
]

autoapi_dirs = ['..']
```
