# Archive Creator with Multiple Formats Support

This Python script allows you to create archives in various formats, such as `.zip`, `.tar`, `.tar.gz`, `.tar.bz2`, `.tar.xz`, `.7z`, and `.rar`. The script uses Python libraries and external utilities for archive creation.

## Usage

### Dependencies

To work with `.rar` and `.7z` archives, you need to install the `rar` and `7z` utilities.

- Install a program to create `.rar` archives (like WinRAR or equivalent).
- Install 7-Zip for `.7z` archive creation.

### Running the Script

To create an archive from the specified folder, run the following command:

```bash
python script.py /path/to/folder archive_name .zip .tar .gz
