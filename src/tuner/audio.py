"""Microphone capture: turns the live audio stream into a sequence of fixed-size blocks."""

import queue

import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100
BLOCK_SIZE = 2048


def stream_blocks(samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE, channels=1):
    """Yield mono float32 blocks of audio from the default input device, forever."""
    block_queue = queue.Queue()

    def callback(indata, frames, time_info, status):
        if status:
            print(status)
        block_queue.put(indata[:, 0].copy())

    with sd.InputStream(
        samplerate=samplerate,
        blocksize=blocksize,
        channels=channels,
        dtype="float32",
        callback=callback,
    ):
        while True:
            yield block_queue.get()
