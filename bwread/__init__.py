import pkg_resources

from bwread.read import read_bigwig  # NOQA: F401

__version__ = pkg_resources.get_distribution("bwread").version
