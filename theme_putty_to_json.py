import json
from pathlib import Path

colours = {
    'foreground': 'Colour0',
    'background': 'Colour2',
    'selectionBackground': 'Colour5',
    'cursorColour': 'Colour5',
    'black': 'Colour6',
    'brightBlack': 'Colour7',
    'red': 'Colour8',
    'brightRed': 'Colour9',
    'green': 'Colour10',
    'brightGreen': 'Colour11',
    'yellow': 'Colour12',
    'brightYellow': 'Colour13',
    'blue': 'Colour14',
    'brightBlue': 'Colour15',
    'purple': 'Colour16',
    'brightPurple': 'Colour17',
    'cyan': 'Colour18',
    'brightCyan': 'Colour19',
    'white': 'Colour20',
    'brightWhite': 'Colour21'
}

theme = {
    'name': 'Solarized Darcula'
}
conf = {}
with Path('Defaults/theme-Solarized-Darcula.txt').open() as f:
    for line in f:
        k, v = line.split('\\')[:2]
        conf[k] = v.split(',')
for k, c in colours.items():
    if c in conf.keys():
        theme[k] = '#{:02X}{:02X}{:02X}'.format(*map(int, conf[c]))
print(json.dumps(theme, indent=4))
