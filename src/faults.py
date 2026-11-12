"""Fault rules and goal labeling.

Applies the thresholds from configs/thresholds.yaml to the metrics over the
critical window (the final T seconds before the shot). Checks each structural
fault (line gap, lagging defender, delayed shift, numerical deficit, unpressured
ball) and labels the goal as a breakdown goal if at least one fault holds, or a
breakthrough goal otherwise. The labels are operational definitions: they
describe measured geometry, not the true cause of the goal.

Input:  per-frame features and config thresholds
Output: list of triggered faults and the final label
"""