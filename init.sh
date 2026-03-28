#!/bin/bash
# OUTLOCAL — Dev server startup script
# Run this at the start of every session

set -e

echo "=== OUTLOCAL Dev Server ==="

# Check Python
if ! command -v python &>/dev/null; then
    echo "ERROR: Python not found. Install Python 3.11+"
    exit 1
fi

PYTHON_VERSION=$(python --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Python: $PYTHON_VERSION"

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/Scripts/activate 2>/dev/null || source venv/bin/activate 2>/dev/null
    echo "Virtual environment activated"
elif [ -d ".venv" ]; then
    source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate 2>/dev/null
    echo "Virtual environment activated"
else
    echo "Creating virtual environment..."
    python -m venv venv
    source venv/Scripts/activate 2>/dev/null || source venv/bin/activate 2>/dev/null
    pip install -r requirements.txt
    echo "Virtual environment created and dependencies installed"
fi

# Check .env
if [ ! -f ".env" ]; then
    echo "WARNING: No .env file found. Copy .env.example to .env and fill in values."
fi

# Run smoke test if tests exist
if [ -f "tests/test_smoke.py" ]; then
    echo "Running smoke test..."
    python -m pytest tests/test_smoke.py -v --tb=short 2>/dev/null || echo "Smoke test failed — fix before continuing"
fi

# Start dev server
echo "Starting OUTLOCAL API server on port 8000..."
python -m uvicorn src.outlocal.api.main:app --reload --port 8000 --host 0.0.0.0
