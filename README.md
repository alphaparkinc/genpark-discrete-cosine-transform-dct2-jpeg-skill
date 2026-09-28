# Discrete Cosine Transform (DCT-II) Skill

Orthonormal Type-II Discrete Cosine Transform engine providing exceptional spectral energy compaction for JPEG image compression and audio codecs.

```mermaid
flowchart LR
    Spatial["Spatial Domain Block / Sample Vector"] --> DCT["Type-II Cosine Kernel Modulation"]
    DCT --> Energy["Compacted Frequency Coefficients (Dominant DC + AC)"]
    Energy --> IDCT["Orthonormal Type-III Reconstruction"]
    IDCT --> Spatial
```

## Features
- **100% Python Standard Library**: Pure standard trigonometric formulation.
- **Orthonormal Normalization**: Preserves total signal energy (Parseval identity).
