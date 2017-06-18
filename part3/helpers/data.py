import pandas as pd
import numpy as np
from os import listdir

data = {}
clean_names = {
    "dailyElectricityWithFeatures": 'electricity',
    "dailyChilledWaterWithFeatures": "water",
    "dailySteamWithFeatures": "steam"
}


def get_data(filename):
    df = pd.read_excel(filename)
    df = df.drop('startDay', 1).drop('endDay', 1)
    df = df.fillna(0)
    return df

path = 'Data/'
for f in listdir(path):
    tmp = get_data(path + f)
    data[clean_names[f.split('.')[0]]] = tmp

e = data['electricity']
w = data['water']
e_w = w.reset_index().merge(e, how='outer', on=list(e.columns[1:])).set_index('index')
s = data['steam']
df = e_w.reset_index().merge(s, how='outer', on=list(e.columns[1:])).set_index('index')
df = df[['electricity-kWh', 'chilledWater-TonDays', 'steam-LBS'] + list(e.columns[1:])]

column_details = {
    "coolingDegrees": "if T-C - 12 > 0, then = T-C - 12, else = 0. Assume that when outdoor temperature is below 12C, no cooling is needed, which is true for many buildings. This will be useful for daily prediction, because the average of hourly cooling degrees is better than average of hourly temperature.",
    "cosHour": "$\text{cos}(\text{hourOfDay} \cdot \frac{2\pi}{24})$",
    "dehumidification": "if humidityRatio - 0.00886 > 0, then = humidityRatio - 0.00886, else = 0. This will be useful for chilled water prediction, especially daily chilled water prediction.",
    "heatingDegrees": "if 15 - T-C > 0, then = 15 - T-C, else = 0. Assume that when outdoor temperature is above 15C, no heating is needed. This will be useful for daily prediction, because the average of hourly heating degrees is better than average of hourly temperature.",
    "occupancy": "A number between 0 and 1. 0 indicated no occupants, 1 indicates normal occupancy. This is an estimate based on holidays, weekends and school academic calendar.",
    "pressure-mbar": "atmospheric pressure",
    "RH-%": "Relative humidity",
    "T-C": "Dry-bulb temperature",
    "Tdew-C": "Dew-point temperature",
    "Humidity ratio": "Humidity ratio is calcluated based on T-C, RH and pressure. Humidity ratio is important for chilled water prediction as chilled water is also used to dry the air discharged to rooms. Using humidity ratio will be more efficient and effective than using RH and dew point temperature."
}