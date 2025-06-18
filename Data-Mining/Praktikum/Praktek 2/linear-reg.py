import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cellphonelabel = ["nama", "camera", "price"]
cellphonename = ["H1", "H2", "H3", "H4", "H5", "H6"]
cellphonecamera = [8, 2, 6, 9, 4, 5, 7, 3]
cellphoneprice = [7, 3, 7, None, 2, None, 8, 3]

# Create Data Dictionary
D = {cellphonelabel[0]:cellphonename, cellphonelabel[1]:cellphonecamera, cellphonelabel[2]:cellphoneprice}

# Import Data dictionary to pandas dataframe
df = pd.DataFrame(data=D)

# Find Sigma Y
sigmaY = sum(filter(lambda y: isinstance(y, int), cellphoneprice))

# Find X^2, X, XY
SigmaXSquare = 0
SigmaX = 0
SigmaXY = 0
datalength = 0

for index, val in enumerate(cellphonecamera):
    if isinstance(cellphoneprice[index], int):
        SigmaXSquare += val**2
        SigmaX += val
        SigmaXY += val*cellphoneprice[index]
        datalength += 1

    sumsigmaXSquare = SigmaX**2

    # Find Constanta beta 0
    constanta = ()
