# system_monitor_py
# 🖥️ Python Real-Time System Monitor

A lightweight, terminal-based system monitoring dashboard built with Python. It provides real-time tracking of CPU, RAM, GPU, and high-performance processes using a beautiful Terminal User Interface (TUI).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6)

## ✨ Features

* **Real-Time Dashboard:** Updates system stats every second without flickering.
* **Universal GPU Support:** Supports NVIDIA, AMD, and Intel Integrated Graphics (via LibreHardwareMonitor).
* **Process Tracking:** Identifies the top resource-consuming processes (sorted by CPU usage).
* **Beautiful UI:** Built using the [Rich](https://github.com/Textualize/rich) library for easy-to-read tables and panels.

## 🛠️ Prerequisites

* Python 3.8 or higher
* **Administrator Privileges:** You must run your terminal as Administrator to access low-level hardware sensors (GPU Temps/Load).

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/system-monitor.git](https://github.com/yourusername/system-monitor.git)
    cd system-monitor
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

**Important:** Open your Command Prompt, PowerShell, or Terminal as **Administrator**.

```bash
python monitor.py
