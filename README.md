# Sensor Anomaly Detector

A small educational AI project that detects unusual sensor readings using an Isolation Forest model.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python anomaly_detector.py --temperature 22 --pressure 101
python anomaly_detector.py --temperature 80 --pressure 140
```

## Test

```bash
python -m unittest test_anomaly_detector.py
```

The normal sensor data is synthetic and included in the source for a self-contained learning example.
