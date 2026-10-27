# Literature Review: Defensive Positioning Features

## Positioning Statement

My project (**Diagnosis Goals in Soccer: Breakdown vs Breakthrough**) will classify conceded goals as **breakdown** (a geometric/positional fault occurs within a window before the shot) or **breakthrough** (defense held shape). The literature below supplies the interpretable features and calculations I plan to use to operationalize "structural integrity" as measurable geometry, rather than subjective eye-test judgment.

---

## Core Sources & Features

### 1. Dash et al. (2025) — Back-Four Defense with Spatial Control
**Citation:** Dash, S., Ide, K., Umemoto, R., Amino, K., & Fujii, K. (2025). *Prediction-based evaluation of back-four defense with spatial control in soccer.* arXiv:2511.06191. [PDF](https://arxiv.org/pdf/2511.06191)

#### Core Idea
Introduces five interpretable spatio-temporal metrics to quantify back-four coordination during negative transitions, then uses them to predict defensive success in LaLiga 2023–24 (Barcelona vs. Real Madrid).

#### Positioning Statement (How This Anchors My Project)

1. **Label lineage:** I can treat my breakdown/breakthrough labels as the single-goal, geometric analogue of their success/failure transition labels—both are operational, not causal.
2. **Feature reuse with modification:** I plan to adopt their line height, relative line height, compactness, and pressure-radius concepts but convert them from **sequence means to per-frame, threshold-triggered faults** with duration conditions (e.g., "> 1 s").
3. **Fault taxonomy validation:** Each of my Table 1 faults (line gap, lagging defender, delayed shift, numerical deficit, unpressured ball) has a measurable counterpart in their feature set—I can use this for construct validity.
4. **Threshold tunability:** Their team-specific findings (Barcelona systematic vs. Real Madrid adaptive) justify my "all thresholds tunable" design.
5. **Single-goal niche:** They evaluate transitions, not individual conceded goals; I plan to fill the **single-goal diagnostic** gap they leave open.
6. **Aggregation gap:** They explicitly list mean-aggregation as a limitation (sacrifices temporal granularity)—I plan to address exactly this with per-frame fault detection.

#### Interpretable Features & Calculations (Reference)

##### 1. Stretch Index — compactness + threat exposure
$$\mathrm{StretchIndex}_t = \lambda \cdot \mathrm{ConvexHullArea}(\mathrm{Defenders}_t) + (1-\lambda)\cdot \mathrm{PA}_t, \quad \lambda = 0.5$$

- $\mathrm{PA}_t$ = mean shortest distance from each of the top-3 attackers to nearest back-four defender.
- Lower = tighter, better-coordinated line.
- **My use:** I can use convex hull area as a natural per-frame proxy for "large gaps"; it complements my discrete line-gap fault.

##### 2. Pressure Index — close marking intensity
$$\mathrm{PressureIndex}_t = \sum_{a \in \mathrm{Attackers}_t} \mathbb{I}\left(\min_{d \in \mathrm{Defenders}_t} \|a - d\| < r\right), \quad r = 3\,\mathrm{m}$$

- Range 0–3; higher = tighter marking.
- **My use:** This validates the "defensive radius" concept in my Figure 2 and directly informs my **Unpressured ball** fault (no defender within *r* for τp s). I plan to use their static radius as a starting point for my speed/direction-based extension.

##### 3. Space Score — zone-weighted spatial dominance
$$\mathrm{SpaceScore}_t = \sum_{z \in Z} w_z \cdot \frac{D_z(t) - A_z(t)}{D_z(t) + A_z(t) + \epsilon}, \quad \epsilon = 1$$

| Zone | Weight $w_z$ |
|---|---|
| Central Final Third | 0.35 |
| Penalty Box Proximity | 0.30 |
| Wing Pockets | 0.20 |
| Ball-Carrier Radius (5 m) | 0.15 |

- **My use:** This is complementary rather than directly reusable—my faults are line-based. I can borrow the 5 m ball-carrier zone concept, which is adjacent to my unpressured-ball rule.

##### 4. Absolute Line Height
$$L_t = \frac{1}{4}\sum_{i \in D_t} x_{i,t}$$

- Mean x-coordinate of four deepest defenders; higher = more advanced line.
- **My use:** This is directly my **line height** metric. I plan to fix the coordinate convention (x from own goal line) before thresholding.

##### 5. Relative Line Height — ball coordination
$$R_t = x_t^{\mathrm{ball}} - L_t$$

- $R_t \approx 0$: line tracking ball; positive = deeper relative to ball.
- **Strongest predictor of defensive success** (Bonferroni p < .001, both teams).
- **My use:** This is a key candidate for my **"Delayed shift" / "lagging defender"** faults—I plan to use a per-frame lateral analogue with a duration condition.

---

### 2. Bischofberger et al. (2026) — Blame is Easier than Praise
**Citation:** Bischofberger, J., Ma, R., Bauer, P., Armsmeyer, K., & Baca, A. (2026). *Blame is easier than praise: Measuring off-ball defensive performance in football.* arXiv:2606.19931. [PDF](https://arxiv.org/pdf/2606.19931)

#### Core Idea
Attributes defensive responsibility for opponent passes using Defensive Pressure Areas (DPAs) and role-conditioned baselines. Key finding: **fault/blame metrics outperform contribution metrics**—defending is fundamentally about preventing mistakes.

#### Positioning Statement (How This Anchors My Project)

1. **Fault-first framing:** Their empirical finding that blame/fault metrics are more valid and robust than credit metrics directly supports my **breakdown (fault-detection)** classification over credit-based approaches.
2. **Defensive radius default:** I plan to use their DPA radius of **r = 5 m** as a principled starting value for my defensive radius and **Unpressured ball** threshold.
3. **Proximity weighting:** I can use the raw proximity formula as a continuous alternative to binary involvement—useful for severity scoring of faults.
4. **Aggregation guidance:** Per-90 aggregation is best for fault metrics; I can use this to justify scoring faults on a per-match/sequence basis in my pipeline.
5. **Single-goal niche:** They evaluate player-level season aggregates, not individual goals—I plan to fill this per-goal diagnostic gap.

#### Interpretable Features & Calculations (Reference)

| Feature | Calculation | My Use |
|---|---|---|
| DPA radius | Circle r = **5 m** around passer/receiver + pass-lane rectangle | Default **defensive radius**; **Unpressured ball** (r) |
| Raw proximity | $R_{p,i} = \frac{r - d_i}{r}$ (d_i = distance to DPA edge) | Proximity weighting |
| Goal-side logic | Defender positioned between ball and goal | **Numerical deficit** |
| Fused metric | $\frac{C_{total}}{\text{passes faced}}\times 250 - \frac{F_{total}}{\text{min played}}\times 90$ | Template for combining fault signals |
| Aggregation | Per-90 for fault metrics; per-pass for contribution | Justifies per-90 fault scoring |

---

## Feature → Fault Mapping (Table 1 Reference)

| Fault | Source(s) | Calculation |
|---|---|---|
| **Line gap** (τg) | Dash | Max adjacent-defender gap > τg |
| **Lagging defender** (τl) | Dash | Depth deviation from line median > τl |
| **Delayed shift** (τs, >1 s) | Dash | Line-center lateral offset vs. ball > τs for >1 s |
| **Numerical deficit** (τn) | Dash, Bischofberger | Count goal-side defenders < τn |
| **Unpressured ball** (r, τp) | Bischofberger, Dash | No defender within r of ball for τp seconds |

## Defensive Radius — Options
1. **Fixed** r ≈ 5 m (Bischofberger DPA default).
2. **Speed/direction-based** reachable area (Dash).
3. **Prediction-based** control probability (Dash).

## Reference Defaults (tunable)
- Pressure radius: **r ≈ 5 m**
- Close-marking radius: **r = 3 m** (Dash Pressure Index)
- Fault window: final **T seconds** before shot
- Delayed-shift persistence: **>1 s**