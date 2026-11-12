import argparse

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

NORMAL_READINGS = np.array([
    [20, 100], [21, 101], [22, 99], [23, 100], [21, 100], [22, 101],
    [24, 100], [20, 98], [23, 102], [22, 100], [21, 99], [24, 101],
], dtype=float)


def build_model():
    model = make_pipeline(
        StandardScaler(),
        IsolationForest(contamination=0.15, random_state=42),
    )
    model.fit(NORMAL_READINGS)
    return model


def classify_reading(temperature: float, pressure: float) -> str:
    reading = np.array([[temperature, pressure]], dtype=float)
    prediction = build_model().predict(reading)[0]
    return "normal" if prediction == 1 else "anomaly"


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect an unusual sensor reading.")
    parser.add_argument("--temperature", type=float, required=True)
    parser.add_argument("--pressure", type=float, required=True)
    args = parser.parse_args()
    print(f"Reading status: {classify_reading(args.temperature, args.pressure)}")


if __name__ == "__main__":
    main()
