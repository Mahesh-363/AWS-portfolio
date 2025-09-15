#!/bin/bash
# Linux Server Management Script
# Monitors system, cleans disk, and provides a snapshot of health

echo "=== LINUX SERVER MANAGEMENT SCRIPT ==="
echo "Date & Time: $(date)"
echo

# 1️⃣ Check top processes
echo "Top 5 processes by CPU usage:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6
echo
echo "Top 5 processes by Memory usage:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6
echo

# 2️⃣ Disk usage
echo "Disk usage:"
df -h
echo

# 3️⃣ Firewall status
echo "Firewall status:"
sudo ufw status
echo

# 4️⃣ Clean Snap old revisions
echo "Cleaning old Snap revisions..."
OLD_SNAPS=$(snap list --all | awk '/disabled/{print $1" --revision "$3}')
for snap_rev in $OLD_SNAPS; do
    sudo snap remove $snap_rev
done
echo "Snap cleanup completed."
echo

# 5️⃣ Clean apt cache and remove unused packages
echo "Cleaning apt cache and unused packages..."
sudo apt clean
sudo apt autoremove -y
echo "Apt cleanup completed."
echo

# 6️⃣ Vacuum system logs (keep max 500MB)
echo "Cleaning old system logs..."
sudo journalctl --vacuum-size=500M
echo "Log cleanup completed."
echo

# 7️⃣ Show disk usage after cleanup
echo "Disk usage after cleanup:"
df -h
echo

echo "=== SCRIPT COMPLETED SUCCESSFULLY ==="
