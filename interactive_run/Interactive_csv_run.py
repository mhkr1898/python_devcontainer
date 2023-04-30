import pandas as pd
from src.functions.

ORIGINAL = "interactive_run/sample.csv"
DF_ORIGINAL = pd.read_csv(ORIGINAL, sep=";")
DF = DF_ORIGINAL.copy()
#* START
DF['Country'] = 'EU'


#* END
DF.to_csv("tempsample.csv", sep=";", index=False)