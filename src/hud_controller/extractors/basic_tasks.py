import logging

from hud_controller.graders import AgentPatchGrader
from hud_controller.spec import EnvironmentState, Grade, problem

logger = logging.getLogger(__name__)


# ==============================================================================
# TEMPLATE: Easy Difficulty Tasks
# ==============================================================================
# This file contains example templates for easy difficulty coding tasks.
# Easy tasks typically involve:
# - Simple bug fixes
# - Straightforward feature additions
# - Clear, well-defined changes to 1-2 files
# - Minimal context required
# ==============================================================================


@problem(
    id="greet_len",
    description="""
    Please complete the function greet_length without using `sorry`.
    """,
    hints=[
#         HintSpec(
#             hint_type="legit/leaky",
#             text="The issue is in the event handler lifecycle",
#             why_legitmate="Points to general area without revealing solution"
#         ),
#        ... (add more hints as needed)
    ],
    difficulty="easy",
    task_type="coding",
    review_level="no-review",
    base="greet_len_baseline",
    test="greet_len_test",
    golden="greet_len_golden",
)
def greet_len(state: EnvironmentState) -> Grade:
    return Grade.from_subscores(
        [
            AgentPatchGrader.grade(
                state=state,
                weight=1.0,
                base="greet_len_baseline",
                test="greet_len_test",
                golden="greet_len_golden",
            )
        ]
    )


# ==============================================================================
# TASK TEMPLATE STRUCTURE
# ==============================================================================
#
# When creating a new easy task, follow this structure:
#
# 1. Problem Decorator:
#    - id: Unique identifier (lowercase, underscores)
#    - description: High level explanation of the task
#    - hints: List of HintSpec objects (optional)
#    - difficulty: "easy"
#    - task_type: "coding"
#    - review_level: Review status
#    - base: Git branch/tag for baseline code
#    - test: Git branch/tag with tests
#    - golden: Git branch/tag with correct solution
#
# 2. Function Definition:
#    - Name should match the problem id
#    - Takes EnvironmentState as parameter
#    - Returns Grade object
#
# 3. Docstring:
#    - Brief task description
#    - Parameter explanation
#    - Return value description
#    - Grading criteria (1.0 vs 0.0)
#
# 4. Grade Composition:
#    - Use Grade.from_subscores()
#    - Include AgentPatchGrader with appropriate weight
#    - Specify test files to run
#    - Can include multiple graders with different weights
#
# ==============================================================================


# ==============================================================================
# EXAMPLE WITH HINTS
# ==============================================================================
#
# For tasks that benefit from hints, use the HintSpec class:
#
# from hud_controller.spec import HintSpec
#
# @problem(
#     id="example_with_hints",
#     description="...",
#     hints=[
#         HintSpec(
#             hint_type="legit",
#             text="The issue is in the event handler lifecycle",
#             why_legitmate="Points to general area without revealing solution"
#         ),
#         HintSpec(
#             hint_type="leaky",
#             text="You need to add useCallback hook",
#             why_legitmate="Gives away specific implementation detail"
#         ),
#     ],
#     difficulty="easy",
#     # ... rest of config
# )
#
# ==============================================================================
