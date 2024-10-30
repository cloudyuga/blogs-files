from flask import Flask
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
import os
app = Flask(__name__)
APPLICATIONINSIGHTS_CONNECTION_STRING="<your_connection_string>"
# Set up logging with Application Insights
app.logger.addHandler(AzureLogHandler(connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING))
logging.basicConfig(level=logging.DEBUG)
@app.route('/')
def hello():
    app.logger.info("Hello World endpoint was accessed")
    return "Hello, World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
