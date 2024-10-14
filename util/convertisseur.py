import argparse
import csv
import json
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convertir des données CSV en format json indexé")
    parser.add_argument('-i', '--input', type=str, required=True, help="Chemin d'accès au fichier CSV")
    parser.add_argument('-o', '--output', type=str, required=True, help="Lieu de sortie du fichier JSON")
    return parser.parse_args()


def parse_commune_csv_to_json(csv_path, output_path):
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        data = {}
        i = 0
        for row in reader:
            commune_data = {
                'name': row['Nom Commune'],
                'zone': row['Zone ABC'],
            }
            data.update({
                row['Code Commune']: commune_data
            })


    with open(output_path, 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    args = parse_arguments()
    assert os.path.isfile(args.input), "Fichier CSV introuvable"
    parse_commune_csv_to_json(args.input, args.output)
