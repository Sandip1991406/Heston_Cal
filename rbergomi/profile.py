"""
Profile the rBergomi model to find timing bottlenecks in the code.
"""

from line_profiler import LineProfiler
from svi_calibrate import fit_bergomi  # noqa: F401
from NeuralNetworkPricing import NeuralNetworkPricer

if __name__ == "__main__":
    # Create a LineProfiler object, specifying the methods to be profiled by line
    lprofiler = LineProfiler(
        NeuralNetworkPricer.Eval, NeuralNetworkPricer.EvalInGrid
    )
    # Wrap the entry function with the LineProfiler object, then run it.
    lp_wrapper = lprofiler(fit_bergomi)
    lp_wrapper()
    # Print the profiling results in milliseconds
    lprofiler.print_stats(output_unit=1e-03)
