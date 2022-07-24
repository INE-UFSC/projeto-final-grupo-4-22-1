import pickle


class RankingDAO:
    def __init__(self, datasource='ranking.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource,'wb'))
    
    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource,'rb'))

    def get_ranking(self):
        return self.__object_cache

    def replace(self, ranking):
        self.__object_cache = ranking
        self.__dump()
