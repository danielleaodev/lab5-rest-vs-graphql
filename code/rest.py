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
    response = requests.get(url, headers=headers, timeout=100)
    end_time = time.time()

    response_time = (end_time - start_time) * 1000 
    response_size = len(response.content)
    
    if (response.status_code != 200):
        return { 'status_code': response.status_code }

    # print('API REST')
    # print(f'Tempo de Resposta: {response_time:.2f} ms')
    # print(f'Tamanho da Resposta: {response_size} bytes')
    return { 'time': response_time, 'size': response_size, 'status_code': response.status_code }
    
def get_repo_prs():
    url = f'https://api.github.com/repos/torvalds/linux/pulls?per_page=100&sort=updated'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    start_time = time.time()
    response = requests.get(url, headers=headers, timeout=100)
    end_time = time.time()

    response_time = (end_time - start_time) * 1000 
    response_size = len(response.content)

    # print('API REST')
    # print(f'Tempo de Resposta: {response_time:.2f} ms')
    # print(f'Tamanho da Resposta: {response_size} bytes')
    return { 'time': response_time, 'size': response_size, 'status_code': response.status_code }

if __name__ == '__main__':
    try:
        get_repo_prs()
    except Exception as e:
        print(f'Erro na consulta REST: {e}')
