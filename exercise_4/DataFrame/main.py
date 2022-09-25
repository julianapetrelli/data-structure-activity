import pandas as pd

# Criar um método para retornar a região dado um estado utilizando DataFrame


def regiao_estado_pandas(estado):
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
    df = df[estado]
    return df

# Crie um método para retornar os estados de uma região do Brasil utilizando DataFrame

def estados_regiao_pandas(regiao):
    estados = {
        'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins'],
        'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
        'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul'],
        'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'],
        'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
    }
    df = pd.DataFrame(estados)
    df = df[regiao]
    return df