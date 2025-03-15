from pymnz.models import Script
import asyncio
import time


async def async_soma(a, b):
  print(f'A soma de {a} + {b} é {a + b}.')
  await asyncio.sleep(1)
  return a + b


def soma(a, b):
  print(f'A soma de {a} + {b} é {a + b}.')
  time.sleep(1)
  return a + b


if __name__ == "__main__":
  script = Script("Script de teste", async_soma, 1, 2)
  script.set_code_start(soma, 1, 10)
  script.run()
