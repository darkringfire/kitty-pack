from pathlib import Path


def get_replace_list(path):
    replace_list = {}
    with path.open(newline='') as f:
        for line in f:
            param = line[:line.find('\\')]
            replace_list[param] = line.rstrip()
    return replace_list


def process_file(path, replace_list):
    """

    :type replace_list: Dict[string]
    :type path: Path
    """
    print(path.resolve())
    content = []
    with path.open(newline='') as f:
        for line in f:
            line = line.rstrip()
            param = line[:line.find('\\')]
            if param in replace_list:
                content.append(replace_list[param])
            else:
                content.append(line)
    with path.open(mode='w', newline='\n') as f:
        print(*content, sep='\n', end='\n', file=f)


def process_dir(path, replace_list):
    for el in path.iterdir():
        if el.is_dir():
            process_dir(el, replace_list)
        elif el.suffix == '.ktx':
            process_file(el, replace_list)


def main():
    replace_list = get_replace_list(Path('def-settings.txt'))
    process_dir(Path('Sessions'), replace_list)


main()
