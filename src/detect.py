"""Player and ball detection, tracking, and team assignment.

Runs YOLO11 on each frame to find players and the ball, uses (tbd) to keep
a consistent ID per player across frames, and clusters jersey colors to assign
each player to a team. Saves a table of per-frame boxes with track ID and team
so later steps can be rerun without repeating this step.

Input:  video clip
Output: per-frame boxes with track_id and team
"""