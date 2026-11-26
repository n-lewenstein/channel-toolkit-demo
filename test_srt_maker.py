import unittest

from srt_maker import make_srt


class MakeSrtTest(unittest.TestCase):
    def test_default_timing(self):
        # 5 words at 2.5 wps = 2s; "Hi" is short, so it gets the 1s minimum.
        # Blank lines are skipped.
        srt = make_srt(["one two three four five\n", "\n", "Hi\n"])
        self.assertEqual(
            srt,
            "1\n00:00:00,000 --> 00:00:02,000\none two three four five\n"
            "\n"
            "2\n00:00:02,000 --> 00:00:03,000\nHi\n",
        )


if __name__ == "__main__":
    unittest.main()
