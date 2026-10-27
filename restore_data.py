"""Restore original names and directories from locally downloaded release assets."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath


def restore(manifest_path, assets_dir, destination):
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    root = destination.resolve()
    for record in manifest['files']:
        relative = PurePosixPath(record['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Unsafe manifest path')
        target = root.joinpath(*relative.parts)
        if not target.resolve().is_relative_to(root):
            raise ValueError('Destination must remain inside the output folder')
        target.parent.mkdir(parents=True, exist_ok=True)
        pending = target.with_name(target.name + '.partial')
        if target.exists() or pending.exists():
            raise FileExistsError(f'Refusing to overwrite: {target}')
        whole = hashlib.sha256()
        total = 0
        with pending.open('xb') as output:
            for asset in record['assets']:
                if Path(asset['name']).name != asset['name']:
                    raise ValueError('Unsafe asset name')
                source = assets_dir / asset['name']
                if source.stat().st_size != asset['bytes']:
                    raise ValueError(f'Incorrect asset length: {source}')
                digest = hashlib.sha256()
                with source.open('rb') as stream:
                    while data := stream.read(8 * 1024 * 1024):
                        digest.update(data)
                        whole.update(data)
                        total += len(data)
                        output.write(data)
                if digest.hexdigest() != asset['sha256']:
                    raise ValueError(f'Asset checksum mismatch: {source}')
        if total != record['bytes'] or whole.hexdigest() != record['sha256']:
            raise ValueError(f'Original-file checksum mismatch: {target}')
        pending.rename(target)
        print(f'Verified: {relative}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=Path(__file__).with_name('manifest.json'))
    parser.add_argument('--assets', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('data'))
    args = parser.parse_args()
    restore(args.manifest, args.assets, args.output)
