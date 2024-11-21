# rest.py

import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GITHUB_TOKEN')
username = 'torvalds' 

def get_user_repos():
    url = f'https://api.github.com/users/{username}/repos?per_page=100&sort=updated'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    start_time = time.time()
    response = requests.get(url, headers=headers)
    end_time = time.time()

    response_time = (end_time - start_time) * 1000 
    response_size = len(response.content)

    print('API REST')
    print(f'Tempo de Resposta: {response_time:.2f} ms')
    print(f'Tamanho da Resposta: {response_size} bytes')

if __name__ == '__main__':
    try:
        get_user_repos()
    except Exception as e:
        print(f'Erro na consulta REST: {e}')
