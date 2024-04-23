import pytest
import os
import zipfile
import shutil
from utils.constants import TMP_DIR, RESOURCES_DIR, ARCHIVE_PATH


@pytest.fixture(scope="session")
def create_archive():
    os.makedirs(TMP_DIR, exist_ok=True)
    with zipfile.ZipFile(ARCHIVE_PATH, "w") as archive:
        for filename in os.listdir(RESOURCES_DIR):
            file_path = os.path.join(RESOURCES_DIR, filename)
            archive.write(file_path, os.path.basename(file_path))

    yield

    shutil.rmtree(TMP_DIR)
