import argparse

# Initialisierung des Parsers
parser = argparse.ArgumentParser(description="CLI Calculator.")

# Hinzufügen der Sub-Parser
subparsers = parser.add_subparsers(help="sub-command help", dest="command")

# Subbefehl für Addition
add = subparsers.add_parser("add", help="add integers")
add.add_argument("ints_to_sum", nargs="*", type=int)

# Subbefehl für Subtraktion
sub = subparsers.add_parser("sub", help="subtract integers")
sub.add_argument("ints_to_sub", nargs=2, type=int)

# Subbefehl für Multiplikation
mul = subparsers.add_parser("mul", help="multiply integers")
mul.add_argument("ints_to_mul", nargs="*", type=int)

# Subbefehl für Division
div = subparsers.add_parser("div", help="divide integers")
div.add_argument("ints_to_div", nargs=2, type=int)

# Argumente parsen
args = parser.parse_args()

# Addition
if args.command == "add":
    our_sum = sum(args.ints_to_sum)
    print(f"the sum of values is: {our_sum}")

# Subtraktion
if args.command == "sub":
    our_sub = args.ints_to_sub[0] - args.ints_to_sub[1]
    print(f"The subtracted result is: {our_sub}")

# Multiplikation
if args.command == "mul":
    # Hier multiplizieren wir alle Zahlen zusammen
    result = 1
    for num in args.ints_to_mul:
        result *= num
    print(f"The multiplied result is: {result}")

# Division
if args.command == "div":
    numerator = args.ints_to_div[0]
    denominator = args.ints_to_div[1]
    if denominator == 0:
        print("cannot divide")
    else:
        result = numerator / denominator
        print(f"The division result is: {result}")
