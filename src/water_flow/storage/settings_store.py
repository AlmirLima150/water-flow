import json
from pathlib import Path

def get_settings_file_path():
    """Retorna o caminho completo para o arquivo water_log.csv na raiz do projeto."""
    # Pega o diretório deste arquivo (storage/)
    current_dir = Path(__file__).parent
    # Sobe até a raiz do projeto (water-flow/)
    project_root = current_dir.parent.parent.parent
    # Monta o caminho para data/water_log.csv
    return project_root / "data" / "settings.json"

def save_settings(settings: dict):
    
    settings_path = get_settings_file_path()

    settings_path.parent.mkdir(parents=True, exist_ok=True)

    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)