''' Twoway Analysis of Variance (ANOVA)

'''

'''
Author:  Thomas Haslwanter
Date:    March-2013
Version: 1.1
'''

import pandas as pd
from getdata import getData
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

def anova_interaction():
    '''ANOVA with interaction: Measurement of fetal head circumference,
    by four observers in three fetuses.'''
    
    # Get the data
    data = getData('altman_12_6.txt')
    
    # Bring them in dataframe-format
    df = pd.DataFrame(data, columns=['hs', 'fetus', 'observer'])
    
    # Determine the ANOVA with interaction
    formula = 'hs ~ C(fetus) + C(observer) + C(fetus):C(observer)'
    lm = ols(formula, df).fit()
    print anova_lm(lm)

if __name__ == '__main__':
    anova_interaction()
