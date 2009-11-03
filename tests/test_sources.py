#!/usr/bin/env python
import os
import unittest

import numpy as np
from numpy.testing import *

import sources


TEST_DATA_DIR = os.path.join(os.path.dirname(sources.__file__), 'test_data')

class TestAudioSource(unittest.TestCase):
    def _test_audio_source(self, filename, length, channels):
        samples = sources.AudioSource(filename).toarray()
        self.assertEqual(samples.shape, (channels, length))

        start = 1000 
        length = 44100
        end = start + length
        nbuf = 100
        samples2 = sources.AudioSource(filename, start=start, end=end,
                                       nbuf=nbuf).toarray()
        self.assertEqual(samples2.shape, (length/nbuf, nbuf))
        assert_array_equal(samples[0,start:end], samples2.flatten())
                
    def test_audio_source_from_file(self):
        filename = os.path.join(TEST_DATA_DIR, 'test.wav')
        samplerate = 44100
        length = 45161
        channels = 1

        self._test_audio_source(filename, length, channels)

    def test_audio_source_from_samples(self):
        length = 45161
        channels = 1
        samples = np.random.rand(length)

        self._test_audio_source(samples, length, channels)


if __name__ == '__main__':
    unittest.main()
