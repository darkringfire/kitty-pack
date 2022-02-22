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
    print(path.resolve())
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
    replaces = {}
    replaces.update(load_conf(Path('Defaults/settings.txt')))
    replaces.update(load_conf(Path('Defaults/theme-Dracula.txt')))
    process_dir(Path('Sessions'), replaces)


main()
