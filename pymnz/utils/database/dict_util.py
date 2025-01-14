import pandas as pd


# Função para substituir valores indesejados por None
def replace_invalid_values(values):
    for record in values:
        for key, value in record.items():
            # Substituir pd.NaT, np.nan, e datas inválidas por None
            if pd.isna(value):
                record[key] = None
    return values
