import os

DB_SERVER = 'SAM\SQLEXPRESS'
DB_NAME = 'TPCSOURCE'
DB_DRIVER = 'SQL Server'
DB_USER = ''
DB_PASS = ''
DB_PREFIX = 'dbo'
VERBOSE = True

OUTPUT_DIR = os.path.abspath(os.path.dirname(__file__) + "/outputs")