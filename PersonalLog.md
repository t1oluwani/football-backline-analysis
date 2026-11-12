# Personal Log:
*Last Entry:* 2026-11-11

## Milestone Presentation Feedback

- **Reduce scope, but define the solution more clearly**
  - Better: a smaller scope with a well-defined solution
  - Worse: a large scope with loose, vague definitions
- **"Defense" needs a precise definition**
  - Defenders aren't the only ones involved in defending
  - Need to decide which of these I'm actually analyzing:
    - the defender players only
    - all players who are defending (any position)
    - the whole pitch (team-wide defensive shape)
  - Then define everything else (metrics, outputs, evaluation) accordingly
- **Don't be too attached to the current plan/methods**
  - Need to try things, prototype, and adapt/adjust based on what happens
- **The homography is the real weight of this project**
  - Camera perspective → field perspective mapping is the core technical challenge
  - Most of the effort should go here

#### <u>Main Takeaways</u>

  - Lock down the definition of "defense" (defenders / defending players / whole pitch) before building more
  - Narrow the scope and write the solution up concretely
  - Stay flexible: adjust the method based on what the prototype shows

## Homography 

#### <u>Original Approach</u>

- Initially discussed with the prof: use the **lawn (mowing) stripes** to compute the camera → field homography
- Prototyped on ~10 videos, deliberately varied:
  - horizontal vs. vertical angles (bench-to-bench vs. post-to-post)
  - different ranges: some cover the whole field, others only half
  - panning cameras

#### <u>Lawn Stripes Aren't Gon Work :C</u>

- **Stripe count and width differ from field to field**
  - roughly 9–12 m wide, from my research
  - no consistent number of stripes to rely on
  - sometimes strips are horizontal, sometimes their vertical
  - especially a problem because my data is so varied in angle and range
- **Stripes are identical to each other, with no numbering**
  - unless the whole field is visible at once, there's no way to tell which stripe is which
  - e.g. if I see 7 stripes, I can't know which one is the leftmost/rightmost → uninterpretable
- **Panning makes it a no-go**
  - stripes would only work if the whole field were visible all the time
  - that isn't the case with panning cameras

#### <u>New Approach</u>

- **Use the white paint pitch markings instead of lawn stripes**
  - should be able to achieve a similar result
  - markings are distinguishable and have meaning (unlike identical stripes)
- **Use ratios instead of absolute coordinates**
  - originally: compute coordinates from a fixed field size
  - problem: field size isn't as consistent between games as I thought
  - now: infer ratios from the white pitch markings themselves

### Raw Notes (Thoughts)
- some of the angles might be impossible, especially the cameras behind the nets, the goals at the other end in very compressed, im curios to see how the model will behave or interpret stuff like that
- going to increase rec video clip from 15s to 20s or maybe 25s some of these goals require larger contexted for proper analysis, this is just a thought atm