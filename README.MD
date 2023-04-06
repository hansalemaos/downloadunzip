# creates, uploads, downloads, extracts and copies archives (zip, tar ...)


```python
pip install downloadunzip
```

```python
from downloadunzip import extract,copy_folder_to_another_folder,zip_folder,download_and_extract
filepath = r"C:\Users\hansc\Downloads\ripgrep-13.0.0-x86_64-pc-windows-msvc.zip"
dest_dir = r"C:\Users\hansc\Downloads\test2xxxx"
extractedzipfiles = extract(filepath, dest_dir)
print(extractedzipfiles)
folder, results = copy_folder_to_another_folder(
    src=dest_dir, dest="e:\\testcopy", allowed_extensions=(), maxsubfolders=1
)
print(folder)
print(results)
foldertmp, resultstmp = copy_folder_to_another_folder(
    src=dest_dir, dest=None, allowed_extensions=(), maxsubfolders=1
)
print(foldertmp)
print(resultstmp)
zipfile, url = zip_folder(
    srcdir=r"C:\Users\hansc\Downloads\test2xxx\ripgrep-13.0.0-x86_64-pc-windows-gnu",
    destfile=r"C:\Users\hansc\Downloads\zippedfile.zip",
    allowed_extensions=("exe",),
    maxsubfolders=-1,
    upload=False,
    password=None,
    maxdownloads=100000,
)
print(zipfile)
print(url)

zipfile, url = zip_folder(
    srcdir=r"C:\Users\hansc\Downloads\test2xxxx\ripgrep-13.0.0-x86_64-pc-windows-msvc",
    destfile=r"C:\Users\hansc\Downloads\zippedfile2.zip",
    allowed_extensions=(),
    maxsubfolders=-1,
    upload=True,
    password=None,
    maxdownloads=100000,
)
print(zipfile)
print(url)

diditwork = download_and_extract(
    url=r"https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep-13.0.0-x86_64-pc-windows-msvc.zip",
    folder="e:\\testdownl",
)
print(diditwork)

[files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='COPYING', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\COPYING', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='LICENSE-MIT', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\LICENSE-MIT', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='README.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\README.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='rg.exe', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\rg.exe', ext='.exe'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='UNLICENSE', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\UNLICENSE', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='rg.bash', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\rg.bash', ext='.bash'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='rg.fish', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\rg.fish', ext='.fish'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='_rg', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\_rg', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='_rg.ps1', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\_rg.ps1', ext='.ps1'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc', file='CHANGELOG.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc\\CHANGELOG.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc', file='FAQ.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc\\FAQ.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc', file='GUIDE.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc\\GUIDE.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='COPYING', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\COPYING', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='LICENSE-MIT', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\LICENSE-MIT', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='README.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\README.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='rg.exe', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\rg.exe', ext='.exe'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='UNLICENSE', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\UNLICENSE', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='rg.bash', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\rg.bash', ext='.bash'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='rg.fish', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\rg.fish', ext='.fish'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='_rg', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\_rg', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='_rg.ps1', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\_rg.ps1', ext='.ps1'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc', file='CHANGELOG.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc\\CHANGELOG.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc', file='FAQ.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc\\FAQ.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc', file='GUIDE.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc\\GUIDE.md', ext='.md')]
e:\testcopy
[(True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\COPYING'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\LICENSE-MIT'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\README.md'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\rg.exe'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\UNLICENSE'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\COPYING'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\LICENSE-MIT'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\README.md'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\rg.exe'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\UNLICENSE')]
C:\Users\hansc\AppData\Local\Temp\tmpx7r88ose
[(True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\COPYING'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\LICENSE-MIT'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\README.md'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\rg.exe'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\UNLICENSE'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\COPYING'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\LICENSE-MIT'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\README.md'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\rg.exe'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmpx7r88ose\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\UNLICENSE')]
C:\Users\hansc\Downloads\zippedfile.zip
None
C:\Users\hansc\Downloads\zippedfile2.zip
https://transfer.sh/A3iiQ4/zippedfile2.zip
True


[files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='COPYING', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\COPYING', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='LICENSE-MIT', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\LICENSE-MIT', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='README.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\README.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='rg.exe', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\rg.exe', ext='.exe'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu', file='UNLICENSE', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\UNLICENSE', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='rg.bash', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\rg.bash', ext='.bash'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='rg.fish', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\rg.fish', ext='.fish'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='_rg', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\_rg', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete', file='_rg.ps1', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\complete\\_rg.ps1', ext='.ps1'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc', file='CHANGELOG.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc\\CHANGELOG.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc', file='FAQ.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc\\FAQ.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc', file='GUIDE.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\doc\\GUIDE.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='COPYING', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\COPYING', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='LICENSE-MIT', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\LICENSE-MIT', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='README.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\README.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='rg.exe', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\rg.exe', ext='.exe'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc', file='UNLICENSE', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\UNLICENSE', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='rg.bash', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\rg.bash', ext='.bash'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='rg.fish', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\rg.fish', ext='.fish'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='_rg', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\_rg', ext=''), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete', file='_rg.ps1', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\complete\\_rg.ps1', ext='.ps1'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc', file='CHANGELOG.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc\\CHANGELOG.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc', file='FAQ.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc\\FAQ.md', ext='.md'), files(folder='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc', file='GUIDE.md', path='C:\\Users\\hansc\\Downloads\\test2xxxx\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\doc\\GUIDE.md', ext='.md')]
e:\testcopy
[(True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\COPYING'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\LICENSE-MIT'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\README.md'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\rg.exe'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\UNLICENSE'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\COPYING'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\LICENSE-MIT'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\README.md'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\rg.exe'), (True, 'e:\\testcopy\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\UNLICENSE')]
C:\Users\hansc\AppData\Local\Temp\tmp6sl3v7v6
[(True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\COPYING'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\LICENSE-MIT'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\README.md'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\rg.exe'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-gnu\\UNLICENSE'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\COPYING'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\LICENSE-MIT'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\README.md'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\rg.exe'), (True, 'C:\\Users\\hansc\\AppData\\Local\\Temp\\tmp6sl3v7v6\\ripgrep-13.0.0-x86_64-pc-windows-msvc\\UNLICENSE')]
C:\Users\hansc\Downloads\zippedfile.zip
None
C:\Users\hansc\Downloads\zippedfile2.zip
https://transfer.sh/EjUBrS/zippedfile2.zip
True
```

