from pathlib import Path


p = Path(input("Введите путь к папке: "))


def check_size(folder, limit):
    file_sizes = []
    for path in folder.rglob('*'):
        if path.is_file():
            size = path.stat().st_size
            file_sizes.append((size, path))
    file_sizes.sort(reverse=True)
    return file_sizes[:limit]


if p.is_dir():
    top = check_size(p, 5)
    if len(top) == 0:
        print("Файлов в папке нет")
    else:
        for num, (size, path) in enumerate(top, 1):
            size_mb = round(size/ 1048576, 2)
            print(f"{num}. {path} - {size_mb} мб.")
else:
    print("Папка не найдена")