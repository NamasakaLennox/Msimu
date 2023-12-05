#!/usr/bin/bash
pip3 install --extra-index-url https://pypi.nvidia.com tensorrt-bindings==8.6.1 tensorrt-libs==8.6.1 --break-system-packages
pip3 install -U tensorflow[and-cuda] --break-system-packages
# Verify the installation:
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
