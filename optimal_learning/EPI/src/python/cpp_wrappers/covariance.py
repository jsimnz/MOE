# -*- coding: utf-8 -*-
"""Thin covariance-related data containers that can be passed to cpp_wrappers.* functions/classes requiring covariance data.

C++ covariance objects currently do not expose their members to Python. Additionally although C++ has several covariance
functions available, runtime-selection is not yet implemented. The containers here just track the hyperparameters of
covariance functions in a format that can be interpreted in C++ calls.

"""

import numpy

from optimal_learning.EPI.src.python.interfaces.covariance_interface import CovarianceInterface


class SquareExponential(CovarianceInterface):

    r"""Implement the square exponential covariance function.

    The function:
    ``cov(x_1, x_2) = \alpha * \exp(-1/2 * ((x_1 - x_2)^T * L * (x_1 - x_2)) )``
    where L is the diagonal matrix with i-th diagonal entry ``1/lengths[i]/lengths[i]``

    This covariance object has ``dim+1`` hyperparameters: ``\alpha, lengths_i``

    """

    def __init__(self, hyperparameters):
        r"""Construct a square exponential covariance object that can be used with cpp_wrappers.* functions/classes.

        :param hyperparameters: hyperparameters of the covariance function; index 0 is \alpha (signal variance, \sigma_f^2)
          and index 1..dim are the per-dimension length scales.
        :type hyperparameters: array-like of size dim+1

        """
        self._hyperparameters = numpy.copy(hyperparameters)

    @property
    def num_hyperparameters(self):
        """Return the number of hyperparameters of this covariance function."""
        return self._hyperparameters.size

    def get_hyperparameters(self):
        """Get the hyperparameters of this covariance."""
        return numpy.copy(self._hyperparameters)

    def set_hyperparameters(self, hyperparameters):
        """Set hyperparameters to the specified hyperparameters; ordering must match."""
        self._hyperparameters = numpy.copy(hyperparameters)

    def covariance(self, point_one, point_two):
        r"""Compute the covariance function of two points, cov(``point_one``, ``point_two``).

        We do not currently expose a C++ endpoint for this call; see covariance_interface.py for interface specification.

        """
        raise NotImplementedError("C++ wrapper currently does not support computing covariance quantities.")

    def grad_covariance(self, point_one, point_two):
        r"""Compute the gradient of self.covariance(point_one, point_two) with respect to the FIRST argument, point_one.

        We do not currently expose a C++ endpoint for this call; see covariance_interface.py for interface specification.

        """
        raise NotImplementedError("C++ wrapper currently does not support computing covariance quantities.")

    def hyperparameter_grad_covariance(self, point_one, point_two):
        r"""Compute the gradient of self.covariance(point_one, point_two) with respect to its hyperparameters.

        We do not currently expose a C++ endpoint for this call; see covariance_interface.py for interface specification.

        """
        raise NotImplementedError("C++ wrapper currently does not support computing covariance quantities.")

    def hyperparameter_hessian_covariance(self, point_one, point_two):
        r"""Compute the gradient of self.covariance(point_one, point_two) with respect to its hyperparameters.

        We do not currently expose a C++ endpoint for this call; see covariance_interface.py for interface specification.

        """
        raise NotImplementedError("C++ wrapper currently does not support computing covariance quantities.")