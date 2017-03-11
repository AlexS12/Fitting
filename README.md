# Fitting
Here I'll include my code for the fitting routine that I need for the project

# How to use this package

* Install Python 3 (use Anaconda or Miniconda).
* Create an environment to install this package and its dependencies.
    ```
    $ conda create -n fitting python=3 ipython ipython-notebook scipy numpy matplotlib numba pytest
    $ source activate fitting  # Linux/OS
    $ activate fitting  # Windows
    $ pip install -e .
    ```

# How to run the tests

```
$ pip install pytest-benchmark
$ py.test
```