import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GITHUB_TOKEN')
username = 'torvalds'

def get_interfaces_info(type_name):
    url = 'https://api.github.com/graphql'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    query = f'''
    query {{
    __type(name: "{type_name}") {{
        name
        kind
        description
        fields {{
            name
        }}
    }}
    }}
    '''

    json_data = {'query': query}

    response = requests.post(url, json=json_data, headers=headers)
    print(response.content)

if __name__ == '__main__':
    try:
        get_interfaces_info("Repository")
        get_interfaces_info("RepositoryOwner")
    except Exception as e:
        print(f'Erro ao buscar tipos: {e}')
