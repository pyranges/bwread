import pyranges as pr
import pandas as pd

from bwread.src.bwread import _bwread

def read_bigwig(f, as_pyranges=True):

    dfs = _bwread(f)

    for chromosome, df in dfs.items():

        chromosomes = pd.Series(chromosome, index=df.index, dtype="category")
        df.insert(0, "Chromosome", chromosomes)
        dfs[chromosome] = df

    return pr.PyRanges(dfs)
