import os
import sys

from Solution1.TranslatorExceptions import ForeignNumberException

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pytest

from Solution1.Translator import Translator


def test_add_and_get_foreign_number():
    t = Translator()
    t.add_foreign_number('foo', 'I')
    assert t.get_foreign_numbers()['foo'] == 'I'


def test_add_knowledge_base_and_get():
    t = Translator()
    t.add_knowledge_base('Silver', 17)
    assert t.get_knowledge_base()['Silver'] == 17


def test_calc_foreign_numbers():
    t = Translator()
    t.add_foreign_number('unu', 'I')
    t.add_foreign_number('du', 'V')
    assert t.calc_foreign_numbers(['unu', 'du']) == 4  # IV


def test_extract_all_foreign_numbers_success_and_fail():
    t = Translator()
    t.add_foreign_number('unu', 'I')
    assert t.extract_all_foreign_numbers(['unu']) == ['unu']
    with pytest.raises(Exception):
        t.extract_all_foreign_numbers(['foo'])


def test_save_and_load_data(tmp_path):
    t = Translator(str(tmp_path / "backup.pkl"))
    t.add_foreign_number('unu', 'I')
    t.add_knowledge_base('Silver', 10)
    t.save_data()
    t2 = Translator(str(tmp_path / "backup.pkl"))
    t2.load_data()
    assert t2.get_foreign_numbers() == {'unu': 'I'}
    assert t2.get_knowledge_base() == {'Silver': 10}


def test_calc_foreign_numbers_empty_list():
    t = Translator()
    assert t.calc_foreign_numbers([]) == 0


def test_add_foreign_number_duplicate_entry(capsys):
    t = Translator()
    t.add_foreign_number('unu', 'I')
    t.add_foreign_number('unu', 'I')
    captured = capsys.readouterr()
    assert "'unu' with 'I' already exists in foreign numbers" in captured.out


def test_extract_all_foreign_numbers_unknown():
    t = Translator()
    t.add_foreign_number('unu', 'I')
    with pytest.raises(ForeignNumberException, match="foo"):
        t.extract_all_foreign_numbers(['foo'])


def test_save_data_invalid_path(tmp_path):
    invalid_path = str(tmp_path / "nonexistent_dir" / "backup.pkl")
    t = Translator(invalid_path)
    with pytest.raises(FileNotFoundError):
        t.save_data()
