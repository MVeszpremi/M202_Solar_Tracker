# Project Proposal

## 1. Motivation & Objective

The objective of this project is to enhance the efficiency and lifespan of solar panels through the creation of an advanced system that optimizes the angle of incoming solar radiation. To achieve this, the panels will be affixed to a dual-axis mechanical gimbal, which will dynamically adjust their orientation. This adjustment is informed by continuous monitoring and analysis of the sky conditions using an upward-facing camera, enabling precise alignment of the panels with the sun's position to maximize energy capture and adjustment to a vertical position reduce wear over during extreme weather.

## 2. State of the Art & Its Limitations

The existing technology in the field predominantly relies on constant rotational adjustments to discover the most effective positioning for solar panels, coupled with the employment of traditional analog sensors for anticipating or identifying severe weather conditions. This approach, however, presents two main drawbacks:

First, the method of continuously sweeping through the entire range of possible angles can lead to significant energy losses, particularly when repeated adjustments are required. This frequent motion not only consumes power but also signifies operational inefficiency.

Second, the deployment of analog sensors, each designed for a singular purpose, is becoming increasingly obsolete. Such a configuration necessitates an extensive suite of sensors, which results in a complex and costly installation process due to the multitude of components involved.

Improvements in these areas could lead to a more streamlined, energy-efficient, and cost-effective system.

## 3. Novelty & Rationale

Developing a dual-axis, photograph-based sun tracking solar panel represents a groundbreaking and unprecedented innovation in the renewable energy landscape. It distinguishes itself as the first technology of its kind due to its unique approach to tracking the sun's position while avoiding cloud cover and inclement weather. While conventional sun tracking systems primarily rely on predetermined algorithms or light sensors, this cutting-edge solution harnesses the power of photograph-based tracking. This novel method employs advanced image recognition technology to constantly evaluate the sun's exact location in the sky, realtive angles, and solar ray disruption thus allowing the solar panel to autonomously adjust both its horizontal and vertical angles with unparalleled precision. This pioneering technology marks a departure from traditional fixed solar panels and even single-axis tracking systems. By offering a more adaptable and responsive approach to capturing solar energy, it promises to significantly enhance energy output. The system's ability to fine-tune its orientation throughout the day and across seasons is a game-changer in the field of solar energy generation. As the first of its kind, this innovation stands as a testament to human ingenuity and our relentless pursuit of sustainable energy solutions that are poised for success. 

The prospects for the success of this innovative dual-axis, photograph-based sun tracking solar panel technology are highly promising. Its success is underpinned by several key factors. Firstly, the precision and adaptability afforded by photograph-based tracking result in significantly increased energy capture efficiency, ensuring optimal energy production across various geographical locations and changing solar conditions. This enhanced efficiency, coupled with a potential reduction in reliance on conventional energy sources, positions the technology as a cost-effective and environmentally responsible solution. Furthermore, the scalability and applicability of this novel system could drive its adoption across residential, commercial, and industrial sectors. With its ability to adapt to local solar patterns, it can cater to a wide range of energy needs. Moreover, as the world's focus on sustainability and renewable energy intensifies, this solar panel represents a pivotal step forward in meeting the growing demand for clean energy. These factors collectively contribute to the technology's potential for success and its ability to revolutionize the solar energy industry.

## 4. Potential Impact

The potential impact of the dual-axis, photograph-based sun tracking solar panel extends far beyond its technical advancements. From a technical standpoint, this innovation has the capacity to significantly enhance solar energy production efficiency, making it a pivotal asset in the transition towards renewable energy sources. By harnessing image recognition technology and its precise tracking capabilities, it can maximize energy capture and adapt to diverse environmental conditions, making it a versatile solution for various regions and applications.

Broadly, its impact has the potential to reshape the entire energy landscape. The adoption of this technology could drive a substantial reduction in greenhouse gas emissions, mitigating the effects of climate change and promoting sustainability. Furthermore, its success could stimulate innovation in the renewable energy sector, encouraging further research and development in similar groundbreaking technologies. As a cleaner and more efficient energy source, it can enhance energy security, reduce dependence on fossil fuels, and drive economic growth by creating new opportunities in manufacturing, installation, and maintenance. Ultimately, the dual-axis, photograph-based sun tracking solar panel represents a transformative force that could propel society towards a greener, more sustainable future.