```python
copy_folder_to_another_folder(src: str, dest: Optional[str] = None, allowed_extensions: tuple = (), maxsubfolders: int = -1) -> Tuple[str, list]
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

download_and_extract(url: str, folder: str, *args, **kwargs) -> bool
	Downloads a file from the given URL and extracts it to the specified folder.
	
	Args:
		url (str): The URL of the file to download.
		folder (str): The folder to extract the downloaded file to.
		*args: Additional positional arguments to pass to the requests.get() function.
		**kwargs: Additional keyword arguments to pass to the requests.get() function.
	
	Returns:
		bool: True if the file was downloaded and extracted successfully, False otherwise.

extract(filepath: str, dest_dir: str) -> list
	Extracts the contents of a compressed file to a specified directory.
	
	Args:
		filepath (str): The path to the compressed file.
		dest_dir (str): The path to the directory where the contents will be extracted.
	
	Returns:
		list: A list of complete file paths for all files extracted.
	
	Raises:
		OSError: If the destination directory cannot be created.
		Exception: If the file cannot be extracted using any of the available formats.

find_same_common_folder(files)

get_tmpfile(suffix='.bin')

iter_find_same_beginning_elements(iters)

tempfolder()

upload_file_to_transfer(filepath: str, password: Optional[str] = None, maxdownloads: int = 100000) -> str

vartolist(regular_expressions)

zip_folder(srcdir: str, destfile: str, allowed_extensions: tuple = (), maxsubfolders: int = -1, upload: bool = False, password: Optional[str] = None, maxdownloads: int = 100000) -> Tuple[str, Optional[str]]
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
```