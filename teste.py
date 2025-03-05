from pymnz.models import Script

def soma(a=1, b=1):
  print(f'A soma de {a} + {b} é {a + b}.')
  raise Exception('Teste de execução')

def subtracao(a=1, b=1):
  print(f"A subtração de {a} - {b} é {a - b}.")
  return a - b

def soma_doida():
  a = 1
  b = 123
  print(f'A soma de {a} + {b} é {a + b}.')
  return a + b

try:
  script = Script('Script de teste', subtracao)
  script.run()
  
except Exception as e:
  assert str(e) == 'Teste de execução'

