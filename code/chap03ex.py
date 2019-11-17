"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
import first
import thinkstats2


def PmfMean(pmf):
    """ This function computes mean of a PMF.
    :param
        pmf: pmf is the passed pmf argument whose mean PMF needs to be calculated using this function.

    :return
        mean: returns float value which is mean of the PMF passed to the function.
    """
    meanOfPMF = 0.0                           # Default mean value
    for x, p in pmf.d.items():                # Loop through each item
        meanOfPMF = meanOfPMF + p * x         # Calculate mean of PMF
    return meanOfPMF                          # Return mean of PMF


def PmfVar(pmf, meanOfPMF=None):
    """This function computes variance of a PMF.
        :param
            pmf: pmf is the passed pmf argument whose variance needs to be calculated using this function.
            meanOfPMF: mean of the PMF passed to the function.

        :return
            variance: returns float value which is variance of the PMF passed to the function.
        """
    if meanOfPMF is None:                     # Calculate mean if not passed to the function
        meanOfPMF = PmfMean(pmf)              # Calculate mean using mean function

    variance = 0.0                            # Default variance
    for x, p in pmf.d.items():                # Loop through each item
        variance += p * (x - meanOfPMF) ** 2  # Calculate variance now
    return variance                           # Return variance value


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()

    # test PmfMean and PmfVar function we created
    prglngth = live.prglngth
    pmf = thinkstats2.Pmf(prglngth)
    mean = PmfMean(pmf)
    var = PmfVar(pmf, mean)

    assert (mean == pmf.Mean())
    assert (var == pmf.Var())

    print('mean/var preg length', mean, var)
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
