import pymnz


def test_classes_singleton():
    # Classe
    @pymnz.classes.singleton
    class TestClass():
        ...

    # Teste de acerto
    assert TestClass() is TestClass(), \
        'Classe 1 e 2 não são a mesma instância'
