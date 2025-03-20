from abc import ABCMeta, abstractmethod
import requests

class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass


class API_Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            dado = requests.get(URL).json()
            return ((dado.get('id'), dado.get('name')))
        except:
            pass

class API_Rick_Morty(API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            data = requests.get(URL).json()
            return ((data.get('id'), data.get('name'), data.get('species')))
        except:
            print("Erro ao consumir a API, verifique o ID, as requisições e tente novamente.")

class API_Star_Wars(API_consumer):
    ''' The universe of Star Wars '''
    def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            data = requests.get(URL).json()
            return ((data.get('name'), data.get('films')))
        except:
            print("Erro ao consumir a API, verifique o ID, as requisições e tente novamente.")
class API_Ice_and_Fire(API_consumer):
    ''' The universe of Ice And Fire '''
    def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            data = requests.get(URL).json()
            return ((data.get('name'), data.get('tvSeries')))
        except:
            print("Erro ao consumir a API, verifique o ID, as requisições e tente novamente.")
