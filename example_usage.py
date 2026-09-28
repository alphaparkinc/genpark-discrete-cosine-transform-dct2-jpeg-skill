"""Example evaluating DCT transform."""
from client import CosineTransform

def main():
    block = [16.0, 11.0, 10.0, 16.0]
    c = CosineTransform.dct2(block)
    print("DCT-II Energy Compaction Coefficients:", c)
    recon = CosineTransform.idct(c)
    print("Inverse DCT Reconstruction:", recon)

if __name__ == "__main__":
    main()
