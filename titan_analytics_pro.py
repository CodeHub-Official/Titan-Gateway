import os
import json

def generate_full_report():
    log_path = os.path.expanduser("~/Titan-Lab/titan_deep_scraper.py_log")
    report_path = os.path.expanduser("~/Titan-Lab/FULL_MARKET_REPORT.txt")
    
    if not os.path.exists(log_path):
        print("Waiting for log file to stabilize...")
        return

    with open(log_path, 'r') as f:
        lines = f.readlines()

    with open(report_path, 'w') as out:
        out.write("CodeHub VIP: FULL MARKET ANALYSIS REPORT\n")
        out.write("="*50 + "\n\n")
        
        count = 0
        for line in lines:
            if "Reported:" in line or "GOLD FOUND" in line:
                count += 1
                clean_line = line.replace("🚀 CodeHub VIP:", "").strip()
                out.write(f"[{count}] {clean_line}\n")
                
                # Highlight critical issues for business
                if "Slow" in line:
                    out.write("   >>> BUSINESS OPPORTUNITY: Critical Speed Lag!\n")
                if "Phones:" in line and "N/A" not in line:
                    out.write("   >>> SALES LEAD: Direct Phone Line Captured.\n")
                out.write("-" * 30 + "\n")

    print(f"Analysis Complete! {count} targets processed into FULL_MARKET_REPORT.txt")

if __name__ == "__main__":
    generate_full_report()

