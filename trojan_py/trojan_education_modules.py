#!/usr/bin/env python3
"""
Módulos Educacionais para Simulação de Cavalo de Tróia
=====================================================

Este módulo contém componentes educacionais específicos para demonstrar
conceitos de segurança cibernética relacionados a trojans.

Autor: Equipe de Criptografia e Segurança - Atitus Educação
Integrantes: Diogo Chaves, Gabriel Vanz, Vitor Badin
Ano: 2024
"""

import random
import time
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

class TrojanFamily(Enum):
    """Famílias de trojans para classificação educacional"""
    BANKING = "Banking Trojan"
    RAT = "Remote Access Trojan"
    KEYLOGGER = "Keylogger"
    BACKDOOR = "Backdoor"
    DOWNLOADER = "Downloader"
    RANSOMWARE = "Ransomware"

class AttackVector(Enum):
    """Vetores de ataque para simulação"""
    EMAIL = "E-mail"
    DOWNLOAD = "Download"
    USB = "Dispositivo USB"
    WEBSITE = "Site Web"
    SOCIAL = "Engenharia Social"
    NETWORK = "Rede"

@dataclass
class TrojanExample:
    """Exemplo de trojan para fins educacionais"""
    name: str
    family: TrojanFamily
    description: str
    impact: str
    year: int
    techniques: List[str]
    detection_difficulty: int  # 1-10

