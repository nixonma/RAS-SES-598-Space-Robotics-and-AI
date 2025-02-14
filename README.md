Demo code and assignments for RAS-598 Space Robotics and AI will be posted here. 

Course website: https://deepgis.org/dreamslab/ses598/

# Assignment 1
## Controller Parameters
- Kp_linear = 10.5
- Kd_linear = 0.1
- Kp_angular = 5.5
- Kd_angular = 0.21
- spacing = 1.1
## Tuning Methodology  
I started with the parameters that were demonstrated in class (10, 0.1, 5.0, 0.1) which gave a decent cross-track error. From there I began tuning each parameter either up or down to see if it had a positive or negative impact on the overall performance. The initial parameters generated:
![10-p1-5-p17](https://github.com/user-attachments/assets/1060a106-92d1-4cc3-b01b-59ed3ac1f1be)
and a cross-track error of about .28  

From here I found that overadjusting any paramater up or down direction led to either an overlapping pattern (where the robot creates a loop of sorts) or wide zig-zags that fail to cover much of the total area. Thus I started adjusting in about .1 increments until two values gave similar results. Next I split the difference of the two values, incrementing in .05 until either no change was found or a more optimal result. I eventually landed on the above parameters, which gave an initial cross-track error of .226, and generated:

![final-tuning](https://github.com/user-attachments/assets/942833aa-f97b-4530-be79-b7fd4fbc8303)

While the y position was a little more rough than the initial design, I find that the x position is much smoother and more consistent than the original, while not creating egregious problems in the y value.

## Challenges and Solutions  
- The first challenge here was in setup, I felt as though I installed all of the environment set-up correctly, but much troubleshooting was required to even get the assignment to run properly.  
- The next challenge was understanding what the difference between what I *thought* the parameters did and what they *actually* did. This just took some alterations of the parameters to figure out, but was nonetheless an issue to begin with.
- Ideally I'd like to have found a manner to smooth both of the x and y curves out more, but I was unable to find a set of paramaters that generated smooth curves for both values at the same time. Thus this middle ground is what I have landed upon.


# Assignment 2

## Baseline Paramaters
- x = 1.0
- x_dot = 1.0
- theta = 10.0
- theta_dot = 10.0
- r = 0.1

## Baseline Performance
The base Paramaters do a decent job of keeping the pole balanced, however the amplitude of the cart drift increases until one of the edges of the track is collided with, at which point the pole falls and the state becomes unrecoverable. The limiting factor seems to be that the drift of the cart is not penalized enough for the algorithm to keep the cart centered as it drifts.

## Tuning the Parameters
I was unable to get rq_plot to display meaningful results for proper analysis here[1], so most of the optimization was repeatedly running the sim and seeing how long the cart could balance the pole.

### Idea 1
Initially, My thought was that the penalty should be high for deviations in theta and theta_dot as we want the pole to be upright, and then smaller penaties for x, and a further smaller penalty for x_dot. This followed from my idea that if I was trying to balance this pole, I am okay with moving my arm quickly to correct the movement, but I really want the pole to stay upright so the penalties for this should be higher. Penalies here came out to:
- x = 1.0
- x_dot = 0.5
- theta = 20.0
- theta_dot = 10.0
- r = 0.1
This sort of worked. The pole was balanced for a good bit longer, but the cart started to deviate more and more from the original position until it collided with a barrier. This comes around because the cart was incurring too high a penalty for the change in theta, and to compensate, it was moving more. However, the cart was still doing a good job with keeping the pole balanced at the beginning.

### Idea 2
The second direction I decided on was to penalize the movement in x until I could get the cart to drop the pole without colliding with a barrier, just to see what the extemes looked like for the parameters, but I wanted to increase incrementally in case I stumbled upon a good solution on the way. I didn't really care about the x_dot or theta_dot, as long as we keep the pole balanced, and mostly centered, the speed isn't super relevant [2]. Thus I kept the penalty for x_dot and theta_dot low-ish, and ramped up the penalty for x. This resulted in the parameters:
- x = 10.0
- x_dot = 0.5
- theta = 20.0
- theta_dot = 10.0
- r = 0.1
This was okay for about 2 trials, before I realized that if I also kept the penalty for theta high, I could keep the system balanced. This occured as a rather obvious idea, an I'm not sure how it wasn't intuative from the directions/assignment goal, but if we want to balance the cart in the center, the corresponding penalties for these should be high (duh). Thus I ramped up both the x and theta penalties while keeping the _dot penalites lower, until I arrived at my final parameters.

[1](I'm not sure what I was doing wrong, but I could not publish statistics or get useful ones in the visualization, if you have/know of a tutorial that would be much appreciated)

[2]: in the case that this were a physical system, these factors would likely be the limiting ones, as you can only get the cart moving at a certain speed, and faster means higher energy consumption

## Final Parameters
- x = 20.0
- x_dot = 3.0
- theta = 60.0
- theta_dot = 5.0
- r = 0.1

## Final Performance
This set of parameters, while likely the most energy-expensive parameters, has managed to keep the pole balanced long enough for me to write this report. This makes it the longest lasting control yet, and the best at adhering to the goals of staying within the boundaries and having the pole upright, just better hope the physical design of the system can output the kind of energy needed to keep this going.


## Challenges and Solutions  
- The first challenge here was in setup again, the state of the VM was not correctly saved after the last assignment, resulting in me needing to re-install jazzy and python, and re-clone the repository. None of this was difficult per se but it was about an hour ish of my time. I believe it was because one of the drives from the original VM was not reloaded properly, but I didn't care to figure it out, just wanted to get the assignment running.
- The next challenge was reading comprehension. As mentioned above, it took me a couple of itterations of trial and error (even when I knew what the paramaters did from the jump) to realize that we should penalize for the factors we care about and are listed as goals in the assignment. Not sure how I didn't think of this sooner, but apparently I'm just editing code with my brain off.
- The last problem I ran into as I mentioned in [1] was I could not get the statistics I wanted out of the sim in a manner that allowed me to compare nicely.
