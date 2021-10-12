#!/usr/bin/env python
import pandas as pd
import sqlite3
from pycaret.regression import *

con = sqlite3.connect('/Users/adg/InsuranceBill/pred_insurance_bill/insurance_db/insurance.db')

df = pd.read_sql("SELECT * FROM InsuaranceTable", con)
df = df.drop('ID', axis = 1)

r2 = setup(df, target = 'charges',
           normalize = True,
           polynomial_features = True,
           trigonometry_features = True,
           bin_numeric_features = ['age', 'bmi'])

lr = create_model('lr')

plot_model(lr, plot = 'residuals')

save_model(lr, model_name = 'lr_model')
