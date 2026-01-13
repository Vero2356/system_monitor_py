import tkinter as tk
from tkinter import ttk
import psutil

# --- 1. Pomocné funkce (Tvoje logika) ---
def convert_size(bytes, suffix="B"):
    """Převede bajty na čitelný formát (MB, GB...)"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

# --- 2. Nastavení hlavního okna ---
root = tk.Tk()
root.title("Hardware Statistics")
root.geometry("500x600")
root.config(background="#E8ECEF") # Tvoje barva pozadí

# Styl pro Progress bary (aby vypadaly moderně)
style = ttk.Style()
style.theme_use('clam')
style.configure("blue.Horizontal.TProgressbar", foreground='#3498DB', background='#3498DB')

# --- 3. Vytvoření Layoutu (Rozložení) ---

# -- Sekce: RAM (Paměť) --
# Vytvoříme bílý rámeček (Frame) jako "kartu"
ram_frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20)
ram_frame.pack(fill="x", padx=20, pady=10) # Odsazení od krajů

tk.Label(ram_frame, text="RAM Memory Usage", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#2C3E50").pack(anchor="w")

# Label pro textové info o RAM
ram_label = tk.Label(ram_frame, text="Loading...", font=("Arial", 10), bg="#FFFFFF", fg="#555555")
ram_label.pack(anchor="w", pady=5)

# Progress bar pro RAM
ram_bar = ttk.Progressbar(ram_frame, style="blue.Horizontal.TProgressbar", orient="horizontal", length=400, mode="determinate")
ram_bar.pack(fill="x", pady=5)


# -- Sekce: CPU (Procesor) --
cpu_frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20)
cpu_frame.pack(fill="both", expand=True, padx=20, pady=10)

tk.Label(cpu_frame, text="CPU Usage per Core", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#2C3E50").pack(anchor="w", pady=(0, 10))

# Kontejner pro jádra (aby se hezky seřadila)
cores_container = tk.Frame(cpu_frame, bg="#FFFFFF")
cores_container.pack(fill="both", expand=True)

# Seznam pro uložení referencí na widgety jader (abychom je mohli aktualizovat)
cpu_widgets = []

def create_cpu_bars():
    """Vytvoří progress bary pro každé jádro dynamicky"""
    cpu_count = psutil.cpu_count(logical=True)
    
    for i in range(cpu_count):
        # Řádek pro jedno jádro
        row = tk.Frame(cores_container, bg="#FFFFFF")
        row.pack(fill="x", pady=2)
        
        # Text "Core X"
        lbl = tk.Label(row, text=f"Core {i}", width=8, anchor="w", bg="#FFFFFF", font=("Arial", 9))
        lbl.pack(side="left")
        
        # Progress bar
        bar = ttk.Progressbar(row, style="blue.Horizontal.TProgressbar", orient="horizontal", length=100, mode="determinate")
        bar.pack(side="left", fill="x", expand=True, padx=10)
        
        # Procenta textem
        perc_lbl = tk.Label(row, text="0%", width=5, anchor="e", bg="#FFFFFF", font=("Arial", 9))
        perc_lbl.pack(side="right")
        
        # Uložíme si bar a label do seznamu
        cpu_widgets.append((bar, perc_lbl))

create_cpu_bars()

# --- 4. Funkce pro aktualizaci dat (The Loop) ---
def update_stats():
    # 1. Aktualizace RAM
    mem = psutil.virtual_memory()
    ram_text = f"Used: {convert_size(mem.used)} / Total: {convert_size(mem.total)} ({mem.percent}%)"
    ram_label.config(text=ram_text)
    ram_bar['value'] = mem.percent # Nastaví délku baru

    # 2. Aktualizace CPU
    # cpu_percent(percpu=True) vrací seznam procent pro každé jádro
    cpu_usage = psutil.cpu_percent(percpu=True)
    
    for i, percentage in enumerate(cpu_usage):
        if i < len(cpu_widgets):
            bar, lbl = cpu_widgets[i]
            bar['value'] = percentage
            lbl.config(text=f"{percentage}%")

    # Spustí tuto funkci znovu za 1000 milisekund (1 sekunda)
    root.after(1000, update_stats)

# --- Spuštění ---
# První volání aktualizace
update_stats()

root.mainloop()