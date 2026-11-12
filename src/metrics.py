"""Defensive geometry metrics computed from pitch coordinates.

Pure geometry:
defensive radius per defender, gaps between neighboring back-line defenders, line height 
relative to the ball, compactness, and the number of defenders goal-side of the ball.
Works on positions from either the video pipeline or open tracking data
(e.g., tbd), so it can be tested independently of video noise.

Input:  per-frame pitch positions with team labels
Output: per-frame feature values
"""