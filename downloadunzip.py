import shutil
import os
import tempfile
import itertools
from typing import Union, Tuple

from touchtouch import touch
from FastCopyFast import copyfile
from list_all_files_recursively import get_folder_file_complete_path
import requests


def tempfolder():
    tempfolder = tempfile.TemporaryDirectory()
    tempfolder.cleanup()
    if not os.path.exists(tempfolder.name):
        os.makedirs(tempfolder.name)

    return tempfolder.name


def extract(
    filepath: str,
    dest_dir: str,
) -> list:
    r"""
    Extracts the contents of a compressed file to a specified directory.

    Args:
        filepath (str): The path to the compressed file.
        dest_dir (str): The path to the directory where the contents will be extracted.

    Returns:
        list: A list of complete file paths for all files extracted.

    Raises:
        OSError: If the destination directory cannot be created.
        Exception: If the file cannot be extracted using any of the available formats.

    """
    extract_dir = os.path.normpath(dest_dir)
    filename = os.path.normpath(filepath)
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    try:
        shutil.unpack_archive(filename, extract_dir)
    except Exception as fe:
        for fo in reversed(shutil.get_unpack_formats()):
            try:
                shutil.unpack_archive(filename, extract_dir, fo[0])
            except Exception as fe:
                continue
    return get_folder_file_complete_path(extract_dir)


def upload_file_to_transfer(
    filepath: str, password: Union[str, None] = None, maxdownloads: int = 100000
) -> str:
    if password:
        headers = {
            "Max-Downloads": str(maxdownloads),
            "X-Encrypt-Password": password,
        }
    else:
        headers = {"Max-Downloads": str(maxdownloads)}

    fileonly = filepath.split(os.sep)[-1]
    with open(filepath, "rb") as f:
        data = f.read()
    response = requests.put(
        f"https://transfer.sh/{fileonly}", headers=headers, data=data
    )
    newlink = response.content.decode("utf-8", "ignore")
    return newlink


def iter_find_same_beginning_elements(iters):
    return (x[0] for x in itertools.takewhile(lambda x: len(set(x)) == 1, zip(*iters)))


def find_same_common_folder(files):
    samebe = "".join(
        list(
            iter_find_same_beginning_elements(
                [x.folder if hasattr(x, "folder") else x for x in files + files]
            )
        )
    )
    while not os.path.isdir(samebe) and not os.path.ismount(samebe):
        samebe = os.sep.join(samebe.split(os.sep)[:-1])
        if not samebe:
            return ""
    return samebe


def vartolist(regular_expressions):
    return (
        [regular_expressions]
        if isinstance(regular_expressions, str)
        else list(regular_expressions)
        if not isinstance(regular_expressions, list)
        else regular_expressions
    )


def copy_folder_to_another_folder(
    src: str,
    dest: Union[str, None] = None,
    allowed_extensions: tuple = (),
    maxsubfolders: int = -1,
) -> Tuple[str, list]:
    r"""
    Copies all files and folders from the source folder to the destination folder.
    If the destination folder is not specified, a temporary folder is created.
    Only files with allowed extensions are copied if specified.
    The maximum number of subfolders to copy can be specified.

    Args:
    - src (str): The path of the source folder to copy from.
    - dest (Union[str, None], optional): The path of the destination folder to copy to. Defaults to None.
    - allowed_extensions (tuple, optional): A tuple of allowed file extensions to copy. Defaults to () (all files allowed).
    - maxsubfolders (int, optional): The maximum number of subfolders to copy. Defaults to -1 (all subfolders).

    Returns:
    - Tuple[str, list]: A tuple containing the path of the destination folder and a list of tuples.
    Each tuple in the list contains a boolean value indicating whether the file was successfully copied and the path of the copied file.
    """
    if not dest:
        temp_package_path = tempfolder()
    else:
        temp_package_path = os.path.normpath(dest)
    allfi = get_folder_file_complete_path(src, maxsubfolders=maxsubfolders)
    if allowed_extensions:
        allowed_extensions = vartolist(allowed_extensions)
        alltypes = ["." + str(x).lower().strip(".") for x in allowed_extensions]
        folders = [y.path for y in allfi if y.ext.lower() in alltypes]
    else:
        folders = [y.path for y in allfi]
    samebe = find_same_common_folder(folders)
    samebe.rstrip(os.sep)
    results = []
    for e in folders:
        old = e
        new = os.path.normpath(
            os.path.join(temp_package_path, e[len(samebe) :].lstrip(os.sep))
        )
        touch(new)
        if os.path.isdir(new):
            os.rmdir(new)
        elif os.path.isfile(new):
            os.remove(new)
        try:
            copyfile(old, new)
            results.append((True, new))
        except Exception as fe:
            print(fe)
            results.append((False, new))
    return temp_package_path, results


