"""Phase 0 sanity check: open the mic and print stats for a handful of incoming buffers."""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from tuner.audio import stream_blocks

NUM_BLOCKS_TO_PRINT = 20


def main():
    print("Listening... make some noise near the mic.\n")
    for i, block in enumerate(stream_blocks()):
        rms = np.sqrt(np.mean(block**2))
        print(
            f"block {i:3d}  shape={block.shape}  dtype={block.dtype}  "
            f"min={block.min():+.3f}  max={block.max():+.3f}  rms={rms:.4f}"
        )
        if i + 1 >= NUM_BLOCKS_TO_PRINT:
            break


if __name__ == "__main__":
    main()
