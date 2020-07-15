Download pdf from a list of doi and a Scihub mirror.

## Installation
### With Python
Install the dependencies
```
pip install requests
pip install argparse
git clone https://github.com/bgallois/scihub_bulk_downloader.git
cd scihub_bulk_downloader
```
### As binary
Download the binary in the [releases](https://github.com/bgallois/scihub_bulk_downloader/releases)

## Usage

Execute the script
```
./scdl doi.txt --mirror urlMirror --dest papers/
```
or
```
python scdl doi.txt --mirror urlMirror --dest papers/
```

## Parameters

#### Mandatory
* List of doi as several arguments or file with one doi by line. `./scdl doi1 doi2 doi3 --mirror urlMirror` or `./scdl doi.txt --mirror urlMirror`
* --mirror: Url to a reachable Scihub mirror.

#### Optional
* --dest: Path to a folder where to store the pdf files.