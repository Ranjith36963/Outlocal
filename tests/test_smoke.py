"""Smoke tests — quick sanity check that core imports work."""


def test_package_imports():
    """Verify core package is importable."""
    import src.outlocal

    assert src.outlocal.__version__ == "0.1.0"


def test_feature_list_exists():
    """Verify feature_list.json exists and is valid JSON."""
    import json
    from pathlib import Path

    feature_list = Path("feature_list.json")
    assert feature_list.exists(), "feature_list.json not found"

    with open(feature_list) as f:
        features = json.load(f)

    assert isinstance(features, list), "feature_list.json should be a list"
    assert len(features) > 0, "feature_list.json should not be empty"

    for feature in features:
        assert "id" in feature, f"Feature missing 'id': {feature}"
        assert "passes" in feature, f"Feature missing 'passes': {feature}"
