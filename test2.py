from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from pymnz.database import async_update_table_from_dataframe
from dotenv import load_dotenv
import asyncio
import pandas as pd
import os

load_dotenv()


dados = [
    {'chave': 1, 'nome': 'John Doe', 'idade': 30},
    {'chave': 2, 'nome': 'Jane Smith', 'idade': 25},
    {'chave': 3, 'nome': 'Bob Johnson', 'idade': 40},
    {'chave': 4, 'nome': 'Alice Brown', 'idade': 35},
    {'chave': 5, 'nome': 'Mike Davis', 'idade': 28},
]

def create_engine():
    HOST = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DATABASE')
    
    engine = create_async_engine(f'mysql+aiomysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}')
    return engine


# Main
async def main():

    # Criar engine
    engine = create_engine()

    # Testar
    try:

        # Abrir conexão
        async with AsyncSession(engine) as conn:

            # Inserir
            df = pd.DataFrame(dados)
            await async_update_table_from_dataframe(df, 'usuarios', 'chave', conn)

            # Comitar
            await conn.commit()
            await conn.close()

    # Tratamento de erro
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
