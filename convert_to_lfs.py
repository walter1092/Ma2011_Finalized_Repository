#!/usr/bin/env python3
import sys
import hashlib

def callback(blob, metadata):
    filename = metadata['filename']
    if (filename.startswith("My project/Library/Artifacts/c1/c1d779f1b165e9661ec68b80e9928ffc") or
        filename.startswith("MA2011 unity/Library/PackageCache/com.unity.sysroot.linux-x86_64@2.0.6/data~/payload.tar.7z") or
        filename.startswith("MA2011 unity/Packages/Exported Package.unitypackage")):
        sha256 = hashlib.sha256(blob.data).hexdigest()
        size = len(blob.data)
        return f"version https://git-lfs.github.com/spec/v1\noid sha256:{sha256}\nsize {size}".encode()
    return blob.data

print("blob_callback")
print(callback)
