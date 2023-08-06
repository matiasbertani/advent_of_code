from pathlib import Path

# Constants
rock = 'rock'
paper = 'paper'
scissors = 'scissors'

win = 'win'
draw = 'draw'
lose = 'lose'


class Tournament:

    def __init__(self, matches: list):
        self.matches = matches

    def print_strategies_scores(self):
        print('First strategy: ', self.first_strategy_score)
        print('Second strategy: ', self.second_strategy_score)

    @property
    def first_strategy_score(self):
        return sum([MatchFisrtStrategy(match).score() for match in self.matches])

    @property
    def second_strategy_score(self):
        return sum([MatchSecondtStrategy(match).score() for match in self.matches])


class MatchBase:

    losing_election = {
        rock: scissors,
        paper: rock,
        scissors: paper,
    }
    result_points = {
        lose: 0,
        draw: 3,
        win: 6,
    }
    choice_points = {
        rock: 1,
        paper: 2,
        scissors: 3,
    }

    def __init__(self, match: str) -> None:
        opponent_choice, my_choice = match.strip().split(' ')
        self.my_choice = self.decode_my_choice(my_choice)
        self.opponent_choice = self.decode_opponent_choice(opponent_choice)

    def decode_opponent_choice(self, opponent_choice: str) -> dict:
        raise NotImplementedError

    def decode_my_choice(self, my_choice: str) -> dict:
        raise NotImplementedError

    def score(self) -> int:
        return self.points_for_result + self.points_for_choice

    @property
    def points_for_result(self) -> int:
        raise NotImplementedError

    @property
    def points_for_choice(self) -> int:
        raise NotImplementedError


class MatchFisrtStrategy(MatchBase):

    def decode_opponent_choice(self, opponent_choice: str) -> dict:
        return {
            'A': rock,
            'B': paper,
            'C': scissors,
        }.get(opponent_choice)

    def decode_my_choice(self, my_choice: str) -> dict:
        return {
            'X': rock,
            'Y': paper,
            'Z': scissors,
        }.get(my_choice)

    @property
    def points_for_result(self) -> int:
        return self.result_points.get(self.result())

    def result(self):
        if self.my_choice == self.opponent_choice:
            return draw
        if self.losing_election.get(self.my_choice) == self.opponent_choice:
            return win
        return lose

    @property
    def points_for_choice(self) -> int:
        return self.choice_points.get(self.my_choice)


class MatchSecondtStrategy(MatchBase):

    def decode_opponent_choice(self, opponent_choice: str) -> dict:
        return {
            'A': rock,
            'B': paper,
            'C': scissors,
        }.get(opponent_choice)

    def decode_my_choice(self, my_choice: str) -> dict:
        return {
            'X': lose,
            'Y': draw,
            'Z': win,
        }.get(my_choice)

    @property
    def points_for_result(self) -> int:
        return self.result_points.get(self.my_choice)

    @property
    def points_for_choice(self) -> int:
        return self.choice_points.get(self.choice_from_needed_result)

    @property
    def choice_from_needed_result(self) -> str:
        needed_result = self.my_choice
        return {
            lose: self.losing_election.get(self.opponent_choice),
            draw: self.opponent_choice,
            win: self.losing_election.get(self.losing_election.get(self.opponent_choice)),
        }.get(needed_result)


def get_input():
    current_dir = Path(__file__).parent
    input_filepath = current_dir / '../../inputs/2022/day_2.txt'
    with open(input_filepath) as f:
        data = f.readlines()
    return data


if __name__ == '__main__':
    all_matchs = get_input()
    Tournament(all_matchs).print_strategies_scores()