## 5. Challenges

The project faces two principal categories of challenges: mechanical robustness and software complexity.

Mechanically, the design must be durable to ensure long-term functionality. The system needs to be able to repetedly rotate to accurate positions and self-calibrate. 

On the software side, we encounter several intricate issues. First, the system requires sophisticated algorithms for cloud detection and precise solar tracking. The latter involves using the Solar Position Algorithm (SPA) to translate solar azimuth and zenith angles into corresponding pixel locations in the camera's field of view. Additionally, the software must intelligently process information about cloud coverage to adjust the panels' angles optimally.

Another significant software challenge is the detection of severe weather conditions. Testing the system in Los Angeles, where such weather is infrequent, limits our ability to refine this feature. Specifically, identifying hail through camera-based methods poses a substantial difficulty, given the limitations of visual detection under such conditions.

## 6. Requirements for Success

Developing this advanced solar panel technology demands a convergence of these technical skills and access to the necessary resources, from engineering expertise to prototyping and validation. The successful integration of these elements will be instrumental in bringing the novel dual-axis, photograph-based sun tracking solar panel to fruition:

1. Solar Engineering Expertise: In-depth knowledge of solar engineering is essential. This includes understanding the photovoltaic effect, solar panel design, and the interaction between solar cells and light to optimize energy conversion as well as sun angles, incident rays, weather obstructions, etc. This motivates our extensive research into the topic. 

2. Image Recognition and Machine Learning: Proficiency in image recognition and machine learning is a core technical skill. We must create algorithms that can accurately locate and track the sun's position in real-time while identifying cloud cover and poor weather conditions. Such algorithms can be developed on Python and/or integrated on Raspberry Pi. Additionally, the datasets described below, can be trained and tested through trial and error. 

3. Mechanical Engineering: We must effecitvely design the tracking mechanism, ensuring precise movement of the solar panel in both horizontal and vertical axes. Our active solar tracker must also account for durability, weather resistance, and maintenance considerations. 3D printers are necessary for part manufacturing and Arduino microcontroller kits are essential for motor installment and callibration. 

4. Electrical Engineering: We must integrate the tracking system with the solar panel and power sources. We must ensure that the electrical connections are developed in a sound manner and the panel operates in a safe and efficient fashion while converting and storing generated electricity. 

5. Material Science: Knowledge of advanced photovoltaic materials and their properties is crucial for selecting the most suitable materials to achieve maximum energy conversion.

6. Testing and Validation: After training data sets, constant validation with new images will be necessary. Because the weather near UCLA does not offer a large variety of weather conditions, most of this will be done virtually. However, we must seize opportunities to test and validate when the weather conditions are less than ideal for more accurate feedback. We must record reliable data and accurately provide the input to our algorithms to assess the system's performance under varying weather conditions over extended periods, ensuring reliability and efficiency.

7. Solar Data Integration: Skills to gather, process, and integrate real-time solar data into the system are critical for accurate sun tracking. This overlaps with algorithm development, but we must make sure that the data we seek to integrate is reliable such as GPS coordinates, callibration references, and relative angles. 

8. Safety and Compliance Knowledge: Although not a major concern for our immediate project, if we seek to continue our project outside of class, a strong understanding of safety standards, electrical codes, and environmental regulations is necessary to ensure the solar panel complies with industry and legal requirements.

9. Environmental Impact Assessment: Again, although a lower priority, for marketing and empirical data purposes, the ability to assess the environmental impact of the solar panel's production and deployment is crucial to address ecological concerns and sustainability.

10. Project Management: Effective project management skills are vital to coordinate the efforts of the multidisciplinary team and ensure the project progresses according to the defined timeline and theoretical budget.

## 7. Metrics of Success

These metrics collectively provide a comprehensive evaluation, guiding the development and optimization of the technology for maximum impact in the field of solar energy:

1. Photograph-Based Tracking Accuracy: Measure the precision of the image recognition system by evaluating how accurately it identifies and tracks the sun's position. This can be quantified as a percentage of tracking accuracy, reflecting how closely the solar panel aligns with the sun.

2. Angular Error Rate: Assess the angular error rate, which quantifies the degree of deviation between the actual sun position and the solar panel's tracked position. A lower angular error rate indicates higher tracking precision.

