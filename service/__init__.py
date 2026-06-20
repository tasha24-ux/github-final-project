import os
import logging
from flask import Flask
from flask_talisman import Talisman

# Initialize the Flask Core Application
app = Flask(__name__)

# Configure Talisman with Content Security Policy (CSP) headers
# This forces HTTPS and sets secure browser headers to mitigate injection vulnerabilities
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': '\'self\'',
        'object-src': '\'none\''
    },
    force_https=False  # Keep False for local development testing; True for cloud production environments
)

# Set up simple logging formatting
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Service initialized with secure Talisman configurations.")

# Import application routes to bind them to the app context
# (Assuming your route logic is defined in service/routes.py)
# from service import routes
