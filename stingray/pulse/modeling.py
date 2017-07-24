import numpy as np
from astropy.modeling import models, fitting


__all__ = ["sinc_square_model", "sinc_square_deriv", "fit_sinc",
           "fit_gaussian", "SincModel"]


def sinc(x):
    """
    Calculate a sinc function.

    sinc(x)=sin(x)/x

    Parameters
    ----------
    x : array-like

    Returns
    -------
    values : array-like
    """
    x_is_zero = x == 0
    values = np.sin(x) / x
    values[x_is_zero] = 1.
    return values


def sinc_square_model(x, amplitude=1., mean=0., width=1.):
    """
    Calculate a sinc-squared function.

    (sin(x)/x)**2

    Parameters
    ----------
    x: array-like

    Other Parameters
    ----------
    amplitude : float
        the value for x=mean
    mean : float
        mean of the sinc function
    width : float
        width of the sinc function

    Returns
    -------
    sqvalues : array-like
         Return square of sinc function
    """
    sqvalues = amplitude * sinc((x-mean)/width) ** 2
    return sqvalues


def sinc_square_deriv(x, amplitude=1., mean=0., width=1.):
    """
    Calculate partial derivatives of sinc-squared.

    Parameters
    ----------
    x: array-like

    Other Parameters
    ----------
    amplitude : float
        the value for x=mean
    mean : float
        mean of the sinc function
    width : float
        width of the sinc function

    Returns
    -------
    d_amplitude : array-like
         partial derivative of sinc-squared function
         with respect to the amplitude
    d_mean : array-like
         partial derivative of sinc-squared function
         with respect to the mean
    d_width : array-like
         partial derivative of sinc-squared function
         with respect to the width
    """

    x_is_zero = x == mean

    d_x = 2 * amplitude * sinc((x-mean)/width) * (x * np.cos((x-mean)/width) \
        - np.sin((x-mean)/width)) / ((x-mean)/width)**2
    d_amplitude = sinc((x-mean)/width)**2
    d_mean = d_x*(-1/width)
    d_width = d_x*(-(x-mean)/(width)**2)

    d_x[x_is_zero] = 0

    return [d_amplitude, d_mean, d_width]


SincModel = models.custom_model(sinc_square_model,
                                fit_deriv=sinc_square_deriv)


def fit_sinc(x, y, amp=1.5, mean=0., width=1., tied={}, fixed={}, bounds={},
             obs_length=None):
    """
    Fit a sinc function to x,y values.

    Parameters
    ----------
    x : array-like
    y : array-like

    Other Parameters
    ----------------
    amp : float
        The initial value for the amplitude
    mean : float
        The initial value for the mean of the sinc
    obs_length : float
        The length of the observation. Default None. If it's defined, it
        fixes width to 1/(pi*obs_length), as expected from epoch folding
        periodograms
    width : float
        The initial value for the width of the sinc. Only valid if
        obs_length is 0
    tied : dict
    fixed : dict
    bounds : dict
        Parameters to be passed to the astropy models
        http://docs.astropy.org/en/stable/api/astropy.modeling.functional_models.Gaussian1D.html

    Returns
    -------
    sincfit : function
        The best-fit function, accepting x as input
        and returning the best-fit model as output
    """
    if obs_length is not None:
        width = 1 / (np.pi * obs_length)
        fixed["width"] = True

    sinc_in = SincModel(amplitude=amp, mean=mean,width=width, tied=tied,
                        fixed=fixed, bounds=bounds)
    fit_sinc = fitting.LevMarLSQFitter()
    sincfit = fit_sinc(sinc_in, x, y)
    return sincfit


def fit_gaussian(x, y, amplitude=1.5,mean=0.,stddev=2., tied={}, fixed={},
                 bounds={}):
    """
    Fit a gaussian function to x,y values.

    Parameters
    ----------
    x : array-like
    y : array-like

    Other Parameters
    ----------------
    amplitude : float
        The initial value for the amplitude
    mean : float
        The initial value for the mean of the gaussian function
    stddev : float
        The initial value for the standard deviation of the gaussian function
    tied : dict
    fixed : dict
    bounds : dict
        Parameters to be passed to the astropy models
        http://docs.astropy.org/en/stable/api/astropy.modeling.functional_models.Gaussian1D.html

    Returns
    -------
    g : function
        The best-fit function, accepting x as input
        and returning the best-fit model as output
    """
    g_in = models.Gaussian1D(amplitude=amplitude,mean=mean,stddev=stddev,
                             tied=tied, fixed=fixed, bounds=bounds)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_in, x, y)
    return g
