class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.__get_score_for_equal_points()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.__get_score_for_over_four()
        else:
            return self.__get_score_for_other()

    def __get_score_for_other(self):
        possible_scores = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{possible_scores[self.player1_score]}-{possible_scores[self.player2_score]}"

    def __get_score_for_over_four(self):
        minus_result = self.player1_score - self.player2_score
        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def __get_score_for_equal_points(self):
        possible_scores = ["Love-All", "Fifteen-All", "Thirty-All"]
        if self.player1_score < 3:
            return possible_scores[self.player1_score]
        else:
            return "Deuce"
