# Integral Simulation
Computes the value of a definite integral using Monte Carlo simulation in Python.
## Problem to solve ✔
If X is a continuous random variable with density function f<sub>x</sub> and g is a continuous function, the expectation of g(X) is given by:

<img src="https://latex.codecogs.com/png.latex?\dpi{80}&space;\bg_white&space;\LARGE&space;E(g(X))=\int_{-\infty&space;}^{\infty&space;}g(x)f_x(x)dx{\color{Blue}&space;}" title="\LARGE E(g(X))=\int_{-\infty }^{\infty }g(x)f_x(x)dx{\color{Blue} }" />
If X is uniformly distributed in [0, 1], then

<img src="https://latex.codecogs.com/png.latex?\dpi{80}&space;\bg_white&space;\LARGE&space;E(g(X))=\int_{0}^{1}g(x)dx" title="\LARGE E(g(X))=\int_{0}^{1}g(x)dx" />

This fact suggests that we can use simulation to estimate the previous integral, estimating the value of E(g(X)). If X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, ..., X<sub>n</sub> are independent and uniformly distributed in [0, 1], then the g(X<sub>i</sub>) are also independent. 
Therefore, if we define the mean of g(X) as:

<img src="https://latex.codecogs.com/png.latex?\dpi{80}&space;\bg_white&space;\LARGE&space;\overline{g(x)}=\frac{g(X_1)&plus;g(X_2)&plus;...&plus;g(X_n)}{n}" title="\LARGE \overline{g(x)}=\frac{g(X_1)+g(X_2)+...+g(X_n)}{n}" />

and we assume that g(X) has mean μ and variance σ², then:

<img src="https://latex.codecogs.com/png.latex?\dpi{80}&space;\bg_white&space;\LARGE&space;E(\overline{g(X)})=\mu&space;\phantom{abcd}&space;V(\overline{g(X)})=\frac{\sigma^2}{n}" title="\LARGE E(\overline{g(X)})=\mu \phantom{abcd} V(\overline{g(X)})=\frac{\sigma^2}{n}"/>

These two equalities suggest that to estimate μ, we can generate a sequence of numbers u<sub>1</sub>, u<sub>2</sub>, u<sub>3</sub>, ..., a uniformly distributed in [0, 1], independent and calculate (g(u<sub>1</sub>)+g(u<sub>2</sub>)+g(u<sub>3</sub>)+...+g(u<sub>n</sub>))/n.
Note that the variance of the mean g(X) can be made as small as you like by taking it large enough.

## Input📋
A menu of options is displayed where you must choose the type of interval where the integral will be calculated, that is:
* 1 == **[a, b]**
* 2 == **[0, 00]** 
* 3 == **[-00 , 00]**

Next, you must write the function in terms of x and the limits of the interval.

```
exp(-x**2)
```
It means
 <img src="https://latex.codecogs.com/png.latex?\dpi{80}&space;\bg_white&space;\LARGE&space;e^{-x^2}" title="\LARGE e^{-x^2}" />
 
 ## Output 📦
 * **Simulated value**
 * **Real value**
 * **Percentage error**
 
 ### Note
 You can do the exact same thing for a multiple integral.
 

