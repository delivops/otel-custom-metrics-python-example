# otel-custom-metrics-python

This project is designed to demonstrate the setup and use of OpenTelemetry for monitoring custom metrics within a Python application.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Metrics](#metrics)
- [License](#license)

## Introduction

This project is designed to demonstrate the setup and use of OpenTelemetry for monitoring custom metrics within a Python application. It covers the implementation of different types of metrics, including counters, gauges, and histograms.

## Features

- **Custom Metric Collection**: Collect and export custom metrics using OpenTelemetry.
- **Counter Metric**: Tracks the number of occurrences of specific events.
- **Gauge Metric**: Monitors the real-time value of ongoing processes.
- **Histogram Metric**: Captures the distribution of observed values, such as task durations.
- **OTLP Exporter**: Sends collected metrics to an OTLP-compatible endpoint.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/delivops/otel-custom-metrics-python-example.git
   cd otel-custom-metrics-python-example

   ```

2. **Run the app:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python custom-metrics.py

```

The script will start collecting and exporting metrics based on the logic implemented.

3. **Deploy the app:**

```bash
kubectl apply -f deployment.yaml
```

Nice! now those metrics will appear in Groundcover.

## Metrics

#### Counter

- **Name**: `work_counter`
- **Description**: Counts the number of work items processed.
- **Dimensions**:
  - `work.type`: Type of work being done.
  - `work.level`: Level or priority of the work.

#### Gauge

- **Name**: `work_gauge`
- **Description**: Represents the current level of ongoing work.
- **Dimensions**:
  - Simulated value that fluctuates over time.

#### Histogram

- **Name**: `work_duration_histogram`
- **Description**: Records the duration of work items.
- **Dimensions**:
  - `work.type`: Type of work being done.
  - `work.level`: Level or priority of the work.

## License

MIT
