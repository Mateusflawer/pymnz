from sqlalchemy import text


def table_exists(conn, table_name):
    """
    Verifica se uma tabela existe no banco de dados.

    :param conn: Conexão ativa com o banco de dados.
    :param table_name: Nome da tabela para verificar.
    :return: True se a tabela existir, caso contrário, False.
    """
    query = text("""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = :table_name
        );
    """)
    result = conn.execute(query, {"table_name": table_name})
    return result.scalar()  # Retorna True ou False
