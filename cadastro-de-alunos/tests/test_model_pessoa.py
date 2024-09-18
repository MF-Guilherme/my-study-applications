from models import Pessoa


def test_idade_calcula_corretamente():
    pessoa = Pessoa('Guilherme', 1991)
    assert pessoa.idade == 33