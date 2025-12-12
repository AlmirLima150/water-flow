import csv
from pathlib import Path

def get_log_file_path():
    """Retorna o caminho completo para o arquivo water_log.csv na raiz do projeto."""
    # Pega o diretório deste arquivo (storage/)
    current_dir = Path(__file__).parent
    # Sobe até a raiz do projeto (water-flow/)
    project_root = current_dir.parent.parent.parent
    # Monta o caminho para data/water_log.csv
    return project_root / "data" / "water_log.csv"

def ensure_log_file():
    """Garante que a pasta data/ e o arquivo water_log.csv existem com cabeçalho."""
    log_path = get_log_file_path()
    
    # Garante que a pasta data/ existe
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Se o arquivo não existe, cria com cabeçalho
    if not log_path.exists():
        with open(log_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "timestamp", "ml", "type", "note"])

def append_entry(entry_id, timestamp, ml, entry_type, note=""):
    """Adiciona um registro no log de água."""
    ensure_log_file()
    log_path = get_log_file_path()
    
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([entry_id, timestamp, ml, entry_type, note])