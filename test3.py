from pymnz.database import update_table_from_dataframe
from sqlalchemy import create_engine
from dotenv import load_dotenv
import asyncio
import pandas as pd
import os

load_dotenv()


dados = [
    {'chave': 1, 'nome': 'John Doe', 'idade': 30, 'sexo': 'M'},
    {'chave': 2, 'nome': 'Jane Smith', 'idade': 25, 'sexo': 'F'},
    {'chave': 3, 'nome': 'Bob Johnson', 'idade': 40, 'sexo': 'M'},
    {'chave': 4, 'nome': 'Alice Brown', 'idade': 35, 'sexo': 'F'},
    {'chave': 5, 'nome': 'Mike Davis', 'idade': 28, 'sexo': 'M'},
]

def create_engine_web():
    HOST = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DATABASE')
    
    engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}')
    return engine


# Main
def main():

    # Criar engine
    engine = create_engine_web()

    # Testar
    try:

        # Abrir conexão
        with engine.connect() as conn:

            # Inserir
            df = pd.DataFrame(dados)
            update_table_from_dataframe(df, 'usuarios', 'chave', conn, ['nome', 'idade'])

            # Comitar
            conn.commit()
            conn.close()

    # Tratamento de erro
    finally:
        engine.dispose()


if __name__ == "__main__":
    main()
