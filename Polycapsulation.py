class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"player - : {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_scores):
        if new_scores >= 0:
            self.__score = new_scores
            print(f"score updated to {self.__score}")
        else:
            print("Score cannot be updated.")

class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"player - : {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} dribbles and scores")

    def get_score(self):
        return self.__score

    def set_score(self, new_scores):
        if new_scores >= 0:
            self.__score = new_scores
            print(f"score updated to {self.__score}")
        else:
            print("score cannot be updated.")

cricket = Cricket("virat", 100)
football = Football("Messi", 200)

print(" === Sports Score Board ===")
cricket.info()
football.info()