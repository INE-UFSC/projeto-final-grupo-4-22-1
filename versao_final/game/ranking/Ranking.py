from game.ranking.RankingDAO import RankingDAO


class Ranking:
    def __init__(self):
        self.__rankingDAO = RankingDAO()
        if self.__rankingDAO.get_ranking() == {}:
            self.__ranking = {'primeiro': ['', 0], 'segundo': ['', 0], 'terceiro': ['', 0], 'quarto': ['', 0], 'quinto': ['', 0]}
        else:
            self.__ranking = self.__rankingDAO.get_ranking()

    def atualiza_ranking(self, usuario, pontuacao):
        if pontuacao > self.__ranking['primeiro'][1]:
            self.__ranking['quinto'] = self.__ranking['quarto']
            self.__ranking['quarto'] = self.__ranking['terceiro']
            self.__ranking['terceiro'] = self.__ranking['segundo']
            self.__ranking['segundo'] = self.__ranking['primeiro']
            self.__ranking['primeiro'] = [usuario, pontuacao]
        elif pontuacao > self.__ranking['segundo'][1]:
            self.__ranking['quinto'] = self.__ranking['quarto']
            self.__ranking['quarto'] = self.__ranking['terceiro']
            self.__ranking['terceiro'] = self.__ranking['segundo']
            self.__ranking['segundo'] = [usuario, pontuacao]
        elif pontuacao > self.__ranking['terceiro'][1]:
            self.__ranking['quinto'] = self.__ranking['quarto']
            self.__ranking['quarto'] = self.__ranking['terceiro']
            self.__ranking['terceiro'] = [usuario, pontuacao]
        elif pontuacao > self.__ranking['quarto'][1]:
            self.__ranking['quinto'] = self.__ranking['quarto']
            self.__ranking['quarto'] = [usuario, pontuacao]
        elif pontuacao > self.__ranking['quinto'][1]:
            self.__ranking['quinto'] = [usuario, pontuacao]

        self.__rankingDAO.replace(self.__ranking)
        print(self.__ranking)

    def reset_ranking(self):
        self.__ranking = {'primeiro': ['', 0], 'segundo': ['', 0], 'terceiro': ['', 0], 'quarto': ['', 0], 'quinto': ['', 0]}
        self.__rankingDAO.replace(self.__ranking)

    @property
    def ranking(self):
        return self.__ranking
