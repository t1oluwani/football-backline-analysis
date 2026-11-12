"""Entry point for the defensive backline analysis.

Runs the full pipeline on a clip: 
detection and tracking, pitch coordinates, metrics, fault rules, and overlay. 
Reads thresholds from configs/config.yaml and writes all results to outputs/.

Usage:
    python -m src.run --clip data/input/clip1.mp4
"""