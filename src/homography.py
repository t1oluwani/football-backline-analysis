"""Conversion from image coordinates to pitch coordinates.

Detects pitch-line keypoints in each frame, estimates a homography to a
top-down pitch model, and smooths or interpolates frames where estimation
fails (camera pan, zoom, occlusion). Projects each player's foot point into
pitch coordinates in meters.

Input:  frames and per-frame boxes from detect_track.py
Output: per-frame (x, y) pitch positions for players and the ball
"""