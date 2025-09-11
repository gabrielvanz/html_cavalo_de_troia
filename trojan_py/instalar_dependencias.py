#!/usr/bin/env python3
"""
Script de Instalação de Dependências
====================================

Este script instala automaticamente as dependências necessárias
para executar as demonstrações de cavalo de tróia.

⚠️ DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️
"""

import subprocess
import sys
import os

def instalar_dependencia(pacote):
    """Instala uma dependência usando pip"""
    try:
        print(f"📦 Instalando {pacote}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
        print(f"✅ {pacote} instalado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar {pacote}: {e}")
        return False

def verificar_dependencia(pacote):
    """Verifica se uma dependência está instalada"""
    try:
        __import__(pacote)
        return True
    except ImportError:
        return False

def main():
    """Função principal"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    📦 INSTALAÇÃO DE DEPENDÊNCIAS 📦                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Este script instala as dependências necessárias para executar             ║
║  as demonstrações de cavalo de tróia.                                       ║
║                                                                              ║
║  ⚠️  DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n🔍 VERIFICANDO DEPENDÊNCIAS...")
    print("=" * 60)
    
    # Lista de dependências
    dependencias = [
        ("cryptography", "cryptography", "Para demonstração 2 (CryptoLocker)"),
        ("pynput", "pynput", "Para demonstração 3 (Keylogger)")
    ]
    
    dependencias_faltando = []
    
    for nome_import, nome_pacote, descricao in dependencias:
        if verificar_dependencia(nome_import):
            print(f"✅ {nome_pacote} - {descricao}")
        else:
            print(f"❌ {nome_pacote} - {descricao}")
            dependencias_faltando.append(nome_pacote)
    
    if not dependencias_faltando:
        print("\n🎉 Todas as dependências já estão instaladas!")
        print("   Você pode executar as demonstrações normalmente.")
        return
    
    print(f"\n📦 INSTALANDO DEPENDÊNCIAS FALTANDO...")
    print("=" * 60)
    
    sucesso = True
    for pacote in dependencias_faltando:
        if not instalar_dependencia(pacote):
            sucesso = False
    
    print("\n" + "=" * 60)
    if sucesso:
        print("🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        print("   Todas as dependências foram instaladas.")
        print("   Você pode agora executar as demonstrações:")
        print("   - python demonstracao_1.py")
        print("   - python demonstracao_2.py")
        print("   - python demonstracao_3.py")
    else:
        print("❌ INSTALAÇÃO FALHOU!")
        print("   Algumas dependências não puderam ser instaladas.")
        print("   Tente instalar manualmente:")
        for pacote in dependencias_faltando:
            print(f"   - pip install {pacote}")
    
    print("\n⚠️  LEMBRE-SE: Estas demonstrações são apenas para fins educacionais!")

if __name__ == "__main__":
    main()
