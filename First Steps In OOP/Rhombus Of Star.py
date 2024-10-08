def print_row(figure_size, row_size):
    print(' ' * (figure_size - row_size), end='')
    for _ in range(1, row_size + 1):
        print('* ', end='')

    print()


n = int(input())

for row in range(1, n + 1):
    print_row(n, row)

for row in range(n - 1, -1, -1):
    print_row(n, row)
