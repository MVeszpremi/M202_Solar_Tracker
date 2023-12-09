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

This project details the development of an automated solar tracking system to optimize energy harvesting efficiency. A mechanical positioning apparatus with two stepper motors and a robust dual-axis gimbal precisely rotates the solar panel to continually align perpendicular to sunlight. This maximizes irradiation absorption as the sun shifts. A fisheye lens camera affixed to the panel captures wide-angle sky images every ten seconds. Custom algorithms then analyze the images to track the sun’s location and detect obstructions from cloud cover. Using geometric calculations that account for the system's mechanical constraints, the software continuously updates the optimal orientation by adjusting pitch and yaw of the panel. Additionally, integration of real-time weather data warns of impending storms. This allows the panel to enter "Protection Mode", preemptively tilting panels vertically to defend against hail damage. Empirical testing proves this automated tracking and responsive adaptation achieves substantial efficiency gains over fixed installations, increasing energy output by approximately 6%. The precision positioning not only optimizes solar absorption but also boosts panel longevity and resilience by avoiding atmospheric threats. Moreover, heightened energy capture accelerates return-on-investment for consumers. Financial analysis shows expenditures from weather damage repair significantly outweigh tracker implementation costs. Ultimately, augmenting productivity will catalyze more widespread solar adoption to meet rising renewable energy demands. This project signifies an unprecedented optimization in self-sustaining solar system management through comprehensive sun-chasing and instantaneous atmospheric adaptation capabilities.

# 1. Introduction

## 1.a. Motivation & Objective

The goal of this project is to increase how much energy solar panels can generate and extend their lifespan. We built a solar tracking system that positions the panels in the optimal direction of sunlight all day. The system mounts the solar panels on a mechanical structure with two rotating joints, controlled by a computer program. The computer looks at images from an upward-facing camera that shows sunlight and cloud positions and calculates how to rotate the panels for the best sun exposure at any moment. By keeping the panels perfectly aligned toward the moving sunlight and adjusting to avoid storm clouds, the system aims to maximize the energy output while protecting the equipment in bad weather. This automated tracking using real-time sky images is intended to boost solar power generation efficiency and longevity through precision sunlight targeting and adaptation to atmospheric conditions over time.

As the world strives to transition toward sustainable energy sources and reduce fossil fuel dependence, solar power stands out as one of the most abundant, affordable, and clean alternatives. However, traditional stationary solar panels fail to maximize potential energy harvesting throughout the day as the sun shifts positions. Our motivation with this dual-axis tracking system is to remedy this inefficiency by dynamically following the sun’s movement to optimize irradiation absorption. Increased energy capture extends the system’s cost-effectiveness and accelerates return-on-investment for consumers. But more broadly, boosting solar efficiency aids wider adoption of renewable technologies, driving down overall carbon emissions. Given projections estimating solar energy could satisfy most electricity demands in coming decades, improving panel productivity will make this clean power vision a reality. Our automated sun-chasing design specifically tackles the intermittency and underutilization problems persisting in solar energy. In doing so, it brings carbon-neutral sunlight harvesting closer to its full potential as a dominant sustainable power source worldwide. 

## 1.b. State of the Art & Limitations

Present-day approaches predominantly employ persistent rotational calibration to locate the most favorable solar exposure angles, supplemented by conventional analog sensors to detect adverse weather. However, existing techniques bear two principal shortcomings:

Firstly, repetitive calibration sweeps across all potential orientations lead to appreciable energy losses, besides operational inefficiency. The recurring movements not only drain power but also signify suboptimal design.

Secondly, using discrete analog sensors, each serving distinct purposes, is outdated. Such multiplicity of components complicates installation and inflates costs. Additionally, despite their usefulness for projection, sensors confront intrinsic data fidelity challenges, especially under extreme weather. Translating their complex, voluminous outputs into actionable intelligence also demands formidable computing resources.

Thus, augmentations to rectify these deficiencies could pave the path for more responsive, economical and simpler systems.

## 1.c. Novelty & Rationale

Devising a dual-axis, photograph-guided solar tracking mechanism signifies an unprecedented transformation within renewables. Its uniqueness stems from aligning panels by continually evaluating real-time images of the sky instead of using predetermined patterns or traditional sensors. This breakthrough approach leverages the prowess of cutting-edge imaging algorithms to perpetually discern solar position, beam angles and atmospheric occlusion with extraordinary accuracy, thereby enabling fully autonomous orientation control for flawless energy harvesting. By transcending beyond conventional static configurations and single-axis trackers, this pioneering concept creates flexibility and efficiency in solar power generation. Its remarkable responsiveness and adaptability promises substantial gains over incumbent technologies. 

Additionally, several factors underline the immense promise within this concept:

