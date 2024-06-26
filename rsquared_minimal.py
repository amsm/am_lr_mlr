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

def r2_2(
    observed,
    predicted
):
    v_sst = sst(observed)
    v_sse = sse(observed, predicted)
    return 1 - (v_sse/v_sst)
# def re_2

def compute_m_b(
    p_x,
    p_y
):
    sum_x = sum(p_x)
    sum_y = sum(p_y)
    sum_xy = sum ( [(x*y) for x,y in zip(p_x, p_y)] )
    sum_x2 = sum ( [x**2 for x in p_x] )

    n = len(p_x)

    n = n*sum_xy - (sum_x * sum_y)
    d = n*sum_x2 - sum_x**2

    m  = n/d

    nb = sum_y - m*sum_x
    db = n
    b = nb/db

    return m, b
# def compute_m_b   

