import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("NO PARAMS")
        return
    total = 0
    
    for i, arg in enumerate(args):
        try:
            num = int(arg)
            sign = 1 if i % 2 == 0 else -1
            total += sign * num
        except ValueError:
            pass
    print(total)

if __name__ == "__main__":
    main()
