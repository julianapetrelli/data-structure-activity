from array import array
import json
import random
import pandas as pd
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def estados(self, data) -> None:
        pass


class Nordeste(Strategy):
    def estados(self) -> array:
        options = [
            'Alagoas',
            'Bahia',
            'Ceará',
            'Maranhão',
            'Paraíba',
            'Pernambuco',
            'Piauí',
            'Rio Grande do Norte',
            'Sergipe'
        ],
        return options


class Norte(Strategy):
    def estados(self) -> array:
        options = [
            'Acre',
            'Amapá',
            'Amazonas',
            'Pará',
            'Rondônia',
            'Roraima',
            'Tocantins'
        ],

        return options


class CentroOeste(Strategy):
    def estados(self) -> array:
        options = [
            'Distrito Federal',
            'Goiás',
            'Mato Grosso',
            'Mato Grosso do Sul'
        ],

        return options


class Sudeste(Strategy):
    def estados(self) -> array:
        options = [
            'Espírito Santo',
            'Minas Gerais',
            'Rio de Janeiro',
            'São Paulo'
        ],
        return options


class Sul(Strategy):
    def estados(self) -> array:
        options = [
            'Paraná',
            'Rio Grande do Sul',
            'Santa Catarina'
        ],
        return options


class Sumario:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def format_json(self) -> None:
        data = self._strategy.estados()

        with open('sumario.json', 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def format_csv(self) -> None:
        data = self._strategy.estados()

        df = pd.DataFrame(data)
        df.to_csv('sumario.csv', index=False, encoding='utf-8', sep=';')


def main():
    regions = [Nordeste(), Norte(), CentroOeste(), Sudeste(), Sul()]
    region = random.choice(regions)

    sumario = Sumario(region)
    print(sumario.format_json())
    print(sumario.format_csv())


if __name__ == "__main__":
    main()
    
