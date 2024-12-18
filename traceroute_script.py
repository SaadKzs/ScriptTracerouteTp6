# Zebiri Saad
# HE202391
# 1TM2

import sys
import argparse
import subprocess

def run_traceroute(target, progressive, output_file):
    if progressive:
        # Mode progressif
        process = subprocess.Popen(['traceroute', target], stdout=subprocess.PIPE, text=True)
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
    else:
        # Mode non-progressif
        result = subprocess.run(['traceroute', target], capture_output=True, text=True)
        if output_file:
            with open(output_file, 'w') as file:
                file.write(result.stdout)
        else:
            print(result.stdout)

def main():
    parser = argparse.ArgumentParser(description='Run traceroute to a specified IP or URL.')
    parser.add_argument('target', type=str, help='IP address or URL to traceroute')
    parser.add_argument('-p', '--progressive', action='store_true', help='Display results progressively')
    parser.add_argument('-o', '--output-file', type=str, help='File to store the results')
    args = parser.parse_args()

    try:
        run_traceroute(args.target, args.progressive, args.output_file)
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
