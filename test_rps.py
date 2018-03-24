# rps.py

import pytest
import subprocess
import sys
import rps

def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True


def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True


def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True


def test_egg_is_invalid_play():
    assert rps.is_valid_play('egg') is False


def test_random_play_is_valid():
    for _ in range(100):
        play = rps.random_play()
        assert rps.is_valid_play(play)


def test_random_play_is_fairish():
    """This should work in most universes!"""
    plays = [rps.random_play() for _ in range(1000)]
    assert plays.count('rock') > 100
    assert plays.count('paper') > 100
    assert plays.count('scissors') > 100


def test_paper_beats_rock():
    assert rps.determine_game_result('paper', 'rock') is 'human'


def test_two_papers_is_tie():
    assert rps.determine_game_result('paper', 'paper') is 'tie'


def input_fake(fake): # ??? ^^^
    def input_fake_(prompt):
        print(prompt)
        return fake
    return input_fake_


@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors']) # vyzkoušej funkci test_whole_game() se všemi možnostmi
def test_whole_game(capsys, monkeypatch, play):
    # monkeypatch.setattr("builtins.input", input_fake_rock) # v cele funkci main pro tento test nahradime skuteckou funkci nasi fejkovou
    rps.main(input_func=input_fake(play))
    captured = capsys.readouterr()
    assert 'rock, paper or scissors?' in captured.out
    assert ('computer wins' in captured.out) or ('human wins' in captured.out) or ('it\'s a tie!' in captured.out)


def run_app(input):
    cp = subprocess.run([sys.executable, 'rps.py'],
        input=input,
        encoding='utf-8',
        stdout=subprocess.PIPE)
    return cp.stdout



def test_game_asks_again_if_wrong_input(): # tohle je nejlepší přístup! bez mockingu a DI
    assert run_app('blablablablbost\nrock').count('rock, paper or scissors?') == 2
    assert run_app('blablabla\nblbost\nrock').count('rock, paper or scissors?') == 3


