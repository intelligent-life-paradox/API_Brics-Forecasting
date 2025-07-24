# API_Brics-Forecasting
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