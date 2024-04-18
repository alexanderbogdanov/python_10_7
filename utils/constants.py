import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
RESOURCES_DIR = os.path.join(PROJECT_ROOT_PATH, 'resources')
TMP_DIR = os.path.join(PROJECT_ROOT_PATH, 'tmp')
ARCHIVE_PATH = os.path.join(TMP_DIR, 'archive.zip')

PDF_FILE = 'pdf_example.pdf'
TXT_FILE = 'txt_example.txt'
XLS_FILE = 'xls_example.xls'
XLSX_FILE = 'xlsx_example.xlsx'

LIST_OF_FILES = {
    PDF_FILE: os.path.join(RESOURCES_DIR, PDF_FILE),
    TXT_FILE: os.path.join(RESOURCES_DIR, TXT_FILE),
    XLS_FILE: os.path.join(RESOURCES_DIR, XLS_FILE),
    XLSX_FILE: os.path.join(RESOURCES_DIR, XLSX_FILE)
}