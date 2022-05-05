from pathlib import Path


def load_conf(path):
    replace_list = {}
    with path.open(newline='') as f:
        for line in f:
            param = line[:line.find('\\')]
            replace_list[param] = line.rstrip()
    return replace_list


def process_file(path, replaces):
    """

    :type replaces: Dict[string]
    :type path: Path
    """

    # print(path.resolve())
    conf = load_conf(path)
    conf.update(replaces)
    # print(*conf.values(), sep='\n', end='\n')
    with path.open(mode='w', newline='\n') as f:
        print(*conf.values(), sep='\n', end='\n', file=f)


def process_dir(path, replaces):
    for el in path.iterdir():
        if el.is_dir():
            process_dir(el, replaces)
            pass
        elif el.suffix == '.ktx' or el.name == 'Default%20Settings':
            process_file(el, replaces)


def main():
    settings_dir = Path(__file__).parent / 'Defaults'
    settings_file = settings_dir / 'settings.txt'
    local_file = settings_dir / 'local.txt'
    theme_file = settings_dir / 'theme.txt'

    replaces = {}
    replaces.update(load_conf(settings_file))
    for file in (local_file, theme_file):
        try:
            replaces.update(load_conf(file))
        except FileNotFoundError:
            print('File "{}" not found'.format(file))

    process_dir(Path('Sessions'), replaces)
    print('Done! Press Enter', end='')
    try:
        input()
    except KeyboardInterrupt:
        pass


main()
