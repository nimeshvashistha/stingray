========
Stingray
========

|Build Status Master| |Readthedocs| |Slack| |joss| |Coverage Status Master| |GitHub release|

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
X-Ray Spectral Timing Made Easy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stingray is an in-development spectral-timing software package for astrophysical X-ray (and more) data.
Stingray merges existing efforts for a (spectral-)timing package in Python, and is
structured with the best guidelines for modern open-source programming, following the example of `Astropy`_.

It is composed of:

1. a library of time series methods, including power spectra, cross spectra, covariance spectra, lags, and so on;
2. a set of scripts to load FITS data files from different missions;
3. a simulator of light curves and event lists, that includes different kinds of variability and more complicated phenomena based on the impulse response of given physical events (e.g. reverberation);
4. finally, an in-development GUI to ease the learning curve for new users.

There are a number of official software packages for X-ray spectral fitting (Xspec, ISIS, Sherpa, ...).
Such a widely used and standard software package does not exist for X-ray timing,
that remains for now mostly done with custom software.
Stingray aims not only at becoming a standard timing package,
but at extending the implementation to the most advanced spectral timing techniques available in the literature.
The ultimate goal of this project is to provide the community with a package that eases
the learning curve for the advanced spectral timing techniques with a correct statistical framework.


Note to Users
-------------

We welcome contributions and we need your help!
If you have your own code duplicating any part of the methods implemented in
Stingray, please try out Stingray and compare to your own results.

We do welcome any sort of feedback: if something breaks, please report it via
the `issues`_ page. Similarly,
please open an issue if any functionality is missing, the API is not intuitive
or if you have suggestions for additional functionality that would be useful to
have.

If you have code you might want to contribute, we'd love to hear from you,
either via a `pull request`_ or via an `issue`_.


Citing Stingray
---------------

Please cite `Huppenkothen et al. (2019)
<https://ui.adsabs.harvard.edu/abs/2019ApJ...881...39H/abstract>`_ if you find this package useful in your
research.

The BibTeX entry for the paper is::

    @ARTICLE{2019ApJ...881...39H,
       author = {{Huppenkothen}, Daniela and {Bachetti}, Matteo and {Stevens}, Abigail L. and {Migliari}, Simone and {Balm}, Paul and {Hammad}, Omar and {Khan}, Usman Mahmood and {Mishra}, Himanshu and {Rashid}, Haroon and {Sharma}, Swapnil and {Martinez Ribeiro}, Evandro and {Valles Blanco}, Ricardo},
        title = "{Stingray: A Modern Python Library for Spectral Timing}",
      journal = {\apj},
     keywords = {methods: data analysis, methods: statistical, X-rays: binaries, X-rays: general, Astrophysics - Instrumentation and Methods for Astrophysics, Astrophysics - High Energy Astrophysical Phenomena},
         year = 2019,
        month = aug,
       volume = {881},
       number = {1},
          eid = {39},
        pages = {39},
          doi = {10.3847/1538-4357/ab258d},
archivePrefix = {arXiv},
       eprint = {1901.07681},
 primaryClass = {astro-ph.IM},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019ApJ...881...39H},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}


Contents
--------
- make a light curve from event data
- make periodograms in Leahy and r.m.s. normalization
- average periodograms
- maximum likelihood fitting of periodograms/parametric models
- coherence
- cross spectra, r.m.s. spectra and lags (time vs energy, time vs frequency)
- covariance spectra
- bispectra
- Bayesian quasi-periodic oscillation searches
- simulate a light curve with a given power spectrum
- simulate a light curve from another light curve and a 1-d (time) or 2-d (time-energy) impulse response
- simulate an event list from a given light curve _and_ with a given energy spectrum
- load event lists from fits files of a few missions (*RXTE*/PCA, *NuSTAR*/FPM, *XMM-Newton*/EPIC)
- cross correlation functions
- pulsar searches with Epoch Folding, $Z^2_n$ test

Future Additions
----------------
- bicoherence
- phase-resolved spectroscopy of quasi-periodic oscillations
- Fourier-frequency-resolved spectroscopy
- power colours
- full HEASARC-compatible mission support
- binary pulsar searches
- (...) Feel free to propose! Use the `Issues`_ page!

Installation
------------

You can find install Stingray via `conda`, `pip` or from the source repository itself.
More details on how to install Stingray can be found `on the Installations page
<https://stingray.readthedocs.io/en/latest/stingray/docs/install.html>`_.

Documentation
-------------

Is hosted at https://stingray.readthedocs.io/

And is generated using `Sphinx`_. Try::

   $ sphinx-build docs docs/_build

Then open ``./docs/_build/index.html`` in the browser of your choice.

.. _Sphinx: http://sphinx-doc.org

Test suite
----------

Stingray uses `py.test <https://pytest.org>`_ and `tox
<https://tox.readthedocs.io>`_ for testing. To run the tests, try::

   $ tox -e test

You may need to install tox first::

   $ pip install tox

If you have installed Stingray via pip or conda, the source directory might
not be easily accessible. Once installed, you can also run the tests using::

   $ python -c 'import stingray; stingray.test()'

or from within a python interpreter:

.. doctest-skip::

   >>> import stingray
   >>> stingray.test()


Copyright
---------

All content © 2019 the authors. The code is distributed under the MIT license.

Pull requests are welcome! If you are interested in the further development of
this project, please `get in touch via the issues
<https://github.com/dhuppenkothen/stingray/issues>`_!

.. |Build Status Master| image:: https://github.com/StingraySoftware/stingray/workflows/CI%20Tests/badge.svg
    :target: https://github.com/StingraySoftware/stingray/actions/
.. |Readthedocs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
    :target: https://stingray.readthedocs.io/
.. |Slack| image:: http://slack-invite.timelabtechnologies.com/badge.svg
    :target: http://slack-invite.timelabtechnologies.com
.. |Coverage Status Master| image:: https://codecov.io/gh/StingraySoftware/stingray/branch/master/graph/badge.svg?token=FjWeFfhU9F
:target: https://codecov.io/gh/StingraySoftware/stingray
.. |GitHub release| image:: https://img.shields.io/github/release/StingraySoftware/stingray.svg
    :target: https://coveralls.io/github/StingraySoftware/stingray?branch=master
.. |joss| image:: http://joss.theoj.org/papers/10.21105/joss.01393/status.svg
   :target: https://doi.org/10.21105/joss.01393
.. _Astropy: https://www.github.com/astropy/astropy
.. _Issues: https://www.github.com/stingraysoftware/stingray/issues
.. _Issue: https://www.github.com/stingraysoftware/stingray/issues
.. _pull request: https://github.com/StingraySoftware/stingray/pulls
