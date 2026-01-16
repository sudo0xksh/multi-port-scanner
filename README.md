# 🔌🔥 Multi Port Scanner 🔥🔌

Multi Port Scanner is a simple Python CLI tool that checks whether a specific port
is open or closed on one or multiple targets using raw sockets 🧠⚙️

No Nmap.  
No fancy flags.  
Just direct TCP reality.

---

## 👀 Overview

Sometimes you don’t want a full scan.
Sometimes you just want to know one thing:

Is this port open or not? 🤨

Multi Port Scanner does exactly that.
You give it an IP (or a list of IPs) and a port,
and it tells you the truth — quickly and clearly.

---

## 🚀 Features

- Scans a single IP address 🌐  
- Supports multiple IPs using a .txt file 📂  
- Checks one specific port at a time 🔌  
- Uses TCP socket connection for accuracy ⚙️  
- Clear OPEN / CLOSED output 🟢🔴  
- Lightweight and fast ⚡  

---

## ⚙️ How It Works

The tool creates a TCP socket connection to the given IP and port.
If the connection succeeds, the port is OPEN.
If it fails, the port is CLOSED.

No guessing.
No assumptions.
Just network behavior.

---

## 🧪 Usage

To scan a single IP address, run  
python port_scan.py 192.168.1.1 -p 80

To scan multiple IPs, create a file like this  
targets.txt  
192.168.1.1  
10.0.0.5  
example.com  

Then run  
python port_scan.py targets.txt -p 22

The scanner will check the same port on every target.

---

## 📤 Example Output

[OPEN ] 192.168.1.1:22  
[CLOSED] 10.0.0.5:22  
[OPEN ] example.com:22  

Simple. Clear. No noise.

---

## 📦 Requirements

- Python 3.x  
- Internet or network access  
- No external libraries required  

Sockets do all the work.

---

## 🧠 What You Learn From This Project

- TCP socket programming basics  
- How port scanning actually works  
- Difference between open and closed ports  
- Handling single vs multiple targets  
- Why scanners don’t need magic — just logic  

---

## 🗿 Final Words

Big tools scan everything.
Smart tools check what matters.

If you understand how this works,
you understand the foundation of port scanning 🔥
