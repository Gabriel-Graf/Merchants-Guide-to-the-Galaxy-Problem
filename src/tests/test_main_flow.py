import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import builtins
import pytest

from Solution1.MainSolution1 import main, is_assignment, is_product_price_definition, is_foreign_question, \
    is_product_question


def test_is_assignment_true_and_false():
    assert is_assignment(['unu', 'is', 'I'])
    assert not is_assignment(['unu', 'unu', 'Silver', 'is', '34', 'coins'])


def test_is_product_price_definition_true_and_false():
    assert is_product_price_definition(['unu', 'unu', 'Silver', 'is', '34', 'coins'])
    assert not is_product_price_definition(['unu', 'is', 'I'])


def test_is_foreign_question_true_and_false():
    assert is_foreign_question(['how', 'much', 'is', 'unu', '?'])
    assert not is_foreign_question(['how', 'many', 'coins', 'is', 'unu', 'Silver', '?'])


def test_is_product_question_true_and_false():
    assert is_product_question(['how', 'many', 'coins', 'is', 'unu', 'Silver', '?'])
    assert not is_product_question(['how', 'much', 'is', 'unu', '?'])


def test_is_assignment_empty_input():
    assert not is_assignment([])


def test_is_product_price_definition_no_coins():
    assert not is_product_price_definition(['unu', 'unu', 'Silver', 'is', '34'])


def test_is_foreign_question_invalid_syntax():
    assert not is_foreign_question(['how', 'much', 'unu', '?'])


def test_is_product_question_missing_coins():
    assert not is_product_question(['how', 'many', 'is', 'unu', 'Silver', '?'])


# Main loop integration test

def test_main_full_flow1(monkeypatch, capsys):
    # Define a session: add numbers, define product, ask questions, exit
    inputs = iter([
        "unu is I",
        "kvin is V",
        "dek is X",
        "kvindek is L",
        "unu unu Silver is 34 coins",
        "unu kvin Gold is 57800 coins",
        "dek dek Iron is 3910 coins",
        "how many coins is unu kvin Silver ?",
        "how many coins is unu kvin Gold ?",
        "how many coins is unu kvin Iron ?",
        "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?",
        "exit"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "Adding new foreign numbers 'unu' with 'I'" in captured.out
    assert "Adding new foreign numbers 'kvin' with 'V'" in captured.out
    assert "Adding new foreign numbers 'dek' with 'X'" in captured.out
    assert "Adding new foreign numbers 'kvindek' with 'L'" in captured.out
    assert "Adding new knowledge base 'Silver' with '17.0'" in captured.out
    assert "Adding new knowledge base 'Gold' with '14450.0'" in captured.out
    assert "Adding new knowledge base 'Iron' with '195.5'" in captured.out
    assert "unu kvin Silver is 68.0 coins" in captured.out
    assert "unu kvin Gold is 57800.0 coins" in captured.out
    assert "unu kvin Iron is 782.0 coins" in captured.out
    assert "I have no idea what you are talking about" in captured.out

def test_main_full_flow2(monkeypatch, capsys):
    # Define a session: add numbers, define product, ask questions, exit
    inputs = iter([
        "unu is I",
        "du is V",
        "unu du Silver is 6 coins",
        "how much is unu du ?",
        "how many coins is unu Silver ?",
        "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?",
        "exit"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "Adding new foreign numbers 'unu' with 'I'" in captured.out
    assert "Adding new foreign numbers 'du' with 'V'" in captured.out
    assert "Adding new knowledge base 'Silver' with '1.5'" in captured.out
    assert "unu du is 4" in captured.out
    assert "unu Silver is 1.5 coins" in captured.out
    assert "I have no idea what you are talking about" in captured.out


def test_main_empty_input(monkeypatch, capsys):
    inputs = iter(["", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "Empty input. Showing help message..." in captured.out