3. Response Time of Tracking System: Evaluate the responsiveness of the photograph-based tracking system by measuring the time it takes to adjust the solar panel's orientation in response to changes in the sun's position. A faster response time enhances overall efficiency.

4. Efficiency Gain Over Fixed Panels: Compare the energy output and efficiency of the photograph-based sun tracking solar panel to fixed solar panels. Express the efficiency gain as a percentage increase in energy production, showcasing the technology's superior performance.

5. Algorithm Optimization: Assess the efficiency of the image recognition algorithms by measuring their processing speed and resource utilization. Optimized algorithms contribute to faster and more accurate sun tracking.

6. Robustness to Environmental Conditions: Evaluate the technology's performance under varying environmental conditions, including cloudy days, shadows, and low light situations. A successful system should demonstrate robustness and adaptability to different scenarios.

7. System Reliability: Measure the reliability of the tracking system by monitoring the occurrence of errors, malfunctions, or downtime. A reliable system minimizes disruptions and ensures consistent energy production.

8. Code Stability and Maintenance: Assess the stability of the software code by tracking any incidents of bugs, glitches, or crashes. Evaluate the ease of maintenance and updates to ensure the long-term sustainability of the technology.

## 8. Execution Plan

1. Define Objectives and Requirements:
   - Clearly define the objectives of the solar panel, such as maximizing energy output and efficiency
   - Specify technical requirements, including tracking accuracy, response time, and adaptability to different environments
   - This was completed in this proposal by the whole team

2. Research and Data Collection:
   - Gather solar data for the target geographic locations, including sun path, intensity, and seasonal variations
   - Research existing solar tracking technologies and image recognition algorithms
   - This was completed by the whole team

3. Design and Engineering:
   - Develop a detailed design of the dual-axis tracking system, considering mechanical and electrical aspects
   - Integrate image recognition algorithms into the control system to enable accurate sun tracking
   - Design the solar panel layout for optimal energy capture
   - This is primarily Marcell's and Russell's job as they have experience with robotic systems

4. Prototyping and Testing:
   - Build a prototype of the solar panel system for testing and validation.
   - Conduct initial tests to evaluate tracking accuracy, system response time, and overall performance
   - Iteratively refine the design based on test results
   - Marcell will primarily execute building the design because of his expertise and resource access
   - The whole team will preform trials and iterate/refine
     
5. Algorithm Development and Optimization:
   - Implement and optimize image recognition algorithms for sun tracking
   - Ensure the algorithms can adapt to changing environmental conditions and provide real-time adjustments
   - This will primarily be Richard's task because of his experience with machine learning
     
6. Software Development:
   - Develop the software that controls the entire solar tracking system, incorporating feedback from camera's and adjusting the panel's orientation
   - Ensure the software is robust, reliable, and capable of real-time decision-making
   - Marcell will focus on image reading and dual-axis motor synchronization
   - Richard will focus on cloud/bad weather detection
   - Russell will focus on optimizing incident angles and solar tracking through GPS
     
7. Testing and Validation:
   - Conduct comprehensive testing under various environmental conditions to validate the system's performance
   - Evaluate the system's reliability, accuracy, and efficiency through extended testing periods
   - This may be limited due to Los Angeles' moderate weather, but training our algorithm over the large dataset should suffice
   - This will be accompished by the whole team

8. Optimization and Feedback Loop:
   - Analyze test results and user feedback to identify areas for improvement
   - Iterate on the design, algorithms, and software to optimize performance and address any identified issues
   - This task will be completed by the whole team in their respective areas described above.
     
9. Documentation:
   - Document the entire development process, including design specifications, algorithms, and testing procedures
   - Compile this documentation into a final report
   - Primarily Russell's job, with the help of the team by gathering information from their respective tasks 

## 9. Related Work

### 9.a. Papers

#### What is Solar Tracking?
This paper provides a foundational base for beginning to understand solar tracking and the existing technologies. It gives a high level overview of GPS and liquid boiling systems currently in industry. This gave us an initial launch point for application, implementation, and optimization. 

#### Various Solar Tracking Technologies
This paper describes how solar panels capture and distribute energy and how they currently utilize single and dual axis tracking systems. It also defines passive and active solar trackers and discusses the advantages of solar tracking and the bright future it entails. With this infomration, we were able to further detail our design and determine the use of an active, dual-axis tracker. 

