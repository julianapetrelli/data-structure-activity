import pandas as pd

# Crie um método estatístico para sumarizar o total de regiões

def total_estados_regiao_pandas():
    estados = {
        'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins'],
        'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
        'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul'],
        'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'],
        'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
    }
    
    df = pd.DataFrame(estados)
    df = df.count()
    return df

# Crie um método estatístico para sumarizar o total de estados

def total_regioes_pandas():
    estados = {
        'Acre': 'Norte',
        'Amapá': 'Norte',
        'Amazonas': 'Norte',
        'Pará': 'Norte',
        'Rondônia': 'Norte',
        'Roraima': 'Norte',
        'Tocantins': 'Norte',
        'Alagoas': 'Nordeste',
        'Bahia': 'Nordeste',
        'Ceará': 'Nordeste',
        'Maranhão': 'Nordeste',
        'Paraíba': 'Nordeste',
        'Pernambuco': 'Nordeste',
        'Piauí': 'Nordeste',
        'Rio Grande do Norte': 'Nordeste',
        'Sergipe': 'Nordeste',
        'Distrito Federal': 'Centro-Oeste',
        'Goiás': 'Centro-Oeste',
        'Mato Grosso': 'Centro-Oeste',
        'Mato Grosso do Sul': 'Centro-Oeste',
        'Espírito Santo': 'Sudeste',
        'Minas Gerais': 'Sudeste',
        'Rio de Janeiro': 'Sudeste',
        'São Paulo': 'Sudeste',
        'Paraná': 'Sul',
        'Rio Grande do Sul': 'Sul',
        'Santa Catarina': 'Sul'
    }
    
    df = pd.DataFrame(estados)
    df = df.count()
    return df

# Crie um método estatístico para coletar a primeira região e estado em uma lista

def primeira_regiao_estado_pandas():
    estados = {
        'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins'],
        'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
        'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul'],
        'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'],
        'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
    }
    df = pd.DataFrame(estados)
    df = df.iloc[0][0]
    return df

# Crie um método estatístico para coletar a última região e estado em uma lista

def ultima_regiao_estado_pandas():
    estados = {
        'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins'],
        'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
        'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul'],
        'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'],
        'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
    }
    df = pd.DataFrame(estados)
    df = df.iloc[-1][-1]
    return df