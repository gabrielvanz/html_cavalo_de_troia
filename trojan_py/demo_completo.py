#!/usr/bin/env python3
"""
Demonstração Completa - Simulador Educacional de Cavalo de Tróia
================================================================

Este script demonstra todas as funcionalidades do simulador educacional
de forma integrada e sequencial.

Autor: Equipe de Criptografia e Segurança - Atitus Educação
Integrantes: Diogo Chaves, Gabriel Vanz, Vitor Badin
Ano: 2024
"""

import time
import sys
import os
from datetime import datetime

# Importar módulos do simulador
try:
    from trojan_horse_simulation import TrojanSimulator, SimulationType
    from trojan_education_modules import TrojanEducationModules
    from trojan_security_analysis import TrojanSecurityAnalyzer
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    print("Certifique-se de que todos os arquivos estão no mesmo diretório.")
    sys.exit(1)

class DemoTrojanSimulator:
    """Demonstração completa do simulador educacional"""
    
    def __init__(self):
        self.simulator = TrojanSimulator()
        self.education = TrojanEducationModules()
        self.analyzer = TrojanSecurityAnalyzer()
        self.demo_start_time = datetime.now()
        
    def display_banner(self):
        """Exibe banner de demonstração"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🐴 DEMONSTRAÇÃO COMPLETA 🐴                              ║
║              SIMULADOR EDUCACIONAL DE CAVALO DE TRÓIA                       ║
║                                                                              ║
║  Criptografia e Segurança - Atitus Educação                                 ║
║  Integrantes: Diogo Chaves, Gabriel Vanz, Vitor Badin                      ║
║  Ano: 2024                                                                  ║
║                                                                              ║
║  ⚠️  DESTINADO EXCLUSIVAMENTE PARA FINS EDUCACIONAIS ⚠️                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
        time.sleep(2)
    
    def demo_educational_simulation(self):
        """Demonstra simulação educacional"""
        print("\n" + "="*60)
        print("📚 DEMONSTRAÇÃO 1: SIMULAÇÃO EDUCACIONAL")
        print("="*60)
        
        print("Executando simulação educacional...")
        result = self.simulator.simulate_trojan_behavior(SimulationType.EDUCATIONAL)
        
        print(f"\n✅ Simulação educacional concluída!")
        print(f"   Tempo de execução: {result['execution_time']:.2f}s")
        print(f"   Conceitos demonstrados: {result['concepts_demonstrated']}")
        print(f"   Modo sandbox: {result['sandbox_mode']}")
        
        time.sleep(3)
    
    def demo_detection_simulation(self):
        """Demonstra simulação de detecção"""
        print("\n" + "="*60)
        print("🔍 DEMONSTRAÇÃO 2: SIMULAÇÃO DE DETECÇÃO")
        print("="*60)
        
        print("Executando simulação de detecção...")
        result = self.simulator.simulate_trojan_behavior(SimulationType.DETECTION)
        
        print(f"\n✅ Simulação de detecção concluída!")
        print(f"   Tempo de execução: {result['execution_time']:.2f}s")
        print(f"   Métodos testados: {result['methods_tested']}")
        print(f"   Ameaças detectadas: {result['threats_detected']}/{result['total_threats']}")
        print(f"   Taxa de detecção: {result['detection_rate']:.1%}")
        
        time.sleep(3)
    
    def demo_prevention_simulation(self):
        """Demonstra simulação de prevenção"""
        print("\n" + "="*60)
        print("🛡️ DEMONSTRAÇÃO 3: SIMULAÇÃO DE PREVENÇÃO")
        print("="*60)
        
        print("Executando simulação de prevenção...")
        result = self.simulator.simulate_trojan_behavior(SimulationType.PREVENTION)
        
        print(f"\n✅ Simulação de prevenção concluída!")
        print(f"   Tempo de execução: {result['execution_time']:.2f}s")
        print(f"   Medidas implementadas: {result['measures_implemented']}/{result['total_measures']}")
        print(f"   Ataques bloqueados: {result['attacks_blocked']}/{result['total_attacks']}")
        print(f"   Taxa de proteção: {result['protection_rate']:.1%}")
        
        time.sleep(3)
    
    def demo_analysis_simulation(self):
        """Demonstra simulação de análise"""
        print("\n" + "="*60)
        print("🔬 DEMONSTRAÇÃO 4: SIMULAÇÃO DE ANÁLISE")
        print("="*60)
        
        print("Executando simulação de análise...")
        result = self.simulator.simulate_trojan_behavior(SimulationType.ANALYSIS)
        
        print(f"\n✅ Simulação de análise concluída!")
        print(f"   Tempo de execução: {result['execution_time']:.2f}s")
        print(f"   Características analisadas: {result['characteristics_analyzed']}")
        print(f"   Achados estáticos: {result['static_findings']}")
        print(f"   Achados dinâmicos: {result['dynamic_findings']}")
        print(f"   Pontuação de ameaça: {result['threat_score']}/100")
        print(f"   Nível de ameaça: {result['threat_level']}")
        
        time.sleep(3)
    
    def demo_education_modules(self):
        """Demonstra módulos educacionais"""
        print("\n" + "="*60)
        print("📖 DEMONSTRAÇÃO 5: MÓDULOS EDUCACIONAIS")
        print("="*60)
        
        print("Demonstrando ciclo de vida de trojan...")
        self.education.demonstrate_trojan_lifecycle()
        time.sleep(2)
        
        print("\nDemonstrando técnicas de detecção...")
        self.education.demonstrate_detection_techniques()
        time.sleep(2)
        
        print("\nDemonstrando medidas de prevenção...")
        self.education.demonstrate_prevention_measures()
        time.sleep(2)
        
        print("\nSimulando cenário de ataque por e-mail...")
        result = self.education.simulate_attack_scenario(0)
        print(f"   Cenário: {result['scenario']}")
        print(f"   Vetor: {result['vector']}")
        print(f"   Etapas: {result['steps_count']}")
        print(f"   Medidas de prevenção: {result['prevention_count']}")
        
        time.sleep(2)
        
        print("\nAnalisando exemplo de trojan Zeus...")
        result = self.education.analyze_trojan_example(0)
        print(f"   Nome: {result['name']}")
        print(f"   Família: {result['family']}")
        print(f"   Dificuldade de detecção: {result['detection_difficulty']}/10")
        print(f"   Nível de risco: {result['risk_level']}")
        
        time.sleep(3)
    
    def demo_security_analysis(self):
        """Demonstra análise de segurança"""
        print("\n" + "="*60)
        print("🔍 DEMONSTRAÇÃO 6: ANÁLISE DE SEGURANÇA")
        print("="*60)
        
        print("Realizando análise estática de arquivo...")
        findings = self.analyzer.analyze_file_static("trojan_example.py")
        print(f"   Achados encontrados: {len(findings)}")
        
        for finding in findings:
            print(f"   • {finding.description} ({finding.indicator.value})")
        
        time.sleep(2)
        
        print("\nAnalisando tráfego de rede...")
        traffic_data = {
            "domains": ["malicious-site.com", "google.com"],
            "ips": ["192.168.1.100", "8.8.8.8"],
            "ports": [80, 443, 8080]
        }
        findings = self.analyzer.analyze_network_traffic(traffic_data)
        print(f"   Achados de rede: {len(findings)}")
        
        for finding in findings:
            print(f"   • {finding.description} ({finding.indicator.value})")
        
        time.sleep(2)
        
        print("\nRealizando análise comportamental...")
        behavior_data = {
            "registry_modifications": 8,
            "files_created": 15,
            "network_connections": 5,
            "persistence_attempts": 2
        }
        findings = self.analyzer.analyze_behavior(behavior_data)
        print(f"   Achados comportamentais: {len(findings)}")
        
        for finding in findings:
            print(f"   • {finding.description} ({finding.indicator.value})")
        
        time.sleep(3)
    
    def demo_quiz_educational(self):
        """Demonstra quiz educacional"""
        print("\n" + "="*60)
        print("📚 DEMONSTRAÇÃO 7: QUIZ EDUCACIONAL")
        print("="*60)
        
        print("Executando quiz educacional...")
        result = self.education.run_educational_quiz()
        
        print(f"\n✅ Quiz concluído!")
        print(f"   Respostas corretas: {result['correct_answers']}/{result['total_questions']}")
        print(f"   Pontuação: {result['score']:.1f}%")
        print(f"   Aprovado: {'Sim' if result['passed'] else 'Não'}")
        
        time.sleep(3)
    
    def demo_reports_and_export(self):
        """Demonstra geração de relatórios e exportação"""
        print("\n" + "="*60)
        print("📊 DEMONSTRAÇÃO 8: RELATÓRIOS E EXPORTAÇÃO")
        print("="*60)
        
        print("Gerando relatório de segurança...")
        report = self.simulator.generate_security_report()
        print("Relatório gerado com sucesso!")
        
        print("\nGerando relatório de análise...")
        analysis_report = self.analyzer.generate_analysis_report()
        print("Relatório de análise gerado com sucesso!")
        
        print("\nExportando dados da simulação...")
        sim_filename = self.simulator.export_simulation_data()
        print(f"   Dados exportados para: {sim_filename}")
        
        print("\nExportando dados de análise...")
        analysis_filename = self.analyzer.export_analysis_data()
        print(f"   Dados exportados para: {analysis_filename}")
        
        time.sleep(3)
    
    def demo_security_warnings(self):
        """Demonstra avisos de segurança"""
        print("\n" + "="*60)
        print("⚠️ DEMONSTRAÇÃO 9: AVISOS DE SEGURANÇA")
        print("="*60)
        
        print("Exibindo avisos de segurança...")
        self.simulator.display_warning()
        
        print("\nDemonstrando logs de auditoria...")
        print("Verificando arquivo de log...")
        
        if os.path.exists('trojan_simulation.log'):
            print("✅ Arquivo de log encontrado!")
            with open('trojan_simulation.log', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                print(f"   Total de linhas de log: {len(lines)}")
                print("   Últimas 3 linhas:")
                for line in lines[-3:]:
                    print(f"   {line.strip()}")
        else:
            print("❌ Arquivo de log não encontrado")
        
        time.sleep(3)
    
    def generate_demo_summary(self):
        """Gera resumo da demonstração"""
        print("\n" + "="*60)
        print("📋 RESUMO DA DEMONSTRAÇÃO")
        print("="*60)
        
        demo_duration = datetime.now() - self.demo_start_time
        
        print(f"⏱️  Duração total: {demo_duration.total_seconds():.1f} segundos")
        print(f"📊 Simulações executadas: 4")
        print(f"📚 Módulos educacionais: 5")
        print(f"🔍 Análises de segurança: 3")
        print(f"📝 Relatórios gerados: 2")
        print(f"💾 Arquivos exportados: 2")
        
        print("\n✅ Demonstração concluída com sucesso!")
        print("   Todos os módulos foram testados e funcionando corretamente.")
        print("   O simulador está pronto para uso educacional.")
        
        print("\n🎓 Funcionalidades demonstradas:")
        print("   • Simulação educacional de trojans")
        print("   • Técnicas de detecção e prevenção")
        print("   • Análise de segurança")
        print("   • Módulos educacionais interativos")
        print("   • Geração de relatórios")
        print("   • Exportação de dados")
        print("   • Logs de auditoria")
        print("   • Avisos de segurança")
    
    def run_complete_demo(self):
        """Executa demonstração completa"""
        try:
            self.display_banner()
            
            # Aguardar confirmação do usuário
            input("\nPressione ENTER para iniciar a demonstração completa...")
            
            # Executar todas as demonstrações
            self.demo_educational_simulation()
            self.demo_detection_simulation()
            self.demo_prevention_simulation()
            self.demo_analysis_simulation()
            self.demo_education_modules()
            self.demo_security_analysis()
            self.demo_quiz_educational()
            self.demo_reports_and_export()
            self.demo_security_warnings()
            
            # Gerar resumo
            self.generate_demo_summary()
            
        except KeyboardInterrupt:
            print("\n\n👋 Demonstração interrompida pelo usuário.")
        except Exception as e:
            print(f"\n❌ Erro durante a demonstração: {e}")
            print("Verifique se todos os módulos estão funcionando corretamente.")

def main():
    """Função principal da demonstração"""
    print("🐴 Iniciando Demonstração Completa do Simulador Educacional")
    print("   Cavalo de Tróia - Criptografia e Segurança")
    print()
    
    demo = DemoTrojanSimulator()
    demo.run_complete_demo()

if __name__ == "__main__":
    main()
