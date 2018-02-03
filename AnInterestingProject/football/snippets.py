df = pd.merge(
    dfh,
    dfa,
    how='outer',
    left_on=['HomeTeam'],
    right_on=['AwayTeam'],
    suffixes=('_H', '_A')
)

df['THG'] = df.groupby(['HomeTeam'])['FTHG'].cumsum()
df['TAG'] = df.groupby(['AwayTeam'])['FTAG'].cumsum()
dfh = df[['Date', 'HomeTeam', 'THG']]
dfa = df[['Date', 'AwayTeam', 'TAG']]
df = df.sort_values(by=['AwayTeam', 'Date'])