#### Sky-Image-Based Solar Forecasting Using Deep Learning
This study investigates different training strategies for solar forecasting models using ground-based sky images from various global datasets with diverse climate patterns. It compares the performance of local models trained individually on single datasets, global models trained on a fusion of multiple datasets, and knowledge transfer from pre-trained models to new datasets. The results show that local models work well in their respective locations with slight errors and provide a robust template for our project. 

#### Active Solar-Tracking Systems for Photovoltaic Technology &amp; Implementation
This journal discusses the significance of solar irradiation for photovoltaic (PV) systems and the benefits of solar tracking in maximizing energy generation. It highlights the limitations of current active sensor-tracking algorithms, including issues with cloudy weather, module positioning after nightfall, and protection from adverse weather conditions. It also suggests incorporating periodic movement and nearly horizontal positioning, offering improved system lifetime and storm damage prevention while maintaining high tracking accuracy which influenced our project design decisions.

#### TrueCapture’s New Split Boost Mode
This article gave us insight into the state-of-the-art in the solar industry. It describes the latest addition to TrueCapture Software known as the "Split Boost", a row-to-row feature designed to maximize energy gain for photovaltaic plants using split-cell solar modules. This innovation leverages the shade-tolerant nature of split-cell modules, adjusting the tracker rows to optimize irradiance on the top half of the modules, resulting in a boost in production, even on flat terrain, with preliminary data showing up to a 1% yield improvement compared to conventional backtracking for specific conditions. 

#### Solar Tracking Investment Review
After learning about the technology, we were interested in the financial considerations of actually implementing that technology. This article provides an in depth investment review at the residential and commerical level. Although this project is not heavily concerned with finanical implications, as engineers and entrepreneurs, we wanted to take the time to understand all aspects of our project. 

### 9.b. Datasets

1. Singapore Whole sky IMaging SEGmentation Database
2. Singapore Whole sky IMaging CATegories Database

### 9.c. Software

1. Pvlib is used as the Solar Positioning Algorithm (SPA) library
2. OpenCV is used for general image processing and cloud segmentation

## 10. References

### i. Papers

Kirsh, Kristan. “TrueCapture’s New Split Boost Mode.” Nextracker, TrueCapture, 10 Jan. 2022, nextracker.com/truecapture-split-boost/. 

Lane, Catherine. “Solar Tracking Investment Review.” Solar Reviews, Solar Reviews, 27 Mar. 2018, www.solarreviews.com/blog/are-solar-axis-trackers-worth-the-      additional-investment. 

Ludt, Billy. “What Is Solar Tracking?” Solar Power World, 24 Sept. 2020, www.solarpowerworldonline.com/2020/01/what-is-a-solar-tracker-and-how-does-it-            work/#:~:text=Solar%20trackers%20use%20different%20drivers,GPS%20coordinates%20of%20its%20position. 
National Renewable Energy Laboratory. “NREL’s Solar Position Algorithm.” Solar Position Algorithm (SPA), Solar Radiation Research Laboratory,                      midcdmz.nrel.gov/spa/. 

Nie, Yuhao, et al. “Sky-Image-Based Solar Forecasting Using Deep Learning.” arXiv.Org, Department of Energy Engineering Resources, Stanford, 5 Dec. 2022,          arxiv.org/abs/2211.02108. 

Sharpe, Jeff. “Various Solar Tracking Technologies.” Stracker Solar, 10 Nov. 2022, strackersolar.com/knowledge-base/what-are-solar-trackers. 

Zsiborács, Henrik, et al. “Active Solar-Tracking Systems for Photovoltaic Technology &amp; Implementation.” Sensors (Basel, Switzerland), U.S. National            Center for Biotechnology Information, 27 Mar. 2022, www.ncbi.nlm.nih.gov/pmc/articles/PMC9003414/. 


### ii. Databases

"SWIMSEG: Singapore Whole sky IMaging SEGmentation Database." National University of Singapore, captured Oct. 2013 to July 2015.

### iii. Softwares

Holmgren, William F., et al. "pvlib python: a python package for modeling solar energy systems." Journal of Open Source Software, vol. 3, no. 29, 2018, p. 884. DOI.org/10.21105/joss.00884.

Bradski, Gary. "The OpenCV Library." Dr. Dobb's Journal of Software Tools, 2000.
