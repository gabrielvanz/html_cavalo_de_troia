#!/usr/bin/env python3
"""
Cavalo de Tróia - Simulação Educacional de Segurança Cibernética
================================================================

Este é um simulador educacional para demonstrar conceitos de segurança cibernética
relacionados ao Cavalo de Tróia (Trojan Horse). O código foi desenvolvido exclusivamente
para fins educacionais e de conscientização sobre segurança.

IMPORTANTE: Este simulador é destinado apenas para fins educacionais e de pesquisa
em segurança cibernética. O uso malicioso de qualquer código aqui apresentado é
expressamente proibido e pode resultar em consequências legais severas.

Autor: Equipe de Criptografia e Segurança - Atitus Educação
Integrantes: Diogo Chaves, Gabriel Vanz, Vitor Badin
Ano: 2024
"""

import os
import sys
import time
import random
import hashlib
import json
import threading
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import logging

# Configuração de logging para auditoria
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trojan_simulation.log'),
        logging.StreamHandler()
    ]
)

class ThreatLevel(Enum):
    """Níveis de ameaça para classificação de simulações"""
    LOW = "Baixo"
    MEDIUM = "Médio"
    HIGH = "Alto"
    CRITICAL = "Crítico"

class SimulationType(Enum):
    """Tipos de simulação disponíveis"""
    EDUCATIONAL = "Educacional"
    DETECTION = "Detecção"
    PREVENTION = "Prevenção"
    ANALYSIS = "Análise"

@dataclass
class SecurityEvent:
    """Estrutura para eventos de segurança"""
    timestamp: datetime
    event_type: str
    description: str
    threat_level: ThreatLevel
    source: str
    details: Dict

class TrojanSimulator:
    """
    Simulador educacional de Cavalo de Tróia
    
    Esta classe implementa simulações controladas e seguras para demonstrar
    conceitos de segurança cibernética relacionados a trojans.
    """
    
    def __init__(self):
        self.simulation_active = False
        self.security_events: List[SecurityEvent] = []
        self.detection_systems = []
        self.prevention_measures = []
        self.simulation_log = []
        
        # Configurações de segurança
        self.max_simulation_time = 300  # 5 minutos máximo
        self.sandbox_mode = True  # Modo sandbox ativado por padrão
        self.ethical_mode = True  # Modo ético ativado
        
        # Inicializar sistemas de segurança
        self._initialize_security_systems()
        
        logging.info("Simulador de Cavalo de Tróia inicializado em modo educacional")
    
    def _initialize_security_systems(self):
        """Inicializa sistemas de segurança e prevenção"""
        self.detection_systems = [
            "Antivírus Simulado",
            "Firewall Educacional",
            "Sistema de Detecção de Intrusão",
            "Análise Comportamental",
            "Sandbox de Segurança"
        ]
        
        self.prevention_measures = [
            "Validação de Entrada",
            "Criptografia de Dados",
            "Backup Automático",
            "Monitoramento de Rede",
            "Educação do Usuário"
        ]
    
    def display_warning(self):
        """Exibe avisos de segurança e ética"""
        warning = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                           ⚠️  AVISO IMPORTANTE ⚠️                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Este é um SIMULADOR EDUCACIONAL para fins de conscientização sobre        ║
