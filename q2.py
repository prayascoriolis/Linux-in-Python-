'''
Assignment 2: Disk and Partition Manager
Description: Develop a Python program to display and manage disk partitions.
Requirements:

    Use the os and shutil modules to display available disks and partitions.
    Integrate psutil to fetch details such as:
        Total space, used space, and free space.
        Mount points.
        File system type.
    Allow users to mount or unmount devices using system commands (subprocess).
    Provide a feature to format a device to a specified file system (e.g., ext4, xfs).
'''

import psutil
import subprocess

def display_disk_info():
    '''
    Disk Partition Menu
    '''
    # Return all mounted disk partitions as a list of named tuples including device,
    # mount point and filesystem type.
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Partition: {partition.device} ===")
        try:
            total, used, free, percent = psutil.disk_usage(partition.mountpoint)
            print(f"Mountpoint: {partition.mountpoint}")
            print(f"Total: {total / (1024**3):.2f} GB")
            print(f"Used:  {used / (1024**3):.2f} GB")
            print(f"Free:  {free / (1024**3):.2f} GB")
            print(f"Percent Used:  {percent:.2f} %")
            print(f"File type:  {partition.fstype}\n")
        except PermissionError:
            print("Access Denied\n")

def mount_device(device, mountpoint):
    '''mounting'''

def unmount_device(device):
    '''unmounting'''

def format_device(device, filesystem):
    ''' change format of a disk'''

if __name__ == "__main__":
    while True:
        print("\nDisk Management Menu:")
        print("1. Display Disk Info")
        print("2. Mount a Device")
        print("3. Unmount a Device")
        print("4. Format a Device")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_disk_info()
        elif choice == "2":
            device = input("Enter the device path (in /dev/): ").strip()
            mountpoint = input("Enter the mountpoint (in /mnt/): ").strip()
            mount_device(device, mountpoint)
        elif choice == "3":
            device = input("Enter the device path to unmount (e.g., /dev/sdb1): ").strip()
            unmount_device(device)
        elif choice == "4":
            device = input("Enter the device path to format (in /dev/): ").strip()
            filesystem = input("Enter filesystem type (ext4, xfs etc): ").strip()
            format_device(device, filesystem)
        elif choice == "5":
            print("Exiting Disk Management.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
