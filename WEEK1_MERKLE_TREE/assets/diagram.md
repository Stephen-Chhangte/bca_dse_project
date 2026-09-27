# Merkle Tree Architecture Visual Diagram

```mermaid
graph TD
    Root["Merkle Root

(Top Hash)"] --> H12["Parent Hash H12


Hash(H1 + H2)"]
Root --> H34["Parent Hash H34


Hash(H3 + H4)"]

H12 --> H1["Leaf Hash H1

Hash(Block A)"]
H12 --> H2["Leaf Hash H2


Hash(Block B)"]

H34 --> H3["Leaf Hash H3

Hash(Block C)"]
H34 --> H4["Leaf Hash H4


Hash(Block D)"]

style Root fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
style H12 fill:#2196F3,stroke:#333,stroke-width:1px,color:#fff
style H34 fill:#2196F3,stroke:#333,stroke-width:1px,color:#fff