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
