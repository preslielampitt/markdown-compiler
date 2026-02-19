def compile_strikethrough(line):
    '''
    Convert "~~strikethrough~~" to "<ins>strikethrough</ins>".

    HINT:
    The strikethrough annotations are very similar to implement as the italic function.
    The difference is that there are two delimiting characters instead of one.
    This will require carefully thinking about the range of your for loop and all of your list indexing.

    >>> compile_strikethrough('~~This is strikethrough!~~ This is not strikethrough.')
    '<ins>This is strikethrough!</ins> This is not strikethrough.'
    >>> compile_strikethrough('~~This is strikethrough!~~')
    '<ins>This is strikethrough!</ins>'
    >>> compile_strikethrough('This is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is not ~~strikethrough!')
    'This is not ~~strikethrough!'
    >>> compile_strikethrough('~~')
    '~~'
    '''
    accumulator = ''
    first_tilds = line.find('~~')
    more_tilds = -1
    i = 0
    while i < len(line):
        if i == first_tilds or i == more_tilds:
            end_tilds = line.find('~~', i+2)
            if end_tilds != -1:
                accumulator += '<ins>' + line[i+2:end_tilds] + '</ins>'
                i = end_tilds + 2
                more_tilds = line.find('~~', i)
            else:
                accumulator += line[i]
                i += 1
        else:
            accumulator += line[i]
            i += 1
    return accumulator 