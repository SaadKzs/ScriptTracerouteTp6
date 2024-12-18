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
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        for raw_line in iter(process.stdout.readline, b''):
            # Remplacer les erreurs de décodage par un caractère de remplacement pour éviter de perdre des informations
            line = raw_line.decode('utf-8', errors='replace')
            print(line, end='')
    else:
        # En mode standard, on exécute 'tracert' et on attend que la commande se termine pour afficher tous les résultats.
        result = subprocess.run(command, capture_output=True)
        # Remplacer les erreurs de décodage par un caractère de remplacement pour éviter de perdre des informations
        output = result.stdout.decode('utf-8', errors='replace')
        if output_file:
            # Si un fichier de sortie est spécifié, on sauvegarde tous les résultats dans ce fichier.
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(output)
        else:
            # Sinon, on affiche simplement les résultats dans la console.
            print(output)

def main():
    # Préparation du parseur d'arguments pour comprendre et traiter les options de ligne de commande.
    parser = argparse.ArgumentParser(description='Effectuer un traceroute vers une adresse IP ou URL specifiee.')
    parser.add_argument('target', type=str, help='Adresse IP ou URL cible pour le traceroute')
    parser.add_argument('-p', '--progressive', action='store_true', help='Afficher progressivement les resultats au fur et à mesure de leur disponibilite')
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
