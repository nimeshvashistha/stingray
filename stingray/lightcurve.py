"""
Definition of :class:`Lightcurve`.

:class:`Lightcurve` is used to create light curves out of photon counting data
or to save existing light curves in a class that's easy to use.
"""

__all__ = ["Lightcurve"]

import numpy as np
import stingray.utils as utils

class Lightcurve(object):
    def __init__(self, time, counts):
        """
        Make a light curve object from an array of time stamps and an
        array of counts.

        Parameters
        ----------
        time: iterable
            A list or array of time stamps for a light curve

        counts: iterable, optional, default None
            A list or array of the counts in each bin corresponding to the
            bins defined in `time` (note: **not** the count rate, i.e.
            counts/second, but the counts/bin).


        Attributes
        ----------
        time: numpy.ndarray
            The array of midpoints of time bins

        counts: numpy.ndarray
            The counts per bin corresponding to the bins in `time`.

        countrate: numpy.ndarray
            The counts per second in each of the bins defined in `time`.

        ncounts: int
            The number of data points in the light curve.

        dt: float
            The time resolution of the light curve.

        tseg: float
            The total duration of the light curve.

        tstart: float
            The start time of the light curve.

        """

        self.time = np.asarray(time)
        self.counts = np.asarray(counts)
        self.ncounts = self.counts.shape[0]
        self.dt = time[1] - time[0]
        self.countrate = self.counts/self.dt
        self.tseg = self.time[-1] - self.time[0] + self.dt
        self.tstart = self.time[0]-0.5*self.dt

    @staticmethod
    def make_lightcurve(toa, dt, tseg=None, tstart=None):
        """
        Make a light curve out of photon arrival times.

        Parameters
        ----------
        toa: iterable
            list of photon arrival times

        dt: float
            time resolution of the light curve (the bin width)

        tseg: float, optional, default None
            The total duration of the light curve.
            If this is `None`, then the total duration of the light curve will
            be the interval between the arrival between the first and the last
            photon in `toa`.

                **Note**: If tseg is not divisible by dt (i.e. if tseg/dt is not
                an integer number), then the last fractional bin will be
                dropped!

        tstart: float, optional, default None
            The start time of the light curve.
            If this is None, the arrival time of the first photon will be used
            as the start time of the light curve.

        Returns
        -------
        lc: :class:`Lightcurve` object
            A light curve object with the binned light curve

        """

        ## tstart is an optional parameter to set a starting time for
        ## the light curve in case this does not coincide with the first photon
        if tstart is None:
            ## if tstart is not set, assume light curve starts with first photon
            tstart = toa[0]

        ## compute the number of bins in the light curve
        ## for cases where tseg/dt are not integer, computer one
        ## last time bin more that we have to subtract in the end
        if tseg is None:
            tseg = toa[-1] - toa[0]

        print("tseg: " + str(tseg))

        timebin = np.int(tseg/dt)
        print("timebin:  " + str(timebin))

        tend = tstart + timebin*dt

        counts, histbins = np.histogram(toa, bins=timebin, range=[tstart, tend])

        dt = histbins[1]-histbins[0]

        time = histbins[:-1]+0.5*dt

        counts = np.asarray(counts)

        return Lightcurve(time, counts)


    def rebin_lightcurve(self, new_dt, method='sum'):
        """
        Rebin the light curve.
        """
        ### calculate number of bins in new light curve
        nbins = np.floor(self.tseg/new_dt)+1
        bin_dt = self.tseg/nbins

        bin_time, bin_counts, _ = utils.rebin_data(self.time,
                                                   self.counts,
                                                   new_dt, method)
        return Lightcurve(bin_time, bin_counts)

