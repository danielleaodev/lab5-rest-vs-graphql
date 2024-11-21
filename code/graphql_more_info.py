import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GITHUB_TOKEN')
username = 'torvalds'

def get_user_repos():
    url = 'https://api.github.com/graphql'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    
    query = f'''
    query {{
        user(login: "{username}") {{
            repositories(first: 100, orderBy: {{field: UPDATED_AT, direction: DESC}}) {{
                nodes {{
                    id
                    name
                    description
                    url
                    createdAt
                    updatedAt
                    pushedAt
                    forkCount
                    stargazerCount
                    isPrivate
                    isArchived
                    isDisabled
                    licenseInfo {{
                        name
                    }}
                    visibility
                    defaultBranchRef {{
                        name
                    }}
                    
                    owner {{
                        avatarUrl
                        id
                        login
                        resourcePath
                        url
                    }}
                }}
            }}
        }}
    }}
    '''

    json_data = {'query': query}

    start_time = time.time()
    response = requests.post(url, json=json_data, headers=headers)
    end_time = time.time()

    response_time = (end_time - start_time) * 1000 
    response_size = len(response.content)

    print('API GraphQL')
    print(f'Tempo de Resposta: {response_time:.2f} ms')
    print(f'Tamanho da Resposta: {response_size} bytes')
    return { 'time': response_time, 'size': response_size, 'status_code': response.status_code }

def get_repo_prs():
    url = 'https://api.github.com/graphql'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    query = '''
    query {
        repository(owner: "torvalds", name: "linux") {
            pullRequests(first: 30, orderBy: {field: UPDATED_AT, direction: DESC}) {
                nodes {
                    title
                    body
                    url
                    createdAt
                    updatedAt
                    mergedAt
                    state
                    author {
                        login
                        url
                    }
                    comments {
                        totalCount
                    }
                    reviews {
                        totalCount
                    }
                }
            }
        }
    }
    '''

    json_data = {'query': query}

    start_time = time.time()
    response = requests.post(url, json=json_data, headers=headers)
    end_time = time.time()

    response_time = (end_time - start_time) * 1000 
    response_size = len(response.content)

    print('API GraphQL')
    print(f'Tempo de Resposta: {response_time:.2f} ms')
    print(f'Tamanho da Resposta: {response_size} bytes')
    return { 'time': response_time, 'size': response_size, 'status_code': response.status_code }


if __name__ == '__main__':
    try:
        get_repo_prs()
    except Exception as e:
        print(f'Erro na consulta GraphQL: {e}')
