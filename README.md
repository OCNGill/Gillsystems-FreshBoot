# Fresh_Boot_Windows v1.0

**Fresh_Boot_Windows** is a safe, non-destructive cleanup utility for Windows.  
It clears volatile trails (logs, temp files, caches, DNS, clipboard, crash dumps, recent files)  
and then forces a reboot for a **fresh boot** experience.

---

## ✨ Features
- Automated elevation with UAC prompt
- Cleans temp directories and browser caches
- Flushes DNS and clears ARP cache
- Clears clipboard and recent file history
- Removes crash dumps
- Resets Windows Event Logs (protected logs skipped silently)
- Forces a reboot for a clean slate

---

## 🛡️ Safety
- **Non-destructive**: No registry edits, no telemetry/service disabling, no prefetch/superfetch wipes.
- **Exclusions**: Development repos, containers, and environments remain untouched.
- **Protected Logs**: Some system logs (e.g., LiveId) cannot be cleared even with admin rights—these are skipped automatically.

---

## 🚀 Usage
1. Download `Fresh_Boot_Windows.bat`
2. Run as Administrator (UAC prompt will appear if needed)
3. System will reboot automatically after cleanup

---

## 👨‍💻 Author
Developed by **Stephen Gill**  
Crafted to demonstrate professional scripting practices and reproducibility.

---

## 💖 Support / Donate

If you find this project helpful, you can support ongoing work — thank you!

<p align="center">
	<img src="qr-paypal.png" alt="PayPal QR code" width="180" style="margin:8px;">
	<img src="qr-venmo.png" alt="Venmo QR code" width="180" style="margin:8px;">
</p>

**Scan to donate:**

- PayPal: [![Donate via PayPal](https://img.shields.io/badge/PayPal-Donate-009cde?logo=paypal&logoColor=white)](https://paypal.me/gillsystems)
- Venmo (US/mobile): [![Donate via Venmo](https://img.shields.io/badge/Venmo-Donate-3d95ce?logo=venmo&logoColor=white)](https://venmo.com/Stephen-Gill-007)

Short links:
- https://paypal.me/gillsystems
- https://venmo.com/Stephen-Gill-007
