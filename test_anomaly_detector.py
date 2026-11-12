import unittest

from anomaly_detector import classify_reading


class AnomalyDetectorTests(unittest.TestCase):
    def test_typical_reading_is_normal(self):
        self.assertEqual(classify_reading(22, 100), "normal")

    def test_extreme_reading_is_anomaly(self):
        self.assertEqual(classify_reading(80, 140), "anomaly")


if __name__ == "__main__":
    unittest.main()
