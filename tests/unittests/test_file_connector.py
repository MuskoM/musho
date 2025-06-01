from pathlib import Path

import pytest

from models.connector import FileConnector, ConnectorException


def test_file_connector_setup_fails_file_passed_as_source(tmp_path: Path):
    test_file = tmp_path / "testy.txt"
    test_file.write_text("test_data", encoding="utf-8")
    tmp_path_str = str(test_file.absolute())
    with pytest.raises(ConnectorException):
        FileConnector(tmp_path_str)


def test_file_connector_setup_success(tmp_path: Path):
    # Arrange
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    tmp_path_str = str(test_dir.absolute())

    # Act
    file_connector = FileConnector(tmp_path_str)

    # Assert
    assert file_connector.name == "FileConnector"
