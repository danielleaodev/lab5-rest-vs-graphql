# benchmark.py

import subprocess
import os
import csv

def run_script(script_name):
    # os scripts estão na mesma pasta
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)
    else:
        output = result.stdout

        # Extrair tempo de resposta e tamanho da resposta
        time_lines = [line for line in output.split('\n') if 'Tempo de Resposta' in line]
        size_lines = [line for line in output.split('\n') if 'Tamanho da Resposta' in line]

        if not time_lines or not size_lines:
            # Se não encontrar as linhas, imprime a saída completa
            print(f"Saída inesperada de {script_name}:\n{output}")
            raise Exception(f"Não foi possível encontrar 'Tempo de Resposta' ou 'Tamanho da Resposta' na saída de {script_name}")

        time_line = time_lines[0]
        size_line = size_lines[0]

        time_ms = float(time_line.split(':')[1].strip().replace(' ms', ''))
        size_bytes = int(size_line.split(':')[1].strip().replace(' bytes', ''))

        return {'time': time_ms, 'size': size_bytes}

def run_benchmark(iterations=50):
    print('Executando Benchmark...\n')

    rest_times = []
    rest_sizes = []
    graphql_times = []
    graphql_sizes = []

    # Abre o arquivo CSV para escrever os resultados
    with open('resultados.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Iteração', 'API', 'Tempo de Resposta (ms)', 'Tamanho da Resposta (bytes)']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(iterations):
            print(f'Iteração {i+1} de {iterations}')

            try:
                rest_result = run_script('rest.py')
                rest_times.append(rest_result['time'])
                rest_sizes.append(rest_result['size'])
                writer.writerow({
                    'Iteração': i+1,
                    'API': 'REST',
                    'Tempo de Resposta (ms)': rest_result['time'],
                    'Tamanho da Resposta (bytes)': rest_result['size']
                })
            except Exception as e:
                print(f'Erro na execução de rest.py: {e}')
                continue

            try:
                graphql_result = run_script('graphql.py')
                graphql_times.append(graphql_result['time'])
                graphql_sizes.append(graphql_result['size'])
                writer.writerow({
                    'Iteração': i+1,
                    'API': 'GraphQL',
                    'Tempo de Resposta (ms)': graphql_result['time'],
                    'Tamanho da Resposta (bytes)': graphql_result['size']
                })
            except Exception as e:
                print(f'Erro na execução de graphql.py: {e}')
                continue

    # Verifica se temos resultados suficientes para calcular as médias
    if rest_times and graphql_times:
        avg_rest_time = sum(rest_times) / len(rest_times)
        avg_rest_size = sum(rest_sizes) / len(rest_sizes)

        avg_graphql_time = sum(graphql_times) / len(graphql_times)
        avg_graphql_size = sum(graphql_sizes) / len(graphql_sizes)

        print('\nResultados Médios:')
        print('API REST')
        print(f'Tempo Médio de Resposta: {avg_rest_time:.2f} ms')
        print(f'Tamanho Médio da Resposta: {avg_rest_size:.2f} bytes')

        print('\nAPI GraphQL')
        print(f'Tempo Médio de Resposta: {avg_graphql_time:.2f} ms')
        print(f'Tamanho Médio da Resposta: {avg_graphql_size:.2f} bytes')
    else:
        print('Não foi possível calcular as médias devido a erros nas execuções.')

if __name__ == '__main__':
    try:
        run_benchmark()
    except Exception as e:
        print(f'Erro durante o benchmark: {e}')
