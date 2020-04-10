

import numpy as np
import random 
import matplotlib.pyplot as plt

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 1 - Simulate continuous RV w/ selected distributions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

a = 1.0
b = 4.0
n = 10000

""" 1.1 - Simulate a Uniform Random Variable """

# Generate the values of the RV x
x = np.random.uniform(a,b,n) # Uniform

# Create bins and histogram
nbins = 30 # Number of bins
edgecolor = 'w';  #color separating bars
bins = [float(x) for x in np.linspace(a,b,nbins+1)]
# bins = [float(x) for x in np.linspace(a,b,nbins+1)]  # Make linspace for 1,400
h1, bin_edges = np.histogram(x,bins,density=True)
# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges)-1]
be2 = bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] #width of bars in bargraphs

# Plot the bar graph
fig1 = plt.figure(1)
plt.bar(b1,h1,width=barwidth, edgecolor=edgecolor)

# Plot the uniform pdf
def UniPDF(a,b,x):
    f=(1/abs(b-a))*np.ones(np.size(x))
    return f
f = UniPDF(a,b,b1)
plt.plot(b1,f,'r')

plt.title('Uniform Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')

plt.show()

# Calculate theoretical and measured mean and standard deviation
mu_x=np.mean(x)
sig_x=np.std(x)
theoretical_mu_x = a + b/2
theoretical_sig_x = (b-a)**2/12

print("1.1 - Uniform Random Variable Calculations")
print("Experimental Measurement for Expectation:", mu_x)
print("Theoretical  Measurement for Expectation:", theoretical_mu_x)
print("Experimental Measurement for Standard Deviation:",sig_x)
print("Theoretical  Measurement for Standard Deviation:",theoretical_sig_x)
print("")


""" 1.2 - Simulate an Exponentially distributed Random Variable """
a=1; b=200; n=10000; beta = 40

# Generate the values of the RV x
x = np.random.exponential(beta,n) # Exponential

# Create bins and histogram
nbins = 30 # Number of bins
edgecolor = 'w';  #color separating bars
bins = [float(x) for x in np.linspace(a,b,nbins+1)]
# bins = [float(x) for x in np.linspace(a,b,nbins+1)]  # Make linspace for 1,400
h1, bin_edges = np.histogram(x,bins,density=True)
# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges)-1]
be2 = bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] #width of bars in bargraphs

# Plot the bar graph
fig1 = plt.figure(1)
plt.bar(b1,h1,width=barwidth, edgecolor=edgecolor)

# Plot the exponential pdf
def ExpPDF(beta,x):
    f=(1/beta) * np.exp((-1 / beta) * x)* np.ones(np.size(x))
    return f
f = ExpPDF(beta,b1)
plt.plot(b1,f,'r')

plt.title('Exponential Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')

plt.show()

# Calculate theoretical and measured mean and standard deviation
mu_x=np.mean(x)
sig_x=np.std(x)
theoretical_mu_x = beta
theoretical_sig_x = beta

print("1.2 - Exponential Random Variable Calculations")
print("Experimental Measurement for Expectation:", mu_x)
print("Theoretical  Measurement for Expectation:", theoretical_mu_x)
print("Experimental Measurement for Standard Deviation:",sig_x)
print("Theoretical  Measurement for Standard Deviation:",theoretical_sig_x)
print("")


""" 1.3 - Simulate an Normal Random Variable """
a=0; b=5; mu=2.5; sigma=0.75; n=10000

import math

# Generate the values of the RV x
x = np.random.normal(mu,sigma,n) # Exponential

# Create bins and histogram
nbins = 30 # Number of bins
edgecolor = 'w';  #color separating bars
bins = [float(x) for x in np.linspace(a,b,nbins+1)]
# bins = [float(x) for x in np.linspace(a,b,nbins+1)]  # Make linspace for 1,400
h1, bin_edges = np.histogram(x,bins,density=True)
# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges)-1]
be2 = bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] #width of bars in bargraphs

# Plot the bar graph
fig1 = plt.figure(1)
plt.bar(b1,h1,width=barwidth, edgecolor=edgecolor)

# Plot the exponential pdf
def NormPDF(mu, sigma,x):
    f=(   (1/(sigma * math.sqrt(2 * math.pi))) * np.exp((-1 * ((x - mu)**2)) / (2 * (sigma**2))    )           * np.ones(np.size(x)))
    return f
f = NormPDF(mu,sigma,b1)
plt.plot(b1,f,'r')

plt.title('Normal Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')

plt.show()


# Calculate theoretical and measured mean and standard deviation
mu_x=np.mean(x)
sig_x=np.std(x)
theoretical_mu_x = mu
theoretical_sig_x = sigma

print("1.3 - Normal Random Variable Calculations")
print("Experimental Measurement for Expectation:", mu_x)
print("Theoretical  Measurement for Expectation:", theoretical_mu_x)
print("Experimental Measurement for Standard Deviation:",sig_x)
print("Theoretical  Measurement for Standard Deviation:",theoretical_sig_x)
print("")

