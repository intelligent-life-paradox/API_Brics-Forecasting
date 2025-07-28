**Engenharia de Sistemas Inteligentes (CK0444 – 2025.1)** da Universidade Federal do Ceará.

## Equipe

| Nome              | Função Principal                                |
|-------------------|--------------------------------------------------|
| Carlos Eduardo    | Pré-processamento de dados, limpeza e tratamento |#Matricula #514072
| Ayuri do Reis     | Coleta de dados, limpeza e tratamento            |#Matricula #536482
| João Luca         | Modelagem e Treinamento                          |#Matricula #548291
| Joab              | Modelagem, validação e visualização              |#Matricula #49592S

# 📈 ETF-Forecasting-and-Clustering

Previsão do comportamento de ETFs de países selecionados utilizando múltiplos modelos de séries temporais e análise de cluster para identificar padrões entre ativos financeiros internacionais.

---

## 🎯 Objetivo

O projeto visa prever os valores de ETFs (Exchange-Traded Funds) de países do BRICS e outros mercados emergentes com diferentes abordagens estatísticas e de aprendizado de máquina. Além disso, aplicamos técnicas de clusterização para identificar semelhanças e agrupamentos de comportamento entre os ETFs analisados.

---

## 🛠️ Tecnologias e Ferramentas

- Python 🐍
- Pandas / NumPy / Matplotlib / Seaborn
- Scikit-learn
- Statsmodels
- XGBoost 
- Random Forest Regressor
- Gradient Boosting 
- KMeans 
- Yahoo Finance API
- Jupyter Notebook

---

## 🔎 Abordagem

- Coleta de dados históricos de ETFs via **Yahoo Finance API**
- Pré-processamento e análise exploratória
- Aplicação de múltiplos modelos preditivos:

  - XGBoost Regressor/GD Boosting/ Random Forest Regressor 
- Avaliação de desempenho com métricas como MAE, RMSE
- Clusterização dos ETFs com base em comportamento e variáveis derivadas (volatilidade, tendência etc.)

---



---

## 🔍 Clusterização de ETFs

Também foi realizada uma análise de agrupamento (clustering) para observar similaridades entre os ETFs com base em suas séries temporais:

- KMeans com Elbow Method

---
ETF-Forecasting-and-Clustering/
├── notebooks/
│ ├── etf_preprocessing.ipynb # Limpeza e tratamento dos dados
│ ├── etf_forecasting.ipynb # Modelos preditivos e validação
│ ├── etf_clustering.ipynb # Clusterização com KMeans
├── comparativo de modelos.png # Gráfico com resultado dos modelos
├── README.md
---

---

## # API_Brics-Forecasting
Tentaremos conectar a uma API e interface os modelos já salvos para países do BRICS


---

## 🚀 Instalação e Execução

### 1. Clone o projeto (ou baixe manualmente)

```bash
git clone https://github.com/seu-usuario/brics-forecasting-api.git
cd brics-forecasting-api/backend
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate.bat  # Windows
```

### 3. Instale as dependências

```bash
pip install -r backend/requirements.txt
```

### 4. Execute o servidor Flask

```bash
python backend/main.py
```

---

### A aplicação estará disponível em:

http://127.0.0.1:5000/api/predict

### Corpo da Requisição:

```json
{
  "country": "Brasil",
  "features": {
    "mes": 1,
    "semestre": 1,
    "quadrimestre": 1,
    "covid": 0,
    "trump": 0,
    "guerra_ucrania": 0,
    "volatilidade": 0.312168,
    "diferenca": -0.526908
  }
}
```


---

## 📚 Referências

- [Yahoo Finance API via yfinance](https://pypi.org/project/yfinance/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- Slides e notas da disciplina CK0444 – Prof. Lincoln S. Rocha (UFC)

---




