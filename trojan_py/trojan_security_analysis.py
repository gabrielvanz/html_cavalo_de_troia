#!/usr/bin/env python3
"""
Módulo de Análise de Segurança para Simulação de Cavalo de Tróia
================================================================

Este módulo implementa ferramentas de análise de segurança para demonstrar
como detectar e analisar trojans de forma educacional e ética.

Autor: Equipe de Criptografia e Segurança - Atitus Educação
Integrantes: Diogo Chaves, Gabriel Vanz, Vitor Badin
Ano: 2024
"""

import hashlib
import json
import re
import time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import logging

class AnalysisType(Enum):
    """Tipos de análise de segurança"""
    STATIC = "Análise Estática"
    DYNAMIC = "Análise Dinâmica"
    BEHAVIORAL = "Análise Comportamental"
    NETWORK = "Análise de Rede"
    MEMORY = "Análise de Memória"

class ThreatIndicator(Enum):
    """Indicadores de ameaça"""
    HIGH = "Alto"
    MEDIUM = "Médio"
    LOW = "Baixo"
    INFO = "Informativo"

@dataclass
class SecurityFinding:
    """Estrutura para achados de segurança"""
    indicator: ThreatIndicator
    category: str
    description: str
    evidence: str
    recommendation: str
    confidence: float  # 0.0 a 1.0

@dataclass
class MalwareSignature:
    """Assinatura de malware para detecção"""
    name: str
    pattern: str
    description: str
    family: str
    severity: ThreatIndicator

