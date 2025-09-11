#!/usr/bin/env python3
"""
Demonstração 2: CryptoLocker Real - Criptografia de Arquivos
============================================================

Esta demonstração mostra como um CryptoLocker REAL funciona,
criptografando um arquivo de teste para fins educacionais.

⚠️ DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️
"""

import os
import time
import json
import base64
import hashlib
import secrets
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def mostrar_aviso():
    """Exibe aviso de segurança"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🔒 DEMONSTRAÇÃO 2: CRYPTOLOCKER REAL 🔒                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Esta demonstração mostra como um CryptoLocker REAL funciona,               ║
║  criptografando um arquivo de teste para fins educacionais.                 ║
║                                                                              ║
║  ⚠️  DESTINADO APENAS PARA FINS EDUCACIONAIS ⚠️                             ║
║  ⚠️  CRIPTOGRAFIA REAL - ARQUIVO SERÁ CIFRADO ⚠️                            ║
║  ⚠️  APENAS UM ARQUIVO DE TESTE SERÁ AFETADO ⚠️                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def criar_arquivo_teste():
    """Cria arquivo de teste para criptografia"""
    print("\n📄 CRIANDO ARQUIVO DE TESTE")
    print("=" * 60)
    
    arquivo_teste = "documento_importante_teste.txt"
    
    conteudo_original = f"""DOCUMENTO IMPORTANTE - TESTE DE CRIPTOGRAFIA
=======================================================

Este é um documento de teste que será criptografado
pelo CryptoLocker para demonstração educacional.

INFORMAÇÕES DO SISTEMA:
- Usuário: {os.getenv('USERNAME', 'Usuário')}
- Data: {datetime.now().strftime('%d/%m/%Y')}
- Hora: {datetime.now().strftime('%H:%M:%S')}
- Sistema: {os.name}
- Diretório: {os.getcwd()}

CONTEÚDO DE TESTE:
- Dados pessoais simulados
- Informações financeiras fictícias
- Documentos confidenciais de exemplo
- Fotos e vídeos (simulados)
- Arquivos de trabalho (simulados)

DADOS SENSÍVEIS SIMULADOS:
- CPF: 123.456.789-00
- RG: 12.345.678-9
- Cartão: 1234 5678 9012 3456
- CVV: 123
- Banco: Banco do Brasil
- Agência: 1234-5
- Conta: 12345-6

⚠️  ATENÇÃO: Este arquivo será criptografado pelo CryptoLocker!
   Em um ataque real, TODOS os seus arquivos seriam afetados.

Data de criação: {datetime.now().isoformat()}
Hash MD5: {hashlib.md5(f'arquivo_teste_{datetime.now()}'.encode()).hexdigest()}
"""
    
    try:
        with open(arquivo_teste, 'w', encoding='utf-8') as f:
            f.write(conteudo_original)
        
        tamanho_original = os.path.getsize(arquivo_teste)
        hash_original = hashlib.md5(conteudo_original.encode('utf-8')).hexdigest()
        
        print(f"✅ Arquivo de teste criado: {arquivo_teste}")
        print(f"   📏 Tamanho: {tamanho_original} bytes")
        print(f"   🔑 Hash MD5: {hash_original}")
        print(f"   📄 Conteúdo: Dados sensíveis simulados")
        
        return arquivo_teste, conteudo_original, hash_original, tamanho_original
        
    except Exception as e:
        print(f"❌ Erro ao criar arquivo de teste: {e}")
        return None, None, None, None

def gerar_chave_criptografia(senha):
    """Gera chave de criptografia usando PBKDF2"""
    print("\n🔑 GERANDO CHAVE DE CRIPTOGRAFIA")
    print("=" * 60)
    
    # Gerar salt aleatório
    salt = secrets.token_bytes(16)
    
    # Derivar chave usando PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    chave = base64.urlsafe_b64encode(kdf.derive(senha.encode()))
    
    print(f"✅ Chave de criptografia gerada")
    print(f"   🔐 Algoritmo: PBKDF2 + SHA256")
    print(f"   🔢 Iterações: 100.000")
    print(f"   🧂 Salt: {salt.hex()}")
    print(f"   🔑 Chave: {chave.decode()[:16]}...")
    
    return chave, salt

def criptografar_arquivo(arquivo_teste, conteudo_original):
    """Criptografa o arquivo usando Fernet (AES-128)"""
    print("\n🔒 INICIANDO CRIPTOGRAFIA REAL")
    print("=" * 60)
    
    try:
        # Gerar senha aleatória para demonstração
        senha = secrets.token_urlsafe(32)
        print(f"🔐 Senha gerada: {senha[:16]}...")
        
        # Gerar chave de criptografia
        chave, salt = gerar_chave_criptografia(senha)
        
        # Criar objeto Fernet para criptografia
        fernet = Fernet(chave)
        
        # Criptografar conteúdo
        print("🔄 Criptografando conteúdo...")
        conteudo_criptografado = fernet.encrypt(conteudo_original.encode('utf-8'))
        
        # Criar arquivo criptografado
        arquivo_criptografado = f"{arquivo_teste}.ENCRYPTED"
        
        # Salvar arquivo criptografado
        with open(arquivo_criptografado, 'wb') as f:
            f.write(conteudo_criptografado)
        
        # Calcular hash do arquivo criptografado
        hash_criptografado = hashlib.sha256(conteudo_criptografado).hexdigest()
        
        print(f"✅ Criptografia concluída!")
        print(f"   📄 Arquivo criptografado: {arquivo_criptografado}")
        print(f"   📏 Tamanho: {len(conteudo_criptografado)} bytes")
        print(f"   🔑 Hash SHA256: {hash_criptografado}")
        print(f"   🔐 Algoritmo: Fernet (AES-128)")
        
        return arquivo_criptografado, conteudo_criptografado, hash_criptografado, senha, salt
        
    except Exception as e:
        print(f"❌ Erro na criptografia: {e}")
        return None, None, None, None, None

def criar_arquivo_resgate(arquivo_original, hash_original, senha, salt):
    """Cria arquivo de resgate (ransom note)"""
    print("\n💀 CRIANDO ARQUIVO DE RESGATE")
    print("=" * 60)
    
    arquivo_resgate = "COMO_RECUPERAR_SEUS_DADOS.txt"
    
    conteudo_resgate = f"""CRYPTOLOCKER RANSOMWARE - DEMONSTRAÇÃO EDUCACIONAL
