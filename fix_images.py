import re
from pathlib import Path

MD_FILE = Path("console.md")
IMG_DIR = Path("assets/images/console")

# Aapke folder ki saari 23 images
ALL_IMAGES = {
    "console-all-projects.png",
    "console-backups.png",
    "console-cluster-actions.png",
    "console-cluster-features.png",
    "console-cluster-overview.png",
    "console-clusters.png",
    "console-connection.png",
    "console-create-cluster-size.png",
    "console-create-cluster.png",
    "console-create-monitoring-logging.png",
    "console-dashboards.png",
    "console-databases.png",
    "console-discovery.png",
    "console-home.png",
    "console-logging-confirm.png",
    "console-login.png",
    "console-migration.png",
    "console-observability.png",
    "console-restore.png",
    "console-sql-editor.png",
    "console-sql-replica.png",
    "console-sql-server.png",
    "console-users.png",
}

text = MD_FILE.read_text(encoding="utf-8")

# <p align="center"> <img ...> <br> <em>caption</em> </p>  ->  ![alt](path) + *caption*
pattern = re.compile(
    r'<p align="center">\s*'
    r'<img src="([^"]+)" alt="([^"]+)" width="100%">\s*'
    r'<br>\s*'
    r'<em>(.*?)</em>\s*'
    r'</p>',
    re.DOTALL,
)

new_text, count = pattern.subn(r'![\2](\1)\n\n*\3*', text)

# Backup + save
Path(str(MD_FILE) + ".bak").write_text(text, encoding="utf-8")
MD_FILE.write_text(new_text, encoding="utf-8")

# Ab file me jitni images hain unko check karo
used = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', new_text)
used_names = {Path(u).name for u in used}

print(f"{count} image blocks convert hue")
print(f"Total images file me use ho rahi: {len(used_names)}")

# Path check: file me likha naam folder me hai ya nahi
for u in used:
    name = Path(u).name
    if name not in ALL_IMAGES:
        print(f"[NAAM GALAT] {u}  (folder me ye naam nahi hai)")
    elif not Path(u).exists():
        print(f"[FILE NAHI MILI] {u}  (script ko docs/ folder se chalao)")

# Unused images
unused = sorted(ALL_IMAGES - used_names)
print("\nUse nahi ho rahi images:")
for n in unused:
    print("  -", n)