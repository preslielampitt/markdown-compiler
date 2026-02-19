'''
Each of the functions in this file takes a single line of input and transforms the line in some way.
'''

def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.

    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the appropriate header markdown commands.

    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''

    if line[:2] == '# ':
        # why doesn't this line do anything?
        # answer: strings are *immutable*; they can never change
        # functions that "seem like they should change the string"
        # actually just return a new string
        line = line.replace('# ', '<h1> ') + '</h1>'
    if line[:3] == '## ':
        line = line.replace('## ', '<h2> ') + '</h2>'
    if line[:4] == '### ':
        line = line.replace('### ', '<h3> ') + '</h3>'
    if line[:5] == '#### ':
        line = line.replace('#### ', '<h4> ') + '</h4>'
    if line[:6] == '##### ':
        line = line.replace('##### ', '<h5> ') + '</h5>'
    if line[:7] == '###### ':
        line = line.replace('###### ', '<h6> ') + '</h6>'
    return line


def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    # all of these functions are easiest to implement with the accumulator pattern
    # use .find or .count functions to check number of stars
    accumulator = ''
    has_opened = False
    num_stars = line.count('*')
    if num_stars % 2 == 0:
        for char in line:
            if char == '*':
                if not has_opened:
                    accumulator += '<i>'
                    has_opened = True
                else:
                    accumulator += '</i>'
                    has_opened = False
            else:
                accumulator += char
    else:
        return line
    return accumulator


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    HINT:
    This function is almost exactly the same as `compile_italic_star`.

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''
    accumulator = ''
    has_opened = False
    num_underscores = line.count('_')
    if num_underscores % 2 == 0:
        for char in line:
            if char == '_':
                if not has_opened:
                    accumulator += '<i>'
                    has_opened = True
                else:
                    accumulator += '</i>'
                    has_opened = False
            else:
                accumulator += char
    else:
        return line
    return accumulator
    return line


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


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''
    accumulator = ''
    first_stars = line.find('**')
    more_stars = -1
    i = 0
    while i < len(line):
        if i == first_stars or i == more_stars:
            end_stars = line.find('**', i+2)
            if end_stars != -1:
                accumulator += '<b>' + line[i+2:end_stars] + '</b>'
                i = end_stars + 2
                more_stars = line.find('**', i)
            else:
                accumulator += line[i]
                i += 1
        else:
            accumulator += line[i]
            i += 1
    return accumulator 


def compile_bold_underscore(line):
    '''
    Convert "__bold__" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''
    accumulator = ''
    first_undersc = line.find('__')
    more_undersc = -1
    i = 0
    while i < len(line):
        if i == first_undersc or i == more_undersc:
            end_undersc = line.find('__', i+2)
            if end_undersc != -1:
                accumulator += '<b>' + line[i+2:end_undersc] + '</b>'
                i = end_undersc + 2
                more_undersc = line.find('__', i)
            else:
                accumulator += line[i]
                i += 1
        else:
            accumulator += line[i]
            i += 1
    return accumulator


def compile_code_inline(line):
    '''
    Add <code> tags.

    HINT:
    This function is like the italics functions because inline code uses only a single character as a delimiter.
    It is more complex, however, because inline code blocks can contain valid HTML inside of them,
    but we do not want that HTML to get rendered as HTML.
    Therefore, we must convert the `<` and `>` signs into `&lt;` and `&gt;` respectively.

    >>> compile_code_inline('You can use backticks like this (`1+2`) to include code in the middle of text.')
    'You can use backticks like this (<code>1+2</code>) to include code in the middle of text.'
    >>> compile_code_inline('This is inline code: `1+2`')
    'This is inline code: <code>1+2</code>'
    >>> compile_code_inline('`1+2`')
    '<code>1+2</code>'
    >>> compile_code_inline('This example has html within the code: `<b>bold!</b>`')
    'This example has html within the code: <code>&lt;b&gt;bold!&lt;/b&gt;</code>'
    >>> compile_code_inline('this example has a math formula in the  code: `1 + 2 < 4`')
    'this example has a math formula in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('this example has a <b>math formula</b> in the  code: `1 + 2 < 4`')
    'this example has a <b>math formula</b> in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('```')
    '```'
    >>> compile_code_inline('```python3')
    '```python3'
    '''
    accumulator = ''
    first_quote = line.find("`")
    more_quotes = -1
    i = 0
    while i < len(line):
        if i == first_quote or i == more_quotes:
            end_quotes = line.find("`", i+1)
            if end_quotes != -1 and end_quotes != i+1:
                if "<" in line or ">" in line:
                    num_greater_less_than = line.count('<') + line.count('>')
                    newLine = line[i+1:end_quotes].replace('<','&lt;')
                    newLine = newLine.replace('>','&gt;')
                    end_quotes += (3*num_greater_less_than)
                else:
                    newLine = line[i+1:end_quotes]
                accumulator += '<code>' + newLine + '</code>'
                i = end_quotes + 1
                more_quotes = line.find("`", i)
            else:
                accumulator += line[i]
                i += 1
        else:
            accumulator += line[i]
            i += 1
    return accumulator

def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    '''
    link = ''
    i = 0
    start = line.find('[')
    bracket_paranth = line.find('](')
    end = line.find(')')
    while i < len(line):
        if start == i and bracket_paranth != -1 and end != -1:
            link += '<a href="' + line[bracket_paranth+2:end] + '">' + line[i+1:bracket_paranth] + '</a>'
            i = end + 1
        else:
            link += line[i]
            i += 1
    return link

def compile_images(line):
    '''
    Add <img> tags.

    HINT:
    Images are formatted in markdown almost exactly the same as links,
    except that images have a leading `!`.
    So your code here should be based off of the <a> tag code.

    >>> compile_images('[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)'
    >>> compile_images('![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '<img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    >>> compile_images('This is an image of Mike Izbicki: ![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    'This is an image of Mike Izbicki: <img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    '''
    link = ''
    i = 0
    start = line.find('![')
    bracket_paranth = line.find('](')
    end = line.find(')')
    while i < len(line):
        if start == i and bracket_paranth != -1 and end != -1:
            link += '<img src="' + line[bracket_paranth+2:end] + '" alt="' + line[start+2:bracket_paranth] + '" />'
            i = end + 1
        else:
            link += line[i]
            i += 1
    return link