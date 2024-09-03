import json
import os

def process_text_file(file_path):
      # Define the header mappings
    header_mapping = {
        'nom': 'name',
        'NOMRAT': 'name',
        'XLONG': 'longitude',
        'YLAT': 'latitude'
    }
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove blank lines
    lines = [line.strip() for line in lines if line.strip()]

    # Ignore the first 10 rows
    lines = lines[10:]

    # Find the last occurrence of "Tri croissantTri décroissant"
    last_tri_line_index = None
    for i, line in enumerate(lines):
        if "Tri croissantTri décroissant" in line:
            last_tri_line_index = i
    
    if last_tri_line_index is None:
        raise ValueError("The string 'Tri croissantTri décroissant' was not found in the file.")

    
    # Extract title and headers
    title = lines[0]  # 11th row
    header_lines = lines[2:last_tri_line_index:2] # Headers are in odd rows before the last "Tri croissantTri décroissant" from 13 rows
    # Replace specific headers based on the mapping
    headers = [header_mapping.get(header, header) for header in header_lines]
    # Extract content starting after the last "Tri croissantTri décroissant"
    content_lines = lines[last_tri_line_index + 1:]
    table_rows = [content_lines[i:i+len(headers)] for i in range(0, len(content_lines), len(headers))]

    # Convert content to GeoJSON features
    features = []
    for row in table_rows:
        properties = {headers[i]: row[i] for i in range(len(headers))}
        feature = {
            "type": "Feature",
            "title": title,
            "properties": properties,
            "geometry": {
                "type" : "Point",
                "coordinates" : [properties.get("longitude"), properties.get("latitude")]
            }
        }
        features.append(feature)

    # Create GeoJSON structure
    geojson = {
        "type": "FeatureCollection",
        "name": title,
        "features": features
    }

    return geojson

def process_all_files_in_folder(input_folder_path,output_folder_path):
    # List all text files in the folder
    for filename in os.listdir(input_folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder_path, filename)
            geojson_data = process_text_file(file_path)

            # Save the GeoJSON data to a file with UTF-8 encoding
            output_filename = filename.replace('.txt', '.geojson')
            output_path = os.path.join(output_folder_path, output_filename)
            with open(output_path, 'w', encoding='utf-8') as geojson_file:
                json.dump(geojson_data, geojson_file, ensure_ascii=False, indent=4)

            print(f"Converted {filename} to {output_filename}")

# Example usage
input_folder_path = 'input'
output_folder_path = 'output'
process_all_files_in_folder(input_folder_path,output_folder_path)
