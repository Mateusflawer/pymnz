from pymnz.models import Script
import asyncio


async def async_soma(a, b):
  print(f'A soma de {a} + {b} é {a + b}.')
  await asyncio.sleep(1)
  return a + b


def soma(a, b):
  print(f'A soma de {a} + {b} é {a + b}.')
  return a + b


if __name__ == "__main__":
  script = Script("Script de teste", async_soma, 1, 2)
  script.run()
