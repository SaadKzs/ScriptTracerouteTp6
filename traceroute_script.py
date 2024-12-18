# Zebiri Saad
# HE202391
# 1TM2

import sys
import argparse
import subprocess

def run_traceroute(target, progressive, output_file):
    # On définit la commande 'tracert' suivie de la cible (URL ou adresse IP).
    command = ['tracert', target]
    if progressive:
        # Si l'option progressive est activée, on affiche chaque ligne de résultat dès qu'elle est disponible.
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
    else:
        # En mode standard, on exécute 'tracert' et on attend que la commande se termine pour afficher tous les résultats.
        result = subprocess.run(command, capture_output=True, text=True)
        if output_file:
            # Si un fichier de sortie est spécifié, on sauvegarde tous les résultats dans ce fichier.
            with open(output_file, 'w') as file:
                file.write(result.stdout)
        else:
            # Sinon, on affiche simplement les résultats dans la console.
            print(result.stdout)

def main():
    # Préparation du parseur d'arguments pour comprendre et traiter les options de ligne de commande.
    parser = argparse.ArgumentParser(description='Effectuer un traceroute vers une adresse IP ou URL spécifiée.')
    parser.add_argument('target', type=str, help='Adresse IP ou URL cible pour le traceroute')
    parser.add_argument('-p', '--progressive', action='store_true', help='Afficher progressivement les résultats au fur et à mesure de leur disponibilité')
    parser.add_argument('-o', '--output-file', type=str, help='Nom du fichier où sauvegarder les résultats si nécessaire')
    args = parser.parse_args()

    # On tente d'exécuter le traceroute avec les options fournies.
    try:
        run_traceroute(args.target, args.progressive, args.output_file)
    except Exception as e:
        # En cas d'erreur, on l'affiche clairement et on arrête l'exécution du script.
        sys.stderr.write(f"Erreur : {str(e)}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
