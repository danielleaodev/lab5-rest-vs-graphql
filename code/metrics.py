import csv

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

if __name__ == '__main__':
    types = ['rest', 'graphql_1', 'graphql_2']
    
    with open('averages.csv', mode='a', newline='') as file:
        fieldnames = ['TIPO', 'average_time', 'average_size']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for type in types:
            average_time, average_size = calculate_average_time(type)

            writer.writerow({'TIPO': type, 'average_time': f'{average_time:.2f}', 'average_size': f'{average_size:.2f}'})