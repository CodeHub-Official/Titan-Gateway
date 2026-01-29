import os

paths = [
    '~/Titan-Lab/Empire_Archive/Egypt/Real_Estate',
    '~/Titan-Lab/Empire_Archive/UAE/Real_Estate',
    '~/Titan-Lab/Empire_Archive/KSA/Real_Estate'
]

with open('REAL_ESTATE_AUCTION.txt', 'w') as out:
    out.write("--- TITAN REAL ESTATE AUCTION LIST (CONFIDENTIAL) ---\n\n")
    for p in paths:
        full_p = os.path.expanduser(p)
        if os.path.exists(full_p):
            for file in os.listdir(full_p):
                with open(os.path.join(full_p, file), 'r', errors='ignore') as f:
                    out.write(f"--- SOURCE: {p}/{file} ---\n")
                    out.write(f.read())
                    out.write("\n\n")

print("\033[1;32m[✅] REAL ESTATE LIST SECURED IN: REAL_ESTATE_AUCTION.txt\033[0m")
