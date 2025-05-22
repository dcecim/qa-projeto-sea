import re

# Expressão regular para validação básica de nome (sem caracteres especiais, dígitos e palavras reservadas)
# Aceita letras com ou sem acento, espaços e hífens.
# Mínimo: 2 caracteres, Máximo: 120 caracteres para o nome completo.
NAME_REGEX = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]{2,120}$" 

# Lista de palavras reservadas de PL/SQL para validação adicional. 
PLSQL_RESERVED_WORDS = [
    "SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "CREATE", "ALTER",
    "TRUNCATE", "GRANT", "REVOKE", "COMMIT", "ROLLBACK", "SAVEPOINT",
    "DECLARE", "BEGIN", "END", "EXCEPTION", "LOOP", "WHILE", "FOR",
    "IF", "THEN", "ELSE", "ELSIF", "FUNCTION", "PROCEDURE", "PACKAGE",
    "BODY", "VIEW", "INDEX", "TRIGGER", "TYPE", "RECORD", "TABLE",
    "FROM", "WHERE", "AND", "OR", "NOT", "IN", "LIKE", "BETWEEN",
    "IS NULL", "ORDER BY", "GROUP BY", "HAVING", "DISTINCT", "AS",
    "JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN",
    "UNION", "UNION ALL", "INTERSECT", "MINUS", "COUNT", "SUM", "AVG",
    "MAX", "MIN", "SYSDATE", "DUAL", "ROWNUM", "SUBSTR", "LENGTH",
    "TO_CHAR", "TO_DATE", "TO_NUMBER", "NVL", "DECODE", "CASE",
    # Adicione outras palavras que considerar relevantes para evitar injeção.
]

def is_valid_name(name: str) -> bool:
    """
    Verifica se um nome é válido de acordo com as regras definidas. 
    """
    if not (2 <= len(name) <= 120): # Verifica min e max caracteres para nome completo 
        return False
    if not re.match(NAME_REGEX, name): # Expressão regular para validação básica 
        return False
    if contains_reserved_words(name): # Complemento com verificação de palavras reservadas 
        return False
    return True

def contains_reserved_words(text: str) -> bool:
    """
    Verifica se o texto contém alguma palavra reservada de PL/SQL. 
    """
    text_upper = text.upper()
    for word in PLSQL_RESERVED_WORDS:
        # Usa boundary para evitar correspondências parciais (ex: 'SELECT' não deve corresponder a 'SELECTED')
        if re.search(r'\b' + re.escape(word) + r'\b', text_upper):
            return True
    return False

# Adicionar outras funções auxiliares aqui, como:
# - Funções para gerar CPF válido/inválido
# - Funções para gerar datas válidas/inválidas
# - Funções para manipular elementos da UI
