# Timeline

> **CURRENTLY: Oct 25, end of Week 3 (~27% through).**
> Should have: setup done, clips chosen, detection and tracking started, rough homography on one clip. Metrics start ~Oct 28.

## Milestones

| Week | Dates | Milestone | PR branch |
|---|---|---|---|
| 1-2 | Oct 8-21 | Setup, literature review, clips chosen | `pipeline/setup` |
| 3-4 | Oct 22-Nov 4 | Video to pitch coordinates | `pipeline/video-to-positions` |
| 4-5 | Oct 29-Nov 11 | Metrics and overlay | `pipeline/metrics-overlay` |
| 5-6 | Nov 5-18 | Fault rules and labeling | `pipeline/faults-labeling` |
| 6-7 | Nov 12-25 | Evaluation | `pipeline/evaluation` |
| 7-8 | Nov 19-Dec 2 | Report and demo | `pipeline/final` |

One PR per milestone, merged to `main` when the milestone's output exists.

## To-do

**Setup** 
- [x] Repo and environment working
- [x] Data access confirmed
- [ ] 5-10 goal clips chosen (IP)
- [ ] Literature review notes (IP)

**Video to positions** 
- [ ] Object detection (IP)
- [ ] Model fine-tuning
- [ ] Tracking
- [ ] Team assignment
- [ ] Homography
- [ ] *Output: one clip as `frame, id, team, x, y`*

**Metrics and overlay**
- [ ] Defensive radius and line metrics
- [ ] Overlay on video
- [ ] Same metrics on open tracking data (fallback)
- [ ] *Output: one annotated clip (main demo visual)*

**Faults and labeling**
- [ ] Fault rules and labels
- [ ] Hand-label validation set
- [ ] End-to-end run on all clips
- [ ] *Output: label and triggering faults per clip*

**Evaluation**
- [ ] Agreement with hand labels
- [ ] Threshold sensitivity
- [ ] Perception error
- [ ] *Output: results table*

**Final**
- [ ] Error analysis
- [ ] README and demo assets
- [ ] Report and slides
