#!/usr/bin/env python3
"""
Demonstração 1: Coleta Real de Dados do Sistema
==============================================

Esta demonstração mostra como um cavalo de tróia REAL coleta
informações do sistema do usuário.

⚠️ DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️
"""

import os
import socket
import platform
import getpass
import json
import time
from datetime import datetime

def mostrar_aviso():
    """Exibe aviso de segurança"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🔍 DEMONSTRAÇÃO 1: COLETA DE DADOS 🔍                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Esta demonstração mostra como um cavalo de tróia REAL coleta               ║
║  informações do seu sistema. TODAS AS INFORMAÇÕES SÃO REAIS!                ║
║                                                                              ║
║  ⚠️  DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️                             ║
║  ⚠️  NÃO CAUSA DANOS REAIS - APENAS COLETA INFORMAÇÕES ⚠️                   ║
║  ⚠️  TODAS AS INFORMAÇÕES MOSTRADAS SÃO REAIS DO SEU SISTEMA ⚠️             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def coletar_informacoes_sistema():
    """Coleta informações REAIS do sistema"""
    print("\n💻 COLETANDO INFORMAÇÕES REAIS DO SISTEMA")
    print("=" * 60)
    
    info = {}
    
    try:
        # Informações básicas do sistema
        info['usuario'] = getpass.getuser()
        info['sistema'] = platform.system()
        info['versao'] = platform.version()
        info['arquitetura'] = platform.architecture()[0]
        info['processador'] = platform.processor()
        info['hostname'] = socket.gethostname()
        info['diretorio_atual'] = os.getcwd()
        info['diretorio_home'] = os.path.expanduser("~")
        info['timestamp'] = datetime.now().isoformat()
        
        print("✅ INFORMAÇÕES BÁSICAS COLETADAS:")
        print(f"   👤 Usuário: {info['usuario']}")
        print(f"   💻 Sistema: {info['sistema']}")
        print(f"   📋 Versão: {info['versao']}")
        print(f"   🏗️  Arquitetura: {info['arquitetura']}")
        print(f"   ⚙️  Processador: {info['processador']}")
        print(f"   🏠 Hostname: {info['hostname']}")
        print(f"   📁 Diretório atual: {info['diretorio_atual']}")
        print(f"   🏡 Diretório home: {info['diretorio_home']}")
        print(f"   ⏰ Timestamp: {info['timestamp']}")
        
        return info
        
    except Exception as e:
        print(f"❌ Erro ao coletar informações: {e}")
        return {}

def coletar_informacoes_rede():
    """Coleta informações REAIS de rede"""
    print("\n🌐 COLETANDO INFORMAÇÕES REAIS DE REDE")
    print("=" * 60)
    
    info = {}
    
    try:
        # IP local
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        info['hostname'] = hostname
        info['ip_local'] = local_ip
        
        # Simular IP externo para demonstração
        info['ip_externo'] = "203.0.113.1"  # IP de exemplo
        
        # Informações de rede
        info['portas_comuns'] = [80, 443, 22, 21, 25, 53, 110, 143, 993, 995]
        info['conexoes_simuladas'] = 15
        
        print("✅ INFORMAÇÕES DE REDE COLETADAS:")
        print(f"   🏠 Hostname: {info['hostname']}")
        print(f"   🌐 IP Local: {info['ip_local']}")
        print(f"   🌍 IP Externo: {info['ip_externo']}")
        print(f"   🔌 Portas comuns: {', '.join(map(str, info['portas_comuns']))}")
        print(f"   📡 Conexões ativas: {info['conexoes_simuladas']}")
        
        return info
        
    except Exception as e:
        print(f"❌ Erro ao coletar informações de rede: {e}")
        return {}

def coletar_arquivos_sistema():
    """Coleta informações REAIS sobre arquivos"""
    print("\n📁 COLETANDO INFORMAÇÕES REAIS DE ARQUIVOS")
    print("=" * 60)
    
    info = {}
    
    try:
        # Listar arquivos do diretório atual
        current_files = os.listdir(".")
        info['arquivos_diretorio_atual'] = current_files
        info['total_arquivos'] = len(current_files)
        
        # Listar arquivos do diretório home (primeiros 10)
        home_dir = os.path.expanduser("~")
        try:
            home_files = os.listdir(home_dir)
            info['arquivos_home'] = home_files[:10]  # Primeiros 10 arquivos
        except:
            info['arquivos_home'] = ["Acesso negado"]
        
        print("✅ INFORMAÇÕES DE ARQUIVOS COLETADAS:")
        print(f"   📊 Total de arquivos no diretório atual: {info['total_arquivos']}")
        print(f"   📄 Primeiros arquivos: {', '.join(info['arquivos_diretorio_atual'][:5])}")
        print(f"   🏠 Arquivos no home: {', '.join(info['arquivos_home'][:5])}")
        
        return info
        
    except Exception as e:
        print(f"❌ Erro ao coletar informações de arquivos: {e}")
        return {}

def coletar_informacoes_adicionais():
    """Coleta informações adicionais do sistema"""
    print("\n🔍 COLETANDO INFORMAÇÕES ADICIONAIS")
    print("=" * 60)
    
    info = {}
    
    try:
        # Variáveis de ambiente (algumas seguras)
        info['path'] = os.environ.get('PATH', 'N/A')[:100] + "..."  # Truncar
        info['username'] = os.environ.get('USERNAME', 'N/A')
        info['computername'] = os.environ.get('COMPUTERNAME', 'N/A')
        info['os'] = os.environ.get('OS', 'N/A')
        
        # Informações de tempo
        info['data_hora'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        info['timezone'] = time.tzname[0] if time.tzname else 'N/A'
        
        print("✅ INFORMAÇÕES ADICIONAIS COLETADAS:")
        print(f"   👤 Username: {info['username']}")
        print(f"   💻 Computer Name: {info['computername']}")
        print(f"   🖥️  OS: {info['os']}")
        print(f"   📅 Data/Hora: {info['data_hora']}")
        print(f"   🌍 Timezone: {info['timezone']}")
        print(f"   🛤️  PATH (truncado): {info['path']}")
        
        return info
        
    except Exception as e:
        print(f"❌ Erro ao coletar informações adicionais: {e}")
        return {}

def salvar_relatorio_coleta(dados_coletados):
    """Salva relatório da coleta de dados"""
    print("\n💾 SALVANDO RELATÓRIO DE COLETA")
    print("=" * 60)
    
    try:
        relatorio = {
            "coleta_realizada": datetime.now().isoformat(),
            "dados_coletados": dados_coletados,
            "observacoes": "Relatório de coleta de dados por cavalo de tróia - DEMONSTRAÇÃO EDUCACIONAL",
            "vítima": {
                "usuario": dados_coletados.get('sistema', {}).get('usuario', 'N/A'),
                "sistema": dados_coletados.get('sistema', {}).get('sistema', 'N/A'),
                "ip": dados_coletados.get('rede', {}).get('ip_local', 'N/A')
            }
        }
        
        filename = f"coleta_dados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, indent=2, ensure_ascii=False)
        
        print(f"✅ RELATÓRIO DE COLETA SALVO:")
        print(f"   📄 Arquivo: {filename}")
        print(f"   📏 Tamanho: {os.path.getsize(filename)} bytes")
        print(f"   📋 Conteúdo: Dados reais coletados do sistema")
        
        return filename
        
    except Exception as e:
        print(f"❌ Erro ao salvar relatório: {e}")
        return None

def mostrar_resumo_coleta(dados_coletados):
    """Mostra resumo da coleta de dados"""
    print("\n📊 RESUMO DA COLETA DE DADOS")
    print("=" * 60)
    
    total_dados = 0
    for categoria, dados in dados_coletados.items():
        if isinstance(dados, dict):
            total_dados += len(dados)
    
    print(f"📈 ESTATÍSTICAS DA COLETA:")
    print(f"   📊 Total de informações coletadas: {total_dados}")
    print(f"   📁 Categorias de dados: {len(dados_coletados)}")
    print(f"   ⏰ Timestamp: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    print(f"\n🎯 DADOS COLETADOS POR CATEGORIA:")
    for categoria, dados in dados_coletados.items():
        if isinstance(dados, dict):
            print(f"   • {categoria.upper()}: {len(dados)} informações")
    
    print(f"\n⚠️  ESTAS SÃO INFORMAÇÕES REAIS DO SEU SISTEMA!")
    print(f"   Em um ataque real, essas informações seriam enviadas para o atacante.")
    print(f"   Por isso é fundamental se proteger contra malwares!")

def main():
    """Função principal da demonstração"""
    mostrar_aviso()
    
    print("\n🔍 DEMONSTRAÇÃO 1: COLETA REAL DE DADOS")
    print("=" * 60)
    print("Esta demonstração mostra como um cavalo de tróia REAL")
    print("coletaria informações do seu sistema.")
    
    input("\nPressione ENTER para começar a coleta de dados...")
    
    # Coletar todas as informações REAIS
    dados_coletados = {}
    
    # Informações do sistema
    dados_coletados['sistema'] = coletar_informacoes_sistema()
    time.sleep(1)
    
    # Informações de rede
    dados_coletados['rede'] = coletar_informacoes_rede()
    time.sleep(1)
    
    # Informações de arquivos
    dados_coletados['arquivos'] = coletar_arquivos_sistema()
    time.sleep(1)
    
    # Informações adicionais
    dados_coletados['adicionais'] = coletar_informacoes_adicionais()
    time.sleep(1)
    
    # Salvar relatório
    filename = salvar_relatorio_coleta(dados_coletados)
    time.sleep(1)
    
    # Mostrar resumo
    mostrar_resumo_coleta(dados_coletados)
    
    print("\n" + "=" * 60)
    print("🎓 DEMONSTRAÇÃO 1 CONCLUÍDA")
    print("=" * 60)
    print("Você viu como um cavalo de tróia REAL coletaria seus dados!")
    print("Use este conhecimento para se proteger melhor.")
    
    if filename:
        print(f"\n📄 Relatório salvo em: {filename}")
        print("   Este arquivo contém as informações que seriam roubadas!")
    
    print("\n⚠️  LEMBRE-SE: A melhor defesa é a educação e a prevenção!")

if __name__ == "__main__":
    main()
