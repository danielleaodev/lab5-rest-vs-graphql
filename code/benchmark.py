import csv
import rest
import graphql
import graphql_more_info
import time

def run_script(function_name, identifier):
 
    result = function_name()
    if result['status_code'] != 200:
        raise Exception(result.stderr)
    else:
        if not result['time'] or not result['size']:
            # Se não encontrar as linhas, imprime a saída completa
            print(f"Saída inesperada de {identifier}:\n{result}")
            raise Exception(f"Não foi possível encontrar 'Tempo de Resposta' ou 'Tamanho da Resposta' na saída de {script_name}")

        return {'time': result['time'], 'size': result['size']}

def run_benchmark(iterations=50):
    print('Executando Benchmark...\n')

    rest_times = []
    rest_sizes = []
    graphql_times = []
    graphql_sizes = []
    graphql_more_info_times = []
    graphql_more_info_sizes = []
    rest_prs_times = []
    rest_prs_sizes = []
    graphql_prs_times = []
    graphql_prs_sizes = []
    graphql_more_info_prs_times = []
    graphql_more_info_prs_sizes = []
    
    apis = [
                ('REST List Repos', 'rest', rest.get_user_repos, rest_times, rest_sizes),
                ('GraphQL List Repos', 'graphql_1', graphql.get_user_repos, graphql_times, graphql_sizes),
                ('GraphQL List Repos More Info', 'graphql_2', graphql_more_info.get_user_repos, graphql_more_info_times, graphql_more_info_sizes),
                ('REST Get Repo PRs','rest', rest.get_repo_prs, rest_prs_times, rest_prs_sizes),
                ('GraphQL Get Repo PRs', 'graphql_1', graphql.get_repo_prs, graphql_prs_times, graphql_prs_sizes),
                ('GraphQL Get Repo PRs More Info', 'graphql_2', graphql_more_info.get_repo_prs, graphql_more_info_prs_times, graphql_more_info_prs_sizes),
            ]

    # Abre o arquivo CSV para escrever os resultados
    with open('resultados.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Iteração', 'API', 'TIPO', 'Tempo de Resposta (ms)', 'Tamanho da Resposta (bytes)']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(iterations):
            time.sleep(3)
            print(f'Iteração {i+1} de {iterations}')

            for api_name, api_type, api_function, times, size in apis:
                try:
                    result = run_script(api_function, f'{api_name}.get_user_repos')
                    times.append(result['time'])
                    size.append(result['size'])
                    
                    writer.writerow({
                        'Iteração': i+1,
                        'API': api_name,
                        'TIPO': api_type,
                        'Tempo de Resposta (ms)': f'{result['time']:.2f}',
                        'Tamanho da Resposta (bytes)': result['size']
                    })
                except Exception as e:
                    print(f'Erro ao salvar {api_function}.py: {e}')
                    continue

    if rest_times and graphql_times and graphql_more_info_times and rest_prs_times and graphql_prs_times and graphql_more_info_prs_times:
        for api_name, api_type, api_function, times, size in apis:
            print(f'\nAPI {api_name}')
            avg_time = sum(times) / len(times) if times else 0
            avg_size = sum(size) / len(size) if size else 0
            print(f'Tempo Médio de Resposta: {avg_time:.2f} ms')
            print(f'Tamanho Médio da Resposta: {avg_size:.2f} bytes')
    else:
        print('Não foi possível calcular as médias devido a erros nas execuções.')

if __name__ == '__main__':
    try:
        run_benchmark(1000)
    except Exception as e:
        print(f'Erro durante o benchmark: {e}')