║  segurança cibernética. O uso malicioso de qualquer código aqui             ║
║  apresentado é EXPRESSAMENTE PROIBIDO e pode resultar em:                   ║
║                                                                              ║
║  • Consequências legais severas (Lei 12.737/2012 - Brasil)                 ║
║  • Prisão de 3 a 5 anos                                                    ║
║  • Multas e indenizações às vítimas                                        ║
║  • Responsabilização civil e criminal                                      ║
║                                                                              ║
║  Este simulador opera em MODO SANDBOX e não pode causar danos reais.       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(warning)
        
        # Log do aviso
        self._log_security_event(
            "WARNING_DISPLAYED",
            "Aviso de segurança exibido ao usuário",
            ThreatLevel.MEDIUM,
            "SecuritySystem"
        )
    
    def _log_security_event(self, event_type: str, description: str, 
                          threat_level: ThreatLevel, source: str, details: Dict = None):
        """Registra eventos de segurança para auditoria"""
        event = SecurityEvent(
            timestamp=datetime.now(),
            event_type=event_type,
            description=description,
            threat_level=threat_level,
            source=source,
            details=details or {}
        )
        self.security_events.append(event)
        logging.info(f"Evento de segurança: {event_type} - {description}")
    
    def simulate_trojan_behavior(self, simulation_type: SimulationType) -> Dict:
        """
        Simula comportamento de trojan de forma controlada e educacional
        
        Args:
            simulation_type: Tipo de simulação a ser executada
            
        Returns:
            Dict com resultados da simulação
        """
        if not self.ethical_mode:
            raise ValueError("Simulação só pode ser executada em modo ético")
        
        self.simulation_active = True
        start_time = time.time()
        
        print(f"\n🔍 Iniciando simulação: {simulation_type.value}")
        print("=" * 60)
        
        # Log do início da simulação
        self._log_security_event(
            "SIMULATION_STARTED",
            f"Simulação {simulation_type.value} iniciada",
            ThreatLevel.LOW,
            "SimulationEngine",
            {"type": simulation_type.value}
        )
        
        try:
            if simulation_type == SimulationType.EDUCATIONAL:
                result = self._run_educational_simulation()
            elif simulation_type == SimulationType.DETECTION:
                result = self._run_detection_simulation()
            elif simulation_type == SimulationType.PREVENTION:
                result = self._run_prevention_simulation()
            elif simulation_type == SimulationType.ANALYSIS:
                result = self._run_analysis_simulation()
            else:
                raise ValueError("Tipo de simulação inválido")
            
            # Verificar tempo máximo
            elapsed_time = time.time() - start_time
            if elapsed_time > self.max_simulation_time:
                print("⏰ Simulação interrompida: tempo máximo excedido")
                self._log_security_event(
                    "SIMULATION_TIMEOUT",
                    "Simulação interrompida por timeout",
                    ThreatLevel.MEDIUM,
                    "SimulationEngine"
                )
            
            result["execution_time"] = elapsed_time
            result["success"] = True
            
        except Exception as e:
            result = {
                "success": False,
                "error": str(e),
                "execution_time": time.time() - start_time
            }
            logging.error(f"Erro na simulação: {e}")
        
        finally:
            self.simulation_active = False
            self._log_security_event(
                "SIMULATION_ENDED",
                f"Simulação {simulation_type.value} finalizada",
                ThreatLevel.LOW,
                "SimulationEngine",
                result
            )
        
        return result
    
    def _run_educational_simulation(self) -> Dict:
        """Executa simulação educacional sobre trojans"""
        print("\n📚 Simulação Educacional - Cavalo de Tróia")
        print("-" * 50)
        
        # Demonstração de conceitos básicos
        concepts = [
            "1. Disfarce: O trojan se apresenta como software legítimo",
            "2. Execução: Requer ação do usuário para ser executado",
            "3. Instalação: Instala-se silenciosamente no sistema",
            "4. Ativação: Inicia atividades maliciosas",
            "5. Persistência: Mantém-se ativo no sistema"
        ]
        
        for concept in concepts:
            print(f"   {concept}")
            time.sleep(1)
        
        # Simulação de processo de infecção
        print("\n🦠 Simulando processo de infecção (SANDBOX):")
        infection_steps = [
            "   • Arquivo suspeito detectado",
            "   • Usuário executa arquivo (simulado)",
            "   • Trojan se instala silenciosamente",
            "   • Modifica configurações do sistema",
            "   • Estabelece conexão remota",
            "   • Inicia coleta de dados"
        ]
        
        for step in infection_steps:
            print(step)
            time.sleep(0.5)
        
        # Demonstração de técnicas de ocultação
        print("\n👁️ Técnicas de ocultação (simuladas):")
        hiding_techniques = [
            "   • Rootkit: Ocultação profunda no sistema",
            "   • Polimorfismo: Mudança de código",
            "   • Criptografia: Código criptografado",
            "   • Packing: Compressão e ofuscação"
        ]
        
        for technique in hiding_techniques:
            print(technique)
            time.sleep(0.5)
        
        return {
            "type": "educational",
            "concepts_demonstrated": len(concepts),
            "infection_steps": len(infection_steps),
            "hiding_techniques": len(hiding_techniques),
            "sandbox_mode": True
        }
    
    def _run_detection_simulation(self) -> Dict:
        """Executa simulação de detecção de trojans"""
        print("\n🔍 Simulação de Detecção de Trojans")
        print("-" * 50)
        
        # Simular diferentes métodos de detecção
        detection_methods = [
            ("Antivírus", "Detecção por assinatura", 0.85),
            ("Análise Heurística", "Detecção comportamental", 0.70),
            ("Sandbox", "Execução em ambiente isolado", 0.90),
            ("Machine Learning", "IA para detecção", 0.80),
            ("Análise de Rede", "Monitoramento de tráfego", 0.75)
        ]
        
        detected_threats = 0
        total_threats = 10  # Simular 10 ameaças
        
        print(f"🎯 Simulando detecção de {total_threats} ameaças:")
        print()
        
        for method, description, accuracy in detection_methods:
            print(f"   {method}: {description}")
            print(f"   Precisão: {accuracy:.0%}")
            
            # Simular detecção
            threats_found = int(total_threats * accuracy * random.uniform(0.8, 1.0))
            detected_threats += threats_found
            
            print(f"   Ameaças detectadas: {threats_found}")
            print()
            time.sleep(1)
        
        # Simular análise de comportamento suspeito
        print("🔬 Análise comportamental em tempo real:")
        behaviors = [
            "   • Acesso não autorizado a arquivos sensíveis",
            "   • Comunicação com servidores suspeitos",
            "   • Modificação de configurações do sistema",
            "   • Tentativas de elevação de privilégios",
            "   • Criação de processos em segundo plano"
        ]
        
        for behavior in behaviors:
            print(behavior)
            time.sleep(0.3)
        
        detection_rate = detected_threats / total_threats
        print(f"\n📊 Taxa de detecção: {detection_rate:.1%}")
        
        return {
            "type": "detection",
            "methods_tested": len(detection_methods),
            "threats_detected": detected_threats,
            "total_threats": total_threats,
            "detection_rate": detection_rate
        }
    
    def _run_prevention_simulation(self) -> Dict:
        """Executa simulação de medidas de prevenção"""
        print("\n🛡️ Simulação de Medidas de Prevenção")
        print("-" * 50)
        
        # Simular implementação de medidas de prevenção
        prevention_measures = [
            ("Firewall", "Bloqueio de conexões suspeitas", "Implementado"),
            ("Antivírus", "Proteção em tempo real", "Atualizado"),
            ("Backup", "Cópias de segurança regulares", "Configurado"),
            ("Educação", "Treinamento de usuários", "Em andamento"),
            ("Atualizações", "Patches de segurança", "Automático"),
            ("Monitoramento", "Análise de rede", "Ativo"),
            ("Criptografia", "Proteção de dados", "Habilitado"),
            ("Controle de Acesso", "Autenticação multifator", "Configurado")
        ]
        
        implemented_measures = 0
        total_measures = len(prevention_measures)
        
        print("🔧 Implementando medidas de prevenção:")
        print()
        
        for measure, description, status in prevention_measures:
            print(f"   {measure}: {description}")
            print(f"   Status: {status}")
            
            if status in ["Implementado", "Atualizado", "Configurado", "Ativo", "Habilitado"]:
                implemented_measures += 1
                print("   ✅ Proteção ativa")
            else:
                print("   ⚠️  Requer atenção")
            
            print()
            time.sleep(0.5)
        
        # Simular teste de penetração
        print("🧪 Testando resistência a ataques:")
        attack_vectors = [
            "   • E-mail de phishing",
            "   • Download malicioso",
            "   • Exploração de vulnerabilidades",
            "   • Ataque de força bruta",
            "   • Engenharia social"
        ]
        
        blocked_attacks = 0
        for vector in attack_vectors:
            print(vector)
            # Simular bloqueio baseado nas medidas implementadas
            if random.random() < (implemented_measures / total_measures):
                print("   ✅ Ataque bloqueado")
                blocked_attacks += 1
            else:
                print("   ❌ Ataque bem-sucedido")
            time.sleep(0.3)
        
        protection_rate = blocked_attacks / len(attack_vectors)
        print(f"\n📊 Taxa de proteção: {protection_rate:.1%}")
        
        return {
            "type": "prevention",
            "measures_implemented": implemented_measures,
            "total_measures": total_measures,
            "attacks_blocked": blocked_attacks,
            "total_attacks": len(attack_vectors),
            "protection_rate": protection_rate
        }
    
    def _run_analysis_simulation(self) -> Dict:
        """Executa simulação de análise de trojans"""
        print("\n🔬 Simulação de Análise de Trojans")
        print("-" * 50)
        
        # Simular análise de amostra de trojan
        print("📋 Analisando amostra de trojan (simulada):")
        print()
        
        # Características do trojan simulado
        trojan_characteristics = {
            "Tamanho": "2.3 MB",
            "Tipo": "Banking Trojan",
            "Técnicas": ["Keylogging", "Screen Capture", "Data Exfiltration"],
            "Comunicação": "C&C Server: 192.168.1.100:8080",
            "Persistence": "Registry Modification",
            "Evasion": "Code Obfuscation"
        }
        
        for characteristic, value in trojan_characteristics.items():
            print(f"   {characteristic}: {value}")
            time.sleep(0.3)
        
        # Simular análise estática
        print("\n🔍 Análise estática:")
        static_analysis = [
            "   • Strings suspeitas encontradas",
            "   • APIs maliciosas identificadas",
            "   • Criptografia de dados detectada",
            "   • Ocultação de código confirmada",
            "   • Assinatura de malware conhecido"
        ]
        
        for analysis in static_analysis:
            print(analysis)
            time.sleep(0.3)
        
        # Simular análise dinâmica
        print("\n⚡ Análise dinâmica (sandbox):")
        dynamic_analysis = [
            "   • Modificação de arquivos do sistema",
            "   • Criação de processos suspeitos",
            "   • Comunicação de rede maliciosa",
            "   • Tentativas de persistência",
            "   • Coleta de dados sensíveis"
        ]
        
        for analysis in dynamic_analysis:
            print(analysis)
            time.sleep(0.3)
        
        # Simular classificação de ameaça
        threat_score = random.randint(70, 95)
        print(f"\n⚠️  Pontuação de ameaça: {threat_score}/100")
        
        if threat_score >= 90:
            threat_level = "CRÍTICA"
        elif threat_score >= 70:
            threat_level = "ALTA"
        elif threat_score >= 50:
            threat_level = "MÉDIA"
        else:
            threat_level = "BAIXA"
        
        print(f"   Nível de ameaça: {threat_level}")
        
        return {
            "type": "analysis",
            "characteristics_analyzed": len(trojan_characteristics),
            "static_findings": len(static_analysis),
            "dynamic_findings": len(dynamic_analysis),
            "threat_score": threat_score,
            "threat_level": threat_level
        }
    
    def generate_security_report(self) -> str:
        """Gera relatório de segurança baseado nas simulações"""
        if not self.security_events:
            return "Nenhum evento de segurança registrado."
        
        report = []
        report.append("=" * 60)
        report.append("RELATÓRIO DE SEGURANÇA - SIMULADOR DE CAVALO DE TRÓIA")
        report.append("=" * 60)
        report.append(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        report.append(f"Total de eventos: {len(self.security_events)}")
        report.append("")
        
        # Agrupar eventos por tipo
        event_types = {}
        for event in self.security_events:
            if event.event_type not in event_types:
                event_types[event.event_type] = []
            event_types[event.event_type].append(event)
        
        for event_type, events in event_types.items():
            report.append(f"📊 {event_type}:")
            for event in events:
                report.append(f"   • {event.timestamp.strftime('%H:%M:%S')} - {event.description}")
            report.append("")
        
        # Estatísticas de ameaças
        threat_levels = {}
        for event in self.security_events:
            level = event.threat_level.value
            threat_levels[level] = threat_levels.get(level, 0) + 1
        
        if threat_levels:
            report.append("📈 Estatísticas de Níveis de Ameaça:")
            for level, count in threat_levels.items():
                report.append(f"   • {level}: {count} eventos")
            report.append("")
        
        report.append("=" * 60)
        report.append("FIM DO RELATÓRIO")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def export_simulation_data(self, filename: str = None) -> str:
        """Exporta dados da simulação para arquivo JSON"""
        if filename is None:
            filename = f"trojan_simulation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        data = {
            "simulation_info": {
                "timestamp": datetime.now().isoformat(),
                "total_events": len(self.security_events),
                "simulation_active": self.simulation_active,
                "sandbox_mode": self.sandbox_mode,
                "ethical_mode": self.ethical_mode
            },
            "security_events": [
                {
                    "timestamp": event.timestamp.isoformat(),
                    "event_type": event.event_type,
                    "description": event.description,
                    "threat_level": event.threat_level.value,
                    "source": event.source,
                    "details": event.details
                }
                for event in self.security_events
            ],
            "detection_systems": self.detection_systems,
            "prevention_measures": self.prevention_measures
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            logging.info(f"Dados da simulação exportados para: {filename}")
            return filename
        except Exception as e:
            logging.error(f"Erro ao exportar dados: {e}")
            raise

def main():
    """Função principal do simulador"""
    print("🐴 Simulador Educacional de Cavalo de Tróia")
    print("   Criptografia e Segurança - Atitus Educação")
    print("   Integrantes: Diogo Chaves, Gabriel Vanz, Vitor Badin")
    print()
    
    # Inicializar simulador
    simulator = TrojanSimulator()
    
    # Exibir aviso de segurança
    simulator.display_warning()
    
    # Menu principal
    while True:
        print("\n" + "=" * 60)
        print("MENU PRINCIPAL - SIMULADOR EDUCACIONAL")
        print("=" * 60)
        print("1. Simulação Educacional")
        print("2. Simulação de Detecção")
        print("3. Simulação de Prevenção")
        print("4. Simulação de Análise")
        print("5. Gerar Relatório de Segurança")
        print("6. Exportar Dados da Simulação")
        print("7. Sair")
        print("=" * 60)
        
        try:
            choice = input("\nEscolha uma opção (1-7): ").strip()
            
            if choice == "1":
                result = simulator.simulate_trojan_behavior(SimulationType.EDUCATIONAL)
                print(f"\n✅ Simulação educacional concluída em {result['execution_time']:.2f}s")
                
            elif choice == "2":
                result = simulator.simulate_trojan_behavior(SimulationType.DETECTION)
                print(f"\n✅ Simulação de detecção concluída em {result['execution_time']:.2f}s")
                
            elif choice == "3":
                result = simulator.simulate_trojan_behavior(SimulationType.PREVENTION)
                print(f"\n✅ Simulação de prevenção concluída em {result['execution_time']:.2f}s")
                
            elif choice == "4":
                result = simulator.simulate_trojan_behavior(SimulationType.ANALYSIS)
                print(f"\n✅ Simulação de análise concluída em {result['execution_time']:.2f}s")
                
            elif choice == "5":
                report = simulator.generate_security_report()
                print("\n" + report)
                
            elif choice == "6":
                filename = simulator.export_simulation_data()
                print(f"\n✅ Dados exportados para: {filename}")
                
            elif choice == "7":
                print("\n👋 Encerrando simulador...")
                print("Obrigado por usar o Simulador Educacional de Cavalo de Tróia!")
                break
                
            else:
                print("\n❌ Opção inválida. Tente novamente.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Simulador interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")
            logging.error(f"Erro no menu principal: {e}")

if __name__ == "__main__":
    main()
