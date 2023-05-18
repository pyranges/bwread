import cython
import numpy as np
import pandas as pd
import pyBigWig
from natsort import natsorted

from libc.stdint cimport int64_t


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
cpdef _bwread(f):

    cdef:
        int64_t length
        int64_t start
        int64_t end
        int64_t i
        double value
        long [::1] starts
        long [::1] ends
        double [::1] values

    bw = pyBigWig.open(f)

    chromosomes = bw.chroms()

    dfs = {}

    for chromosome in natsorted(chromosomes):

        intervals = bw.intervals(chromosome)
        length = len(intervals)

        if intervals is None:
            continue

        starts_arr = np.zeros(length, dtype=long)
        starts = starts_arr

        ends_arr = np.zeros(length, dtype=long)
        ends = ends_arr

        values_arr = np.zeros(length, dtype=np.double)
        values = values_arr

        for i in range(length):
            start, end, value = intervals[i]
            starts[i] = start
            ends[i] = end
            values[i] = value

        dfs[chromosome] = pd.DataFrame({"Start": starts_arr, "End": ends_arr, "Value": values_arr})

    return dfs
