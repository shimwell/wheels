
from pathlib import Path

# Every directory holding wheels is a package in the index
folders = sorted(p for p in Path(".").iterdir() if p.is_dir() and not p.name.startswith(".") and any(p.glob("*.whl")))

for folder_path in folders:
    wheel_files = sorted([f.name for f in folder_path.glob("*.whl")])
    html_content = "<!DOCTYPE html>\n<html>\n  <body>\n"
    for wheel in wheel_files:
        html_content += f'    <a href="{wheel}">{wheel}</a><br>\n'
    html_content += "  </body>\n</html>\n"
    # Write to index.html inside the folder
    with open(folder_path / "index.html", "w") as f:
        f.write(html_content)
    print(f"index.html generated in {folder_path} with links to all .whl files.")

# Root index listing every package, as required by PEP 503
root_content = "<!DOCTYPE html>\n<html>\n  <body>\n"
for folder_path in folders:
    root_content += f'    <a href="{folder_path.name}/">{folder_path.name}</a><br>\n'
root_content += "  </body>\n</html>\n"
Path("index.html").write_text(root_content)
print(f"index.html generated in the root with links to {len(folders)} packages.")
