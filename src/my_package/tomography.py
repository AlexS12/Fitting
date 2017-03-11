"""
Benchmarks for tomography functions

author: Jaime Sáez Mollejo

"""
import numpy as np
from numba import njit


def click(N, eta, p):
    """Calculates the click probability for a given number of photos N.

    Parameters
    ----------
    N : int
        Number of photons.
    eta : float
        Efficiency of the detector.
    p : ndarray
        Probability of detection of a number of photons from one (first)
        to N (last).

    Returns
    -------
    r : float
        Click probability.

    Notes
    -----
    .. math:: R(N)=1-e^{-\eta N}\sum_{i=0}^m(1-p_i)\frac{(\eta N)^i}{i!}

    References
    ----------
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
    expert systems and adaptive co-kriging for environmental habitat
    modelling of the Highland Haggis using object-oriented, fuzzy-logic
    and neural-network techniques," Computers & Geosciences, vol. 22,
    pp. 585-588, 1996.

    """
    sum_ = 0
    factorial_i = 1
    for ii in range(1, N+1):
        factorial_i *= ii
        sum_ += (1 - p[ii-1]) * (eta * N) ** ii / factorial_i
    r = 1 - np.exp(-eta * N) * sum_
    return r


def click_vectorial(N, eta, p):
    """ Calculates the click probabilities for a given number of photons
    between zero and N.

    Parameters
    ----------
    N : int
        Maximum number of photons.
    eta : float
            Efficiency of the detector.
    p : ndarray
        Probability of detection of a number of photons from one (first)
        to N (last).

    Returns
    -------
    R : ndarray
        Click probabilities.

    Notes
    -----
    .. math:: R(N)=1-e^{-\eta N}\sum_{i=0}^m(1-p_i)\frac{(\eta N)^i}{i!}

    References
    ----------
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
    expert systems and adaptive co-kriging for environmental habitat
    modelling of the Highland Haggis using object-oriented, fuzzy-logic
    and neural-network techniques," Computers & Geosciences, vol. 22,
    pp. 585-588, 1996.

    """
    sum_ = np.zeros_like(p)
    factorial_i = 1
    N_ = np.arange(1, N+1)
    for ii in N_:
        factorial_i *= ii
        sum_ += (1 - p[ii-1]) * (eta * N_) ** (ii) / factorial_i
    r = 1 - np.exp(-eta * N_) * sum_
    return r


def click_loop(N, eta, p):
    """ Calculates the click probabilities for a given number of photons
    between zero and N.

    Parameters
    ----------
    N : int
        Maximum number of photons.
    eta : float
            Efficiency of the detector.
    p : ndarray
        Probability of detection of a number of photons from one (first)
        to N (last).

    Returns
    -------
    R : ndarray
        Click probabilities.

    Notes
    -----
    .. math:: R(N)=1-e^{-\eta N}\sum_{i=0}^m(1-p_i)\frac{(\eta N)^i}{i!}

    References
    ----------
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
    expert systems and adaptive co-kriging for environmental habitat
    modelling of the Highland Haggis using object-oriented, fuzzy-logic
    and neural-network techniques," Computers & Geosciences, vol. 22,
    pp. 585-588, 1996.

    """
    r = np.empty_like(p)
    sum_ = np.zeros_like(p)
    factorial_i = 1
    for ii, N in enumerate(range(1, N+1)):
        r[ii] = click_jit(N, eta, p[:ii+1])
    return r


click_jit = njit(click)
click_vectorial_jit = njit(click_vectorial)
click_loop_jit = njit(click_loop)
