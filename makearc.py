import os
import subprocess
import zipfile
import tarfile
import shutil

def create_zip(path, archive_name):
    with zipfile.ZipFile(f"{archive_name}.zip", 'w', zipfile.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(path):
            for file in files:
                archive.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), path))

def create_tar(path, archive_name):
    with tarfile.open(f"{archive_name}.tar", "w") as archive:
        archive.add(path, arcname=os.path.basename(path))

def create_gz(path, archive_name):
    with tarfile.open(f"{archive_name}.tar.gz", "w:gz") as archive:
        archive.add(path, arcname=os.path.basename(path))

def create_bz2(path, archive_name):
    with tarfile.open(f"{archive_name}.tar.bz2", "w:bz2") as archive:
        archive.add(path, arcname=os.path.basename(path))

def create_xz(path, archive_name):
    with tarfile.open(f"{archive_name}.tar.xz", "w:xz") as archive:
        archive.add(path, arcname=os.path.basename(path))

def create_7z(path, archive_name):
    subprocess.run(['7z', 'a', f'{archive_name}.7z', path])

def create_rar(path, archive_name):
    subprocess.run(['rar', 'a', f'{archive_name}.rar', path])

def create_archives(path, archive_name, *formats):
    for fmt in formats:
        if fmt == '.zip':
            create_zip(path, archive_name)
        elif fmt == '.tar':
            create_tar(path, archive_name)
        elif fmt == '.tar.gz':
            create_gz(path, archive_name)
        elif fmt == '.tar.bz2':
            create_bz2(path, archive_name)
        elif fmt == '.tar.xz':
            create_xz(path, archive_name)
        elif fmt == '.7z':
            create_7z(path, archive_name)
        elif fmt == '.rar':
            create_rar(path, archive_name)
        else:
            print(f"this format {fmt} not supported.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Using: python script.py <path> <archive_name> <format>")
    else:
        create_archives(sys.argv[1], sys.argv[2], *sys.argv[3:])
