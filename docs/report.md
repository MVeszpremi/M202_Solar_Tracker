<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

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

**Mechanical System**

The solar panel positioning system was engineered to automatically align with the sun. It incorporates two Nema 17 Stepper motors, each equipped with a 26:1 gearbox, to ensure precise rotation speed and strong holding torque. At the start of operation, Hall effect sensors (AH3572-SA-7) on each axis are employed for accurate calibration of position. The system's 2-axis tracker, or gimbal, is elevated using slender legs, designed to reduce impact on the ground, and it boasts a sturdy construction with several bearings on each axis.

For mounting the solar panel, the gimbal utilizes six M5 screws. Additionally, a fisheye lens camera is affixed to the side of the solar panel, enabling it to capture wide-angle images of the sky.

**Software Technologies**

We capture and process images every 10 seconds to identify the centroids of the three largest clouds detected. Concurrently, we track the sun's position, which is continuously mapped onto a spherical coordinate system. Utilizing geometric calculations, we determine the optimal pitch and yaw angles for our solar panel, considering both the sun's position and the panel's mechanical constraints. This process is visually represented in a plot below, and the equations used to calculate the yaw and pitch angles are also detailed.

$$
\text{pitch} = \frac{\pi}{2} - \arctan\left(\frac{\text{sun direction}[2]}{\text{sun direction}[1]}\right)
$$

$$
\text{if } (\text{sun direction}[1] > 0): \quad \text{pitch} = \text{pitch} \times -1
$$

$$
\text{pitch} = \text{clamp}\left(\text{pitch}, -27.5 \times \frac{\pi}{180}, 27.5 \times \frac{\pi}{180}\right)
$$

$$
\text{rot x} = \begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\text{pitch}) & -\sin(\text{pitch}) \\
0 & \sin(\text{pitch}) & \cos(\text{pitch})
\end{bmatrix}
$$

$$
\text{yaw} = \arctan2(\text{sun direction pitch rotated}[0], \text{sun direction pitch rotated}[2])
$$

$$
\text{yaw} = \text{clamp}\left(\text{yaw}, -60.0 \times \frac{\pi}{180}, 27.5 \times \frac{\pi}{180}\right)
$$

$$
\text{self.rot x} = \text{yaw} \times \frac{180}{\pi}
$$

$$
\text{self.rot y} = \text{pitch} \times \frac{180}{\pi}
$$

$$
\text{rot y} = \begin{bmatrix}
\cos(\text{yaw}) & 0 & \sin(\text{yaw}) \\
0 & 1 & 0 \\
-\sin(\text{yaw}) & 0 & \cos(\text{yaw})
\end{bmatrix}
$$

$$
\text{rectangle} = \text{rectangle} \cdot \text{rot x}^T \cdot \text{rot y}^T
$$


After computing these angles, we account for any deviations caused by the panel's mechanical limits, referred to as the 'error' offset. Ideally, our panel would directly face the sun under clear skies, but mechanical limitations sometimes prevent this. To accurately locate the sun in the camera image, we calculate the error in the pitch and yaw angles. These calculations are presented below.

Pitch Error:

$$
\text{pitch error} = \arccos\left( \frac{\text{normal} \cdot \text{direction}}{\|\text{normal}\| \cdot \|\text{direction}\|} \right)
$$

where

$$
\text{normal} = \frac{\text{np.cross}(v1, v2)}{\|\text{np.cross}(v1, v2)\|} \quad \text{and} \quad \text{direction} = \frac{\text{point} - \text{rectangle}[0]}{\|\text{point} - \text{rectangle}[0]\|}
$$

Yaw Error:

$$
\text{yaw error} = \pm \arccos\left( \frac{\text{normal xy} \cdot \text{direction xy}}{\|\text{normal xy}\| \cdot \|\text{direction xy}\|} \right)
$$

where

$$
\text{normal xy} = \frac{[\text{normal}[0], \text{normal}[1], 0]}{\|[\text{normal}[0], \text{normal}[1], 0]\|} \quad \text{and} \quad \text{direction xy} = \frac{[\text{direction}[0], \text{direction}[1], 0]}{\|[\text{direction}[0], \text{direction}[1], 0]\|}
$$

The sign of yaw error is determined by the Z component of

$$ 
\text{np.cross}(\text{normal xy}, \text{direction xy})
$$


Subsequently, we pinpoint the sun's position on the camera image. This is achieved by referring to the degree matrix generated during camera calibration (see Appendix 1.1 Camera Calibration). We iteratively search this matrix to find the closest yaw and pitch angles. The corresponding matrix entry (i,j) is then used to accurately locate the sun within the camera's field of view.

Once the sun's position is pinpointed, we compare the cloud centroids to assess cloud cover. This analysis is conducted using various methods, which are outlined as follows:
1.
2.
3.
...


**On Device Processing**


**Cloud Data**

For the creation of an advanced weather monitoring system, we initially utilized a semantic segmentation technique using YOLOv8 to record and analyze cloud imagery. The YOLOv8 model, renowned for its advanced deep learning architecture, has exhibited remarkable proficiency in various image identification fields. Nevertheless, while implementing it in real-world scenarios, we faced substantial obstacles in terms of performance and efficiency of recognition. Deep learning models, although highly capable, can require significant computer resources. This requirement resulted in a significant reduction in processing speed and a decline in overall system efficiency.