=======================================================

⚠️  SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! ⚠️

Este é um exemplo EDUCACIONAL de como o CryptoLocker funciona.
Em um ataque real, TODOS os seus arquivos seriam criptografados.

DETALHES DA CRIPTOGRAFIA:
- Arquivo original: {arquivo_original}
- Algoritmo: Fernet (AES-128)
- Hash original: {hash_original}
- Data da criptografia: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
- Salt: {salt.hex()}

COMO RECUPERAR SEUS DADOS (DEMONSTRAÇÃO):
1. Execute o script de descriptografia
2. Use a senha: {senha}
3. O arquivo será descriptografado automaticamente

⚠️  ATENÇÃO: Este é apenas um exemplo educacional!
   Em um ataque real, você precisaria pagar um resgate
   para receber a chave de descriptografia.

INFORMAÇÕES TÉCNICAS:
- Chave derivada com PBKDF2
- 100.000 iterações
- Salt aleatório de 16 bytes
- Criptografia simétrica AES-128

Data: {datetime.now().isoformat()}
"""
    
    try:
        with open(arquivo_resgate, 'w', encoding='utf-8') as f:
            f.write(conteudo_resgate)
        
        print(f"✅ Arquivo de resgate criado: {arquivo_resgate}")
        print(f"   📏 Tamanho: {os.path.getsize(arquivo_resgate)} bytes")
        print(f"   📋 Conteúdo: Instruções de resgate")
        
        return arquivo_resgate
        
    except Exception as e:
        print(f"❌ Erro ao criar arquivo de resgate: {e}")
        return None

def remover_arquivo_original(arquivo_teste):
    """Remove o arquivo original (simula o comportamento real do CryptoLocker)"""
    print("\n🗑️  REMOVENDO ARQUIVO ORIGINAL")
    print("=" * 60)
    
    try:
        if os.path.exists(arquivo_teste):
            os.remove(arquivo_teste)
            print(f"❌ Arquivo original removido: {arquivo_teste}")
            print(f"   ⚠️  O arquivo original foi permanentemente deletado!")
            print(f"   ⚠️  Em um ataque real, TODOS os seus arquivos seriam afetados!")
            return True
        else:
            print(f"⚠️  Arquivo original não encontrado: {arquivo_teste}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao remover arquivo original: {e}")
        return False

def demonstrar_criptografia_real():
    """Demonstra criptografia real do CryptoLocker"""
    print("\n🔒 DEMONSTRAÇÃO DE CRIPTOGRAFIA REAL")
    print("=" * 60)
    
    print("💀 CRYPTOLOCKER - RANSOMWARE REAL")
    print("   Este é um exemplo REAL de como o CryptoLocker funciona!")
    print("   Um arquivo será realmente criptografado e o original removido.")
    
    input("\nPressione ENTER para iniciar a criptografia...")
    
    # Criar arquivo de teste
    arquivo_teste, conteudo_original, hash_original, tamanho_original = criar_arquivo_teste()
    
    if not arquivo_teste:
        print("❌ Falha ao criar arquivo de teste")
        return
    
    time.sleep(2)
    
    # Criptografar arquivo
    arquivo_criptografado, conteudo_criptografado, hash_criptografado, senha, salt = criptografar_arquivo(arquivo_teste, conteudo_original)
    
    if not arquivo_criptografado:
        print("❌ Falha na criptografia")
        return
    
    time.sleep(2)
    
    # Criar arquivo de resgate
    arquivo_resgate = criar_arquivo_resgate(arquivo_teste, hash_original, senha, salt)
    
    time.sleep(2)
    
    # Remover arquivo original
    remover_arquivo_original(arquivo_teste)
    
    time.sleep(2)
    
    # Mostrar estatísticas
    mostrar_estatisticas_criptografia(arquivo_teste, arquivo_criptografado, arquivo_resgate, 
                                    tamanho_original, len(conteudo_criptografado), 
                                    hash_original, hash_criptografado)
    
    return {
        "arquivo_original": arquivo_teste,
        "arquivo_criptografado": arquivo_criptografado,
        "arquivo_resgate": arquivo_resgate,
        "senha": senha,
        "salt": salt.hex(),
        "hash_original": hash_original,
        "hash_criptografado": hash_criptografado
    }

def mostrar_estatisticas_criptografia(arquivo_original, arquivo_criptografado, arquivo_resgate,
                                    tamanho_original, tamanho_criptografado, 
                                    hash_original, hash_criptografado):
    """Mostra estatísticas da criptografia"""
    print("\n📊 ESTATÍSTICAS DA CRIPTOGRAFIA")
    print("=" * 60)
    
    print(f"📈 ESTATÍSTICAS:")
    print(f"   📄 Arquivo original: {arquivo_original}")
    print(f"   🔒 Arquivo criptografado: {arquivo_criptografado}")
    print(f"   💀 Arquivo de resgate: {arquivo_resgate}")
    print(f"   📏 Tamanho original: {tamanho_original} bytes")
    print(f"   📏 Tamanho criptografado: {tamanho_criptografado} bytes")
    print(f"   🔑 Hash original (MD5): {hash_original}")
    print(f"   🔑 Hash criptografado (SHA256): {hash_criptografado}")
    print(f"   ⏰ Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    print(f"\n⚠️  IMPACTO REAL DO CRYPTOLOCKER:")
    print(f"   🔒 Arquivo original foi criptografado")
    print(f"   🗑️  Arquivo original foi removido")
    print(f"   💀 Arquivo de resgate foi criado")
    print(f"   🔐 Criptografia é real e segura")
    print(f"   ⚠️  Em um ataque real, TODOS os arquivos seriam afetados!")

def salvar_relatorio_cryptolocker(dados_criptografia):
    """Salva relatório da criptografia"""
    print("\n💾 SALVANDO RELATÓRIO DE CRIPTOGRAFIA")
    print("=" * 60)
    
    try:
        relatorio = {
            "cryptolocker_demonstracao": {
                "arquivo_original": dados_criptografia.get("arquivo_original", "N/A"),
                "arquivo_criptografado": dados_criptografia.get("arquivo_criptografado", "N/A"),
                "arquivo_resgate": dados_criptografia.get("arquivo_resgate", "N/A"),
                "algoritmo": "Fernet (AES-128)",
                "derivacao_chave": "PBKDF2 + SHA256",
                "iteracoes": 100000,
                "salt": dados_criptografia.get("salt", "N/A"),
                "hash_original": dados_criptografia.get("hash_original", "N/A"),
                "hash_criptografado": dados_criptografia.get("hash_criptografado", "N/A")
            },
            "timestamp": datetime.now().isoformat(),
            "observacoes": "Demonstração educacional do CryptoLocker - CRIPTOGRAFIA REAL"
        }
        
        filename = f"cryptolocker_demonstracao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, indent=2, ensure_ascii=False)
        
        print(f"✅ RELATÓRIO DE CRIPTOGRAFIA SALVO:")
        print(f"   📄 Arquivo: {filename}")
        print(f"   📏 Tamanho: {os.path.getsize(filename)} bytes")
        print(f"   📋 Conteúdo: Dados da criptografia real")
        
        return filename
        
    except Exception as e:
        print(f"❌ Erro ao salvar relatório: {e}")
        return None

def main():
    """Função principal da demonstração"""
    mostrar_aviso()
    
    print("\n🔒 DEMONSTRAÇÃO 2: CRYPTOLOCKER REAL")
    print("=" * 60)
    print("Esta demonstração mostra como um CryptoLocker REAL funciona,")
    print("criptografando um arquivo de teste para fins educacionais.")
    
    input("\nPressione ENTER para começar a demonstração...")
    
    # Executar demonstração de criptografia real
    dados_criptografia = demonstrar_criptografia_real()
    
    if dados_criptografia:
    # Salvar relatório
        filename = salvar_relatorio_cryptolocker(dados_criptografia)
    
    print("\n" + "=" * 60)
    print("🎓 DEMONSTRAÇÃO 2 CONCLUÍDA")
    print("=" * 60)
    print("Você viu como um CryptoLocker REAL funciona!")
    print("Um arquivo foi realmente criptografado e o original removido.")
    
    if filename:
        print(f"\n📄 Relatório salvo em: {filename}")
        print("   Este arquivo contém os dados da criptografia real!")
    
        print(f"\n⚠️  LEMBRE-SE: Em um ataque real, TODOS os seus arquivos seriam afetados!")
        print(f"   Por isso é fundamental se proteger contra ransomware!")
    else:
        print("\n❌ Demonstração falhou - verifique os erros acima")

if __name__ == "__main__":
    main()
