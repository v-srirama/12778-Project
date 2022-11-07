# Measuring Static and Dynamic Loading on a Surface   <img src="https://pbs.twimg.com/profile_images/1291079250074894336/8LWaj7yF_400x400.jpg" width="70" height="70" align = "right">

### [_12-778_](https://sites.inferlab.org/courses/12-778/): _Sensors, Circuits and Data Interpretation/Management for Infrastructure Systems (Fall 2022)_

### Instructor : [_Prof. Mario Bergés_](https://www.inferlab.org/author/mario-berges/) , Professor of Civil and Environmental Engineering, CMU

### Group Members:

| Name        | @Andrew           | @GitHub  |
| ------------- |:-------------| :-----|
| Balaji Pulipakkam Sridhar     | [_bpsridha_](mailto:bpsridha@andrew.cmu.edu) | [_Bpsridha_](https://github.com/Bpsridha) |
| Ishwrya Achuthan Geetha      | [_iachutha_](mailto:iachutha@andrew.cmu.edu)      |   [_IshwryaAG_](https://github.com/IshwryaAG)|
| Sakar Adhikari | [_sakara_](mailto:sakara@andrew.cmu.edu)      |   [_sakaradhikari97_](https://github.com/sakaradhikari97) |
| Sri Ramana Saketh Vasanthawada | [_vsrirama_](mailto:vsrirama@andrew.cmu.edu)      |   [_v-srirama_](https://github.com/v-srirama) |


#### Project Proposal Presentation: [10/10/2022](https://docs.google.com/presentation/d/1D6wiyP8TMsjKfLq7qg-S6Jve4d0Y-7zr/edit?usp=sharing&ouid=105676526214084463560&rtpof=true&sd=true)



## Motivation and measurement goals

Structural health monitoring (SHM) examines and analyzes the infrastructure system over time to understand the response to externally induced forces. SHM is becoming increasingly relevant due to the growing research and awareness of interconnected devices, their consequent availability of data, and the influx of technology in construction. Among numerous SHM-based applications in a traditional Civil Engineering context, Bridge monitoring is one of the critical maintenance activities which is time-consuming and carries higher economic costs due to unexpected maintenance and repair. Therefore, it is vital to develop a system that assesses the dynamic loading and location of loads on the structure. This would help in real-time assessment of the structure and function as a predictive maintenance mechanism protecting people and inhibiting costs and time. With the overarching theme of measuring static and dynamic loading, the project is aimed to develop a real-time load monitoring system using Raspberry Pico W and compatible load measurement sensors. As a Proof of Concept (PoC), a table with custom dimensions - in consideration with sensor characteristics -  is being designed to attain the proposed objectives:

1. Measuring the weight of the object on the surface
2. Static and Dynamic position of an object on the surface
3. Location change of object across the surface



## Identified Electronic Measurement Components

| Sensors       | Serial / Make  | Quantity  | Purchase Link  |   
| :-------------: |:-------------:| :-----:| :-----:|
| Load Cell      | 5Kg / 114990100 / Seeed Technology Co., Ltd | 4 | [_Digi-Key Electronics_](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/114990100/5487619) |
| Load Cell Amplifier   | HX711  |  4 | [_SparkFun_](https://www.sparkfun.com/products/13879)|
| Resistor Kit | 1/4W 500 pieces |  1 | [_CanaKit_](https://www.canakit.com/resistor-kit-1-4w-com-09258.html)| 


## Potential Challenges 
With the current level of understanding, the following challenges have been identified for developing the PoC: 
1. Accuracy in measuring sensitive quantities 
2. Identifying the location of light loads placed on the surface 
3. Identifying dynamic loading on the surface 
4. Interfacing RPi Pico, sensors and amplifiers

## Validation of measurement system 
1. Placing standard weights and verifying with sensor-based computations 
2. Visual inspecting of the object location

