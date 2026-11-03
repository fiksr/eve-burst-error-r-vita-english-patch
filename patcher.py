#!/usr/bin/env python3
"""
EVE burst error R (PS Vita) - English Translation Patcher
Title ID: PCSG00817

This tool injects translated scenario scripts and localized UI textures into 
the game's data.psarc archive. Requires a legally dumped original data.psarc.
Zero external dependencies required (uses standard library only).
"""

import struct
import zlib
import os
import sys
import time

def find_data_psarc():
    candidates = [
        "data.psarc",
        "data/data.psarc",
        "PCSG00817/data/data.psarc",
    ]
    for c in candidates:
        if os.path.exists(c) and os.path.getsize(c) > 100_000_000:
            return c
    return None

def patch_psarc(input_psarc_path, output_psarc_path, patch_dir):
    print("=" * 65)
    print("  EVE burst error R (PS Vita) - English Translation Patcher")
    print("  Title ID: PCSG00817")
    print("=" * 65)
    print(f"\n[+] Input archive:  {input_psarc_path}")
    print(f"[+] Output archive: {output_psarc_path}")
    print(f"[+] Patch folder:   {patch_dir}")

    if not os.path.exists(input_psarc_path):
        print(f"\n[!] Error: Input archive '{input_psarc_path}' not found!")
        sys.exit(1)

    t0 = time.time()
    with open(input_psarc_path, "rb") as f_in:
        header = f_in.read(32)
        magic, ver_maj, ver_min, compression_type, toc_size, entry_size, num_entries, block_size, flags = struct.unpack(">4sHH4sIIIII", header)
        if magic != b"PSAR":
            print("[!] Error: File is not a valid PSARC archive.")
            sys.exit(1)
        if compression_type != b"zlib":
            print(f"[!] Error: Expected zlib compression, got {compression_type}.")
            sys.exit(1)

        print(f"[+] Reading archive TOC: {num_entries} entries, block size {block_size} bytes...")

        # Read TOC entries
        entries = []
        for i in range(num_entries):
            e_bytes = f_in.read(entry_size)
            name_hash = e_bytes[:16]
            zblock_idx, = struct.unpack(">I", e_bytes[16:20])
            uncomp_size = int.from_bytes(e_bytes[20:25], "big")
            offset = int.from_bytes(e_bytes[25:30], "big")
            entries.append({
                "index": i,
                "name_hash": name_hash,
                "zblock_idx": zblock_idx,
                "uncomp_size": uncomp_size,
                "offset": offset,
            })

        # Read zblock table
        entries_len = entry_size * num_entries
        zblock_table_len = toc_size - entries_len
        zblock_bytes = f_in.read(zblock_table_len)
        num_zblocks = zblock_table_len // 2
        zblocks = list(struct.unpack(f">{num_zblocks}H", zblock_bytes))

        # Read entry 0 manifest
        zb_start = entries[0]["zblock_idx"]
        next_zb = entries[1]["zblock_idx"]
        e_zblocks = zblocks[zb_start:next_zb]
        f_in.seek(entries[0]["offset"])
        manifest_bytes = bytearray()
        for zb in e_zblocks:
            sz = zb if zb != 0 else block_size
            chunk = f_in.read(sz)
            if zb != 0:
                manifest_bytes.extend(zlib.decompress(chunk))
            else:
                manifest_bytes.extend(chunk)

        manifest_lines = [l.strip() for l in manifest_bytes.decode('utf-8', errors='ignore').split('\n') if l.strip()]
        name_to_index = {manifest_lines[i]: i + 1 for i in range(len(manifest_lines))}

        # Collect replacements
        replacements = {}
        for root, dirs, files in os.walk(patch_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, patch_dir).replace("\\", "/")
                if rel_path in name_to_index:
                    idx = name_to_index[rel_path]
                    with open(full_path, "rb") as pf:
                        replacements[idx] = pf.read()

        print(f"[+] Found {len(replacements)} files to patch in archive.")
        if len(replacements) == 0:
            print("[!] Error: No matching patch files found in patch directory.")
            sys.exit(1)

        temp_out = output_psarc_path + ".tmp"
        with open(temp_out, "wb") as f_out:
            print("[+] Compressing updated scripts and textures...")
            entry_payloads = {}
            new_zblock_list = []

            for i, entry in enumerate(entries):
                if i in replacements:
                    data = replacements[i]
                    chunks = [data[p:p+block_size] for p in range(0, len(data), block_size)] if data else [b""]
                    comp_chunks = []
                    entry_zblocks = []
                    for chunk in chunks:
                        if len(chunk) == 0:
                            comp = b""
                            zsize = 0
                        else:
                            c = zlib.compress(chunk, level=9)
                            if len(c) < len(chunk):
                                comp = c
                                zsize = len(c)
                            else:
                                comp = chunk
                                zsize = 0
                        comp_chunks.append(comp)
                        entry_zblocks.append(zsize)

                    payload = b"".join(comp_chunks)
                    entry_payloads[i] = (payload, len(data), entry_zblocks)
                else:
                    entry_payloads[i] = None

            for i, entry in enumerate(entries):
                if entry_payloads[i] is not None:
                    _, _, e_zblocks = entry_payloads[i]
                    new_zblock_list.extend(e_zblocks)
                else:
                    next_zblock = entries[i+1]["zblock_idx"] if i + 1 < num_entries else len(zblocks)
                    count = next_zblock - entry["zblock_idx"]
                    orig_blocks = zblocks[entry["zblock_idx"] : entry["zblock_idx"] + count]
                    new_zblock_list.extend(orig_blocks)

            new_toc_size = (entry_size * num_entries) + (len(new_zblock_list) * 2)

            new_header = struct.pack(">4sHH4sIIIII", magic, ver_maj, ver_min, compression_type, new_toc_size, entry_size, num_entries, block_size, flags)
            f_out.write(new_header)

            toc_placeholder_pos = f_out.tell()
            f_out.write(b"\x00" * new_toc_size)

            current_file_offset = 32 + new_toc_size
            final_entries = []
            final_zblock_counter = 0

            print("[+] Writing patched archive stream...")
            for i, entry in enumerate(entries):
                if entry_payloads[i] is not None:
                    payload, uncomp_len, e_zblocks = entry_payloads[i]
                    z_start = final_zblock_counter
                    final_zblock_counter += len(e_zblocks)

                    f_out.write(payload)
                    final_entries.append({
                        "name_hash": entry["name_hash"],
                        "zblock_idx": z_start,
                        "uncomp_size": uncomp_len,
                        "offset": current_file_offset
                    })
                    current_file_offset += len(payload)
                else:
                    next_offset = entries[i+1]["offset"] if i + 1 < num_entries else None
                    if next_offset is not None:
                        chunk_len = next_offset - entry["offset"]
                    else:
                        f_in.seek(0, os.SEEK_END)
                        chunk_len = f_in.tell() - entry["offset"]

                    f_in.seek(entry["offset"])
                    copied = 0
                    while copied < chunk_len:
                        to_read = min(2 * 1024 * 1024, chunk_len - copied)
                        buf = f_in.read(to_read)
                        f_out.write(buf)
                        copied += len(buf)

                    next_zblock = entries[i+1]["zblock_idx"] if i + 1 < num_entries else len(zblocks)
                    count = next_zblock - entry["zblock_idx"]
                    z_start = final_zblock_counter
                    final_zblock_counter += count

                    final_entries.append({
                        "name_hash": entry["name_hash"],
                        "zblock_idx": z_start,
                        "uncomp_size": entry["uncomp_size"],
                        "offset": current_file_offset
                    })
                    current_file_offset += chunk_len

            f_out.seek(toc_placeholder_pos)
            for fe in final_entries:
                e_bytes = bytearray(entry_size)
                e_bytes[:16] = fe["name_hash"]
                struct.pack_into(">I", e_bytes, 16, fe["zblock_idx"])
                e_bytes[20:25] = fe["uncomp_size"].to_bytes(5, "big")
                e_bytes[25:30] = fe["offset"].to_bytes(5, "big")
                f_out.write(e_bytes)

            zblock_bytes_out = struct.pack(f">{len(new_zblock_list)}H", *new_zblock_list)
            f_out.write(zblock_bytes_out)

    if os.path.exists(output_psarc_path):
        os.remove(output_psarc_path)
    os.rename(temp_out, output_psarc_path)

    elapsed = time.time() - t0
    final_mb = os.path.getsize(output_psarc_path) / (1024 * 1024)
    print(f"\n[+] SUCCESS! Patched archive created in {elapsed:.1f}s ({final_mb:.1f} MB)")
    print(f"[+] Output: {output_psarc_path}\n")

if __name__ == "__main__":
    patch_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patch_files")
    
    if len(sys.argv) > 1:
        in_psarc = sys.argv[1]
        out_psarc = sys.argv[2] if len(sys.argv) > 2 else "data_patched.psarc"
    else:
        in_psarc = find_data_psarc()
        if in_psarc is None:
            print("\n[!] Could not automatically find 'data.psarc' in current folder.")
            in_psarc = input("Enter path to your original data.psarc: ").strip('\"\'')
        out_psarc = "data_patched.psarc"

    patch_psarc(in_psarc, out_psarc, patch_dir)
