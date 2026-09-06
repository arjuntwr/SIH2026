"""
Netlify Functions ASGI Entrypoint for Bhumi-Niti (भूमि-नीति)
Adapts FastAPI ASGI app to AWS Lambda / Netlify Serverless runtime via Mangum.
"""

from mangum import Mangum
from main import app

# Serverless handler for Netlify Functions
handler = Mangum(app, lifespan="off")
