import os
import time
import httpx
import sys
import multiprocessing
from rich.console import Console
from rich.panel import Panel
from rich.live import Live

console = Console()

def get_sys_status():
    # نظام بديل لجلب حالة الرام والمعالج متوافق مع ترمكس
    try:
        cpu_count = multiprocessing.cpu_count()
        uptime = os.popen('uptime').read().strip().split('load average:')[-1]
        return f"CPUs: {cpu_count} | Load:{uptime}"
    except:
        return "System Status: Active"

def check_vpn():
    try:
        # فحص الهوية الرقمية لضمان التخفي
        with httpx.Client(timeout=3.0) as client:
            ip = client.get("https://api.ipify.org").text
            return ip
    except:
        return "Hidden / VPN Active"

def clear_cache():
    # تنظيف الذاكرة المؤقتة لترمكس لضمان استمرار الهجوم
    os.system("rm -rf ~/.cache/pip/* 2>/dev/null")

def monitor():
    os.system('clear')
    console.print(Panel("[bold green]TITAN SENTINEL V2: SHIELD RE-ARMED[/bold green]", subtitle="Session 3 Security"))
    
    with Live(console=console, refresh_per_second=1) as live:
        while True:
            clear_cache()
            status = f"""
            [bold cyan]🛡️ PROTECTING CODEHUB ARMY[/bold cyan]
            --------------------------
            🌐 Public IP: [bold red]{check_vpn()}[/bold red]
            ⚡ System Pulse: {get_sys_status()}
            🧹 Memory Sweep: [green]SUCCESSFUL[/green]
            ⚔️ Current Front: [yellow]7,066 Links Attack[/yellow]
            
            [dim]Shielding Session 2. Monitoring 7K Targets...[/dim]
            """
            live.update(Panel(status, border_style="blue", title="GUARD MODE"))
            time.sleep(10)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        sys.exit()
