## COMP1730/6730 S1 2020 - Homework 5
# Submission is due 11:55pm, Thursday the 7th of May, 2020.

## YOUR ANU ID: u7075106
## YOUR NAME: MAITREYI SINGH

## Implement the function interpolate below.
## (The statement "pass" is just a placeholder that does nothing: you
## should replace it.)
## You can define other functions if it helps you decompose the problem
## and write a better organised and/or more readable solution.

def interpolate(x, y, x_test):
    ''' Input - This function takes two sequences i.e. x and y and one
            parameter 'x_test' which is the test case.
        Functionality - This function interpolates the values to find
            the value of the test case. The equation of line used: 
            y = a*x + b.
        Output - Returns the corresponding interpolated value for the 
            test case (x_test). '''
    
    if x_test in x:
        return y[x.index(x_test)]
    else:
        i = 0
        while i < len(x):
           if x[i] > x_test:
               x_above = x[i] ## x_above = x point just above the test case
               x_below = x[i-1] ## x_below = x point just below the test case
               break
           i += 1
        y_above = y[i] ## y_above = y point just above the test case
        y_below = y[i-1] ## y_below = y point just below the test case
        
        ## a = slope of the line
        a = calculate_slope(x_above, y_above, x_below, y_below)
        
        ## b = intercept of the line
        b = calculate_intercept(a, x_below, y_below)
        
        return (a*x_test)+b
            

def calculate_slope(x2, y2, x1, y1):
    ''' Input - Takes 4 double parameters i.e 2 pair of coordinates.
        Functionality - Calculates the slope of the line formed by coordinates
            (x2, y2) and (x1,y1).
        Output - Returns slope as double.'''
        
    return (y2-y1)/(x2-x1)
    
        

def calculate_intercept(slope, x, y):
    ''' Input - Takes 3 double parameters : slope and x and y coordinates
            of the point just below the test case.
        Functionality - Calculates the intercept.
        Output - Returns intercept as double.'''
        
    return y-(slope*x)