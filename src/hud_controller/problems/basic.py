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
        description="""The FIFO connects two independent clock domains (wr_clk and rd_clk).
Parameterizable width and depth (power of two).
All logic must be synthesizable.
Implement a clean, correct, and CDC-safe async FIFO.

Inputs:
     input [data_size-1:0]  write_data,
	 input 				    write_increment, write_clk, write_reset_n,
	 input 				    read_increment, read_clk, read_reset_n,
Outputs:	 
     output [data_size-1:0] read_data,
	 output write_full,
	 output read_empty
 );
""",
        difficulty="medium",
        base="async_fifo_baseline",
        test="async_fifo_test",
        golden="async_fifo_golden",
        test_files=["tests/test_fifo.py"],
    )
)
