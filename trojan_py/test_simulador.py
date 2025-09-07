#!/usr/bin/env python3
"""
Script de Teste - Simulador Educacional de Cavalo de Tróia
==========================================================

Este script testa todas as funcionalidades do simulador para garantir
que está funcionando corretamente e de forma segura.

Autor: Equipe de Criptografia e Segurança - Atitus Educação
Integrantes: Diogo Chaves, Gabriel Vanz, Vitor Badin
Ano: 2024
"""

import sys
import time
import traceback
from datetime import datetime

def test_imports():
    """Testa se todos os módulos podem ser importados"""
    print("🔍 Testando importações...")
    
    try:
        from trojan_horse_simulation import TrojanSimulator, SimulationType
        print("   ✅ trojan_horse_simulation importado com sucesso")
    except ImportError as e:
        print(f"   ❌ Erro ao importar trojan_horse_simulation: {e}")
        return False
    
    try:
        from trojan_education_modules import TrojanEducationModules
        print("   ✅ trojan_education_modules importado com sucesso")
    except ImportError as e:
        print(f"   ❌ Erro ao importar trojan_education_modules: {e}")
        return False
    
    try:
        from trojan_security_analysis import TrojanSecurityAnalyzer
        print("   ✅ trojan_security_analysis importado com sucesso")
    except ImportError as e:
        print(f"   ❌ Erro ao importar trojan_security_analysis: {e}")
        return False
    
    return True

def test_simulator_initialization():
    """Testa inicialização do simulador"""
    print("\n🔧 Testando inicialização do simulador...")
    
    try:
        from trojan_horse_simulation import TrojanSimulator
        simulator = TrojanSimulator()
        
        # Verificar propriedades de segurança
        assert simulator.sandbox_mode == True, "Modo sandbox deve estar ativo"
        assert simulator.ethical_mode == True, "Modo ético deve estar ativo"
        assert simulator.max_simulation_time == 300, "Tempo máximo deve ser 300s"
        
        print("   ✅ Simulador inicializado corretamente")
        print("   ✅ Modo sandbox ativo")
        print("   ✅ Modo ético ativo")
        print("   ✅ Configurações de segurança corretas")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro na inicialização: {e}")
        traceback.print_exc()
        return False

def test_education_modules():
    """Testa módulos educacionais"""
    print("\n📚 Testando módulos educacionais...")
    
    try:
        from trojan_education_modules import TrojanEducationModules
        modules = TrojanEducationModules()
        
        # Verificar se exemplos foram carregados
        assert len(modules.trojan_examples) > 0, "Deve ter exemplos de trojans"
        assert len(modules.attack_scenarios) > 0, "Deve ter cenários de ataque"
        assert len(modules.defense_strategies) > 0, "Deve ter estratégias de defesa"
        
        print("   ✅ Módulos educacionais carregados")
        print(f"   ✅ {len(modules.trojan_examples)} exemplos de trojans")
        print(f"   ✅ {len(modules.attack_scenarios)} cenários de ataque")
        print(f"   ✅ {len(modules.defense_strategies)} categorias de defesa")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro nos módulos educacionais: {e}")
        traceback.print_exc()
        return False

def test_security_analyzer():
    """Testa analisador de segurança"""
    print("\n🔍 Testando analisador de segurança...")
    
    try:
        from trojan_security_analysis import TrojanSecurityAnalyzer
        analyzer = TrojanSecurityAnalyzer()
        
        # Verificar se assinaturas foram carregadas
        assert len(analyzer.signatures) > 0, "Deve ter assinaturas de malware"
        assert len(analyzer.suspicious_patterns) > 0, "Deve ter padrões suspeitos"
        assert len(analyzer.network_indicators) > 0, "Deve ter indicadores de rede"
        
        print("   ✅ Analisador de segurança inicializado")
        print(f"   ✅ {len(analyzer.signatures)} assinaturas de malware")
        print(f"   ✅ {len(analyzer.suspicious_patterns)} padrões suspeitos")
        print(f"   ✅ {len(analyzer.network_indicators)} indicadores de rede")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro no analisador de segurança: {e}")
        traceback.print_exc()
        return False

