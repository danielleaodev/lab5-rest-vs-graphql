import csv
import matplotlib.pyplot as plt

file_path = 'resultados.csv'

def calculate_average_time(type):
    total_time = 0
    total_size = 0
    count = 0

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['TIPO'] == type:
                total_time += float(row['Tempo de Resposta (ms)'])
                total_size += int(row['Tamanho da Resposta (bytes)'])
                count += 1

    if count == 0:
        return 0

    return total_time / count, total_size / count

def get_averages():
    types = ['rest', 'graphql_1', 'graphql_2']
    
    with open('averages.csv', mode='a', newline='') as file:
        fieldnames = ['TIPO', 'average_time', 'average_size']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for type in types:
            average_time, average_size = calculate_average_time(type)

            writer.writerow({'TIPO': type, 'average_time': f'{average_time:.2f}', 'average_size': f'{average_size:.2f}'})
    
def create_time_boxplots():
    data = {'rest': [], 'graphql_1': [], 'graphql_2': []}

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['TIPO'] in data:
                data[row['TIPO']].append(float(row['Tempo de Resposta (ms)']))

    plt.figure(figsize=(10, 6))
    plt.boxplot([data['rest'], data['graphql_1'], data['graphql_2']], labels=['rest', 'graphql_1', 'graphql_2'])
    plt.title('Tempo de Resposta (ms)')
    plt.ylabel('Tempo de Resposta (ms)')
    plt.xlabel('Consulta')
    plt.savefig('../plot/time_boxplot.png')

def create_size_boxplots():
    data = {'rest': [], 'graphql_1': [], 'graphql_2': []}

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['TIPO'] in data:
                data[row['TIPO']].append(int(row['Tamanho da Resposta (bytes)']))

    plt.figure(figsize=(10, 6))
    plt.boxplot([data['rest'], data['graphql_1'], data['graphql_2']], labels=['rest', 'graphql_1', 'graphql_2'])
    plt.title('Tamanho da Resposta (bytes)')
    plt.ylabel('Tamanho da Resposta (bytes)')
    plt.yscale('log')
    plt.xlabel('Consulta')
    plt.savefig('../plot/size_boxplot.png')

if __name__ == '__main__':
    get_averages()
    create_time_boxplots()
    create_size_boxplots()