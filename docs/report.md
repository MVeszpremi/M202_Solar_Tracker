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
## 2.a. Papers

**What is Solar Tracking?**

This paper provides a foundational base for beginning to understand solar tracking and the existing technologies. It gives a high level overview of GPS and liquid boiling systems currently in industry. This gave us an initial launch point for application, implementation, and optimization.

**Various Solar Tracking Technologies**

This paper describes how solar panels capture and distribute energy and how they currently utilize single and dual axis tracking systems. It also defines passive and active solar trackers and discusses the advantages of solar tracking and the bright future it entails. With this infomration, we were able to further detail our design and determine the use of an active, dual-axis tracker.

**Sky-Image-Based Solar Forecasting Using Deep Learning**

This study investigates different training strategies for solar forecasting models using ground-based sky images from various global datasets with diverse climate patterns. It compares the performance of local models trained individually on single datasets, global models trained on a fusion of multiple datasets, and knowledge transfer from pre-trained models to new datasets. The results show that local models work well in their respective locations with slight errors and provide a robust template for our project.

**Active Solar-Tracking Systems for Photovoltaic Technology & Implementation**

This journal discusses the significance of solar irradiation for photovoltaic (PV) systems and the benefits of solar tracking in maximizing energy generation. It highlights the limitations of current active sensor-tracking algorithms, including issues with cloudy weather, module positioning after nightfall, and protection from adverse weather conditions. It also suggests incorporating periodic movement and nearly horizontal positioning, offering improved system lifetime and storm damage prevention while maintaining high tracking accuracy which influenced our project design decisions.

**TrueCapture’s New Split Boost Mode**

This article gave us insight into the state-of-the-art in the solar industry. It describes the latest addition to TrueCapture Software known as the "Split Boost", a row-to-row feature designed to maximize energy gain for photovaltaic plants using split-cell solar modules. This innovation leverages the shade-tolerant nature of split-cell modules, adjusting the tracker rows to optimize irradiance on the top half of the modules, resulting in a boost in production, even on flat terrain, with preliminary data showing up to a 1% yield improvement compared to conventional backtracking for specific conditions.

**Solar Tracking Investment Review**

After learning about the technology, we were interested in the financial considerations of actually implementing that technology. This article provides an in depth investment review at the residential and commerical level. Although this project is not heavily concerned with finanical implications, as engineers and entrepreneurs, we wanted to take the time to understand all aspects of our project.

## 2.b. Datasets

Singapore Whole sky IMaging SEGmentation Database

Singapore Whole sky IMaging CATegories Database

## 2.c. Software

Pvlib is used as the Solar Positioning Algorithm (SPA) library

OpenCV is used for general image processing and cloud segmentation

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

The WeatherPredictor class, which incorporates this sophisticated classifier, exhibited exceptional effectiveness in predicting real-time weather. The device's capacity to understand and analyze images captured by the fisheye camera and provide instant weather forecasts enhances its usefulness in meteorology, environmental monitoring, and integration with smart home systems. Here is the final detection results for both cloudy and sunny day:

In conclusion, the combination of the fisheye camera and advanced machine learning techniques in this weather forecast system highlights a seamless integration of hardware capabilities and software expertise. The system's ability to provide precise weather forecasts, based on a diverse and extensive dataset, demonstrates the significant impact of machine learning in real-world situations, especially in environmental analysis and meteorological research. Moreover, by utilizing the camera as the main method of verification, the prediction outputs are made more reliable and precise, taking into account the potential flaws of weather forecasts.

**Implementation Procedure**

In the proposed methodology, we elaborate on an autonomous operational protocol, which is conceptualized through a sequential flowchart designed for real-time environmental monitoring and actuation based on solar positioning and weather conditions. The flowchart of implementation of whole system is shown as following:

<p align="center">
  <img src="https://github.com/MVeszpremi/M202_Solar_Tracker/assets/131337093/24b6f3ea-27e0-44b2-9b21-2f6cd6eb20bc" width="75%" />
</p>

_Figure 3.1 Flowchart Diagram_

The methodology encapsulates a self-sufficient system that integrates environmental sensing, data processing, and mechanical actuation to optimize solar energy harvesting. Each segment's implementation is a testament to the system's robustness and reflects a harmonious interplay between software algorithms and hardware components.

# 4. Evaluation and Results

**Financial Projections**

Our team analyzed past severe weather events to model possible damage scenarios for solar farms. We made cost and destruction projections based on a moderate 5% panel loss scenario, then compared it to a case mimicking the recent level of damage at a Nebraska farm. In June 2023, a violent hailstorm ruined nearly 80% of their unprotected panel system in minutes. With climate change, more violent weather and potential damage is likely. Storms with baseball-sized hail are happening more often now and can shatter glass panels that are not equipped with our "Protection Mode" feature.

Replacing shattered panels and lost sales are major hits. The are also indirect costs from losing electricity sales, customers finding power elsewhere, and payment for repair crews. Weather disasters on this level seem rare but are becoming more common globally. Even one happening over decades of operation can cripple finances. The following analysis depicts risks that used to seem improbable becoming commonplace now.

Our team conducted an analysis of potential cost impacts to a 5.2 MW solar farm under different damage scenarios. We looked at baseline costs of $5.72 million to build the 5.2 MW farm, comprised of 13,000 400W solar panels. We assumed electricity sells at the national average of $0.16 per kW. 

For a conservative scenario, we estimated 5% of panels damaged, costing $286k to replace mechanisms plus $17k in labor. With 260 kWh generation capacity lost over 3 repair days and valuing customer inconvenience at $360k, total costs reached $681k on top of the original investment. 

