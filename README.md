# Text File to GeoJSON Converter

This Python script processes text files containing tabular data and converts them into GeoJSON format. The script is designed to handle files with varying header lengths and specific patterns in the content.

## Features

- **Header Mapping**: Automatically maps specific header names (`nom`, `NOMRAT`, `XLONG`, `YLAT`) to `name`, `longitude`, and `latitude`.
- **Flexible Header Handling**: The script can handle text files where headers are on odd-numbered lines, starting from line 13. It identifies the end of the header section using the string "Tri croissantTri décroissant".
- **GeoJSON Output**: Converts table rows into GeoJSON features, identifying and using the `longitude` and `latitude` fields for the geometry.
- **UTF-8 Encoding**: The output files are saved with UTF-8 encoding to handle special characters.
- **Output Folder Management**: The script creates an `output` folder in the specified directory if it does not already exist, storing all converted GeoJSON files there.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the script files to your local machine.
    git clone https://github.com/binaryking979/text-to-geojson.git
    cd text-to-geojson
2. Ensure you have Python 3.x installed on your system.

## Usage

1. Place your text files in "input" folder.
2. Run the script using the following command:

   ```bash
   python converter.py
