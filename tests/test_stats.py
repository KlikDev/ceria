"""Tests for the `stats` module."""

import pytest

from ceria import Stats


@pytest.fixture(scope="module")
def stats() -> Stats:
    """
    Provide a Stats instance.

    Returns:
        A Stats instance.
    """
    return Stats(
        {
            "downloadSpeed": "0",
            "numActive": "0",
            "numStopped": "0",
            "numStoppedTotal": "0",
            "numWaiting": "0",
            "uploadSpeed": "0",
        }
    )


def test_download_speed(stats):
    """
    Test the `download_speed` property.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.download_speed == 0


def test_download_speed_string(stats):
    """
    Test the `download_speed_string` method.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.download_speed_string() == "0.00 B/s"


def test_download_speed_string_not_human_readable(stats):
    """
    Test the `download_speed_string` method with human readable option.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.download_speed_string(human_readable=False) == "0 B/s"


def test_upload_speed(stats):
    """
    Test the `upload_speed` property.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.upload_speed == 0


def test_upload_speed_string(stats):
    """
    Test the `upload_speed_string` method.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.upload_speed_string() == "0.00 B/s"


def test_upload_speed_string_not_human_readable(stats):
    """
    Test the `upload_speed_string` method with human readable option.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.upload_speed_string(human_readable=False) == "0 B/s"


def test_num_active(stats):
    """
    Test the `numnum_active_waiting` property.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.num_active == 0


def test_num_stopped(stats):
    """
    Test the `num_stopped` property.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.num_stopped == 0


def test_num_stopped_total(stats):
    """
    Test the `num_stopped_total` property.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.num_stopped_total == 0


def test_num_waiting(stats):
    """
    Test the `num_waiting` property.

    Arguments:
        stats: A Stats instance.
    """
    assert stats.num_waiting == 0
