import hashlib

class MerkleTree:
    def __init__(self, data_blocks=None):
        self.data_blocks = data_blocks or []
        self.leaves = [self._hash_data(data) for data in self.data_blocks]
        self.tree = []
        if self.leaves:
            self.build_tree()

    def _hash_data(self, data: str) -> str:
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def _hash_pair(self, left: str, right: str) -> str:
        return hashlib.sha256((left + right).encode('utf-8')).hexdigest()

    def build_tree(self):
        if not self.leaves:
            return
        
        current_layer = list(self.leaves)
        self.tree = [current_layer]

        while len(current_layer) > 1:
            if len(current_layer) % 2 != 0:
                current_layer.append(current_layer[-1])
            
            next_layer = []
            for i in range(0, len(current_layer), 2):
                combined_hash = self._hash_pair(current_layer[i], current_layer[i+1])
                next_layer.append(combined_hash)
            
            self.tree.append(next_layer)
            current_layer = next_layer

    def get_root(self) -> str:
        if not self.tree:
            return None
        return self.tree[-1][0]

    def get_proof(self, index: int) -> list:
        if index < 0 or index >= len(self.leaves):
            return []
        
        proof = []
        for layer in self.tree[:-1]:
            is_right_sibling = (index % 2 == 0)
            sibling_index = index + 1 if is_right_sibling else index - 1
            
            if sibling_index < len(layer):
                proof.append((layer[sibling_index], "right" if is_right_sibling else "left"))
            else:
                proof.append((layer[index], "right"))
            
            index //= 2
        return proof

    def verify_proof(self, leaf_data: str, proof: list, root_hash: str) -> bool:
        current_hash = self._hash_data(leaf_data)
        for sibling_hash, direction in proof:
            if direction == "right":
                current_hash = self._hash_pair(current_hash, sibling_hash)
            else:
                current_hash = self._hash_pair(sibling_hash, current_hash)
        return current_hash == root_hash