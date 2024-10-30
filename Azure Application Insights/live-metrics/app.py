from flask import Flask
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import psutil
import time

# Configure Azure Monitor for OpenTelemetry with live metrics enabled
configure_azure_monitor(
    connection_string="<your_connection_string>",
    enable_live_metrics=True
)

# Initialize Flask application
app = Flask(__name__)

# Instrument Flask app to capture incoming requests and outgoing HTTP calls
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route('/')
def hello():
    return "Hello, World!"

# Example endpoint to simulate CPU load
@app.route('/cpu')
def cpu_load():
    # Simulate CPU load by performing a calculation
    start_time = time.time()
    [x**2 for x in range(1000000)]
    end_time = time.time()
    return f"CPU intensive task completed in {end_time - start_time} seconds"

# Example endpoint to track memory usage
@app.route('/memory')
def memory_usage():
    # Get the current process memory usage
    memory_info = psutil.Process().memory_info()
    return f"Memory usage: {memory_info.rss / (1024 * 1024)} MB"

if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(host='0.0.0.0', port=5000)

