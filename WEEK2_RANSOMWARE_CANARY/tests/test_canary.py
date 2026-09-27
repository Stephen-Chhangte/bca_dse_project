import os
import pytest
from WEEK2_RANSOMWARE_CANARY.src.canary_monitor import CanaryTrap

CANARY_PATH = "WEEK2_RANSOMWARE_CANARY/tests/temp_canary.txt"

@pytest.fixture
def setup_canary():
    trap = CanaryTrap(CANARY_PATH)
    yield trap
    if os.path.exists(CANARY_PATH):
        os.remove(CANARY_PATH)

def test_canary_intact(setup_canary):
    res = setup_canary.inspect()
    assert res["status"] == "OK"

def test_canary_tampered(setup_canary):
    with open(CANARY_PATH, "a") as f:
        f.write("[UNAUTHORIZED_RANSOMWARE_ENCRYPTION_SIMULATION]")
    res = setup_canary.inspect()
    assert res["status"] == "ALERT"
    assert res["event"] == "RANSOMWARE_ENCRYPTION_DETECTED"

def test_canary_deleted(setup_canary):
    os.remove(CANARY_PATH)
    res = setup_canary.inspect()
    assert res["status"] == "ALERT"
    assert res["event"] == "CANARY_FILE_DELETED"