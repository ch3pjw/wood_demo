Wood Programming Club Python Demo
=================================

This is an example pipe flow calculation repository built as a demonstration to
Wood's programming club.

Richard Bell's original inspiration source code can be found
[on GitHub](https://github.com/richard-edgar/pipe-flow-calculations).

We covered a number of concepts:
  * Python code running as a script. Issues being:
    * Inter-related functionality from different files is hard
    * Distribution is hard
    * Re-use is hard
    * Dependency management is hard
    * Versioning is hard
  * We added an `__init__.py` file to show how we could turn a folder of scripts
    into a Python pacakge.
  * We added a `setup.py` file to show how to create an installable Python
    package that will eventually:
    * Have author and other metadata
    * Express its dependencies on other Python code
    * Describe what new packages it provides
    * Describe dependencies for additional functionality like tests or deployment
    * Describe command-line entry points into the python code.
  * We had a brief look at `pip`, Python's standard tool for installing packages
    defined with `setuptools`/`setup.py.
  * We looked at how installing Python packages in a virtual environment with
    `virtualenv` (and I used `virtualenvwrapper`) on top.
    * This avoids conflicting global dependencies
    * Means we can check we have just what we need for each individual project
    * Can use multiple verions of Python together on the same machine with ease.
  * I installed `ipython` to show you a slightly nicer tool for playing with
    Python at the commandline.
  * We version-controlled the demo code so that we could look at what changed at
    every step and revert our source tree to previous versions should we need
    to.
  * I highlighted some features of my prompt that I use to make my life easier:
    * Full current working directory
    * Current Python virtual environment
    * Current git status
    * Exit status of last command (success/failure)
  * You can get my prompt for
    * [`bash`](https://github.com/ch3pjw/bash_prompt)
    * [`zsh`](https://github.com/ch3pjw/zsh_prompt)
    * (Use `zsh` if you can, it's great!)
  * I wrote some simple functions in
    [`wood_demo/equations.py`](https://github.com/ch3pjw/wood_demo/blob/master/wood_demo/equations.py)
    to encapsulate the maths we needed to do in our program. This made them easy
    to use later on as we tried to combine the functions into a bigger system.
  * I wrote an object-oriented
    [domain model](https://github.com/ch3pjw/wood_demo/blob/master/wood_demo/model.py)
    just to touch on classes, methods, attributes and properties very briefly.
  * Very very quickly, I wrapped the whole thing up as a CLI tool using the
    `click` library (others are available), and exposed it as an entrypoint to
    the Python code via `setup.py`.

Installation
------------

 1. Clone this git repository from github.
 2. I recommend setting up your own Python 3 `virtualenv` with
    `virtualenvwrapper` to play around installing things in.
 3. In the top level of the source code repository (where `setup.py` is) run:
    ```bash
    pip install -e .
    ```
    to install the package as a linked install (`-e`), which means that as you
    change your source code it will be reflected in the installed code straight
    away. (This is not recommended for production.)
 4. You should have the `flow` entry point now available in your virtual env,
    and you should be able to run:
    ```bash
    flow 1000 25 400 100 1 360
    ```
    and get
    ```
    Pipe pressure loss = 0.0 kPa
    Velocity = 0.80 m s⁻¹
    Reynolds number = 1.27e+04
    Friction factor = 0.01212
    ```
    out.
 5. Use
    ```bash
    flow --help
    ```
    to get auto-generate help information.
