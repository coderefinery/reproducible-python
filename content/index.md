# Reproducible research software development using Python


## Big-picture goal

This is a **hands-on course on research software engineering**. In this
workshop we assume that most workshop participants use Python in their work or
a leading a group which uses Python.  Therefore, some of the examples will use
Python as the example language.

We will work with an example project and go through all the steps of a typical
software project.  Once we have seen the building blocks, we will try to apply
them to own projects. Workshop participants will receive and also learn to give
constructive code feedback.


## Prerequisites

:::{prereq} Preparation
1. Get a **GitHub account** following [these instructions](https://coderefinery.github.io/installation/github/).
1. You will need a **text editor**. If you don't have a favorite one, we recommend
   [VS Code](https://coderefinery.github.io/installation/vscode/).
1. **If you prefer to work in the terminal** and not in VS Code, set up these two (skip this if you use VS Code):
   - [Git in the terminal](https://coderefinery.github.io/installation/git-in-terminal/)
   - [SSH or HTTPS connection to GitHub from terminal](https://coderefinery.github.io/installation/ssh/)
1. **One of these two software environments** (if you are not sure which one to
   choose or have no preference, choose Conda):
   - {ref}`conda`
   - {ref}`venv` (Snakemake is not available in this environment)
1. **Optional** and only on Linux: [Apptainer](https://apptainer.org/) following
   [these instructions](https://apptainer.org/docs/admin/1.3/installation.html#install-from-pre-built-packages).
:::


## Schedule

:::{note}
The schedule will very soon contain links to lesson material and exercises.
:::


### Day 1 (Sep 16)

- 13:00-13:30 - **Welcome and introduction**
  - Practical information (tools, communication, breaks, etc.)
  - Motivation (reproducibility, robustness, distribution, improvement, trust, etc.)
  - What will learn and achieve from this course?
  - {ref}`example-project`

- 13:30-14:45 (1.25h) - **Introduction to version control with Git and GitHub (1/2)**
  - Creating a repository and porting your project to Git and GitHub
  - Basic commands

- 15:00-16:30 (1.5h) - **Introduction to version control with Git and GitHub (2/2)**
  - Branching and merging
  - Recovering from typical mistakes

- 16:45-18:00 - {ref}`documentation`
  - In-code documentation including docstrings
  - Writing good README files
  - Markdown
  - Sphinx
  - Building documentation with GitHub Actions
  - Jupyter Notebooks


### Day 2 (Sep 17)

- 09:00-10:30 (1.5h) - **Collaborative version control and code review (1/2)**
  - Practice code review using issues and pull requests
  - Forking workflow
  - Contributing changes to projects of others

- 10:45-12:15 (1.5h) - **Collaborative version control and code review (2/2)**
  - Organization strategies
  - Merge vs. rebase
  - Conflict resolution

- 16:45-18:00 - **Debriefing and Q&A**
  - Participants work on their projects
  - Together we study actual codes that participants wrote or work on
  - Constructively we discuss possible improvements
  - Give individual feedback on code projects


### Day 3 (Sep 18)

- 09:00-10:30 - {ref}`testing`
  - Unit tests
  - End-to-end tests
  - pytest
  - GitHub Actions

- 10:45-12:15 - {ref}`reusable`
  - Tracking dependencies with requirements.txt and environment.yml
  - Recording environments in containers

- 13:00-14:45 - {ref}`refactoring`
  - Naming (and other) conventions, project organization, modularity
  - Refactoring (explained through examples)
  - Design patterns: functional design vs. object-oriented design
  - How to design your code before writing it
  - Structuring larger software projects in a modular way
  - Command-line interfaces
  - Workflows with Snakemake

- 15:00-16:30 - {ref}`publishing`
  - Licenses
  - Publishing the code via Zenodo
  - Packaging the code
  - Sharing the code via PyPI

- 16:45-18:00 - **Debriefing and Q&A**
  - Participants work on their projects
  - Together we study actual codes that participants wrote or work on
  - Constructively we discuss possible improvements
  - Give individual feedback on code projects


### Extra material if we have time

- Profiling memory and CPU usage
- Strategies for parallelization


```{toctree}
:maxdepth: 1
:caption: Software environment
:hidden:

installation/conda
installation/virtual-environment
```

```{toctree}
:maxdepth: 1
:caption: Episodes
:hidden:

example
documentation
testing
reusable
refactoring
publishing
```

```{toctree}
:maxdepth: 1
:caption: Reference
:hidden:

All lessons <https://coderefinery.org/lessons/>
CodeRefinery <https://coderefinery.org/>
Reusing <https://coderefinery.org/lessons/reusing/>
```