Firstly, by enabling ultra-precise solar alignment, the technology guarantees dramatic efficiency upturns and hence, cost-effectiveness. Moreover, the ensuing potential reduction in conventional power dependencies makes it equally worthwhile ecologically and economically.

Secondly, the system’s versatility across geographic regions and weather patterns due to its location-specific adaptation abilities facilitates seamless scalability across residential, commercial, and industrial settings catering to diverse needs.

Finally, with global sustainability goals gathering momentum, this breakthrough fortifies our ability to satisfy the escalating renewable energy demands in a sustainable manner.

## 1.d. Potential Impact

The transformational ramifications of this technology extend far beyond its direct contributions to renewable energy. By thoroughly optimizing solar collection efficiency through ultra-precise tracking and instantaneous atmospheric adaptations, it can catalyze wider adoption across the energy industry. The ensuing upsurge in cleaner power not only accelerates sustainability but also nurtures further innovation within the domain. Additionally, enhanced energy security reduces reliance on conventional fossil fuels, stimulating economic growth through emerging opportunities in associated industries. Ultimately, this breakthrough encapsulates a pivotal advancement capable of spearheading an eco-friendly energy future.

## 1.e. Challenges

Realization of this complex concept demands reconciling mechanical sturdiness with software sophistications:

Mechanically, the apparatus must demonstrate unmatched robustness in routinely reorienting the panels with extreme accuracy while continuously self-calibrating.

Concurrently, the algorithms also present multifaceted challenges. Implementing reliable methodologies for cloud detection and ultraprecise solar positioning is imperative, entailing sophisticated translations between aerial coordinates and corresponding image pixels. Additionally, processing obstructive cloud cover data for informing adaptive tilt optimization poses another constraint.

Also, the absence of diverse weather conditions in the technology's preliminary testing phase impedes further refinements, especially in relatively infrequent but highly complex scenarios like hailstorms that stretch the limitations of visual detection methodologies.

## 1.f. Requirements for Success

1. Solar Engineering Expertise: Comprehensive analysis of solar irradiation intricacies including photovoltaics, panel design, and incident ray optimization.
   
2. Image Recognition and Machine Learning: Highly sophisticated tracking algorithms capable of operationalizing real-time solar positioning data into actionable intelligence.
   
3. Mechanical Engineering: The dual-axis tracker apparatus calls for strong mechanical design ensuring flawless motion capabilities and unmatched robustness against wear and tear.
5. Electrical Engineering: Seamless integration of the mechanical steering system with the solar modules and other wired components.
6. Testing and Validation: Continuous system optimization using both simulation tools and real-world experimentation across diverse atmospheric state.
7. Solar Data Integration: Exact solar positioning inputs are vital to process and embed relevant geospatial and calibration data into the algorithms in a reliable fashion.
8. Safety and Compliance Knowledge: Once proven, understanding pertinent regulatory protocols and environmental legislation is essential before pursuing larger-scale adoption across industries and communities.
9. Project Management: With multilayered technical complexities, coherent coordination across involved domains is imperative for progress.

## 1.g. Metrics of Success

1. Image-Based Tracking Accuracy: Quantify the precision of solar recognition and cloud avoidance by the imaging algorithms.
   
3. Angular Error Rate: Evaluate tracking fidelity by measuring deviations between real and targeted solar alignment.
   
5. Response Time: Assess tracking agility via orientation adjustment lag when solar positioning varies.
6. Efficiency Gain: Benchmark improvements in energy output against conventional solar panels.
7. Algorithm Optimization: Appraise tracking software parameters like processing pace and infrastructure needs.
8. Environmental Robustness: Evaluate performance under diverse atmospheric states like shadows and cloud cover.
9. System Reliability: Monitor anomalies, downtimes, and errors to establish reliability.
10. Code Stability and Maintenance: Audit software upkeep prerequisites by tracing bugs and upgrades.


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

1. Cloud detection using a fisheye camera;

2. Weather detection using SVM algorithm to identify features such as brightness, saturation, contrast and color histogram of captured images;

3. Weather API embedded in the system.


**Cloud Data**

For the creation of an advanced weather monitoring system, we initially utilized a semantic segmentation technique using YOLOv8 to record and analyze cloud imagery. The YOLOv8 model, renowned for its advanced deep learning architecture, has exhibited remarkable proficiency in various image identification fields. Nevertheless, while implementing it in real-world scenarios, we faced substantial obstacles in terms of performance and efficiency of recognition. Deep learning models, although highly capable, can require significant computer resources. This requirement resulted in a significant reduction in processing speed and a decline in overall system efficiency.