def zip_folder(
    srcdir: str,
    destfile: str,
    allowed_extensions: tuple = (),
    maxsubfolders: int = -1,
    upload: bool = False,
    password: Union[None, str] = None,
    maxdownloads: int = 100000,
) -> Tuple[str, Union[None, str]]:
    r"""
    Compresses the contents of a source directory into a ZIP file and saves it to a destination file.
    If specified, uploads the ZIP file to a file transfer service and returns a download link.

    Args:
        srcdir (str): The path to the source directory to be compressed.
        destfile (str): The path to the destination file where the ZIP file will be saved.
        allowed_extensions (tuple, optional): A tuple of file extensions to include in the ZIP file. Defaults to ().
        maxsubfolders (int, optional): The maximum number of subfolders to include in the ZIP file. Defaults to -1 (no limit).
        upload (bool, optional): Whether to upload the ZIP file to a file transfer service. Defaults to False.
        password (Union[None, str], optional): The password to protect the ZIP file with. Defaults to None.
        maxdownloads (int, optional): The maximum number of times the uploaded file can be downloaded. Defaults to 100000.

    Returns:
        Tuple[str, Union[None, str]]: A tuple containing the path to the saved ZIP file and, if uploaded, a download link.

    Raises:
        OSError: If the destination file cannot be created or removed.
        Exception: If a file cannot be removed after being added to the ZIP file.

    """
    resultscopy = copy_folder_to_another_folder(
        src=srcdir,
        dest=None,
        allowed_extensions=allowed_extensions,
        maxsubfolders=maxsubfolders,
    )
    if destfile.lower().endswith(".zip"):
        destfile = destfile[:-4]
    destfile = os.path.normpath(destfile)
    touch(destfile)
    if os.path.isdir(destfile):
        os.rmdir(destfile)
    elif os.path.isfile(destfile):
        os.remove(destfile)
    _ = shutil.make_archive(
        destfile,
        "zip",
        resultscopy[0],
    )
    for qq in resultscopy[1:]:
        for q in qq:
            if q[0]:
                try:
                    os.remove(q[1])
                except Exception as fe:
                    print(fe)
                    continue
    link = None
    destfile = destfile + ".zip"
    if upload:
        link = upload_file_to_transfer(
            filepath=destfile, password=password, maxdownloads=maxdownloads
        )
    return destfile, link


def get_tmpfile(suffix=".bin"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    touch(filename)
    return filename


def download_and_extract(url: str, folder: str, *args, **kwargs) -> bool:
    r"""
    Downloads a file from the given URL and extracts it to the specified folder.

    Args:
        url (str): The URL of the file to download.
        folder (str): The folder to extract the downloaded file to.
        *args: Additional positional arguments to pass to the requests.get() function.
        **kwargs: Additional keyword arguments to pass to the requests.get() function.

    Returns:
        bool: True if the file was downloaded and extracted successfully, False otherwise.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    data = None
    with requests.get(url, *args, **kwargs) as f:
        if str(f.status_code)[0] == "2":
            data = f.content
    filepath = get_tmpfile(".tmp")[:-4]
    if data:
        with open(filepath, mode="wb") as f:
            f.write(data)
        extract(filepath, folder)
        return True
    return False

