import statistics

def sst(
    observed
):
    mean = statistics.mean(observed)
    squared_dists = [(value-mean)**2 for value in observed]
    return sum(squared_dists)
# def sst

def ssr(
    observed,
    predicted
):
    mean = statistics.mean(observed)
    squared_dists = [(value-mean)**2 for value in predicted]
    return sum(squared_dists)
# def ssr

def sse(
    observed,
    predicted
):
    squared_dists = [(o-p)**2 for o,p in zip(observed, predicted)]
    return sum(squared_dists)
# def sse

def r2_1(
    observed,
    predicted
):
    v_sst = sst(observed)
    v_ssr = ssr(observed, predicted)
    return v_ssr / v_sst
# def r2_1

# preferred to r2_1
def r2_2(
    observed,
    predicted
):
    v_sst = sst(observed)
    v_sse = sse(observed, predicted)
    return 1 - (v_sse/v_sst)
# def r2_2

def compute_m_b(
    p_x,
    p_y
):
    sum_x = sum(p_x)
    sum_y = sum(p_y)
    sum_xy = sum ( [(x*y) for x,y in zip(p_x, p_y)] )
    sum_x2 = sum ( [x**2 for x in p_x] )

    n = len(p_x)

    numerator = n*sum_xy - (sum_x * sum_y)
    denominator = n*sum_x2 - sum_x**2

    # compute m
    m = numerator/denominator

    numerator = sum_y - m*sum_x
    denominator = n
    # compute b
    b = numerator/denominator

    return m, b
# def compute_m_b

#-----------------------------------------------------------------------------------------------------------------------
x_months = [1,2,3,4,5,6,7,8,9,10,11,12] # months

#-----------------------------------------------------------------------------------------------------------------------
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
m, b = compute_m_b(
    p_x = x_months,
    p_y = y_total_rain_fall
)

msg0 = f"slope: {m} ; b={b}"
print(msg0)

predicted_y_by_linear_regression = [(m*x + b) for x in x_months]

SST = sst(
    observed=y_total_rain_fall
)
msg = f"SST={SST}"
print(msg)

SSR = ssr(
    observed=y_total_rain_fall,
    predicted=predicted_y_by_linear_regression,
)

SSE = sse(
    observed=y_total_rain_fall,
    predicted=predicted_y_by_linear_regression,
)

r2_1 = r2_1(
    observed=y_total_rain_fall,
    predicted=predicted_y_by_linear_regression,
)

r2_2 = r2_2(
    observed=y_total_rain_fall,
    predicted=predicted_y_by_linear_regression,
)

msg1 = f"R**2=SSR/SST={SSR}/{SST}={r2_1}"
print(msg1)

msg2 = f"R**2=1-(SSE/SST)=1-{SSE}/{SST}={r2_1}"
print(msg2)

"""
CORRECT:
slope: 34.95454545454545 ; b=-24.787878787878793
R**2=SSR/SST=174720.2954545454/176118.9166666667=0.9920586542400304
R**2=1-(SSE/SST)=1-1398.6212121212131/176118.9166666667=0.9920586542400304

"""