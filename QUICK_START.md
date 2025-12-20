# Quick Start Guide

## Prerequisites

- Docker Desktop (running)
- Python 3.10+
- Git
- uv (`pip install uv`)

## Setup

### 1. Clone the template

```bash
cd ~/Documents/GitHub
git clone https://github.com/phinitylabs/verilog-coding-template.git
cd verilog-coding-template
uv sync
```

### 2. Clone the problems repo

```bash
mkdir -p local-repos
cd local-repos
git clone https://github.com/phinitylabs/microcode_sequencer.git
cd microcode_sequencer

# Checkout all branches locally
for branch in $(git branch -r | grep -v HEAD | sed 's/origin\///'); do
  git checkout $branch 2>/dev/null || true
done
git checkout main

cd ../..
```

### 3. Build and validate

```bash
# Build one problem
uv run utils/imagectl3.py verilog_ -b --ids lifo_stack

# Validate one problem
uv run utils/imagectl3.py verilog_ -v --ids lifo_stack

# Build and validate all registered problems
uv run utils/imagectl3.py verilog_ -bv --jobs 4
```

## Adding a New Problem

### 1. Create branches in microcode_sequencer repo

Each problem needs 3 branches:
- `<problem_id>_baseline` - Starting code (stubs or buggy)
- `<problem_id>_test` - Baseline + hidden tests
- `<problem_id>_golden` - Complete solution (no tests)

```bash
cd local-repos/microcode_sequencer

# Create baseline
git checkout -b my_problem_baseline
# Add sources/my_problem.v with TODO stubs
# Add tests/test_my_problem.py with pytest runner only
git add . && git commit -m "Baseline"

# Create test branch
git checkout -b my_problem_test
# Add tests/test_my_problem_hidden.py with actual tests
git add . && git commit -m "Add hidden tests"

# Create golden branch from baseline
git checkout my_problem_baseline
git checkout -b my_problem_golden
# Implement the solution in sources/my_problem.v
git add . && git commit -m "Golden solution"

# Push all branches
git push origin my_problem_baseline my_problem_test my_problem_golden
```

### 2. Register the problem

Edit `src/hud_controller/problems/basic.py`:

```python
PROBLEM_REGISTRY.append(
    ProblemSpec(
        id="my_problem",
        description="""Task description here.""",
        difficulty="easy",  # easy, medium, or hard
        base="my_problem_baseline",
        test="my_problem_test",
        golden="my_problem_golden",
        test_files=["tests/test_my_problem_hidden.py"],
    )
)
```

### 3. Build and validate

```bash
uv run utils/imagectl3.py verilog_ -bv --ids my_problem
```

Expected output: All 6 validation checks pass.

## Running Agent Evaluations

```bash
# Generate JSON config
uv run utils/imagectl3.py verilog_ -j

# Run evaluation (requires API key)
uv run hud eval local-hud.json claude --model claude-sonnet-4-5-20250929 --max-steps 150
```

## File Structure

```
verilog-coding-template/
├── local-repos/
│   └── microcode_sequencer/     # Clone of problems repo (all branches)
├── src/hud_controller/
│   └── problems/basic.py        # Problem registry
├── Dockerfile                   # Docker build config
└── utils/imagectl3.py           # Build/validate tool
```

## Troubleshooting

**Build fails with "branch not found"**
- Ensure all 3 branches exist in local-repos/microcode_sequencer
- Run the branch checkout loop in step 2

**Validation fails**
- Baseline must compile
- Tests must fail on baseline
- Tests must pass on golden

**Docker cache issues**
- Increment `ENV random=randomN` in Dockerfile

