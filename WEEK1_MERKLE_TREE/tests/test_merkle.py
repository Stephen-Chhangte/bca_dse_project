import pytest
from WEEK1_MERKLE_TREE.src.merkle_tree import MerkleTree

def test_empty_tree():
    tree = MerkleTree()
    assert tree.get_root() is None

def test_single_leaf():
    tree = MerkleTree(["log_0"])
    assert tree.get_root() is not None

def test_proof_verification():
    logs = ["Tx1", "Tx2", "Tx3", "Tx4"]
    tree = MerkleTree(logs)
    root = tree.get_root()
    
    proof = tree.get_proof(1)
    assert tree.verify_proof("Tx2", proof, root) is True
    assert tree.verify_proof("Tx2_tampered", proof, root) is False