For the more extreme case study with 80% panel damage, costs escalated dramatically to $4.58 million for parts, $270k labor, $299k lost electricity sales, and $630k customer inconvenience over 3 days. Total costs hit $5.78 million. 

While both scenarios have major cost implications, the case study illustrates how exponentially higher the expenses can grow if catastrophic damage occurs. Thus, our "Protection Mode" feature on our panel is proven to be quite valuable in the long run. 

Figure # below depicts the potential costs incurred on a typical solar panel farm due to severe weather conditions:

![Cost Analysis of Solar Farms without _Protection Mode_](https://github.com/MVeszpremi/M202_Solar_Tracker/assets/149114738/b640ddda-d3db-4ebc-b3e4-3b181d9f7934)

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

The solar panel positioning system project, epitomizing a synergy of mechanical ingenuity and software innovation, stands as a pivotal advancement in the domain of autonomous energy systems. Central to this project is a meticulously crafted mechanical system, equipped with Nema 17 Stepper motors and Hall effect sensors, which ensures the meticulous alignment of solar panels with the sun's trajectory. Augmented by a robust 2-axis tracker and a design that judiciously minimizes environmental impact, the system exemplifies a confluence of robustness and environmental consideration. An innovative integration in this system is the fisheye lens camera, affixed to the solar panel, which facilitates expansive sky imaging, thereby enhancing the overall functionality of the system.

In the software spectrum, the project distinguishes itself through its adeptness in real-time environmental monitoring and advanced predictive analytics. The continuous capture and processing of images, at ten-second intervals, feed into a sophisticated algorithm. This algorithm adeptly identifies cloud centroids and meticulously tracks the solar azimuth and elevation, culminating in the precise adjustment of the solar panel's pitch and yaw. This amalgamation of geometric computation and live data analysis marks a considerable stride in the enhancement of solar energy optimization. The integration of the OpenWeatherMap API, coupled with the fisheye camera, further attests to the project's commitment to precision and anticipatory planning. Collectively, these technological elements not only bolster energy efficiency but also furnish the system with the capability to adapt to adverse meteorological conditions, such as hailstorms, thereby fortifying the solar panels against potential damage.

This aspect of the project is critical, particularly in geographies like California, where precipitation is infrequent but the risk of hail is present. Empirical testing, simulating hailstorm conditions sporadically over a series of days, has demonstrated the system's proficiency in detecting severe weather conditions and promptly reorienting the solar panels vertically to ensure their protection. This empirical validation emphasizes the robustness and dependability of the system, carving a path for further sophisticated advancements in the realm of solar energy management and safeguarding.

Projecting into the future, the solar panel positioning system is poised for substantial growth and refinement. Prospective developments could entail the integration of advanced environmental sensors, broadening the system's adaptability to encompass not only meteorological changes but also fluctuations in air quality and ambient temperature. Additionally, the infusion of more refined machine learning algorithms could substantially enhance the system's predictive acumen, leading to heightened efficiencies in solar energy harvesting. Such advancements promise not only to elevate the system's operational efficacy but also to contribute significantly to a more sustainable and ecologically mindful approach to harnessing solar energy.

# 6. References

## i. Papers

Kirsh, Kristan. “TrueCapture’s New Split Boost Mode.” Nextracker, TrueCapture, 10 Jan. 2022, nextracker.com/truecapture-split-boost/.

Lane, Catherine. “Solar Tracking Investment Review.” Solar Reviews, Solar Reviews, 27 Mar. 2018, www.solarreviews.com/blog/are-solar-axis-trackers-worth-the- additional-investment.

Ludt, Billy. “What Is Solar Tracking?” Solar Power World, 24 Sept. 2020, www.solarpowerworldonline.com/2020/01/what-is-a-solar-tracker-and-how-does-it- work/#:~:text=Solar%20trackers%20use%20different%20drivers,GPS%20coordinates%20of%20its%20position. National Renewable Energy Laboratory. “NREL’s Solar Position Algorithm.” Solar Position Algorithm (SPA), Solar Radiation Research Laboratory, midcdmz.nrel.gov/spa/.

Nie, Yuhao, et al. “Sky-Image-Based Solar Forecasting Using Deep Learning.” arXiv.Org, Department of Energy Engineering Resources, Stanford, 5 Dec. 2022, arxiv.org/abs/2211.02108.

Sharpe, Jeff. “Various Solar Tracking Technologies.” Stracker Solar, 10 Nov. 2022, strackersolar.com/knowledge-base/what-are-solar-trackers.

Zsiborács, Henrik, et al. “Active Solar-Tracking Systems for Photovoltaic Technology & Implementation.” Sensors (Basel, Switzerland), U.S. National Center for Biotechnology Information, 27 Mar. 2022, www.ncbi.nlm.nih.gov/pmc/articles/PMC9003414/.

## ii. Databases

"SWIMSEG: Singapore Whole sky IMaging SEGmentation Database." National University of Singapore, captured Oct. 2013 to July 2015.

## iii. Softwares

Holmgren, William F., et al. "pvlib python: a python package for modeling solar energy systems." Journal of Open Source Software, vol. 3, no. 29, 2018, p. 884. DOI.org/10.21105/joss.00884.

Bradski, Gary. "The OpenCV Library." Dr. Dobb's Journal of Software Tools, 2000.

# 7. Appendix

![alt text](https://github.com/MVeszpremi/M202_Solar_Tracker/blob/main/docs/media/calib_matrix.png?raw=true)

_Figure 1.1 Fisheye Lens Calibration Visualization_