class TrojanEducationModules:
    """Módulos educacionais para simulação de trojans"""
    
    def __init__(self):
        self.trojan_examples = self._load_trojan_examples()
        self.attack_scenarios = self._load_attack_scenarios()
        self.defense_strategies = self._load_defense_strategies()
    
    def _load_trojan_examples(self) -> List[TrojanExample]:
        """Carrega exemplos reais de trojans para fins educacionais"""
        return [
            TrojanExample(
                name="Zeus",
                family=TrojanFamily.BANKING,
                description="Troyan bancário que rouba credenciais financeiras",
                impact="$100+ milhões roubados",
                year=2007,
                techniques=["Keylogging", "Form Grabbing", "Web Injection"],
                detection_difficulty=8
            ),
            TrojanExample(
                name="Emotet",
                family=TrojanFamily.DOWNLOADER,
                description="Evoluiu de troyan bancário para plataforma de distribuição",
                impact="1.6+ milhões de vítimas",
                year=2014,
                techniques=["Modular Design", "Email Propagation", "C&C Communication"],
                detection_difficulty=9
            ),
            TrojanExample(
                name="TrickBot",
                family=TrojanFamily.BANKING,
                description="Troyan bancário modular usado para distribuir ransomware",
                impact="Ainda ativo globalmente",
                year=2016,
                techniques=["Modular Architecture", "Lateral Movement", "Credential Harvesting"],
                detection_difficulty=9
            ),
            TrojanExample(
                name="NetBus",
                family=TrojanFamily.RAT,
                description="Um dos primeiros RATs amplamente conhecidos",
                impact="Demonstrou vulnerabilidades de RAT",
                year=1998,
                techniques=["Remote Control", "File Transfer", "Screen Capture"],
                detection_difficulty=3
            ),
            TrojanExample(
                name="Sub7",
                family=TrojanFamily.RAT,
                description="Remote Access Trojan popular na década de 2000",
                impact="Milhares de sistemas comprometidos",
                year=1999,
                techniques=["Remote Control", "Keylogging", "File Management"],
                detection_difficulty=4
            )
        ]
    
    def _load_attack_scenarios(self) -> List[Dict]:
        """Carrega cenários de ataque para simulação"""
        return [
            {
                "name": "Phishing por E-mail",
                "vector": AttackVector.EMAIL,
                "description": "E-mail falso com anexo malicioso",
                "steps": [
                    "Criação de e-mail falso",
                    "Anexo de arquivo trojan",
                    "Envio para lista de contatos",
                    "Usuário executa anexo",
                    "Trojan se instala silenciosamente"
                ],
                "prevention": [
                    "Verificar remetente",
                    "Não abrir anexos suspeitos",
                    "Usar filtros de spam",
                    "Educar usuários"
                ]
            },
            {
                "name": "Download Malicioso",
                "vector": AttackVector.DOWNLOAD,
                "description": "Site falso oferecendo software legítimo",
                "steps": [
                    "Criação de site falso",
                    "Oferta de software gratuito",
                    "Download de arquivo infectado",
                    "Execução pelo usuário",
                    "Instalação do trojan"
                ],
                "prevention": [
                    "Verificar fonte do download",
                    "Usar sites oficiais",
                    "Verificar assinatura digital",
                    "Antivírus atualizado"
                ]
            },
            {
                "name": "USB Malicioso",
                "vector": AttackVector.USB,
                "description": "Dispositivo USB abandonado com trojan",
                "steps": [
                    "Preparação de USB infectado",
                    "Abandono em local público",
                    "Usuário conecta USB",
                    "Execução automática",
                    "Infecção do sistema"
                ],
                "prevention": [
                    "Desabilitar auto-executa",
                    "Verificar antes de usar",
                    "Não usar USBs desconhecidos",
                    "Escaneamento com antivírus"
                ]
            }
        ]
    
    def _load_defense_strategies(self) -> List[Dict]:
        """Carrega estratégias de defesa"""
        return [
            {
                "category": "Prevenção",
                "strategies": [
                    "Educação e conscientização dos usuários",
                    "Políticas de segurança robustas",
                    "Controle de acesso baseado em funções",
                    "Backup regular e testado",
                    "Atualizações de segurança automáticas"
                ]
            },
            {
                "category": "Detecção",
                "strategies": [
                    "Antivírus com detecção heurística",
                    "Sistemas de detecção de intrusão (IDS)",
                    "Monitoramento de rede em tempo real",
                    "Análise comportamental com IA",
                    "Sandbox para análise de arquivos"
                ]
            },
            {
                "category": "Resposta",
                "strategies": [
                    "Plano de resposta a incidentes",
                    "Isolamento de sistemas infectados",
                    "Análise forense digital",
                    "Comunicação com stakeholders",
                    "Recuperação de dados e sistemas"
                ]
            }
        ]
    
    def demonstrate_trojan_lifecycle(self) -> None:
        """Demonstra o ciclo de vida de um trojan"""
        print("\n🔄 CICLO DE VIDA DE UM CAVALO DE TRÓIA")
        print("=" * 50)
        
        lifecycle_stages = [
            ("1. Desenvolvimento", "Criação do código malicioso"),
            ("2. Distribuição", "Envio via e-mail, sites, USBs"),
            ("3. Execução", "Usuário executa o arquivo"),
            ("4. Instalação", "Trojan se instala silenciosamente"),
            ("5. Ativação", "Inicia atividades maliciosas"),
            ("6. Persistência", "Mantém-se ativo no sistema"),
            ("7. Comunicação", "Conecta-se ao servidor C&C"),
            ("8. Coleta", "Rouba dados e informações"),
            ("9. Propagação", "Tenta infectar outros sistemas"),
            ("10. Ocultação", "Esconde-se de ferramentas de segurança")
        ]
        
        for stage, description in lifecycle_stages:
            print(f"   {stage}: {description}")
            time.sleep(0.5)
    
    def demonstrate_detection_techniques(self) -> None:
        """Demonstra técnicas de detecção de trojans"""
        print("\n🔍 TÉCNICAS DE DETECÇÃO DE TROJANS")
        print("=" * 50)
        
        detection_techniques = [
            {
                "name": "Detecção por Assinatura",
                "description": "Compara arquivos com banco de assinaturas conhecidas",
                "pros": ["Rápida", "Eficaz para malware conhecido"],
                "cons": ["Não detecta malware novo", "Fácil de evadir"]
            },
            {
                "name": "Análise Heurística",
                "description": "Analisa comportamento suspeito do código",
                "pros": ["Detecta malware novo", "Análise comportamental"],
                "cons": ["Falsos positivos", "Mais lenta"]
            },
            {
                "name": "Sandboxing",
                "description": "Executa arquivos em ambiente isolado",
                "pros": ["Seguro", "Análise completa"],
                "cons": ["Recursos intensivos", "Evasão avançada"]
            },
            {
                "name": "Machine Learning",
                "description": "IA para detectar padrões maliciosos",
                "pros": ["Adaptável", "Detecção avançada"],
                "cons": ["Complexa", "Requer treinamento"]
            }
        ]
        
        for technique in detection_techniques:
            print(f"\n   📊 {technique['name']}")
            print(f"      Descrição: {technique['description']}")
            print(f"      ✅ Vantagens: {', '.join(technique['pros'])}")
            print(f"      ❌ Desvantagens: {', '.join(technique['cons'])}")
            time.sleep(1)
    
    def demonstrate_prevention_measures(self) -> None:
        """Demonstra medidas de prevenção"""
        print("\n🛡️ MEDIDAS DE PREVENÇÃO")
        print("=" * 50)
        
        for category in self.defense_strategies:
            print(f"\n   📋 {category['category']}:")
            for strategy in category['strategies']:
                print(f"      • {strategy}")
                time.sleep(0.3)
    
    def simulate_attack_scenario(self, scenario_index: int) -> Dict:
        """Simula um cenário de ataque específico"""
        if scenario_index >= len(self.attack_scenarios):
            raise ValueError("Índice de cenário inválido")
        
        scenario = self.attack_scenarios[scenario_index]
        
        print(f"\n🎯 SIMULANDO: {scenario['name']}")
        print("=" * 50)
        print(f"Vetor: {scenario['vector'].value}")
        print(f"Descrição: {scenario['description']}")
        print()
        
        print("📋 Etapas do ataque:")
        for i, step in enumerate(scenario['steps'], 1):
            print(f"   {i}. {step}")
            time.sleep(0.5)
        
        print("\n🛡️ Medidas de prevenção:")
        for i, prevention in enumerate(scenario['prevention'], 1):
            print(f"   {i}. {prevention}")
            time.sleep(0.3)
        
        return {
            "scenario": scenario['name'],
            "vector": scenario['vector'].value,
            "steps_count": len(scenario['steps']),
            "prevention_count": len(scenario['prevention'])
        }
    
    def analyze_trojan_example(self, example_index: int) -> Dict:
        """Analisa um exemplo específico de trojan"""
        if example_index >= len(self.trojan_examples):
            raise ValueError("Índice de exemplo inválido")
        
        example = self.trojan_examples[example_index]
        
        print(f"\n🔬 ANÁLISE: {example.name}")
        print("=" * 50)
        print(f"Família: {example.family.value}")
        print(f"Descrição: {example.description}")
        print(f"Impacto: {example.impact}")
        print(f"Ano: {example.year}")
        print(f"Dificuldade de Detecção: {example.detection_difficulty}/10")
        print()
        
        print("🔧 Técnicas utilizadas:")
        for technique in example.techniques:
            print(f"   • {technique}")
            time.sleep(0.3)
        
        # Simular análise de risco
        risk_level = "ALTO" if example.detection_difficulty >= 8 else "MÉDIO" if example.detection_difficulty >= 5 else "BAIXO"
        print(f"\n⚠️  Nível de Risco: {risk_level}")
        
        return {
            "name": example.name,
            "family": example.family.value,
            "detection_difficulty": example.detection_difficulty,
            "techniques_count": len(example.techniques),
            "risk_level": risk_level
        }
    
    def generate_educational_quiz(self) -> List[Dict]:
        """Gera um quiz educacional sobre trojans"""
        questions = [
            {
                "question": "O que é um Cavalo de Tróia (Trojan)?",
                "options": [
                    "Um vírus que se replica automaticamente",
                    "Malware que se disfarça como software legítimo",
                    "Um tipo de firewall",
                    "Um sistema de backup"
                ],
                "correct": 1,
                "explanation": "Um trojan é um tipo de malware que se disfarça como software legítimo para enganar usuários."
            },
            {
                "question": "Como os trojans se propagam?",
                "options": [
                    "Automaticamente como vírus",
                    "Apenas através de e-mail",
                    "Dependem da ação do usuário",
                    "Só em redes locais"
                ],
                "correct": 2,
                "explanation": "Diferentemente de vírus, os trojans dependem da ação do usuário para serem executados."
            },
            {
                "question": "Qual é a melhor forma de prevenir infecções por trojans?",
                "options": [
                    "Usar apenas antivírus",
                    "Educar usuários e implementar múltiplas camadas de segurança",
                    "Desconectar da internet",
                    "Usar apenas software pirata"
                ],
                "correct": 1,
                "explanation": "A melhor prevenção combina educação do usuário com múltiplas camadas de segurança."
            },
            {
                "question": "O que é sandboxing?",
                "options": [
                    "Um tipo de trojan",
                    "Execução de arquivos em ambiente isolado",
                    "Um método de criptografia",
                    "Uma técnica de backup"
                ],
                "correct": 1,
                "explanation": "Sandboxing é a execução de arquivos em um ambiente isolado e controlado para análise."
            },
            {
                "question": "Qual lei brasileira trata de crimes cibernéticos?",
                "options": [
                    "Lei 8.069/1990",
                    "Lei 12.737/2012",
                    "Lei 13.709/2018",
                    "Lei 14.129/2021"
                ],
                "correct": 1,
                "explanation": "A Lei 12.737/2012, conhecida como Lei de Crimes Cibernéticos, estabelece as penalidades para crimes cibernéticos no Brasil."
            }
        ]
        
        return questions
    
    def run_educational_quiz(self) -> Dict:
        """Executa o quiz educacional"""
        questions = self.generate_educational_quiz()
        correct_answers = 0
        total_questions = len(questions)
        
        print("\n📚 QUIZ EDUCACIONAL - CAVALO DE TRÓIA")
        print("=" * 50)
        print("Responda as perguntas para testar seus conhecimentos!")
        print()
        
        for i, q in enumerate(questions, 1):
            print(f"Pergunta {i}/{total_questions}:")
            print(f"   {q['question']}")
            print()
            
            for j, option in enumerate(q['options']):
                print(f"   {j + 1}. {option}")
            
            while True:
                try:
                    answer = int(input("\nSua resposta (1-4): ")) - 1
                    if 0 <= answer <= 3:
                        break
                    else:
                        print("❌ Resposta inválida. Digite 1, 2, 3 ou 4.")
                except ValueError:
                    print("❌ Resposta inválida. Digite um número.")
            
            if answer == q['correct']:
                print("✅ Correto!")
                correct_answers += 1
            else:
                print("❌ Incorreto!")
            
            print(f"   Explicação: {q['explanation']}")
            print("-" * 50)
            time.sleep(1)
        
        score = (correct_answers / total_questions) * 100
        
        print(f"\n📊 RESULTADO DO QUIZ")
        print("=" * 30)
        print(f"Respostas corretas: {correct_answers}/{total_questions}")
        print(f"Pontuação: {score:.1f}%")
        
        if score >= 80:
            print("🏆 Excelente! Você tem um bom conhecimento sobre trojans!")
        elif score >= 60:
            print("👍 Bom! Continue estudando para melhorar ainda mais!")
        else:
            print("📚 Estude mais sobre segurança cibernética para se proteger melhor!")
        
        return {
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "score": score,
            "passed": score >= 60
        }

