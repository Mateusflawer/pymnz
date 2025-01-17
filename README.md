# pymnz
Biblioteca para facilitar a criação de scripts de bot e automações em Python.

## Instalação
```bash
pip install pymnz


# USO BÁSICO
from pymnz import utils


@utils.classes.singleton
class Carro:
    ...


carro1 = Carro()
carro2 = Carro()


if carro1 is carro2:
    print('Mesmo carro')
else:
    print('Carro diferente')
