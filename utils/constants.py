import os


PROJECT_ROOT_PATH = os.path.dirname(
    os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
)
RESOURCES_DIR = os.path.join(PROJECT_ROOT_PATH, "resources")
TMP_DIR = os.path.join(PROJECT_ROOT_PATH, "tmp")
ARCHIVE_PATH = os.path.join(TMP_DIR, "archive.zip")

PDF_FILE = "pdf_example.pdf"
CSV_FILE = "csv_example.csv"
XLSX_FILE = "xlsx_example.xlsx"

LIST_OF_FILES = {
    PDF_FILE: os.path.join(RESOURCES_DIR, PDF_FILE),
    CSV_FILE: os.path.join(RESOURCES_DIR, CSV_FILE),
    XLSX_FILE: os.path.join(RESOURCES_DIR, XLSX_FILE),
}
