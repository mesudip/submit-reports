import math

import allure
import pytest


def test_addition_pass() -> None:
    with allure.step("Compute 2 + 3"):
        assert 2 + 3 == 5


def test_sqrt_pass() -> None:
    with allure.step("Compute sqrt(144)"):
        assert math.sqrt(144) == 12


def test_dummy_trigger_pass() -> None:
    with allure.step("Dummy trigger to validate upload pipeline"):
        assert (3 * 7) - 2 == 19


@pytest.mark.xfail(reason="Intentional unstable signal for report timelines")
def test_intentional_fail() -> None:
    with allure.step("Deliberate mismatch"):
        assert 2 + 2 == 5
