import pandas as pd

def baseinas_clean():
    baseinas_df = pd.read_csv('Baseino laisvos vietos.csv')
    baseinas_df['Data_laikas'] = pd.to_datetime(baseinas_df['Data_laikas'])
    baseinas_df['Year'] = baseinas_df['Data_laikas'].dt.year
    baseinas_df['Month'] = baseinas_df['Data_laikas'].dt.strftime('%B')
    baseinas_df['Day'] = baseinas_df['Data_laikas'].dt.day
    baseinas_df['Hour'] = baseinas_df['Data_laikas'].dt.strftime('%H')
    baseinas_df['Weekday'] = baseinas_df['Data_laikas'].dt.day_name()


    # cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    baseinas_cleen_df = baseinas_df[['Year', 'Month', 'Day', 'Weekday', 'Hour', 'Laisvos_vietos']]
    # baseinas_cleen_df['Weekday'] = pd.Categorical(baseinas_cleen_df['Weekday'], categories=cats, ordered=True)
    # baseinas_cleen_df = baseinas_cleen_df.sort_values('Weekday')

    baseinas_cleen_df.to_csv('Baseino_laisvos_vietos_cleen.csv',index=False)
    print(f'Baseino_laisvos_vietos_cleen: issaugota')
    # print(baseinas_cleen_df)

# baseinas_clean()

