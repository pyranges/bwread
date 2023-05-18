import pandas as pd
import pyranges as pr  # type: ignore

from bwread.src.bwread import _bwread  # type: ignore


def read_bigwig(f):
    dfs = _bwread(f)

    for chromosome, df in dfs.items():
        chromosomes = pd.Series(chromosome, index=df.index, dtype="category")
        df.insert(0, "Chromosome", chromosomes)
        dfs[chromosome] = df

    return pr.PyRanges(dfs)
