import re
import sys
from utils import color_text, extract_header_field

def analyze_header(header_text):
    print("\n=== Phishing Email Header Analysis ===\n")

    from_field = extract_header_field(header_text, "From")
    return_path = extract_header_field(header_text, "Return-Path")
    spf_result = re.search(r"spf=(\w+)", header_text, re.IGNORECASE)
    dkim_result = re.search(r"dkim=(\w+)", header_text, re.IGNORECASE)
    dmarc_result = re.search(r"dmarc=(\w+)", header_text, re.IGNORECASE)
    received_ips = re.findall(r"Received: from.*\[(\d+\.\d+\.\d+\.\d+)\]", header_text)

    print(f"From: {from_field}")
    print(f"Return-Path: {return_path}")

    if from_field and return_path and from_field.split('@')[-1] != return_path.split('@')[-1]:
        print(color_text("⚠️ From and Return-Path domains do not match — possible spoofing!", "yellow"))

    print("\nSPF Result:", color_text(spf_result.group(1), "green" if "pass" in spf_result.group(1).lower() else "red") if spf_result else "Not found")
    print("DKIM Result:", color_text(dkim_result.group(1), "green" if "pass" in dkim_result.group(1).lower() else "red") if dkim_result else "Not found")
    print("DMARC Result:", color_text(dmarc_result.group(1), "green" if "pass" in dmarc_result.group(1).lower() else "red") if dmarc_result else "Not found")

    print("\nEmail Hops (Received IPs):")
    for ip in received_ips:
        print(f"  ➤ {ip}")

    print("\nAnalysis complete.\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 analyzer.py <header_file.txt>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        header = f.read()
        analyze_header(header)
