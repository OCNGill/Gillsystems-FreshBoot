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
Developed by **Stephen Gill** with Copilot assistance.  
Crafted to demonstrate professional scripting practices and reproducibility.
