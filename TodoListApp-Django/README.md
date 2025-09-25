# ToDoList Django App

Pequeno projeto Django para gerenciar tarefas.

## Instalação

Clone o repositorio

Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate  
```

Instale as dependências:
```bash
pip install -r requirements.txt
```
Crie um arquivo '.env' e coloque:
```bash
DJANGO_EXAMPLE_SECRET_KEY="sua_chave_secreta_do_settings.py"
```
Va no settings.py e faça:
```bash
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get('DJANGO_EXAMPLE_SECRET_KEY') 
```
Rode as migrations:
```bash
python manage.py migrate
```
Rode o servidor de desenvolvimento:
```bash
python manage.py runserver
```
Acesse no navegador:
```bash
http://127.0.0.1:8000/
```
