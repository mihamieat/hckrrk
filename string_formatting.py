def print_formatted(number):
    decimals = [int(n) for n in range(1, number + 1)]
    all_octals = list(map(oct, decimals))
    all_octals = [n[2:] for n in all_octals]
    all_hexadecimals = list(map(hex, decimals))
    all_hexadecimals = [n[2:] for n in all_hexadecimals]
    all_binaries = list(map(bin, decimals))
    all_binaries = [n[2:] for n in all_binaries]
    decimals_str = [str(n) for n in decimals]
    max_padding = len(bin(number)[2:])
    for i in range(len(decimals)):
        print(
            decimals_str[i].rjust(max_padding, " "),
            all_octals[i].rjust(max_padding, " "),
            all_hexadecimals[i].upper().rjust(max_padding, " "),
            all_binaries[i].rjust(max_padding, " "),
        )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
