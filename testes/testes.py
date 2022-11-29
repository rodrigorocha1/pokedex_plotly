import pickle


def read_file( mode='../pokemons'):
    with open(mode, 'rb') as fp:
        n_list = pickle.load(fp)
        return n_list


lista_pokemons = read_file()
print(lista_pokemons[649])
