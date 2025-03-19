def table_exists(con, table_name):
    result = con.execute(
        """
        SELECT COUNT(*) 
        FROM information_schema.tables 
        WHERE table_schema = 'main' AND table_name = ?
    """,
        [table_name],
    ).fetchone()[0]
    return result > 0
