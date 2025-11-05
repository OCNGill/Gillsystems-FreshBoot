# Fresh_Boot_Windows v1.0

This script is designed for **safe, non-destructive cleanup** before a reboot.  
It clears volatile trails (logs, temp, caches, DNS, clipboard, crash dumps, recent files)  
and then forces a reboot for a **fresh boot** experience.

---

## 🔐 Elevation Logic
The script checks if it’s running with admin rights.  
If not, it relaunches itself using PowerShell with `-Verb RunAs`, triggering the UAC prompt.  
This ensures full access without requiring manual right-click elevation.

---

## 🧹 Cleanup Modules

### 1. Temp Files
- `%TEMP%` and `C:\Windows\Temp`

### 2. Event Logs
- Clears all Windows Event Logs with `wevtutil cl`
- **Note**: Protected logs like `LiveId/Analytic` and `LiveId/Operational` will be silently skipped
- Error suppression added with `>nul 2>&1` for clean output

### 3. Browser Caches
- Chrome, Edge, Firefox caches wiped
- Leaves passwords and sync data intact

### 4. Clipboard
- Clears only the **active clipboard contents**
- Does not affect IDEs or Notepad++ session memory

### 5. Network
- Flush DNS (`ipconfig /flushdns`)
- Clear ARP cache (`arp -d *`)
- Stop any active `netsh trace`

### 6. Crash Dumps
- Clears `%SystemRoot%\Minidump` and `MEMORY.DMP`

### 7. Recent Files
- Clears Explorer "Recent" list

### 8. Reboot
- `shutdown /r /f /t 0` for a forced reboot
- Ensures RAM and pagefile are fresh on restart

---

## 🛡️ Safety Notes
- **Non-destructive**: No registry edits, no telemetry/service disabling, no prefetch/superfetch wipes.
- **Exclusions**: GillSystems repos, containers, and dev environments remain untouched.
- **Protected Logs**: Some system logs (LiveId) cannot be cleared even with admin rights—these are silently skipped.
- **Use Case**: Run when you want a clean slate or before handing off a machine.