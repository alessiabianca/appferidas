🩹 Análise de Área de Feridas com FastAPI
Este projeto é uma API desenvolvida em FastAPI para analisar imagens e calcular a área de feridas em cm². Ele processa imagens enviadas pelo usuário, identifica a ferida e retorna a imagem com contorno desenhado, além dos valores da área calculada.

🚀 Tecnologias Utilizadas
Python
FastAPI
OpenCV
Pillow (PIL)
NumPy
Uvicorn
📌 Funcionalidades
✅ Upload de imagens para análise
✅ Processamento da imagem para detecção da ferida
✅ Cálculo da área da ferida em pixels e cm²
✅ Retorno da imagem processada com contorno desenhado

📂 Instalação e Execução
🔹 1. Clonar o repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
🔹 2. Criar e ativar um ambiente virtual (opcional, mas recomendado)
bash
Copiar
Editar
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate  # Windows  
🔹 3. Instalar as dependências
bash
Copiar
Editar
pip install -r requirements.txt
🔹 4. Executar o servidor FastAPI
bash
Copiar
Editar
python principal.py
O servidor será iniciado em http://localhost:8001.

📤 Como Usar a API
🔹 Enviar uma imagem para análise
Faça um POST para o endpoint /upload, enviando uma imagem no formato JPEG/PNG.

Exemplo usando curl:
bash
Copiar
Editar
curl -X POST -F "file=@caminho_para_sua_imagem.jpg" http://localhost:8001/upload -o resultado.jpg
A resposta será a imagem processada com a ferida contornada, além dos valores da área em pixels e cm² nos headers.

🔹 Página inicial
Acesse http://localhost:8001/ para visualizar a interface HTML básica.
