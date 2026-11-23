"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import graphmeld


def test_version_is_set() -> None:
    assert graphmeld.__version__