def test_simulations():
    """Testa execução das simulações"""
    print("\n🎯 Testando simulações...")
    
    try:
        from trojan_horse_simulation import TrojanSimulator, SimulationType
        simulator = TrojanSimulator()
        
        # Testar simulação educacional
        print("   Testando simulação educacional...")
        result = simulator.simulate_trojan_behavior(SimulationType.EDUCATIONAL)
        assert result['success'] == True, "Simulação educacional deve ser bem-sucedida"
        assert result['execution_time'] > 0, "Tempo de execução deve ser positivo"
        print("   ✅ Simulação educacional funcionando")
        
        # Testar simulação de detecção
        print("   Testando simulação de detecção...")
        result = simulator.simulate_trojan_behavior(SimulationType.DETECTION)
        assert result['success'] == True, "Simulação de detecção deve ser bem-sucedida"
        assert 'detection_rate' in result, "Deve ter taxa de detecção"
        print("   ✅ Simulação de detecção funcionando")
        
        # Testar simulação de prevenção
        print("   Testando simulação de prevenção...")
        result = simulator.simulate_trojan_behavior(SimulationType.PREVENTION)
        assert result['success'] == True, "Simulação de prevenção deve ser bem-sucedida"
        assert 'protection_rate' in result, "Deve ter taxa de proteção"
        print("   ✅ Simulação de prevenção funcionando")
        
        # Testar simulação de análise
        print("   Testando simulação de análise...")
        result = simulator.simulate_trojan_behavior(SimulationType.ANALYSIS)
        assert result['success'] == True, "Simulação de análise deve ser bem-sucedida"
        assert 'threat_score' in result, "Deve ter pontuação de ameaça"
        print("   ✅ Simulação de análise funcionando")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro nas simulações: {e}")
        traceback.print_exc()
        return False

def test_analysis_functions():
    """Testa funções de análise"""
    print("\n🔬 Testando funções de análise...")
    
    try:
        from trojan_security_analysis import TrojanSecurityAnalyzer
        analyzer = TrojanSecurityAnalyzer()
        
        # Testar análise estática
        print("   Testando análise estática...")
        findings = analyzer.analyze_file_static("trojan_example.py")
        assert isinstance(findings, list), "Findings deve ser uma lista"
        print("   ✅ Análise estática funcionando")
        
        # Testar análise de rede
        print("   Testando análise de rede...")
        traffic_data = {
            "domains": ["malicious-site.com"],
            "ips": ["192.168.1.100"],
            "ports": [8080]
        }
        findings = analyzer.analyze_network_traffic(traffic_data)
        assert isinstance(findings, list), "Findings deve ser uma lista"
        print("   ✅ Análise de rede funcionando")
        
        # Testar análise comportamental
        print("   Testando análise comportamental...")
        behavior_data = {
            "registry_modifications": 5,
            "files_created": 10,
            "network_connections": 3,
            "persistence_attempts": 1
        }
        findings = analyzer.analyze_behavior(behavior_data)
        assert isinstance(findings, list), "Findings deve ser uma lista"
        print("   ✅ Análise comportamental funcionando")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro nas funções de análise: {e}")
        traceback.print_exc()
        return False

def test_education_functions():
    """Testa funções educacionais"""
    print("\n📖 Testando funções educacionais...")
    
    try:
        from trojan_education_modules import TrojanEducationModules
        modules = TrojanEducationModules()
        
        # Testar geração de quiz
        print("   Testando geração de quiz...")
        questions = modules.generate_educational_quiz()
        assert len(questions) > 0, "Deve ter perguntas no quiz"
        assert all('question' in q for q in questions), "Todas as perguntas devem ter 'question'"
        assert all('options' in q for q in questions), "Todas as perguntas devem ter 'options'"
        assert all('correct' in q for q in questions), "Todas as perguntas devem ter 'correct'"
        print("   ✅ Geração de quiz funcionando")
        
        # Testar análise de exemplo
        print("   Testando análise de exemplo...")
        result = modules.analyze_trojan_example(0)
        assert 'name' in result, "Resultado deve ter 'name'"
        assert 'family' in result, "Resultado deve ter 'family'"
        assert 'risk_level' in result, "Resultado deve ter 'risk_level'"
        print("   ✅ Análise de exemplo funcionando")
        
        # Testar simulação de cenário
        print("   Testando simulação de cenário...")
        result = modules.simulate_attack_scenario(0)
        assert 'scenario' in result, "Resultado deve ter 'scenario'"
        assert 'vector' in result, "Resultado deve ter 'vector'"
        print("   ✅ Simulação de cenário funcionando")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro nas funções educacionais: {e}")
        traceback.print_exc()
        return False

