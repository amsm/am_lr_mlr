# r_squared_minimal2.py
import statistics
def sst_v1(p_observed):
    mean = statistics.mean(p_observed)
    sum = 0
    for yi in p_observed:
        diff = yi-mean
        diff = diff**2
        sum+=diff
    # for
    return sum
# def sst_v1

def sst(p_observed):
    mean = statistics.mean(p_observed)

    partials = [(yi-mean) ** 2 for yi in p_observed]

    return sum(partials)
# def sst

# to be used, requires the regression model
def ssr_v1(p_observed, p_predicted):
    mean = statistics.mean(p_observed)
    sum = 0
    for ypredi in p_predicted:
        sqdiff = (ypredi - mean)**2
        sum += sqdiff
    # for
    return sum
# def ssr_v1

# to be used, requires the regression model
def ssr(
    p_observed,
    p_predicted
):
    mean = statistics.mean(p_observed)
    partials = [ (ypred-mean)**2 for ypred in p_predicted ]
    return sum(partials)
# def ssr

def sse_v1(
    p_o,
    p_p
):
    sum = 0
    for idx in range(len(p_o)):
        o = p_o[idx]
        p = p_p[idx]
        diff = (o-p)**2
        sum+=diff
    # for
    return sum
# def sse_v1

def sse(
    p_observed,
    p_predicted
):
    partials = [ (o-p)**2 for o,p in zip(p_observed, p_predicted) ]
    return sum(partials)
# def sse

def m_b(
    p_x,
    p_y
):
    sumx = sum(p_x)
    sumy = sum(p_y)
    sumxy = sum( [x*y for x,y in zip(p_x, p_y)] )
    sumx2 = sum( [x**2 for x in p_x] )

    n = len(p_x)

    num = n * sumxy - sumx*sumy
    den = n * sumx2 - sumx**2

    m = num/den

    num = sumy - m*sumx
    den = n

    b = num/den

    return m, b
# def m_b


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

sst1 = sst_v1(y_total_rain_fall)
sst2 = sst(y_total_rain_fall)
print(sst1)
print(sst2)

m, b = m_b(
    p_x=x_months,
    p_y=y_total_rain_fall
)
msg = (f"m={m} ; b={b}")
print(msg)

y_pred = [ (m*x + b) for x in x_months]

ssr1 = ssr_v1(p_observed=y_total_rain_fall,p_predicted=y_pred)
ssr2 = ssr(p_observed=y_total_rain_fall,p_predicted=y_pred)

sse1 = sse_v1(p_o=y_total_rain_fall, p_p = y_pred)
sse2 = sse(p_observed=y_total_rain_fall, p_predicted=y_pred)

msg = f"ssr1={ssr1} ; ssr2={ssr2} ; sse1={sse1} ; sse2={sse2}"
print(msg)