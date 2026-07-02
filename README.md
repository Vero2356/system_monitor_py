# 🖥️ System Monitor CLI

A lightweight Python script that monitors system performance in real-time directly in your terminal. It tracks CPU usage, Memory (RAM), Swap, Disk usage, and general system information.

## 🚀 Features

* **Interactive Refresh Rate:** You decide how often the data updates by entering a time in seconds at startup.
* **System Info:** OS version, Node name, Processor type.
* **CPU:** Physical/Logical cores, Frequency, and Usage per core.
* **Memory:** RAM and SWAP usage.
* **Disk:** Partitions, Space usage, and Read/Write statistics.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* **Python 3.x** installed on your machine.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    ```
    *(Or download the ZIP file and extract it)*

2.  **Navigate to the project directory:**
    ```bash
    cd YOUR_REPOSITORY_NAME
    ```

3.  **Install the required library:**
    This project uses `psutil` to fetch system data. Install it via pip:
    ```bash
    pip install psutil
    ```

## ▶️ How to Run

Run the script using Python:

```bash
python main.py