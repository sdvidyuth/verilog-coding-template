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
        id="simple_counter",
        description="""Please implement a simple synchronous counter with reset, enable, and load functionality.

Inputs:
- clk: Clock signal (rising edge triggered)
- rst: Synchronous reset signal
- ena: Enable signal (allows counting)
- set: Load signal (sets counter to a specific value)
- din: 8-bit data input (value to load when set is high)

Output:
- counter: 8-bit counter value
""",
        difficulty="easy",
        base="simple_counter_baseline",
        test="simple_counter_test",
        golden="simple_counter_golden",
        test_files=["tests/test_simple_counter_hidden.py"],
    )
)
