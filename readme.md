Download pdf from a list of doi and a Scihub mirror.

## Installation

Install the dependencies
```
pip install requests
pip install argparse
```

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