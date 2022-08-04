#!/bin/bash

# This script is used to start hypercorn.
# Hypercorn is running with QUIC http/3 on port 4433. But also runs on port 8000 by default.

hypercorn api.main:app --quic-bind localhost:4433