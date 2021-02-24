# -*- coding: utf-8 -*-
"""

parabolaFit - a Python package for determining the closest parabola to a linear
trend line. Reasons to find a closest fit parabola to a trend line include
analyzing the risk that an apparently linear trend is actually parabolic,
determining best exit point of short sales, and fitting a parabola with an 
amount of data not sufficient to fit 3 degrees of freedom but sufficient to 
fit 2.

Current version is just the trendParabola class, which is sufficient to the
purpose if the inflection point is known. Later versions may include methods 
for locating inflection points.

trendParabola - a class that finds and analyzes the closes parabola to a trend
line for a given inflection point. Requires the x-values of the data point at
which the trend line was fit, in order to avoid extrapolation fallacies.

Inputs required:
    
    X - the list of scalar values at which the trend line was fit.
    m - the trendline slope
    b - the trendline y-intercept
    I - the inflection point
    zrsub - Optional input to indicate zero substitution used to guard against
        divide by zero errors. Default setting is 10**-13. Note that a message
        prints whenever the zero substitution is initiated.

Created on Thu Jan  7 10:46:43 2021

@author: Alexander Fretheim
"""

class trendParabola:
    def __init__(self, X, m, B, I, zrsub = 0.000000000001):
        self.m = m;
        self.b = B;
        self.I = I;
        self.trainingset = X;
        a = 0.0;
        b = 0.0;
        
        for x in X:
            print(x);
            t = float(x)
            a += m*t + B
            print(str(m*t + B) + " added to numerator.");
            b += t**2 - 2*t*I + I**2
            print(str(t**2 - 2*t*I + I**2) + "added to denominator.");
    
        if b == 0:
            b = zrsub;
            print("Zero substitution in use.")
            
        self.c = a/b #c*(x-i)**2 is the closest fit parabola
        print("Resultant c is " + str(self.c));
    
    def predictY(self, x):
        return self.c*(x-self.I)**2
    
    def predictYs(self, X):
        ret = [];
        for x in X:
            ret.append(self.predictY(x));
        return ret;
    
    def getCoefficients(self):
        return (self.c, self.I);
    
    #note that Y must be at least as large as X, and if larger, the last values are ignored:
    def getResiduals(self, Y):
        ret = [];
        i = 0;
        for x in self.trainingset:
            ret.append(Y[i] - self.predictY(x));
            i += 1;
        return ret;