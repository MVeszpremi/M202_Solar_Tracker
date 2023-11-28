# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

The proposed project aims to improve solar panel efficiency and longevity by implementing a novel dual-axis, image-based sun tracking system. A mechanical gimal is utilized to dynamically adjust solar panels' orientation, optimizing the angle of incoming solar radiation. The core innovation is the use of an  upward-facing camera for continuous sky condition monitoring, enabling precise alignment with the sun and vertical repositioning during extreme weather to minimize wear.

Our apporach improved on the traditional solar tracking methods that suffer from energy inefficiencies due to constant rotational adjustments and the use of outdated analog sensors for weather prediction. This project addresses these shortcomings by employing advanced computer vision algorithms for accurate sun positioning and cloud detection, drastically improving energy capture efficiency and operational effectiveness.

Success metrics include image-based tracking accuracy, angular error rate, response time, efficiency gains, algorithm optimization, environmental robustness, system reliability, and code stability. The project plan encompasses objective definition, design and engineering, prototyping, algorithm development, software creation, testing, and documentation.

# 1. Introduction

Our team is pioneering a camera-based solar tracking system aimed at boosting the effectiveness of solar panel farms and safeguarding them against adverse weather conditions.

Traditional systems rely on analog sensors, which not only limit the scope of sensing but are also costlier. These conventional sensors often cause unnecessary oscillations in the tracking mechanism, leading to energy losses.

Our innovative approach utilizes camera technology to precisely detect cloud positions and estimate the optimal angle for solar panels, thus eliminating the need for superfluous movements. This method is more efficient as it directly identifies the best orientation without resorting to trial-and-error adjustments.

The significance of this project extends beyond immediate efficiency gains; it has the potential to revolutionize the solar energy sector. By enhancing performance and reducing long-term maintenance costs associated with weather-related damage, our system could accelerate the adoption of solar technology, contributing to a more sustainable and greener planet.

However, the project does present challenges. Determining the most effective angle from the camera images, accurately assessing cloud thickness, and identifying cloud cover are complex tasks that we are striving to solve.



This section should cover the following items:

* Motivation & Objective: What are you trying to do and why? (plain English without jargon)
* State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
* Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
* Challenges: What are the challenges and risks?
* Requirements for Success: What skills and resources are necessary to perform the project?
* Metrics of Success: What are metrics by which you would check for success?

# 2. Related Work

# 3. Technical Approach

Mechanical System

The solar panel positioning system was engineered to automatically align with the sun. It incorporates two Nema 17 Stepper motors, each equipped with a 26:1 gearbox, to ensure precise rotation speed and strong holding torque. At the start of operation, Hall effect sensors (AH3572-SA-7) on each axis are employed for accurate calibration of position. The system's 2-axis tracker, or gimbal, is elevated using slender legs, designed to reduce impact on the ground, and it boasts a sturdy construction with several bearings on each axis.

For mounting the solar panel, the gimbal utilizes six M5 screws. Additionally, a fisheye lens camera is affixed to the side of the solar panel, enabling it to capture wide-angle images of the sky.

Software Technologies


On Device Processing



  Cloud Data



# 4. Evaluation and Results

Power Data Collection


# 5. Discussion and Conclusions

# 6. References
