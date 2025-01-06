import os
import pwd
import grp
from datetime import datetime
from pathlib import Path

def check_file_metadata(directory='.'):
    """Check files in directory for metadata."""
    results = []
    
    for path in Path(directory).rglob('*'):
        if path.is_file():
            stats = path.stat()
            try:
                results.append({
                    'file': str(path),
                    'owner': pwd.getpwuid(stats.st_uid).pw_name,
                    'group': grp.getgrgid(stats.st_gid).gr_name,
                    'permissions': oct(stats.st_mode)[-3:],
                    'created': datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                    'modified': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    'accessed': datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S'),
                    'size': stats.st_size
                })
            except KeyError:
                # Skip if user/group lookup fails
                continue
            
    return results

if __name__ == '__main__':
    metadata = check_file_metadata()
    for item in metadata:
        print(f"\nFile: {item['file']}")
        print(f"Owner: {item['owner']}")
        print(f"Group: {item['group']}")
        print(f"Permissions: {item['permissions']}")
        print(f"Created: {item['created']}")
        print(f"Modified: {item['modified']}")
        print(f"Accessed: {item['accessed']}")
        print(f"Size: {item['size']} bytes")