"""
Example problem registry for verilog evaluation template.
For internal problems, use phinitylabs/verilog-eval-internal.
"""
import logging
from hud_controller.spec import ProblemSpec, PROBLEM_REGISTRY

logger = logging.getLogger(__name__)

# =============================================================================
# EXAMPLE PROBLEMS - For demonstration only
# =============================================================================

PROBLEM_REGISTRY.append(
   ProblemSpec(
       id="async_fifo",
       description="""Complete the implementation of Asynch FIFO.
       The FIFO connects two independent clock domains (wr_clk and rd_clk).
       Parameterizable width and depth (power of two).
       All logic must be synthesizable.
       Implement a clean, correct, and CDC-safe async FIFO.""",
       difficulty="medium",
       base="async_fifo_baseline",
       test="async_fifo_test",
       golden="async_fifo_golden",
       test_files=["tests/test_fifo.py"],
   )
)


