# Primality Tests

The repository contains scripts for a simple application whose purpose is to check whether a number is prime using the Solovay–Strassen and Miller–Rabin algorithms. It was created for the purposes of Automation and Robotics studies at the AGH University of Science and Technology. The interface was developed using the PyQt5 library.
<p align="center">
<img src=".\zdjęcia\gui1.JPG" alt="a1" width="600" height="auto">
</p>

## How to Use the Application
To test whether a number is prime, enter it into the "Number" field. It can also be generated randomly from a predefined range. Below, there is an option to enter the number of iterations that the algorithm will perform. This value affects the probability of the result being correct. After clicking the "Start Test" button, the application checks primality using the Solovay–Strassen and Miller–Rabin algorithms. After clicking the "Show Details" button, the important parts of each algorithm will be displayed, but the tests must be run again to generate the results.

The results of both algorithms are displayed in separate windows:
•	iteration number k, 
•	randomly generated numbers that are potential Euler witnesses a, 
•	and the algorithm result. 

The probability that the tested number is prime is displayed below each window.

<p float="center">
  <img src=".\zdjęcia\gui2.JPG" alt="a2" width="400" height="auto">
  <img src=".\zdjęcia\gui3.JPG" alt="a3" width="400" height="auto">
</p>

After selecting the "Show Details" option, the important steps of the algorithms and their results are also displayed. If x or y are equal to 1 or n−1, then the number is prime. Otherwise, it is composite.

<p float="center">
  <img src=".\zdjęcia\gui5.JPG" alt="a5" width="400" height="auto">
  <img src=".\zdjęcia\gui4.JPG" alt="a4" width="400" height="auto">
</p>

After clicking the "Advanced Options" button in the bottom-right corner, you can change the range of randomly generated numbers and also force the first witness a to be selected. It must belong to the specified range.

<p align="center">
<img src=".\zdjęcia\gui6.JPG" alt="a6" width="600" height="auto">
</p>


