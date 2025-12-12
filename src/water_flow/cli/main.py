from water_flow.storage import water_log_store
from datetime import datetime
import uuid

def registrar_agua(ml, tipo, nota=""):
    """Registra uma entrada de água no log."""
    entry_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    water_log_store.append_entry(entry_id, timestamp, ml, tipo, nota)
    print(f"✓ Registrado: {ml}ml de água\n")

def mostrar_menu():
    """Exibe o menu principal do aplicativo."""
    print("\n" + "="*40)
    print("  💧 WATER FLOW TRACKER 💧")
    print("="*40)
    print("1. Registrar 250ml")
    print("2. Registrar 500ml")
    print("3. Registrar valor manual")
    print("4. Sair")
    print("="*40)

def main():
    # Garante que o arquivo existe
    water_log_store.ensure_log_file()
    
    print("Bem-vindo ao Water Flow Tracker!")
    print("Registre sua ingestão de água ao longo do dia.\n")
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            registrar_agua(250, "preset")
        
        elif opcao == "2":
            registrar_agua(500, "preset")
        
        elif opcao == "3":
            try:
                ml = int(input("Quantos ml você bebeu? "))
                if ml <= 0:
                    print("❌ Por favor, insira um valor positivo.\n")
                    continue
                nota = input("Observação (opcional, Enter para pular): ").strip()
                registrar_agua(ml, "manual", nota)
            except ValueError:
                print("❌ Por favor, insira um número válido.\n")
        
        elif opcao == "4":
            print("\n👋 Até logo! Continue se hidratando!")
            break
        
        else:
            print("❌ Opção inválida. Por favor, escolha 1, 2, 3 ou 4.\n")

if __name__ == "__main__":
    main()