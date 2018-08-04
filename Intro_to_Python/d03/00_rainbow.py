def print_format_table(string, style, fg, bg):
    """
    prints table of formatted text format options
    """
    if (0 <= style <= 8) and (30 <= fg <= 38) and (40 <= bg <= 48):
        s1 = ''
        color = ';'.join([str(style), str(fg), str(bg)])
        s1 += '\x1b[%sm %s \x1b[0m' % (color, string)
    print(s1, end='')


print_format_table('R', 0, 31, 40)
print_format_table('A', 0, 36, 40)
print_format_table('I', 0, 33, 40)
print_format_table('N', 0, 32, 40)
print_format_table('B', 0, 34, 40)
print_format_table('O', 0, 35, 40)
print_format_table('W', 0, 37, 40)
print('')
