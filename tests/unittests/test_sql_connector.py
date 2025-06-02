from pathlib import Path

from sqlalchemy import text

from models.connector import SQLConnector


def test_sql_connector_setup_succeded(tmp_path: Path):
    db_path_file = tmp_path / "test.db"
    assert not db_path_file.exists()

    db_path_str = str(db_path_file.absolute())

    conn = SQLConnector(f"sqlite:///{db_path_str}")
    with conn._session() as session:
        session.execute(text("SELECT 'HELLO WORLD'"))
    assert db_path_file.exists()
