import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


def get_data():
    DATA_SET = '../data/E0 (1).csv'
    df = pd.read_csv(DATA_SET)
    return df[df.columns[1:6]]


# tips[(tips['size'] >= 5) | (tips['total_bill'] > 45)]
def getGoalsScored(df):
    toDateGoals = None
    dates = df.Date.unique()
    for date in dates:
        toDateHome = df[(df['Date'] < date)].groupby('HomeTeam')['FTHG'].sum().to_frame('TG').reset_index()
        toDateAway = df[(df['Date'] < date)].groupby('AwayTeam')['FTAG'].sum().to_frame('TG').reset_index()

        data = pd.merge(
            toDateHome,
            toDateAway,
            how='outer',
            left_on=['HomeTeam'],
            right_on=['AwayTeam'],
            suffixes=('_H', '_A')
        )
        data['Date'] = date
        data['Team'] = data.HomeTeam.combine_first(data.AwayTeam)
        if toDateGoals is not None:
            toDateGoals = toDateGoals.append(data)
        else:
            toDateGoals = data

    return toDateGoals[['Date', 'Team', 'TG_H', 'TG_A']].fillna(value=0)


# FTHG    FTAG
raw = get_data()
raw['Date'] = pd.to_datetime(raw.Date, dayfirst=True)
totalGoals = getGoalsScored(raw)
totalGoals = totalGoals.sort_values(by=['Date', 'Team'])
modelData = pd.merge(
    raw,
    totalGoals,
    how='left',
    left_on=['HomeTeam', 'Date'],
    right_on=['Team', 'Date'],
)
modelData = pd.merge(
    modelData,
    totalGoals,
    how='left',
    left_on=['AwayTeam', 'Date'],
    right_on=['Team', 'Date'],
    suffixes=('_HOMETEAM', '_AWAYTEAM')
)
modelData = modelData[[
    'Date',
    'HomeTeam',
    'Team_HOMETEAM',
    'Team_AWAYTEAM',
    'FTHG',
    'TG_H_HOMETEAM',
    'TG_A_HOMETEAM',
    'AwayTeam',
    'FTAG',
    'TG_H_AWAYTEAM',
    'TG_A_AWAYTEAM',
]].fillna(value=0)
modelData['TGames_H_HOMETEAM'] = modelData.groupby(['HomeTeam', 'Team_HOMETEAM'])['Date'].cumcount()
modelData['TGames_A_HOMETEAM'] = modelData.groupby(['HomeTeam', 'Team_AWAYTEAM'])['Date'].cumcount()
modelData['FT'] = modelData['FTAG'] + modelData['FTHG'] > 1
modelData['TG_HOMETEAM'] = modelData['TG_H_HOMETEAM'] + modelData['TG_A_HOMETEAM']
modelData['TG_AWAYTEAM'] = modelData['TG_H_AWAYTEAM'] + modelData['TG_A_AWAYTEAM']

print(modelData.tail(30))
corr = modelData.corr()
plt.pcolor(modelData.corr(), cmap='RdBu_r', vmax=1, vmin=-1)
plt.colorbar()
plt.yticks(np.arange(0.1, len(corr.index), 1), corr.index)
plt.yticks(np.arange(0.5, len(corr.index)), corr.index)
plt.xticks(np.arange(0.1, len(corr.index), 1), corr.index)
plt.xticks(np.arange(0.5, len(corr.index)), corr.index, rotation='vertical')
# plt.show()
