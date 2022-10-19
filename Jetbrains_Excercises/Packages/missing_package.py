
# Sequence of names
# There are a lot of packages for Python, for example, SciPy is the most popular library for advanced math.
# Suppose you need to work with the function csgraph_from_dense from this module: it constructs a sparse graph
# representation from a dense matrix. This function is located in the csgraph submodule of the sparse subpackage of the scipy library.
#
# Take a look at the code below. If we run it right now, we will get the ImportError. Can you figure out what is wrong
# with this code snippet? Fix the mistake and run the code again.
#
#
#
# Memory limit: 256 MB
# Time limit: 15 seconds
#
# Caution
#
# You may see errors in your code or execution results due to missing context. Don’t worry about it, just write the solution and press Check.


# Part to fix below
# from scipy.sparse import csgraph_from_dense
from scipy.sparse.csgraph import csgraph_from_dense
