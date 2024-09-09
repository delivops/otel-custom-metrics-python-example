import time
import random
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import (
    PeriodicExportingMetricReader,
)

# Set up the OTLP Metric Exporter
otlp_exporter = OTLPMetricExporter(
    endpoint="http://groundcover-custom-metrics.groundcover.svc.cluster.local:8429/opentelemetry/api/v1/push",
)

# Set up the Metric Reader and Provider
metric_reader = PeriodicExportingMetricReader(otlp_exporter)
provider = MeterProvider(metric_readers=[metric_reader])

# Set the global default meter provider
metrics.set_meter_provider(provider)

meter = metrics.get_meter("my.meter.name")

# Create a Counter
work_counter = meter.create_counter(
    "work_counter",
    unit="1",
    description="Counts the amount of work done"
)

# Create a Histogram
work_duration_histogram = meter.create_histogram(
    "work_duration_histogram",
    unit="ms",
    description="Records the duration of work"
)

# Function to observe the current value for the gauge
def observe_gauge(options):
    current_value = random.random() * 100  # Simulating a fluctuating value
    print(f"Gauge value observed: {current_value}")
    return current_value

# Create a Gauge
work_gauge = meter.create_observable_gauge(
    "work_gauge",
    callbacks=[observe_gauge],
    unit="1",
    description="Represents the current level of ongoing work"
)

def do_work(work_item):
    # Increment the Counter
    work_counter.add(1, {
        "work.type": work_item.work_type,
        "work.level": work_item.work_level
    })
    
    # Simulate some work by sleeping for a random duration
    duration = random.uniform(0.1, 1.0)
    time.sleep(duration)
    
    # Record the duration in the Histogram
    work_duration_histogram.record(duration * 1000, {  # Convert to milliseconds
        "work.type": work_item.work_type,
        "work.level": work_item.work_level
    })
    
    print(f"Doing some work... Duration: {duration:.3f} seconds")

# Example usage
class WorkItem:
    def __init__(self, work_type, work_level):
        self.work_type = work_type
        self.work_level = work_level

# Create an example WorkItem and call do_work
example_work_item = WorkItem("example_type", "example_level")
while True:
    do_work(example_work_item)
    time.sleep(0.2)   
