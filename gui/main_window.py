import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from threading import Thread
from ips.network_monitor import capture_traffic
from ips.alerting import send_alert
from ips.prevention import block_ip
from ai.model import AIModel

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced IPS System")
        self.geometry("1000x700")
        self.is_monitoring = False
        self.model = AIModel('ai/example_model.pkl')
        
        self.setup_ui()
        
    def setup_ui(self):
        self.start_button = tk.Button(self, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(self, text="Stop Monitoring", command=self.stop_monitoring, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.log_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=20)
        self.log_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def start_monitoring(self):
        self.is_monitoring = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, "Monitoring started...\n")
        self.monitor_thread = Thread(target=self.monitor_traffic)
        self.monitor_thread.start()
        
    def stop_monitoring(self):
        self.is_monitoring = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.log_area.insert(tk.END, "Monitoring stopped.\n")
        
    def monitor_traffic(self):
        def process_packet(packet):
            if self.is_monitoring:
                ip_src = packet[scapy.IP].src
                ip_dst = packet[scapy.IP].dst
                data = np.array([ip_src, ip_dst]).reshape(1, -1)
                prediction = self.model.predict(data)
                if prediction == 1:  # Example condition for alert
                    self.log_area.insert(tk.END, f"Suspicious activity detected from {ip_src}\n")
                    send_alert(f"Suspicious activity detected from {ip_src}")
                    block_ip(ip_src)
                    
        capture_traffic(process_packet)
        
    def on_closing(self):
        if self.is_monitoring:
            self.stop_monitoring()
        self.destroy()
