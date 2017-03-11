"""
Tests for tomography functions

author: Jaime Sáez Mollejo

"""
import numpy as np
from numpy.testing import assert_almost_equal

from my_package.tomography import (
    click, click_loop, click_vectorial,
    click_jit, click_loop_jit, click_vectorial_jit)


def test_click():
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Expected result
    expected_r = 0.0
    # Real result
    r = click(N, eta, p)
    # Check
    assert_almost_equal(r, expected_r)


def test_click_vectorial():
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Expected result
    expected_r = [0.0, 0.0, 0.0]
    # Real result
    r = click_vectorial(N, eta, p)
    # Check
    assert_almost_equal(r, expected_r)


def test_click_loop():
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Expected result
    expected_r = [0.0, 0.0, 0.0]
    # Real result
    r = click_loop(N, eta, p)
    # Check
    assert_almost_equal(r, expected_r)


def test_click_jit():
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Expected result
    expected_r = click(N, eta, p)
    # Real result
    r = click_jit(N, eta, p)
    # Check
    assert_almost_equal(r, expected_r)


def test_click_vectorial_jit():
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Expected result
    expected_r = click_vectorial(N, eta, p)
    # Real result
    r = click_vectorial_jit(N, eta, p)
    # Check
    assert_almost_equal(r, expected_r)


def test_click_loop_jit():
    # Test parameters
    N = 3
    eta = 0.95
    p = np.array([0.0, 0.1, 0.1])
    # Expected result
    expected_r = click_loop(N, eta, p)
    # Real result
    r = click_loop_jit(N, eta, p)
    # Check
    assert_almost_equal(r, expected_r)
