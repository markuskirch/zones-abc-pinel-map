## convertisseur.py
Convertir des données CSV en format json indexé.

Assurez-vous que le CSV ; est utilisé comme délimiteur et que la première ligne contient les colonnes _Code Commune_, _Nom Commune_ et _Zone ABC_.

### Utilisation
```shell
python convertisseur.py -i ../data/Zonage_abc_communes_2024.csv -o ../data/Zonage_abc_communes_2024-index.json
```