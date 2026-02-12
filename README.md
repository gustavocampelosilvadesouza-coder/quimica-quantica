# ⚗️ Projeto de Química Computacional (PySCF)

Este repositório contém simulações de química quântica realizadas utilizando a biblioteca **PySCF** e **Python**. O objetivo é explorar propriedades moleculares fundamentais, termodinâmica e interações droga-enzima.

## 🚀 Experimentos Realizados

### 1. A Molécula da Vida (Água - H₂O)
* **Arquivo:** `scripts/h2o_angulo.py`
* **O que faz:** Realiza uma varredura de energia potencial (PES) variando o ângulo de ligação H-O-H.
* **Resultado:** Determina o ângulo de menor energia (geometria de equilíbrio) previsto pela mecânica quântica.

### 2. Termodinâmica de Ácidos (Ácido Benzoico)
* **Arquivos:** `scripts/acido_benzoico.py`, `scripts/benzoato.py`, `scripts/analise_acidez.py`
* **O que faz:**
    * Calcula a energia do ácido neutro e de sua base conjugada (ânion benzoato).
    * Determina a **Energia de Desprotonação** (Acidez em fase gasosa).
    * Analisa a distribuição de cargas (Mulliken) para identificar o hidrogênio ácido.

### 3. Química Medicinal (Rosuvastatina)
* **Arquivo:** `scripts/rosuvastatina.py`
* **O que faz:**
    * Calcula a estrutura eletrônica do fármaco inibidor da HMG-CoA Redutase.
    * Analisa o **Momento de Dipolo** (polaridade) e **Mapa de Potencial Eletrostático** (MEP).
    * Investiga as interações chave (flúor hidrofóbico e sulfonamida polar) responsáveis pelo "encaixe" na enzima.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Biblioteca de Química:** PySCF (Python Simulations of Chemistry Framework)
* **Método:** DFT (Teoria do Funcional da Densidade) com funcional B3LYP e base STO-3G.
* **Ambiente:** WSL (Windows Subsystem for Linux).

---
*Projeto desenvolvido por Gustavo Campelo.*
