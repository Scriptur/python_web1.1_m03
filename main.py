import shutil
import sys
import scan
import normalize
from pathlib import Path
from threading import Thread



def handle_file(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))


def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.name)
    if new_name.endswith('.zip'):
        new_name = new_name.replace('.zip', '')

    if new_name.endswith('tar.gz'):
        new_name = new_name.replace('tar.gz', '')
        
    if new_name.endswith('.gz'):
        new_name = new_name.replace('.gz', '')
        
    if new_name.endswith('.tar'):
        new_name = new_name.replace('.tar', '')

        
    archive_folder = root_folder / dist / new_name
    
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass


def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass

def sorting_files(folder_path):

    scan.scan(folder_path)

    threads = [] 

    for file in scan.jpeg_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "images"))
        thread.start()
        threads.append(thread)

    [thread.join() for thread in threads]
            
    for file in scan.png_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "images"))
        thread.start()
        threads.append(thread)

    [thread.join() for thread in threads]

    for file in scan.jpg_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "images"))
        thread.start()
        threads.append(thread)

    for file in scan.svg_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "images"))
        thread.start()
        threads.append(thread)
    
    for file in scan.avi_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "video"))
        thread.start()
        threads.append(thread)

    for file in scan.mp4_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "video"))
        thread.start()
        threads.append(thread)

    for file in scan.mov_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "video"))
        thread.start()
        threads.append(thread)

    for file in scan.mkv_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "video"))
        thread.start()
        threads.append(thread)

    for file in scan.doc_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "documents"))
        thread.start()
        threads.append(thread)

    for file in scan.docx_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "documents"))
        thread.start()
        threads.append(thread)

    for file in scan.txt_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "documents"))
        thread.start()
        threads.append(thread)

    for file in scan.pdf_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "documents"))
        thread.start()
        threads.append(thread)

    for file in scan.xlsx_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "documents"))
        thread.start()
        threads.append(thread)

    for file in scan.pptx_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "documents"))
        thread.start()
        threads.append(thread)

    for file in scan.mp3_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "audio"))
        thread.start()
        threads.append(thread)

    for file in scan.ogg_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "audio"))
        thread.start()
        threads.append(thread)

    for file in scan.wav_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "audio"))
        thread.start()
        threads.append(thread)

    for file in scan.amr_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "audio"))
        thread.start()
        threads.append(thread)

    for file in scan.zip_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "archives"))
        thread.start()
        threads.append(thread)

    for file in scan.gz_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "archives"))
        thread.start()
        threads.append(thread)

    for file in scan.tar_files:
        thread = Thread(target=handle_file, args=(file, folder_path, "archives"))
        thread.start()
        threads.append(thread)
    
    for file in scan.unknown:
        thread = Thread(target=handle_file, args=(file, folder_path, "unknown"))
        thread.start()
        threads.append(thread)

    get_folder_objects(folder_path)

def main():
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    sorting_files(arg.resolve())

if __name__ == '__main__':
    main()