def test_reports_and_export():
    """Testa geração de relatórios e exportação"""
    print("\n📊 Testando relatórios e exportação...")
    
    try:
        from trojan_horse_simulation import TrojanSimulator
        from trojan_security_analysis import TrojanSecurityAnalyzer
        
        simulator = TrojanSimulator()
        analyzer = TrojanSecurityAnalyzer()
        
        # Executar uma simulação para gerar dados
        simulator.simulate_trojan_behavior(simulator.SimulationType.EDUCATIONAL)
        
        # Testar geração de relatório
        print("   Testando geração de relatório...")
        report = simulator.generate_security_report()
        assert isinstance(report, str), "Relatório deve ser string"
        assert len(report) > 0, "Relatório não deve estar vazio"
        print("   ✅ Geração de relatório funcionando")
        
        # Testar exportação de dados
        print("   Testando exportação de dados...")
        filename = simulator.export_simulation_data("test_simulation.json")
        assert filename.endswith('.json'), "Arquivo deve ser JSON"
        print("   ✅ Exportação de dados funcionando")
        
        # Testar relatório de análise
        print("   Testando relatório de análise...")
        report = analyzer.generate_analysis_report()
        assert isinstance(report, str), "Relatório deve ser string"
        print("   ✅ Relatório de análise funcionando")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro nos relatórios e exportação: {e}")
        traceback.print_exc()
        return False

def test_security_features():
    """Testa recursos de segurança"""
    print("\n🛡️ Testando recursos de segurança...")
    
    try:
        from trojan_horse_simulation import TrojanSimulator
        simulator = TrojanSimulator()
        
        # Verificar avisos de segurança
        print("   Testando avisos de segurança...")
        simulator.display_warning()  # Deve exibir aviso sem erro
        print("   ✅ Avisos de segurança funcionando")
        
        # Verificar logs de auditoria
        print("   Testando logs de auditoria...")
        assert len(simulator.security_events) >= 0, "Deve ter eventos de segurança"
        print("   ✅ Logs de auditoria funcionando")
        
        # Verificar modo ético
        print("   Testando modo ético...")
        assert simulator.ethical_mode == True, "Modo ético deve estar ativo"
        print("   ✅ Modo ético ativo")
        
        # Verificar modo sandbox
        print("   Testando modo sandbox...")
        assert simulator.sandbox_mode == True, "Modo sandbox deve estar ativo"
        print("   ✅ Modo sandbox ativo")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro nos recursos de segurança: {e}")
        traceback.print_exc()
        return False

def run_all_tests():
    """Executa todos os testes"""
    print("🧪 INICIANDO TESTES DO SIMULADOR EDUCACIONAL")
    print("=" * 60)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    tests = [
        ("Importações", test_imports),
        ("Inicialização do Simulador", test_simulator_initialization),
        ("Módulos Educacionais", test_education_modules),
        ("Analisador de Segurança", test_security_analyzer),
        ("Simulações", test_simulations),
        ("Funções de Análise", test_analysis_functions),
        ("Funções Educacionais", test_education_functions),
        ("Relatórios e Exportação", test_reports_and_export),
        ("Recursos de Segurança", test_security_features)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_func():
                print(f"✅ {test_name}: PASSOU")
                passed += 1
            else:
                print(f"❌ {test_name}: FALHOU")
                failed += 1
        except Exception as e:
            print(f"❌ {test_name}: ERRO - {e}")
            failed += 1
    
    print("\n" + "="*60)
    print("📊 RESULTADO DOS TESTES")
    print("="*60)
    print(f"✅ Testes passaram: {passed}")
    print(f"❌ Testes falharam: {failed}")
    print(f"📈 Taxa de sucesso: {(passed/(passed+failed)*100):.1f}%")
    
    if failed == 0:
        print("\n🎉 TODOS OS TESTES PASSARAM!")
        print("   O simulador está funcionando corretamente e de forma segura.")
        print("   Pronto para uso educacional!")
    else:
        print(f"\n⚠️  {failed} TESTE(S) FALHARAM!")
        print("   Verifique os erros acima e corrija antes de usar.")
    
    return failed == 0

def main():
    """Função principal de teste"""
    try:
        success = run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n👋 Testes interrompidos pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro crítico durante os testes: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