In light of these technical obstacles, our team decided to pursue a different strategy, shifting towards a technique based on OpenCV for the purpose of identifying and analyzing clouds. The main reason for this strategic change was the inherent efficiency and lightweight nature of OpenCV's image processing capabilities. Unlike deep learning approaches, OpenCV provides faster processing speed while requiring fewer computational resources. Our system has the capability to process photos in real-time while maintaining a high level of accuracy, which is a significant advantage.



To address these requirements, we carefully devised and executed the CloudSegmentation class. The purpose of this class is crucial in our weather monitoring system, specifically in gathering and analyzing cloud photos using a camera. The capture_image method efficiently retrieves real-time photos from the camera. Subsequently, the class enhances the processing efficiency of these photos by reducing their dimensions and subsequently saves them for further study.



The CloudSegmentation class utilizes the create_cloud_mask function specifically for the purpose of cloud detection and analysis. This technique converts the collected pictures into grayscale and using a binary threshold to differentiate clouds from the sky. In order to improve the accuracy of the produced mask, the method also includes morphological processes.



In addition, the processForClouds function of the class enhances the analysis by manipulating the collected photos to generate cloud masks and outlining hexagons around the clouds. This procedure is essential for precisely determining and examining the positions of clouds. The find_closest method of the class calculates the closest point to a specified angular error, which is a crucial operation for accurately determining the precise location of clouds.



The draw_hexagon_around_clouds function of the CloudSegmentation class visually represents the form and position of clouds by creating polygons around identified clouds. This capability is essential for monitoring and evaluating the movements and alterations of clouds.



To summarize, the CloudSegmentation class includes a release method for releasing camera resources and a setErrAngle method for changing the acquired picture angles depending on angular faults. The CloudSegmentation class is a crucial part of our weather monitoring system, providing strong support for cloud identification and analysis with its efficient and effective image processing algorithms.


**Weather Dectection**

The genesis of this project was the conceptualization of a mechanism to position solar panels vertically during unexpected hailstorms and other extreme weather events. This would help mitigate potential financial losses caused by significant property damage. This program goes beyond just protecting assets and demonstrates a wider commitment to innovation.

To achieve this goal, we utilized the OpenWeatherMap API to gather weather data, specifically targeting the identification of circumstances that align with established severe weather parameters. To address the inherent limitations in the accuracy of weather forecasts, a camera system was added to provide an extra layer of verification. Importantly, the camera used was not a typical one, but rather a fisheye version known for its wide field of view, which allowed for thorough sky imaging.

The utilization of a fisheye camera played a crucial role in obtaining a wide-ranging and comprehensive dataset that was essential for training and validating the SVM classifier. A total of around 400 photos were collected, creating a strong basis for the system's prediction precision. The camera's wide field of view was crucial, as it captured large portions of the sky, enabling a comprehensive investigation of different meteorological components. The thorough analysis of the sky's image was crucial for the identification of its characteristics, including brightness, saturation, contrast, and color histograms. This ensured a realistic representation of the vast and varied sky.

The subsequent picture processing entailed utilizing a sequence of advanced analyzers, such as BrightnessAnalyzer, SaturationAnalyzer, ContrastAnalyzer, and ColorHistogramAnalyzer. Each of these analyzers had a vital function in extracting precise image properties, which were then inputted into the SVM classifier. The comprehensive method of combining features greatly improved the classifier's capacity to accurately distinguish between sunny and non-sunny circumstances.

The WeatherPredictor class, which incorporates this sophisticated classifier, exhibited exceptional effectiveness in predicting real-time weather. The device's capacity to understand and analyze images captured by the fisheye camera and provide instant weather forecasts enhances its usefulness in meteorology, environmental monitoring, and integration with smart home systems.

In conclusion, the combination of the fisheye camera and advanced machine learning techniques in this weather forecast system highlights a seamless integration of hardware capabilities and software expertise. The system's ability to provide precise weather forecasts, based on a diverse and extensive dataset, demonstrates the significant impact of machine learning in real-world situations, especially in environmental analysis and meteorological research. Moreover, by utilizing the camera as the main method of verification, the prediction outputs are made more reliable and precise, taking into account the potential flaws of weather forecasts.

# 4. Evaluation and Results

System Solar Tracking Timelapse:

<video width="320" height="240" controls>
  <source src="https://github.com/MVeszpremi/M202_Solar_Tracker/assets/102561670/e725a0c8-c1f7-4c2e-83fb-e54552dda78a" type="video/mp4">
  Your browser does not support the video tag.
</video>

From the camera perspective:

<video width="320" height="240" controls>
  <source src="https://github.com/MVeszpremi/M202_Solar_Tracker/assets/102561670/75688c7c-75bd-4c7a-a383-a41ac750f8b1" type="video/mp4">
  Your browser does not support the video tag.
</video>

Power Comparison:

We noticed about a 6% increase in power when we were tracking the position of the sun.

![tracking_processeed](https://github.com/MVeszpremi/M202_Solar_Tracker/assets/102561670/109947f1-69ac-4870-b4d3-ac40fd031277)


# 5. Discussion and Conclusions

# 6. References

# 7. Appendix

![alt text](https://github.com/MVeszpremi/M202_Solar_Tracker/blob/main/docs/media/calib_matrix.png?raw=true)

_Figure 1.1 Fisheye Lens Calibration Visualization_
