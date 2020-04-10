# Simulate Continous Random Variables with Selected Distributions

import numpy as np
import random 
import matplotlib
import matplotlib.pyplot as plt
import math

#----- 1.1 Simulate a Uniform Random Variable -------------
# Plot the Uniform PDF
def UnifPDF(a,b,x): 
    f = (1/abs(b-1))*np.ones(np.size(x))
    return f

# Generate the vlues of the RV X
a = 1.0; b = 4.0; n = 10000
x = np.random.uniform(a,b,n)

# Create bins and histogram
nbins = 30;     # Number of bins
edgecolor = 'w' # Color seperating bars in the bargraph 

bins = [float(x) for x in np.linspace(a,b,nbins+1)]
h1, bin_edges = np.histogram(x,bins,density=True)

# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges) - 1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1+be2)/2
barwidth = b1[1] - b1[0] #Width of bars in the bargraph
plt.close('all')

# Plot the Bar Graph
fig1 = plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

f = UnifPDF(a,b,b1)
plt.plot(b1,f,'r')
plt.title('Uniform Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')

plt.show()
# Calculate the mean and standard deviation
mu_x = np.mean(x)
sig_x = np.std(x)
theo_calc = a + b/2
exp_meas = (b-a)**2/12

print("Uniform Random Variable")
print("Expectation Experimental Measurement:", mu_x)
print("Expectation Theoretical  Measurement for Expectation:", theo_calc)
print("Starndard Deviation Experimental Measurement:",sig_x)
print("Standard DeviaitonTheoretical  Measurement:",exp_meas)
print("\n")

#----- 1.2 Simulate an Exponentiallly distrubuted Random Variable -------------
beta = 40; a = 1.0; b = 200; n = 10000

# Generate the values of the RV x
x = np.random.exponential(beta,n) 

# Create bins and histogram
nbins = 30;     # Number of bins
edgecolor = 'w' # Color seperating bars in the bargraph 

bins = [float(x) for x in np.linspace(a,b,nbins+1)]
h1, bin_edges = np.histogram(x,bins,density=True)

# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges) - 1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1+be2)/2
barwidth = b1[1] - b1[0] #Width of bars in the bargraph
plt.close('all')

# Plot the Bar Graph
fig1 = plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

f = UnifPDF(a,b,b1)
plt.plot(b1,f,'r')

# Plot the exponential pdf
def ExpoPDF(beta,x):
    f = (1/beta)*(np.exp(((-1/beta)*x))* np.ones(np.size(x)))
    return f

f = ExpoPDF(beta,b1)

plt.plot(b1,f,'r')
plt.title('Exponential Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')
plt.show()

# Calculate the mean and standard deviation
mu_x = np.mean(x) 
sig_x = np.std(x)
theo_calc =beta
exp_meas = beta

print("Exponentially Random Variable")
print("Expectation Experimental Measurement:", mu_x)
print("Expectation Theoretical  Measurement for Expectation:", theo_calc)
print("Starndard Deviation Experimental Measurement:",sig_x)
print("Standard DeviaitonTheoretical  Measurement:",exp_meas)
print("\n")


#----- 1.3 Simulate a Normal Random Variable -------------
mu = 2.5; sigma = 0.75; a=1; b=5; 

# Generate the vles of the RV x
x = np.random.normal(mu,sigma,n) 

# Create bins and histogram
nbins = 30;     # Number of bins
edgecolor = 'w' # Color seperating bars in the bargraph 

bins = [float(x) for x in np.linspace(a,b,nbins+1)]
h1, bin_edges = np.histogram(x,bins,density=True)

# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges) - 1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1+be2)/2
barwidth = b1[1] - b1[0] #Width of bars in the bargraph
plt.close('all')

# Plot the Bar Graph
fig1 = plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

# Plot the Normal PDF
def NormPDF(mu,sigma,x):
    f=((1/(sigma*math.sqrt(2*math.pi)))*(np.exp((-1*((x-mu)**2))/(2*(sigma**2)))*np.ones(np.size(x))))
    return f

f = NormPDF(mu,sigma,b1)

plt.plot(b1,f,'r')
plt.title('Normal Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')
plt.show()

# Calculate the mean and standard deviation
mu_x = np.mean(x) 
sig_x = np.std(x)
theo_calc = mu
exp_meas = sigma

print("Normal Random Variable")
print("Expectation Experimental Measurement:", mu_x)
print("Expectation Theoretical  Measurement for Expectation:", theo_calc)
print("Stanndard Deviation Experimental Measurement:",sig_x)
print("Standard DeviaitonTheoretical  Measurement:",exp_meas)
print("\n")