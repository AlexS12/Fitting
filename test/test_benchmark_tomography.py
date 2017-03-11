"""
Tests for tomography functions

author: Jaime Sáez Mollejo

"""
import numpy as np

from my_package.tomography import (
    click, click_loop, click_vectorial,
    click_jit, click_loop_jit, click_vectorial_jit)


def test_click(benchmark):
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Real result
    benchmark(click, N, eta, p)


def test_click_vectorial(benchmark):
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Real result
    benchmark(click_vectorial, N, eta, p)


def test_click_loop(benchmark):
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Real result
    benchmark(click_loop, N, eta, p)


def test_click_jit(benchmark):
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Real result
    benchmark(click_jit, N, eta, p)


def test_click_vectorial_jit(benchmark):
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Real result
    benchmark(click_vectorial_jit, N, eta, p)


def test_click_loop_jit(benchmark):
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Real result
    benchmark(click_loop_jit, N, eta, p)
