# -*- coding: utf-8 -*-
from pathlib import Path
from warnings import simplefilter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import MaxNLocator


def _get_windows(cv, y):
    """Generate windows"""
    train_windows = []
    test_windows = []
    for train, test in cv.split(y):
        train_windows.append(train)
        test_windows.append(test)
    return train_windows, test_windows


def plot_windows(cv, y, title=""):
    """Plot training and test windows.

    Parameters
    ----------
    y : pd.Series
        Time series to split
    cv : temporal cross-validation iterator object
        Temporal cross-validation iterator
    title : str
        Plot title
    """

    simplefilter("ignore", category=UserWarning)

    train_windows, test_windows = _get_windows(cv, y)

    def get_y(length, split):
        # Create a constant vector based on the split for y-axis."""
        return np.ones(length) * split

    n_splits = len(train_windows)
    n_timepoints = len(y)
    len_test = len(test_windows[0])

    train_color, test_color = sns.color_palette("colorblind")[:2]

    fig, ax = plt.subplots(figsize=plt.figaspect(0.3))

    for i in range(n_splits):
        train = train_windows[i]
        test = test_windows[i]

        ax.plot(
            np.arange(n_timepoints), get_y(n_timepoints, i), marker="o", c="lightgray"
        )
        ax.plot(
            train,
            get_y(len(train), i),
            marker="o",
            c=train_color,
            label="Window",
        )
        ax.plot(
            test,
            get_y(len_test, i),
            marker="o",
            c=test_color,
            label="Forecasting horizon",
        )
    ax.invert_yaxis()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set(
        title=title,
        ylabel="Window number",
        xlabel="Time",
        xticklabels=y.index,
    )
    # remove duplicate labels/handles
    handles, labels = [(leg[:2]) for leg in ax.get_legend_handles_labels()]
    ax.legend(handles, labels)


def load_benzene_concentration_sample():
    """Load sample of benzene concentration dataset [1].

    Missing values have been imputed using the mean value.

    Returns
    -------
    X : np.ndarray
        Feature time series data.
    y : np.ndarray
        Target data.

    References
    ----------
    .. [1] https://zenodo.org/record/3902673#.YXqxNy8w3UI
    """
    file = Path(__file__).parent.parent / "data/benzene_concentration_sample.csv"
    df = pd.read_csv(file)
    y = df["target"].to_numpy()
    X = df.drop(columns="target").to_numpy()
    X = np.expand_dims(X, axis=1)
    return X, y
