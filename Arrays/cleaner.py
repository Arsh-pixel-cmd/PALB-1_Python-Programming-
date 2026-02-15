import os
import threading
import multiprocessing as mp
import psutil
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from collections import defaultdict
import matplotlib.pyplot as plt
import squarify
import csv
MIN_SIZE_MB = 50
JUNK_EXTENSIONS = (".tmp", ".log", ".cache", ".old")
JUNK_KEYWORDS = ("temp", "cache", "crashdumps")
def scan_worker(args):
    path, min_size = args
    try:
        size = os.path.getsize(path)
        if size < min_size:
            return None
        lower = path.lower()
        is_junk = lower.endswith(JUNK_EXTENSIONS) or any(k in lower for k in JUNK_KEYWORDS)
        return (path, size, is_junk)
    except:
        return None
def get_drives():
    return [p.mountpoint for p in psutil.disk_partitions() if os.path.exists(p.mountpoint)]
def size_mb(size):
    return round(size / 1024 / 1024, 2)
def size_gb(size):
    return round(size / 1024 / 1024 / 1024, 2)
class DiskCleanerApp:
    def _init_(self, root):
        self.root = root
        root.title("Disk Cleaner Pro (Safe Mode)")
        root.geometry("1200x650")
        self.files = []
        self.folder_sizes = defaultdict(int)
        self.total_files = 0
        self.processed_files = 0
        self.progress_win = None
        self.progress_bar = None
        self.progress_label = None
        self.build_ui()
    def build_ui(self):
        top = ttk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=5)
        ttk.Label(top, text="Drive:").pack(side="left")
        self.drive_box = ttk.Combobox(top, values=get_drives(), width=10)
        self.drive_box.pack(side="left", padx=5)
        ttk.Button(top, text="Scan", command=self.start_scan).pack(side="left", padx=5)
        ttk.Button(top, text="TreeMap", command=self.show_treemap).pack(side="left", padx=5)
        ttk.Button(top, text="Folder Summary", command=self.show_folder_summary).pack(side="left", padx=5)
        ttk.Button(top, text="Export Delete Commands", command=self.export_delete).pack(side="right")
        self.tree = ttk.Treeview(
            self.root,
            columns=("check", "size_mb", "size_gb", "junk", "path"),
            show="headings"
        )
        self.tree.heading("check", text="✔")
        self.tree.heading("size_mb", text="Size (MB)")
        self.tree.heading("size_gb", text="Size (GB)")
        self.tree.heading("junk", text="Junk")
        self.tree.heading("path", text="Path")
        self.tree.column("check", width=40, anchor="center")
        self.tree.column("size_mb", width=90)
        self.tree.column("size_gb", width=90)
        self.tree.column("junk", width=60)
        self.tree.column("path", width=750)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<Button-1>", self.toggle_check)
    def toggle_check(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return
        col = self.tree.identify_column(event.x)
        if col != "#1":
            return
        row = self.tree.identify_row(event.y)
        if not row:
            return
        current = self.tree.set(row, "check")
        self.tree.set(row, "check", "" if current == "✔" else "✔")
    def show_progress_window(self):
        self.progress_win = Toplevel(self.root)
        self.progress_win.title("Scanning...")
        self.progress_win.geometry("420x130")
        self.progress_win.resizable(False, False)
        ttk.Label(self.progress_win, text="Scanning files, please wait...").pack(pady=5)
        self.progress_bar = ttk.Progressbar(
            self.progress_win,
            orient="horizontal",
            length=380,
            mode="determinate"
        )
        self.progress_bar.pack(pady=5)
        self.progress_label = ttk.Label(self.progress_win, text="Starting...")
        self.progress_label.pack()
    def start_scan(self):
        drive = self.drive_box.get()
        if not drive:
            messagebox.showerror("Error", "Select a drive")
            return
        self.tree.delete(*self.tree.get_children())
        self.files.clear()
        self.folder_sizes.clear()
        self.total_files = 0
        self.processed_files = 0
        self.show_progress_window()
        threading.Thread(target=self.scan_drive, daemon=True).start()
        self.root.after(200, self.update_progress)
    def scan_drive(self):
        drive = self.drive_box.get()
        min_size = MIN_SIZE_MB * 1024 * 1024
        all_paths = []
        for root, _, files in os.walk(drive):
            for f in files:
                all_paths.append(os.path.join(root, f))
        self.total_files = len(all_paths)
        pool = mp.Pool(mp.cpu_count())
        results = pool.imap_unordered(
            scan_worker,
            ((p, min_size) for p in all_paths)
        )
        for r in results:
            self.processed_files += 1
            if r:
                path, size, junk = r
                self.files.append(r)
                self.folder_sizes[os.path.dirname(path)] += size
        pool.close()
        pool.join()
        self.root.after(0, self.finish_scan)
    def update_progress(self):
        if not self.progress_win:
            return
        if self.total_files > 0:
            percent = (self.processed_files / self.total_files) * 100
            self.progress_bar["value"] = percent
            self.progress_label.config(
                text=f"Processed {self.processed_files} / {self.total_files} files"
            )
        if self.processed_files < self.total_files:
            self.root.after(200, self.update_progress)
    def finish_scan(self):
        if self.progress_win:
            self.progress_win.destroy()
            self.progress_win = None
        self.populate_table()
        self.export_folder_summary_csv()
    def populate_table(self):
        self.files.sort(key=lambda x: x[1], reverse=True)
        for path, size, junk in self.files:
            self.tree.insert(
                "",
                "end",
                values=(
                    "",
                    size_mb(size),
                    size_gb(size),
                    "YES" if junk else "NO",
                    path
                )
            )
    def export_delete(self):
        cmds = []
        for row in self.tree.get_children():
            if self.tree.set(row, "check") == "✔":
                path = self.tree.set(row, "path")
                cmds.append(f'del "{path}"')
        if not cmds:
            messagebox.showinfo("Info", "No files selected")
            return
        with open("safe_delete_commands.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(cmds))
        messagebox.showinfo("Done", "safe_delete_commands.txt generated")
    def show_folder_summary(self):
        if not self.folder_sizes:
            messagebox.showinfo("Info", "Scan first")
            return
        win = Toplevel(self.root)
        win.title("Folder Size Summary")
        win.geometry("900x500")
        tree = ttk.Treeview(
            win,
            columns=("mb", "gb", "path"),
            show="headings"
        )
        tree.heading("mb", text="Total Size (MB)")
        tree.heading("gb", text="Total Size (GB)")
        tree.heading("path", text="Folder Path")
        tree.column("mb", width=120)
        tree.column("gb", width=120)
        tree.column("path", width=650)
        tree.pack(fill="both", expand=True)
        for folder, size in sorted(self.folder_sizes.items(), key=lambda x: x[1], reverse=True):
            tree.insert("", "end", values=(size_mb(size), size_gb(size), folder))
    def export_folder_summary_csv(self):
        with open("folder_sizes.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Folder Path", "Total Size (MB)", "Total Size (GB)"])
            for folder, size in sorted(self.folder_sizes.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([folder, size_mb(size), size_gb(size)])
    def show_treemap(self):
        if not self.folder_sizes:
            messagebox.showinfo("Info", "Scan first")
            return

        top = sorted(self.folder_sizes.items(), key=lambda x: x[1], reverse=True)[:30]
        labels = [f"{os.path.basename(k) or k}\n{size_gb(v)} GB" for k, v in top]
        sizes = [v for _, v in top]

        plt.figure(figsize=(12, 8))
        squarify.plot(sizes=sizes, label=labels, pad=True)
        plt.axis("off")
        plt.title("Disk Usage TreeMap")
        plt.show()


# ---------- ENTRY ----------
if _name_ == "_main_":
    mp.freeze_support()  # REQUIRED ON WINDOWS
    root = tk.Tk()
    DiskCleanerApp(root)
    root.mainloop()