def main():
    """Função principal para testar os módulos educacionais"""
    print("📚 Módulos Educacionais - Cavalo de Tróia")
    print("=" * 50)
    
    modules = TrojanEducationModules()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Demonstrar ciclo de vida de trojan")
        print("2. Demonstrar técnicas de detecção")
        print("3. Demonstrar medidas de prevenção")
        print("4. Simular cenário de ataque")
        print("5. Analisar exemplo de trojan")
        print("6. Executar quiz educacional")
        print("7. Sair")
        
        choice = input("\nOpção: ").strip()
        
        try:
            if choice == "1":
                modules.demonstrate_trojan_lifecycle()
            elif choice == "2":
                modules.demonstrate_detection_techniques()
            elif choice == "3":
                modules.demonstrate_prevention_measures()
            elif choice == "4":
                print("\nCenários disponíveis:")
                for i, scenario in enumerate(modules.attack_scenarios):
                    print(f"   {i}. {scenario['name']}")
                scenario_idx = int(input("\nEscolha um cenário: "))
                modules.simulate_attack_scenario(scenario_idx)
            elif choice == "5":
                print("\nExemplos disponíveis:")
                for i, example in enumerate(modules.trojan_examples):
                    print(f"   {i}. {example.name}")
                example_idx = int(input("\nEscolha um exemplo: "))
                modules.analyze_trojan_example(example_idx)
            elif choice == "6":
                modules.run_educational_quiz()
            elif choice == "7":
                print("👋 Encerrando módulos educacionais...")
                break
            else:
                print("❌ Opção inválida.")
        except (ValueError, IndexError) as e:
            print(f"❌ Erro: {e}")
        except KeyboardInterrupt:
            print("\n👋 Encerrando...")
            break

if __name__ == "__main__":
    main()
