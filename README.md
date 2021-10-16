<a href="https://sktime.org"><img src="https://github.com/alan-turing-institute/sktime/blob/main/docs/source/images/sktime-logo-no-text.jpg?raw=true)" width="175" align="right" /></a>

Welcome to the sktime tutorial at PyData Global 2021
====================================================

:tv: **Watch the tutorial live at [PyData Global 2021](https://pydata.org/global2021/schedule/presentation/22/sktime-a-unified-toolbox-for-machine-learning-with-time-series/)!**

This tutorial is about [sktime] - a unified framework for machine learning with time series. sktime features various time series algorithms and modular tools for pipelining, ensembling and tuning. You will learn how to use, combine and evaluate different algorithms on real-world data sets and integrate functionality from many existing libraries, including scikit-learn.

[sktime]: https://sktime.org

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sktime/sktime-pydata-global-2021-tutorial/main?filepath=notebooks)


## :bulb: Description

Time series are ubiquitous in real-world applications, but often add considerable complications to data science workflows. Many machine learning libraries (e.g. scikit-learn) focus on non-temporal data. And even though there are many time series libraries, they are often incompatible with each other.

In this tutorial, we will present [sktime] - a unified framework for machine learning with time series. sktime covers multiple time series learning problems, including time series transformation, classification and forecasting, among others. In addition, sktime allows you to easily apply an algorithm for one task to solve another (e.g. a scikit-learn regressor to solve a forecasting problem). In the tutorial, you will learn about how you can identify these problems, what their key differences are and how they are related.

To solve these problems, sktime provides various time series algorithms and modular tools for pipelining, ensembling and tuning. In addition, sktime is interfaces with many existing libraries, including scikit-learn, statsmodels and fbprophet.

You will learn how to use, combine, tune and evaluate different algorithms on real-world data sets. We'll work through all of this step by step using Jupyter Notebooks. Finally, you will find out about how to get involved in sktime's community.

:movie_camera: **Check out our [previous tutorial](https://github.com/sktime/sktime-tutorial-pydata-amsterdam-2020) from the PyData Amsterdam 2020!**

## :rocket: How to get started

You have different options how to run the tutorial notebooks:

* Run the notebooks in the cloud on [Binder] - for this you don't have to install anything!
* Run the notebooks on your machine. [Clone] this repository, get [conda], install the required packages using `conda env create -f environment.yml` and launch Jupyter Lab by running: `jupyter lab`. For trouble shooting, see sktime's more detailed [installation instructions].

[Binder]: https://mybinder.org/v2/gh/sktime/sktime-pydata-global-2021-tutorial/main?filepath=notebooks
[clone]: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[conda]: https://docs.conda.io/en/latest/
[installation instructions]: https://www.sktime.org/en/latest/installation.html

## :wave: How to contribute

If you're interested in contributing to sktime, you can find out more how to get involved [here](https://www.sktime.org/en/stable/get_involved.html).

Any contributions are welcome, not just code!
