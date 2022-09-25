# Criar um método para retornar a região dado um estado

def regiao_estado(estado):
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
    return estados[estado]