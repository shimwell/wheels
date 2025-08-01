
from pathlib import Path

# List of folders to process
folders = ["moab", "openmc"]

for folder in folders:
    folder_path = Path(folder)
    wheel_files = sorted([f.name for f in folder_path.glob("*.whl")])
    html_content = "<!DOCTYPE html>\n<html>\n  <body>\n"
    for wheel in wheel_files:
        html_content += f'    <a href="{wheel}">{wheel}</a><br>\n'
    html_content += "  </body>\n</html>\n"
    # Write to index.html inside the folder
    with open(folder_path / "index.html", "w") as f:
        f.write(html_content)
    print(f"index.html generated in {folder} with links to all .whl files.")