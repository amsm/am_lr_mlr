# r_squared_by_hand.py

import math
import statistics
"""
Month	Min rainfall	Max rainfall	Total rainfall
1	22	30	24
2	22	25	48
3	25	27	75
4	49	54	128
5	8	8	136
6	29	47	168
7	40	41	209
8	35	63	263
9	14	25	277
10	45	57	333
11	20	39	364
12	39	51	404
"""

#-----------------------------------------------------------------------------------------------------------------------
x_months = [1,2,3,4,5,6,7,8,9,10,11,12] # months

#-----------------------------------------------------------------------------------------------------------------------

# the observed values
# total rain fall per month
y_total_rain_fall = [
    24,
    48,
    75,
    128,
    136,
    168,
    209,
    263,
    277,
    333,
    364,
    404,
]

#-----------------------------------------------------------------------------------------------------------------------
# 1 - compute SST "Sum of Squares Total" AKA "Total Sum of Squares"
# SST = sum( (Y - Ymean)^2 )
# The variance in the "response variable" that needs to be explained
# SST = "Sum of Squares Total"
def r_squared_aux_sst(
    p_observed_values:list
):
    mean = statistics.mean(p_observed_values)

    sum = 0
    for current_observed_value in p_observed_values:
        current_observed_value_distance_to_mean =\
            current_observed_value - mean
        abs_value = math.fabs(
            current_observed_value_distance_to_mean
        )
        square = abs_value**2
        sum+=square
    # for

    return sum
# def r_squared_aux_sst

#-----------------------------------------------------------------------------------------------------------------------
# 2 - compute SSR (Sum of Squares Regression)
# SSR = sum( (Ypred - Ymean)^2 )
"""
"the amount of variance explained by the model"

a measure of how well the regression model captures the variance in the observed data.
If the model fits well, most of the variance in the observed y will be close to the variance in the predicted y,
leading to a high SSR.
"""

def r_squared_aux_ssr(
    p_observed_value:list,
    p_predicted_values:list
):
    Ymean = statistics.mean(p_observed_value)
    sum = 0
    for current_predicted_value in p_predicted_values:
        diff_to_Ymean = abs(
            current_predicted_value - Ymean
        )
        diff_squared = diff_to_Ymean**2
        sum += diff_squared
    # for

    return sum
# def r_squared_aux_ssr

#-----------------------------------------------------------------------------------------------------------------------
# 3 - compute SSE
# SSE = "Residual Sum of Squares"
# SSE = sum ( Y-Ypred)^2 )
#-----------------------------------------------------------------------------------------------------------------------
# SSE = "Sum of Squares of rEsiduals"
# SSE indicates the discrepancy between the data and an estimation model.
# A low SSE indicates a tight fit of the model to the data.
def r_squared_aux_sse(
    p_observed_values:list,
    p_predicted_values:list
):
    residuals:list = [(observed-predicted)**2 for observed, predicted in zip(p_observed_values, p_predicted_values)]
    return sum(residuals)
# def r_squared_residual_sum_of_squares_sse