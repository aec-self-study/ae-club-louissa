# calc
import argparse

parser = argparse.ArgumentParser(description="CLI Calculator.")

subparsers = parser.add_subparsers(help="sub-command help", dest="command")

add = subparsers.add_parser("add", help="add integers")
add.add_argument("ints_to_sum", nargs='*', type=int)

sub = subparsers.add_parser("sub", help="subtract integers")
sub.add_argument("ints_to_sub", nargs=2, type=int)

div = subparsers.add_parser("div", help="divide integers")
div.add_argument("ints_to_div", nargs=2, type=int)

def aec_subtract(ints_to_sub):
    if len(ints_to_sub) != 2:
        raise ValueError("Subtract requires exactly two arguments.")
    our_sub = ints_to_sub[0] - ints_to_sub[1]
    print(f"the subtracted result of values is: {our_sub}")   
    return our_sub

def aec_divide(ints_to_div):
    if len(ints_to_div) != 2:
        raise ValueError("Divide requires exactly two arguments.")
    
    if ints_to_div[1] == 0:
        print("Division durch Null ist nicht erlaubt!")
        return 0  
    
    our_div = ints_to_div[0] / ints_to_div[1]
    print(f"the divided result of values is: {our_div}")   
    return our_div

if __name__ == "__main__":
    args = parser.parse_args()

    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"the sum of values is: {our_sum}")

    if args.command == "sub":
        aec_subtract(args.ints_to_sub)

    if args.command == "div":
        aec_divide(args.ints_to_div)
