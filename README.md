# 🖥️ Lightweight Python System Monitor

A simple, dependency-light terminal dashboard for monitoring system performance. It tracks CPU, RAM, GPU, and high-resource processes in real-time using standard Python output.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6)

## ✨ Features

* **Real-Time Monitoring:** Updates system stats every second.
* **Universal GPU Support:** Works with NVIDIA, AMD, and Intel Integrated Graphics (via LibreHardwareMonitor).
* **Lightweight:** Uses standard text formatting instead of heavy UI libraries.
* **Process Tracking:** Lists the top 5 processes consuming the most CPU.

## 🛠️ Prerequisites

* Python 3.8 or higher.
* **Administrator Privileges:** You must run your terminal as **Administrator** to access GPU hardware sensors.

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
