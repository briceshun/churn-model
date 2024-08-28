from scipy.stats import ttest_ind
import numpy as np

def t_test(
    x: list, 
    y: list,
    alternative: str,
    var: bool
    ) -> float:

    _, double_p = ttest_ind(x,y,equal_var=var)
    if alternative == 'both':
        pval = double_p
    elif alternative == 'greater':
        if np.mean(x) > np.mean(y):
            pval = double_p/2.00
        else:
            pval = 1.00 - double_p/2.00
    elif alternative == 'less':
        if np.mean(x) < np.mean(y):
            pval = double_p/2.00
        else:
            pval = 1.00 - double_p/2.00
    return pval