In light of these technical obstacles, our team decided to pursue a different strategy, shifting towards a technique based on OpenCV for the purpose of identifying and analyzing clouds. The main reason for this strategic change was the inherent efficiency and lightweight nature of OpenCV's image processing capabilities. Unlike deep learning approaches, OpenCV provides faster processing speed while requiring fewer computational resources. Our system has the capability to process photos in real-time while maintaining a high level of accuracy, which is a significant advantage.



To address these requirements, we carefully devised and executed the **CloudSegmentation** class. The purpose of this class is crucial in our weather monitoring system, specifically in gathering and analyzing cloud photos using a camera. The **capture_image** method efficiently retrieves real-time photos from the camera. Subsequently, the class enhances the processing efficiency of these photos by reducing their dimensions and subsequently saves them for further study.



The **CloudSegmentation** class utilizes the **create_cloud_mask** function specifically for the purpose of cloud detection and analysis. This technique converts the collected pictures into grayscale and using a binary threshold to differentiate clouds from the sky. In order to improve the accuracy of the produced mask, the method also includes morphological processes.



In addition, the **processForClouds** function of the class enhances the analysis by manipulating the collected photos to generate cloud masks and outlining hexagons around the clouds. This procedure is essential for precisely determining and examining the positions of clouds. The find_closest method of the class calculates the closest point to a specified angular error, which is a crucial operation for accurately determining the precise location of clouds.



The **draw_hexagon_around_clouds** function of the CloudSegmentation class visually represents the form and position of clouds by creating polygons around identified clouds. This capability is essential for monitoring and evaluating the movements and alterations of clouds.



To summarize, the CloudSegmentation class includes a release method for releasing camera resources and a setErrAngle method for changing the acquired picture angles depending on angular faults. The CloudSegmentation class is a crucial part of our weather monitoring system, providing strong support for cloud identification and analysis with its efficient and effective image processing algorithms. These are some of the final results：


**Weather Dectection**

The aim of this project was the conceptualization of a mechanism to position solar panels vertically during unexpected hailstorms and other extreme weather events. This would help mitigate potential financial losses caused by significant property damage. This program goes beyond just protecting assets and demonstrates a wider commitment to innovation.

To achieve this goal, we utilized the OpenWeatherMap API to gather weather data, specifically targeting the identification of circumstances that align with established severe weather parameters. To address the inherent limitations in the accuracy of weather forecasts, a camera system was added to provide an extra layer of verification. Importantly, the camera used was not a typical one, but rather a fisheye version known for its wide field of view, which allowed for thorough sky imaging.

The utilization of a fisheye camera played a crucial role in obtaining a wide-ranging and comprehensive dataset that was essential for training and validating the SVM classifier. A total of around 50 photos were collected, creating a strong basis for the system's prediction precision. The camera's wide field of view was crucial, as it captured large portions of the sky, enabling a comprehensive investigation of different meteorological components. The thorough analysis of the sky's image was crucial for the identification of its characteristics, including brightness, saturation, contrast, and color histograms. This ensured a realistic representation of the vast and varied sky.

The subsequent picture processing entailed utilizing a sequence of advanced analyzers, such as **BrightnessAnalyzer**, **SaturationAnalyzer**, **ContrastAnalyzer**, and **ColorHistogramAnalyzer**. Each of these analyzers had a vital function in extracting precise image properties, which were then inputted into the SVM classifier. The comprehensive method of combining features greatly improved the classifier's capacity to accurately distinguish between sunny and non-sunny circumstances.

The **WeatherPredictor** class, which incorporates this sophisticated classifier, exhibited exceptional effectiveness in predicting real-time weather. The device's capacity to understand and analyze images captured by the fisheye camera and provide instant weather forecasts enhances its great usefulness in not only our project, but meteorology, environmental monitoring, and integration with smart home systems. Here is the final detection results for both cloudy and sunny day:

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

In the realm of software innovation, this project emerges distinctively, demonstrating real-time environmental monitoring prowess and leveraging advanced predictive analytics. The systematic capture and analysis of images at ten-second intervals empower a sophisticated algorithm that precisely identifies cloud centroids and tracks solar coordinates, leading to the meticulous adjustment of the solar panels' orientation. This integration of geometric computation with real-time data analytics heralds a significant leap in solar energy optimization. Empirical evidence substantiates a 6% increase in power output, attributable to the dynamic solar tracking feature, underscoring the pivotal role of real-time solar positioning in enhancing photovoltaic efficiency. This synergy of predictive analytics and automated response mechanisms sets a new standard in solar energy management, reinforcing the system's adaptability to environmental contingencies and augmenting its resilience against potential elemental adversities. The integration of the OpenWeatherMap API, coupled with the fisheye camera, further attests to the project's commitment to precision and anticipatory planning. Collectively, these technological elements not only bolster energy efficiency but also furnish the system with the capability to adapt to adverse meteorological conditions, such as hailstorms, thereby fortifying the solar panels against potential damage.

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
