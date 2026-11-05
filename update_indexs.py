from pathlib import Path


def package_folders(root):
    """Every directory directly under root holding wheels is a package."""
    return sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".") and any(p.glob("*.whl")))


def write_index(root):
    folders = package_folders(root)
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
    (root / "index.html").write_text(root_content)
    print(f"index.html generated in {root} with links to {len(folders)} packages.")


# The repository root is the main index. A top-level directory whose
# subdirectories hold wheels is a separate index, for builds that share a
# package name with the main index, such as openmc-extras/openmc.
root = Path(".")
write_index(root)
for index_root in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".") and package_folders(p)):
    write_index(index_root)
