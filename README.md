# Projeto Web Laboratório de Engenharia de Software - FATEC - Receitas Online

Aplicação web em Flask para cadastros de ingredientes e receitas

## Preparando Ambiente

Primeiro passo é realizar a clonagem do repositório:

```bash
git clone https://github.com/scsoliveira/projeto-receita.git
cd projeto-receita
```

Clonado, dentro da pasta do projeto, crie e inicialize o ambiente virtual:

```bash
python -m virtualenv venv
.\venv\scripts\activate  
```

Após a criação e inicialização do ambiente virtual instale as dependências do projeto:

```
pip install -r requirements.txt 
```

## Para Executar

### Executar em ambiente de desenvolvimento

Para executar o projeto em ambiente de desenvolvimento, entre no diretório 'receitas' e execute 'app.py'

```bash
cd .\receitas\    
python app.py
```
## Vídeo Demonstrativo/Explicativo
[Video 1 Entrega](https://youtu.be/U-BSwrBbVGg)

## Preparando Ambiente Segunda Entrega

```
git pull origin main
```
```
venv/Scripts/activate
```
Atualização das novas dependências

```
pip install -r requirements.txt
```

Criar connection e schema no mysql workbench 
- Schema = l-es
- user = root
- senha = oh6zlppn5

**É provável que seja necessária a trocar a senha da conexão no app.py**

## Vídeo Demonstrativo/Explicativo
[Video 2 Entrega](https://youtu.be/P93GW4lyVAw)
