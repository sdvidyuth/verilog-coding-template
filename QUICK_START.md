# Contractor Quick Start Guide

## Prerequisites

Install these first:
- **Docker Desktop**: https://www.docker.com/products/docker-desktop (download, install, open it)
- **Python 3.10+**: https://www.python.org/downloads/
- **Git**: https://git-scm.com/downloads
- **uv**: Open terminal and run `pip install uv`

## Step 1: Get GitHub Access

### 1.1 Create GitHub Account (skip if you have one)
1. Go to https://github.com
2. Click "Sign up"
3. Follow the prompts

### 1.2 Get Added to phinitylabs Organization
- Ask Sonya to add you to the phinitylabs organization on GitHub
- You'll receive an email invitation - accept it

### 1.3 Create a Personal Access Token
1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Set:
   - **Note**: `verilog-eval` (or any name)
   - **Expiration**: 90 days
   - **Scopes**: Check `repo` (full control of private repositories)
4. Click "Generate token"
5. **COPY THE TOKEN NOW** - you won't see it again
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 1.4 Save Your Token
Add this to your shell config so you don't have to set it every time:

**Mac/Linux:**
```bash
echo 'export GITHUB_TOKEN=ghp_your_token_here' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell):**
```powershell
[Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "ghp_your_token_here", "User")
```

## Step 2: Clone the Template

Open terminal and run:
```bash
cd ~/Documents/GitHub
git clone https://github.com/phinitylabs/verilog-coding-template.git
cd verilog-coding-template
uv sync
```

## Step 3: Test Your Setup

```bash
uv run utils/imagectl3.py verilog_ -bv --ids lifo_stack
```

If successful, you'll see "Validation succeeded" at the end.

---

## Adding a New Problem

### Step A: Clone the Problems Repo

```bash
cd ~/Documents/GitHub
git clone https://github.com/phinitylabs/microcode_sequencer.git
cd microcode_sequencer
```

### Step B: Create Your Problem Branches

Each problem needs 3 branches. Replace `my_problem` with your problem name:

```bash
# 1. Create baseline branch (starting code with TODOs)
git checkout main
git checkout -b my_problem_baseline

# Add your files:
# - sources/my_problem.v (with TODO stubs)
# - tests/test_my_problem.py (runner only, no actual tests)
# - pyproject.toml

git add .
git commit -m "Add my_problem baseline"

# 2. Create test branch (adds hidden tests)
git checkout -b my_problem_test

# Add: tests/test_my_problem_hidden.py (actual test cases)

git add .
git commit -m "Add hidden tests"

# 3. Create golden branch (complete solution, no tests)
git checkout my_problem_baseline
git checkout -b my_problem_golden

# Edit sources/my_problem.v to have the complete working solution

git add .
git commit -m "Add golden solution"

# 4. Push all branches
git push origin my_problem_baseline my_problem_test my_problem_golden
```

### Step C: Register Your Problem

Edit `src/hud_controller/problems/basic.py` in the verilog-coding-template folder:

```python
PROBLEM_REGISTRY.append(
    ProblemSpec(
        id="my_problem",
        description="""Description of what the contractor should implement.""",
        difficulty="easy",  # or "medium" or "hard"
        base="my_problem_baseline",
        test="my_problem_test",
        golden="my_problem_golden",
        test_files=["tests/test_my_problem_hidden.py"],
    )
)
```

### Step D: Build and Validate

```bash
cd ~/Documents/GitHub/verilog-coding-template
uv run utils/imagectl3.py verilog_ -bv --ids my_problem
```

You should see all 6 checks pass:
- ✓ Baseline compiles
- ✓ Test patch applies
- ✓ Tests fail on baseline
- ✓ Golden patch applies
- ✓ Golden compiles
- ✓ Tests pass on golden

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `GITHUB_TOKEN not set` | Run `export GITHUB_TOKEN=ghp_xxx` or check Step 1.4 |
| `could not read Password` | Token is empty or invalid - regenerate it |
| `repository not found` | Ask Sonya to add you to phinitylabs org |
| `branch not found` | Make sure you pushed all 3 branches |
| Docker not running | Open Docker Desktop app |

## Need Help?

Email sonya@phinity.ai
