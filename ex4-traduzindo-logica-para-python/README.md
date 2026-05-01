# Projeto: Algoritmo de Auditoria de Dados de Vendas

## 📋 Descrição

Este projeto consiste em um algoritmo em Python desenvolvido para realizar uma análise básica de vendas, aplicando regras de auditoria e segurança sobre valores inseridos pelo usuário.

O sistema calcula a média das vendas registradas, identifica discrepâncias significativas, verifica se valores ultrapassam limites de segurança predefinidos e permite ajuste manual desse limite quando necessário.

---

## 🎯 Objetivo

Automatizar uma verificação inicial de dados financeiros para:

- Calcular média de vendas
- Detectar vendas anormais
- Aplicar controle de limite de segurança
- Permitir revisão manual de valores suspeitos
- Reforçar validação operacional de dados

---

## ⚙️ Funcionalidades

### ✔️ Cálculo de média

O sistema soma todas as vendas registradas e calcula o valor médio.

### ✔️ Quarentena de segurança

Caso a média ultrapasse o limite definido (`10000`), o sistema ativa um alerta:

```python
SISTEMA EM QUARENTENA
```

### ✔️ Detecção de discrepâncias

Se alguma venda for superior a 5 vezes a média geral, o sistema sinaliza possível inconsistência:

```python
DISCREPÂNCIA DETECTADA (Revisão manual indicada)
```

### ✔️ Ajuste de limite

Quando uma venda ultrapassa o limite de segurança, o usuário pode:

- Manter limite atual
- Definir novo limite

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`for`)
- Funções
- Variáveis globais
- Entrada de dados com `input()`

---

## 📂 Estrutura Lógica

```text
1. Definir limite de segurança
2. Coletar 3 vendas
3. Calcular média
4. Verificar quarentena
5. Detectar discrepâncias
6. Revisar vendas acima do limite
7. Exibir resultados finais
```

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3 instalado

### Execução

```bash
python nome_do_arquivo.py
```

### Entrada esperada

```bash
Digite o valor da venda 1:
Digite o valor da venda 2:
Digite o valor da venda 3:
```

---

## 📌 Exemplo de Uso

```bash
Digite o valor da venda 1: 5000
Digite o valor da venda 2: 15000
Digite o valor da venda 3: 3000
```

### Saída possível

```bash
O valor medio das vendas é: 7666.67
DISCREPÂNCIA DETECTADA (Revisão manual indicada).
```

---

## ⚠️ Pontos de Melhoria

O código atual apresenta oportunidades de evolução:

- Correção de indentação
- Melhor organização estrutural
- Tratamento de erros para entradas inválidas
- Remoção de variáveis globais
- Modularização avançada
- Interface mais amigável
- Armazenamento em banco de dados ou arquivos

---

## 🚀 Possíveis Expansões

- Dashboard de auditoria
- Exportação de relatórios
- Integração com APIs financeiras
- Sistema de logs
- Análise estatística avançada
- Machine Learning para detecção de fraude

---

## 👨‍💻 Autor

Desenvolvido como projeto de estudo para lógica de programação, auditoria de dados e automação de segurança operacional.

---

## 📄 Licença

Uso educacional e demonstrativo.

---

## 🧠 Resumo Técnico

Este projeto demonstra conhecimentos em:

- Programação procedural
- Segurança de dados
- Monitoramento de anomalias
- Interação com usuário
- Controle lógico operacional

---

**Projeto ideal para aprendizado em Python aplicado à análise e auditoria de dados.**
