import os
import shutil
import re

downloads_folder = os.path.expanduser("~/Downloads")
imports_folder = os.path.join(os.getcwd(), "data/imports/usa")
exports_folder = os.path.join(os.getcwd(), "data/exports/usa")

# Create target directories for imports and exports
os.makedirs(imports_folder, exist_ok=True)
os.makedirs(exports_folder, exist_ok=True)

unique_countries = set()

# Handle faulty country names
faulty_names = {
    "Nam": ["Vietnam", "Viet"],
    "Chinese": ["Taiwan", "Taipei"],
    "Kingdom": ["UnitedKingdom", "United"],
}

for filename in os.listdir(downloads_folder):
    if filename.startswith("Trade_Map"):
        parts = filename.split('_')
        country_name = parts[-1].replace('.xls', '').strip()
        country_name = re.sub(r"\s\(\d+\)", "", country_name)
        check_name = country_name

        # Handle faulty country names
        if country_name in faulty_names:
            check_name = faulty_names[country_name][1]
            country_name = faulty_names[country_name][0]

        # Add country to the set
        unique_countries.add(country_name)

        old_file_path = os.path.join(downloads_folder, filename)

        # Read the file content to determine if it’s an import or export file
        with open(old_file_path, 'r') as f:
            content = f.read()

        if f"imports from {check_name.capitalize()}" in content:
            new_file_name = f"{country_name}_Import.xls"
            target_folder = imports_folder  # Use imports folder for imports
        else:
            new_file_name = f"{country_name}_Export.xls"
            target_folder = exports_folder  # Use exports folder for exports

        # Copy file to the appropriate target folder
        new_file_path = os.path.join(target_folder, new_file_name)
        shutil.copy(old_file_path, new_file_path)

        # Clean up the new file by removing the first 15 lines
        with open(new_file_path, 'r') as f:
            lines = f.readlines()

        if len(lines) > 15:
            with open(new_file_path, 'w') as f:
                f.writelines(lines[15:])

# Write the list of processed countries to countries.md
countries_file_path = 'countries.md'
with open(countries_file_path, 'w') as f:
    f.write("# List of Processed Countries\n\n")
    for country in sorted(unique_countries):
        f.write(f"- {country}\n")

print("Files processed successfully.")