class TrojanSecurityAnalyzer:
    """Analisador de segurança para trojans"""
    
    def __init__(self):
        self.signatures = self._load_malware_signatures()
        self.suspicious_patterns = self._load_suspicious_patterns()
        self.network_indicators = self._load_network_indicators()
        self.analysis_results = []
        
        # Configurar logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def _load_malware_signatures(self) -> List[MalwareSignature]:
        """Carrega assinaturas de malware conhecidas"""
        return [
            MalwareSignature(
                name="Zeus_Trojan",
                pattern=r"(?i)(zeus|zbot|gameover)",
                description="Assinatura do trojan Zeus",
                family="Banking Trojan",
                severity=ThreatIndicator.HIGH
            ),
            MalwareSignature(
                name="Emotet_Trojan",
                pattern=r"(?i)(emotet|geodo|heodo)",
                description="Assinatura do trojan Emotet",
                family="Downloader Trojan",
                severity=ThreatIndicator.HIGH
            ),
            MalwareSignature(
                name="TrickBot_Trojan",
                pattern=r"(?i)(trickbot|trick)",
                description="Assinatura do trojan TrickBot",
                family="Banking Trojan",
                severity=ThreatIndicator.HIGH
            ),
            MalwareSignature(
                name="Generic_Keylogger",
                pattern=r"(?i)(keylog|keystroke|keyboard)",
                description="Padrão genérico de keylogger",
                family="Keylogger",
                severity=ThreatIndicator.MEDIUM
            ),
            MalwareSignature(
                name="Remote_Access",
                pattern=r"(?i)(remote|backdoor|rat)",
                description="Padrão de acesso remoto",
                family="RAT",
                severity=ThreatIndicator.HIGH
            )
        ]
    
    def _load_suspicious_patterns(self) -> List[Dict]:
        """Carrega padrões suspeitos para análise"""
        return [
            {
                "name": "Registry Modification",
                "pattern": r"(?i)(regedit|registry|hkey)",
                "description": "Modificação do registro do Windows",
                "severity": ThreatIndicator.MEDIUM
            },
            {
                "name": "File System Access",
                "pattern": r"(?i)(createfile|writefile|readfile)",
                "description": "Acesso suspeito ao sistema de arquivos",
                "severity": ThreatIndicator.MEDIUM
            },
            {
                "name": "Network Communication",
                "pattern": r"(?i)(socket|connect|send|recv)",
                "description": "Comunicação de rede suspeita",
                "severity": ThreatIndicator.MEDIUM
            },
            {
                "name": "Process Injection",
                "pattern": r"(?i)(inject|dll|process)",
                "description": "Injeção de processo suspeita",
                "severity": ThreatIndicator.HIGH
            },
            {
                "name": "Persistence Mechanism",
                "pattern": r"(?i)(startup|autostart|service)",
                "description": "Mecanismo de persistência",
                "severity": ThreatIndicator.MEDIUM
            }
        ]
    
    def _load_network_indicators(self) -> List[Dict]:
        """Carrega indicadores de rede maliciosos"""
        return [
            {
                "domain": "malicious-site.com",
                "ip": "192.168.1.100",
                "description": "Servidor C&C suspeito",
                "severity": ThreatIndicator.HIGH
            },
            {
                "domain": "phishing-bank.net",
                "ip": "10.0.0.50",
                "description": "Site de phishing bancário",
                "severity": ThreatIndicator.HIGH
            },
            {
                "domain": "malware-distribution.org",
                "ip": "172.16.0.25",
                "description": "Distribuição de malware",
                "severity": ThreatIndicator.HIGH
            }
        ]
    
    def analyze_file_static(self, file_path: str) -> List[SecurityFinding]:
        """Realiza análise estática de arquivo"""
        self.logger.info(f"Iniciando análise estática de: {file_path}")
        findings = []
        
        try:
            # Simular leitura de arquivo (em ambiente real, seria um arquivo real)
            file_content = self._simulate_file_content(file_path)
            
            # Análise de assinaturas de malware
            for signature in self.signatures:
                if re.search(signature.pattern, file_content):
                    finding = SecurityFinding(
                        indicator=signature.severity,
                        category="Malware Signature",
                        description=f"Assinatura de malware detectada: {signature.name}",
                        evidence=f"Padrão encontrado: {signature.pattern}",
                        recommendation=f"Arquivo suspeito de ser {signature.family}",
                        confidence=0.9
                    )
                    findings.append(finding)
            
            # Análise de padrões suspeitos
            for pattern in self.suspicious_patterns:
                if re.search(pattern["pattern"], file_content):
                    finding = SecurityFinding(
                        indicator=pattern["severity"],
                        category="Suspicious Pattern",
                        description=f"Padrão suspeito detectado: {pattern['name']}",
                        evidence=f"Padrão: {pattern['pattern']}",
                        recommendation="Analisar comportamento do arquivo",
                        confidence=0.7
                    )
                    findings.append(finding)
            
            # Análise de hash
            file_hash = self._calculate_file_hash(file_content)
            if self._is_known_malware_hash(file_hash):
                finding = SecurityFinding(
                    indicator=ThreatIndicator.HIGH,
                    category="Known Malware Hash",
                    description="Hash do arquivo corresponde a malware conhecido",
                    evidence=f"Hash: {file_hash}",
                    recommendation="Arquivo deve ser removido imediatamente",
                    confidence=1.0
                )
                findings.append(finding)
            
        except Exception as e:
            self.logger.error(f"Erro na análise estática: {e}")
            finding = SecurityFinding(
                indicator=ThreatIndicator.INFO,
                category="Analysis Error",
                description=f"Erro durante análise: {str(e)}",
                evidence="Log de erro",
                recommendation="Verificar integridade do arquivo",
                confidence=0.0
            )
            findings.append(finding)
        
        self.analysis_results.extend(findings)
        return findings
    
    def analyze_network_traffic(self, traffic_data: Dict) -> List[SecurityFinding]:
        """Analisa tráfego de rede em busca de indicadores de trojan"""
        self.logger.info("Iniciando análise de tráfego de rede")
        findings = []
        
        # Verificar domínios suspeitos
        for domain in traffic_data.get("domains", []):
            for indicator in self.network_indicators:
                if domain == indicator["domain"]:
                    finding = SecurityFinding(
                        indicator=indicator["severity"],
                        category="Malicious Domain",
                        description=f"Domínio malicioso detectado: {domain}",
                        evidence=f"Domínio: {domain}",
                        recommendation="Bloquear comunicação com este domínio",
                        confidence=0.95
                    )
                    findings.append(finding)
        
        # Verificar IPs suspeitos
        for ip in traffic_data.get("ips", []):
            for indicator in self.network_indicators:
                if ip == indicator["ip"]:
                    finding = SecurityFinding(
                        indicator=indicator["severity"],
                        category="Malicious IP",
                        description=f"IP malicioso detectado: {ip}",
                        evidence=f"IP: {ip}",
                        recommendation="Bloquear comunicação com este IP",
                        confidence=0.95
                    )
                    findings.append(finding)
        
        # Verificar portas suspeitas
        for port in traffic_data.get("ports", []):
            if port in [4444, 6666, 8080, 31337]:  # Portas comumente usadas por trojans
                finding = SecurityFinding(
                    indicator=ThreatIndicator.MEDIUM,
                    category="Suspicious Port",
                    description=f"Porta suspeita detectada: {port}",
                    evidence=f"Porta: {port}",
                    recommendation="Investigar comunicação nesta porta",
                    confidence=0.6
                )
                findings.append(finding)
        
        self.analysis_results.extend(findings)
        return findings
    
    def analyze_behavior(self, behavior_data: Dict) -> List[SecurityFinding]:
        """Analisa comportamento de processo em busca de indicadores de trojan"""
        self.logger.info("Iniciando análise comportamental")
        findings = []
        
        # Verificar modificações de registro
        if behavior_data.get("registry_modifications", 0) > 5:
            finding = SecurityFinding(
                indicator=ThreatIndicator.MEDIUM,
                category="Registry Modification",
                description="Muitas modificações no registro detectadas",
                evidence=f"Modificações: {behavior_data['registry_modifications']}",
                recommendation="Investigar processo suspeito",
                confidence=0.7
            )
            findings.append(finding)
        
        # Verificar criação de arquivos
        if behavior_data.get("files_created", 0) > 10:
            finding = SecurityFinding(
                indicator=ThreatIndicator.MEDIUM,
                category="File Creation",
                description="Muitos arquivos criados pelo processo",
                evidence=f"Arquivos criados: {behavior_data['files_created']}",
                recommendation="Verificar propósito dos arquivos criados",
                confidence=0.6
            )
            findings.append(finding)
        
        # Verificar comunicação de rede
        if behavior_data.get("network_connections", 0) > 3:
            finding = SecurityFinding(
                indicator=ThreatIndicator.MEDIUM,
                category="Network Activity",
                description="Múltiplas conexões de rede detectadas",
                evidence=f"Conexões: {behavior_data['network_connections']}",
                recommendation="Analisar destinos das conexões",
                confidence=0.7
            )
            findings.append(finding)
        
        # Verificar tentativas de persistência
        if behavior_data.get("persistence_attempts", 0) > 0:
            finding = SecurityFinding(
                indicator=ThreatIndicator.HIGH,
                category="Persistence Attempt",
                description="Tentativas de persistência detectadas",
                evidence=f"Tentativas: {behavior_data['persistence_attempts']}",
                recommendation="Remover mecanismos de persistência",
                confidence=0.8
            )
            findings.append(finding)
        
        self.analysis_results.extend(findings)
        return findings
    
    def _simulate_file_content(self, file_path: str) -> str:
        """Simula conteúdo de arquivo para análise"""
        # Em um ambiente real, aqui seria lido o arquivo real
        # Para fins educacionais, simulamos conteúdo baseado no nome do arquivo
        
        if "trojan" in file_path.lower():
            return """
            # Simulated Trojan Code
            import socket
            import subprocess
            import os
            
            def connect_to_c2():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('malicious-site.com', 8080))
                return s
            
            def keylogger():
                # Keylogging functionality
                pass
            
            def persistence():
                # Registry modification for persistence
                pass
            """
        else:
            return """
            # Normal Application Code
            def main():
                print("Hello World")
            
            if __name__ == "__main__":
                main()
            """
    
    def _calculate_file_hash(self, content: str) -> str:
        """Calcula hash MD5 do conteúdo do arquivo"""
        return hashlib.md5(content.encode()).hexdigest()
    
    def _is_known_malware_hash(self, file_hash: str) -> bool:
        """Verifica se hash corresponde a malware conhecido"""
        # Simulação de banco de dados de hashes maliciosos
        known_malware_hashes = [
            "5d41402abc4b2a76b9719d911017c592",  # Exemplo de hash malicioso
            "098f6bcd4621d373cade4e832627b4f6",  # Outro exemplo
        ]
        return file_hash in known_malware_hashes
    
    def generate_analysis_report(self) -> str:
        """Gera relatório de análise de segurança"""
        if not self.analysis_results:
            return "Nenhuma análise realizada ainda."
        
        report = []
        report.append("=" * 60)
        report.append("RELATÓRIO DE ANÁLISE DE SEGURANÇA")
        report.append("=" * 60)
        report.append(f"Data/Hora: {time.strftime('%d/%m/%Y %H:%M:%S')}")
        report.append(f"Total de achados: {len(self.analysis_results)}")
        report.append("")
        
        # Agrupar achados por categoria
        categories = {}
        for finding in self.analysis_results:
            if finding.category not in categories:
                categories[finding.category] = []
            categories[finding.category].append(finding)
        
        for category, findings in categories.items():
            report.append(f"📊 {category}:")
            for finding in findings:
                report.append(f"   • {finding.description}")
                report.append(f"     Indicador: {finding.indicator.value}")
                report.append(f"     Evidência: {finding.evidence}")
                report.append(f"     Recomendação: {finding.recommendation}")
                report.append(f"     Confiança: {finding.confidence:.2f}")
                report.append("")
        
        # Estatísticas de ameaças
        threat_counts = {}
        for finding in self.analysis_results:
            level = finding.indicator.value
            threat_counts[level] = threat_counts.get(level, 0) + 1
        
        if threat_counts:
            report.append("📈 Estatísticas de Ameaças:")
            for level, count in threat_counts.items():
                report.append(f"   • {level}: {count} achados")
            report.append("")
        
        report.append("=" * 60)
        report.append("FIM DO RELATÓRIO")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def export_analysis_data(self, filename: str = None) -> str:
        """Exporta dados de análise para arquivo JSON"""
        if filename is None:
            filename = f"security_analysis_{int(time.time())}.json"
        
        data = {
            "analysis_info": {
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "total_findings": len(self.analysis_results),
                "analyzer_version": "1.0.0"
            },
            "findings": [
                {
                    "indicator": finding.indicator.value,
                    "category": finding.category,
                    "description": finding.description,
                    "evidence": finding.evidence,
                    "recommendation": finding.recommendation,
                    "confidence": finding.confidence
                }
                for finding in self.analysis_results
            ]
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Dados de análise exportados para: {filename}")
            return filename
        except Exception as e:
            self.logger.error(f"Erro ao exportar dados: {e}")
            raise

def main():
    """Função principal para testar o analisador de segurança"""
    print("🔍 Analisador de Segurança - Cavalo de Tróia")
    print("=" * 50)
    
    analyzer = TrojanSecurityAnalyzer()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Análise estática de arquivo")
        print("2. Análise de tráfego de rede")
        print("3. Análise comportamental")
        print("4. Gerar relatório de análise")
        print("5. Exportar dados de análise")
        print("6. Sair")
        
        choice = input("\nOpção: ").strip()
        
        try:
            if choice == "1":
                file_path = input("Caminho do arquivo (ou 'trojan' para simular): ")
                findings = analyzer.analyze_file_static(file_path)
                print(f"\n✅ Análise concluída. {len(findings)} achados encontrados.")
                
            elif choice == "2":
                # Simular dados de tráfego
                traffic_data = {
                    "domains": ["malicious-site.com", "google.com"],
                    "ips": ["192.168.1.100", "8.8.8.8"],
                    "ports": [80, 443, 8080]
                }
                findings = analyzer.analyze_network_traffic(traffic_data)
                print(f"\n✅ Análise de rede concluída. {len(findings)} achados encontrados.")
                
            elif choice == "3":
                # Simular dados comportamentais
                behavior_data = {
                    "registry_modifications": 8,
                    "files_created": 15,
                    "network_connections": 5,
                    "persistence_attempts": 2
                }
                findings = analyzer.analyze_behavior(behavior_data)
                print(f"\n✅ Análise comportamental concluída. {len(findings)} achados encontrados.")
                
            elif choice == "4":
                report = analyzer.generate_analysis_report()
                print("\n" + report)
                
            elif choice == "5":
                filename = analyzer.export_analysis_data()
                print(f"\n✅ Dados exportados para: {filename}")
                
            elif choice == "6":
                print("👋 Encerrando analisador...")
                break
                
            else:
                print("❌ Opção inválida.")
                
        except Exception as e:
            print(f"❌ Erro: {e}")
        except KeyboardInterrupt:
            print("\n👋 Encerrando...")
            break

if __name__ == "__main__":
    main()
