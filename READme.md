# defensive-breakdown-detector

Given a short clip of the build-up to a goal, the system recovers player positions on the pitch, overlays defensive radii and inter-defender lines on the video, and flags whether the goal was a breakthrough goal or the defense showed a structural breakdown (formational and positional faults only; one-on-one defending is excluded).

> **Status:** work in progress (master's semester project, Simon Fraser University (CMPT 742)).

## Labels (operational definitions)

- **Breakdown goal:** at least one structural fault (see below) holds in the critical window before the shot.
- **Breakthrough goal:** the goal was scored with no structural fault detected.

These labels describe measured geometry only. They are not claims about the true cause of the goal or the quality of either team. All thresholds are tunable parameters.

## Tech stack

- Python
- PyTorch
- YOLO11 (player and ball detection)
- BoT-SORT (multi-object tracking)
- OpenCV (homography, overlays)
- NumPy (geometric metrics)

## Data

| Source | Use |
|---|---|
| [Football Matches Tactical Cam (YouTube playlist)](https://www.youtube.com/playlist?list=PL29faCH1zKViiz6tMwTwvZy43Fgow5RIA) | Tactical-camera views of goals, used as input clips |

Video and large data files are **not** stored in this repo (see `.gitignore`).

## Pipeline

1. **Input:** a 10-15 s clip ending at the shot.
2. **Detection:** ...
3. **Tracking:** ...
4. **Pitch coordinates:** ...
5. **Metrics:** ...
6. **Fault rules:** ...
7. **Output:** ...

### Triggering faults

| Fault | Condition (team-level geometry) | Initial value |
|---|---|---|
| Line gap | Gap between adjacent back-line defenders exceeds a threshold | 15 m |
| Lagging defender | A defender is out of line depth by more than a threshold | 5 m |
| Delayed shift | Line center lags the ball laterally for over 1 s | 8 m |
| Numerical deficit | Too few defenders goal-side of the ball | 3 |
| Unpressured ball | No defender within a radius of the ball for a set time | 5 m, 1.5 s |

Initial values are starting points to be tuned.

## Repo structure (suggested)

```
defensive-breakdown-detector/
├── data/            # not tracked; see Data section
├── src/
│   ├── detect_track.py
│   ├── homography.py
│   ├── metrics.py
│   ├── faults.py
│   └── overlay.py
├── configs/         # thresholds as parameters
├── notebooks/
├── outputs/
├── requirements.txt
└── README.md
```

## Setup and usage (stub)

```bash
# TODO
pip install -r requirements.txt
python src/run.py --clip path/to/clip.mp4
```

## Evaluation

...

## Limitations

...

## References

- [Football Matches Tactical Cam](https://www.youtube.com/playlist?list=PL29faCH1zKViiz6tMwTwvZy43Fgow5RIA) (YouTube playlist) for tactical-camera clips.
