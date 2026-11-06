"""Imports an Instagram export supplied by the account owner. No Instagram login or scraping."""
import argparse, shutil, zipfile
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True,help="Owner-provided export ZIP or folder")
    p.add_argument("--output",default="./imports")
    a=p.parse_args()
    src=Path(a.input).expanduser().resolve()
    dst=Path(a.output).expanduser().resolve()
    dst.mkdir(parents=True,exist_ok=True)
    if not src.exists(): raise SystemExit("Input does not exist")
    if src.is_file() and src.suffix.lower()==".zip":
        with zipfile.ZipFile(src) as z:
            for item in z.infolist():
                target=(dst/item.filename).resolve()
                if dst not in target.parents and target!=dst: raise SystemExit("Unsafe ZIP path; cancelled")
            z.extractall(dst)
    elif src.is_dir():
        for item in src.iterdir():
            target=dst/item.name
            shutil.copytree(item,target,dirs_exist_ok=True) if item.is_dir() else shutil.copy2(item,target)
    else: raise SystemExit("Provide an export ZIP or folder")
    print(f"Owner export imported to {dst}; no private account access was attempted.")

if __name__=="__main__": main()
