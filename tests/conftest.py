"""OUTLOCAL test configuration and shared fixtures."""

import random


def pytest_addoption(parser):
    """Add --fast flag for 10% random subsample of tests."""
    parser.addoption(
        "--fast",
        action="store_true",
        default=False,
        help="Run 10% random subsample of tests for quick feedback",
    )


def pytest_collection_modifyitems(config, items):
    """If --fast flag is set, randomly select ~10% of tests."""
    if config.getoption("--fast"):
        sample_size = max(1, len(items) // 10)
        selected = random.sample(items, sample_size)
        items[:] = selected
