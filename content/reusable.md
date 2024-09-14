(reusable)=

# How to make the project more reusable

:::{objectives}
There are not many codes that have no dependencies.
How should we **deal with dependencies**?
:::


## How to avoid: "It works on my machine &#129335;"

Use a **standard way** to list dependencies in your project:
- Python: `requirements.txt` or `environment.yml`
- R: `DESCRIPTION` or `renv.lock`
- Rust: `Cargo.lock`
- Julia: `Project.toml`
- C/C++/Fortran: `CMakeLists.txt` or `Makefile` or `spack.yaml` or the module
  system on clusters or containers
- Other languages: ...


## Tools and what problems they try to solve

**Conda, Anaconda, mamba, pip, virtualenv, Pipenv, pyenv, Poetry, requirements.txt,
environment.yml, renv**, ..., these tools try to solve the following problems:

- **Defining a specific set of dependencies**, possibly with well defined versions
- **Installing those dependencies** mostly automatically
- **Recording the versions** for all dependencies
- **Isolate environments**
  - On your computer for projects so they can use different software
  - Isolate environments on computers with many users (and allow self-installations)
- Using **different Python/R versions** per project
- Provide tools and services to **share packages**

Essential XKCD comics:
- [xkcd - dependency](https://xkcd.com/2347/)
- [xkcd - superfund](https://xkcd.com/1987/)


## Best practices

Install dependencies into **isolated environments**:
- For each project, create a new environment.
- Don't install dependencies globally for all projects.
- Install them **from a file** which documents them at the same time.

:::{keypoints}
If somebody asks you what dependencies you have in your project, you should be
able to answer this question **with a file**.

In Python, the two most common ways to do this are:
- **requirements.txt** (for `pip` and virtual environments)
- **environment.yml** (for conda and similar)

You can export the dependencies from your current environment into these files:
```bash
# inside a conda environment
$ conda env export --from-history > environment.yml

# inside a virtual environment
$ pip freeze > requirements.txt
```
:::

:::{discussion}
- The dependencies in our [example
  project](https://github.com/workshop-material/planets) are listed in a
  [environment.yml](https://github.com/workshop-material/planets/blob/main/environment.yml)
  file.
- Shouldn't the dependencies be pinned to specific versions?
- When is a good time to pin them?
:::


## Exercise

::::::{challenge} Exercise: Time-capsule of dependencies

Situation: 5 students (A, B, C, D, E) wrote a code that depends on a couple of libraries.
They uploaded their projects to GitHub. We now travel 3 years into the future
and find their GitHub repositories and try to re-run their code before adapting
it.

- Which version do you expect to be easiest to re-run? Why?
- What problems do you anticipate in each solution?

  :::::{tabs}
    ::::{group-tab} Conda
      **A**:
      You find a couple of library imports across the code but that's it.

      **B**:
      The README file lists which libraries were used but does not mention
      any versions.

      **C**:
      You find a `environment.yml` file with:
      ```
      name: student-project
      channels:
        - conda-forge
      dependencies:
        - scipy
        - numpy
        - sympy
        - click
        - python
        - pip
        - pip:
          - git+https://github.com/someuser/someproject.git@master
          - git+https://github.com/anotheruser/anotherproject.git@master
      ```

      **D**:
      You find a `environment.yml` file with:
      ```
      name: student-project
      channels:
        - conda-forge
      dependencies:
        - scipy=1.3.1
        - numpy=1.16.4
        - sympy=1.4
        - click=7.0
        - python=3.8
        - pip
        - pip:
          - git+https://github.com/someuser/someproject.git@d7b2c7e
          - git+https://github.com/anotheruser/anotherproject.git@sometag
      ```

      **E**:
      You find a `environment.yml` file with:
      ```
      name: student-project
      channels:
        - conda-forge
      dependencies:
        - scipy=1.3.1
        - numpy=1.16.4
        - sympy=1.4
        - click=7.0
        - python=3.8
        - someproject=1.2.3
        - anotherproject=2.3.4
      ```
    ::::

    ::::{group-tab} Python virtualenv
      **A**:
      You find a couple of library imports across the code but that's it.

      **B**:
      The README file lists which libraries were used but does not mention
      any versions.

      **C**:
      You find a `requirements.txt` file with:
      ```
      scipy
      numpy
      sympy
      click
      python
      git+https://github.com/someuser/someproject.git@master
      git+https://github.com/anotheruser/anotherproject.git@master
      ```

      **D**:
      You find a `requirements.txt` file with:
      ```
      scipy==1.3.1
      numpy==1.16.4
      sympy==1.4
      click==7.0
      python==3.8
      git+https://github.com/someuser/someproject.git@d7b2c7e
      git+https://github.com/anotheruser/anotherproject.git@sometag
      ```

      **E**:
      You find a `requirements.txt` file with:
      ```
      scipy==1.3.1
      numpy==1.16.4
      sympy==1.4
      click==7.0
      python==3.8
      someproject==1.2.3
      anotherproject==2.3.4
      ```
    ::::
  :::::

  :::::{solution}
  **A**: It will be tedious to collect the dependencies one by one. And after
  the tedious process you will still not know which versions they have used.

  **B**: If there is no standard file to look for and look at and it might
  become very difficult for to create the software environment required to
  run the software. But at least we know the list of libraries. But we don't
  know the versions.

  **C**: Having a standard file listing dependencies is definitely better
  than nothing. However, if the versions are not specified, you or someone
  else might run into problems with dependencies, deprecated features,
  changes in package APIs, etc.

  **D** and **E**: In both these cases exact versions of all dependencies are
  specified and one can recreate the software environment required for the
  project. One problem with the dependencies that come from GitHub is that
  they might have disappeared (what if their authors deleted these
  repositories?).

  **E** is slightly preferable because version numbers are easier to understand than Git
  commit hashes or Git tags.
  :::::
::::::


## Containers

- A container is like an **operating system inside a file**.
- "Building a container": Container definition file (recipe) -> Container image
- Let us explore and discuss the [container definition
  file](https://github.com/workshop-material/planets/blob/main/container.def)
  in our example project.
- This can be used with [Apptainer](https://apptainer.org/)/
  [SingularityCE](https://sylabs.io/singularity/).

Containers offer the following advantages:
- **Reproducibility**: The same software environment can be recreated on
  different computers. They force you to know and **document all your dependencies**.
- **Portability**: The same software environment can be run on different computers.
- **Isolation**: The software environment is isolated from the host system.
- "**Time travel**":
  - You can run old/unmaintained software on new systems.
  - Code that needs new dependencies which are not available on old systems can
    still be run on old systems.


## Demonstration: Building a container

::::::{exercise} Demo: Build a container and run it on a cluster

Here we will try to build a container from
[the definition file](https://github.com/workshop-material/planets/blob/main/container.def)
of our example project.

Requirements:
1. Linux (it is possible to build them on a macOS or Windows computer but it is
   more complicated).
2. An installation of [Apptainer](https://apptainer.org/) (e.g. following the
   [quick installation](https://apptainer.org/docs/user/latest/quick_start.html#quick-installation)).
   Alternatively, [SingularityCE](https://sylabs.io/singularity/) should also
   work.

Now you can build the container image from the container definition file.
Depending on the configuration you might need to run the command with `sudo`
or with `--fakeroot`.

Hopefully one of these four will work:
```console
$ sudo apptainer build container.sif container.def
$ apptainer build --fakeroot container.sif container.def

$ sudo singularity build container.sif container.def
$ singularity build --fakeroot container.sif container.def
```

Once you have the `container.sif`, copy it to a cluster and try to run it
there.

Here are two job script examples:

:::::{tabs}
   ::::{group-tab} Dardel (Sweden)
     ```bash
     #!/usr/bin/env bash

     # the SBATCH directives and the module load below are only relevant for the
     # Dardel cluster and the PDC Summer School; adapt them for your cluster

     #SBATCH --account=edu24.summer
     #SBATCH --job-name='container'
     #SBATCH --time=0-00:05:00

     #SBATCH --partition=shared

     #SBATCH --nodes=1
     #SBATCH --tasks-per-node=1
     #SBATCH --cpus-per-task=16


     module load PDC singularity


     # catch common shell script errors
     set -euf -o pipefail


     echo
     echo "what is the operating system on the host?"
     cat /etc/os-release


     echo
     echo "what is the operating system in the container?"
     singularity exec container.sif cat /etc/os-release


     # 1000 planets, 20 steps
     time ./container.sif 1000 20 ${SLURM_CPUS_PER_TASK} results
     ```
   ::::

   ::::{group-tab} Saga (Norway)
     ```bash
     #!/usr/bin/env bash

     #SBATCH --account=nn9997k
     #SBATCH --job-name='container'
     #SBATCH --time=0-00:05:00

     #SBATCH --mem-per-cpu=1G

     #SBATCH --nodes=1
     #SBATCH --tasks-per-node=1
     #SBATCH --cpus-per-task=16


     # catch common shell script errors
     set -euf -o pipefail


     echo
     echo "what is the operating system on the host?"
     cat /etc/os-release


     echo
     echo "what is the operating system in the container?"
     singularity exec container.sif cat /etc/os-release


     # 1000 planets, 20 steps
     time ./container.sif 1000 20 ${SLURM_CPUS_PER_TASK} results
     ```
   ::::
::::::


## Where to explore more

- [Reproducible research](https://coderefinery.github.io/reproducible-research/)
- [The Turing Way: Guide for Reproducible Research](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html)
- [Ten simple rules for writing Dockerfiles for reproducible data science](https://doi.org/10.1371/journal.pcbi.1008316)
- [Computing environment reproducibility](https://doi.org/10.5281/zenodo.8089471)
- [Carpentries incubator lesson on Docker](https://carpentries-incubator.github.io/docker-introduction/)
- [Carpentries incubator lesson on Singularity/Apptainer](https://carpentries-incubator.github.io/singularity-introduction/)
