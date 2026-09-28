"""Discrete Cosine Transform (DCT-II / IDCT).
100% Python Standard Library.
"""

import math

class CosineTransform:
    @staticmethod
    def dct2(signal):
        n = len(signal)
        out = []
        factor = math.pi / (2.0 * n)
        for k in range(n):
            alpha = math.sqrt(1.0 / n) if k == 0 else math.sqrt(2.0 / n)
            s = sum(signal[i] * math.cos((2.0 * i + 1.0) * k * factor) for i in range(n))
            out.append(round(alpha * s, 5))
        return out

    @staticmethod
    def idct(coeffs):
        n = len(coeffs)
        signal = []
        factor = math.pi / (2.0 * n)
        for i in range(n):
            s = 0.0
            for k in range(n):
                alpha = math.sqrt(1.0 / n) if k == 0 else math.sqrt(2.0 / n)
                s += alpha * coeffs[k] * math.cos((2.0 * i + 1.0) * k * factor)
            signal.append(round(s, 5))
        return signal
