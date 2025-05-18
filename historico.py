import json
from datetime import datetime
import os

def carregar_historico():
    try:
        with open('historico.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_historico(historico):
    try:
        with open('historico.json', 'w') as f:
            json.dump(historico, f, indent=2)
    except Exception as e:
        print(f"Erro ao salvar histórico: {e}")

def registrar_pontuacao(pontos, palavra, dificuldade):
    #print(f"\nDEBUG: Registrando pontuação - {pontos} pts, {palavra}, {dificuldade}")
    historico = carregar_historico()
    nova_entrada = {
        "pontos": pontos,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "palavra": palavra,
        "dificuldade": dificuldade
    }
    #print(f"DEBUG: Nova entrada: {nova_entrada}")
    historico.append(nova_entrada)
    salvar_historico(historico)

# Teste automático ao executar o módulo
if __name__ == "__main__":
    print("Executando teste do módulo historico...")
    registrar_pontuacao(100, "teste", "Fácil")
    print("Histórico atual:", carregar_historico())