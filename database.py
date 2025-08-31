# database.py
import sqlite3
from pathlib import Path

# Caminho do arquivo do banco (na raiz do projeto)
DB_PATH = Path(__file__).with_name("app.db")

def get_connection():
    """Abre conexão com o SQLite e retorna rows como dict-like."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acessar colunas por nome: row["nome"]
    return conn

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT,
    quantidade REAL NOT NULL DEFAULT 1,
    comprado INTEGER NOT NULL DEFAULT 0, -- 0 = falso, 1 = verdadeiro
    criado_em TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime'))
);
CREATE INDEX IF NOT EXISTS idx_itens_comprado ON itens (comprado);
"""

def init_db():
    """Cria as tabelas/índices se não existirem."""
    with get_connection() as conn:
        conn.executescript(SCHEMA_SQL)
