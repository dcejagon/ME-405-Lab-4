# RC Circuit Analysis
## Description
### Overall 
The main task in this lab was to analyze the loading of an RC circuit. We did this by
utilizing an analong to digital converter (ADC) on the nucleo
### Physical Implementation
We built the circuit according to the lab handout for lab 4, however, we were unable 
to find a capacitor in the range of 4uF-10uF. We instead used a 1uF capacitor 
as it was the closest we could find in the lab equipment.
### RC Circuit Loading Response
The goal of this lab was to generate a plot to demonstrate how the circuit loads 
by taking ADC reading at a choosen interval, and reading that data through the 
serial port using a port reader file. 
## Plot Results
### Initial Arbitrary Kp Value
The plot below demonstrates a pretty exact step response. If we were to run our 
code on a circuit that uses a 10uF capacitor instead of a 1uF capacitor, we would
expect to see a gradual and smooth response instead of a sharp step seen in
our plot. 
![RC Circuit Response](https://github.com/dcejagon/ME-405-Lab-4/blob/999794663a00441d3c52f93647251b1937c19a7f/RC_Circuit_Responce.png)
RC circuit response to initial loading. 
