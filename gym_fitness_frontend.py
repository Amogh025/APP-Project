import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass


BG = "#F4F7FB"
NAVY = "#11263D"
NAVY_2 = "#1B3854"
TEAL = "#008F88"
ORANGE = "#D97706"
TEXT = "#17212B"
MUTED = "#526170"
WHITE = "#FFFFFF"
LINE = "#DDE4EC"


class GymApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FitCore | Gym & Fitness Membership Management")
        self.geometry("1240x760")
        self.minsize(1060, 650)
        self.option_add("*Font", "Arial 10")
        self.configure(bg=BG)
        self.active_page = "Dashboard"
        self.members = [
            ["M-1001", "Aarav Sharma", "Premium", "Active", "14 Nov 2026"],
            ["M-1002", "Priya Nair", "Gold", "Active", "30 Nov 2026"],
            ["M-1003", "Rohan Mehta", "Basic", "Expiring", "20 Nov 2026"],
            ["M-1004", "Kavya Iyer", "Premium", "Active", "07 Dec 2026"],
        ]
        self.attendance = []
        self._styles()
        self._build_shell()
        self.show_page("Dashboard")

    def _styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", background=WHITE, fieldbackground=WHITE,
                        foreground="#000000", rowheight=38, font=("Arial", 10), borderwidth=0)
        style.configure("Treeview.Heading", background="#EAF0F6", foreground="#17212B",
                        font=("Arial", 10, "bold"), relief="flat")
        style.map("Treeview", background=[("selected", "#D8F0EE")], foreground=[("selected", "#17212B")])
        style.configure("TCombobox", padding=7, font=("Arial", 10), foreground="#000000")

    def _build_shell(self):
        self.sidebar = tk.Frame(self, bg=NAVY, width=232)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        tk.Label(self.sidebar, text="FITCORE", bg=NAVY, fg=WHITE,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w", padx=27, pady=(32, 0))
        tk.Label(self.sidebar, text="FITNESS MANAGEMENT", bg=NAVY, fg="#A9C1D2",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=29, pady=(0, 31))

        self.nav_buttons = {}
        nav = [("Dashboard", "⌂"), ("Members", "♙"), ("Trainers", "★"),
               ("Memberships", "◇"), ("Settings", "⚙")]
        for name, icon in nav:
            b = tk.Button(self.sidebar, text=f"  {icon}    {name}", anchor="w", bd=0,
                          bg=NAVY, fg="#C8D8E5", activebackground=NAVY_2,
                          activeforeground=WHITE, font=("Arial", 11, "bold"), padx=26, pady=12,
                          command=lambda p=name: self.show_page(p))
            b.pack(fill="x", pady=1)
            self.nav_buttons[name] = b
        tk.Frame(self.sidebar, bg="#2F4B63", height=1).pack(fill="x", padx=22, pady=(30, 15))
        tk.Label(self.sidebar, text="●  System Online", bg=NAVY, fg="#6EE7B7",
                 font=("Segoe UI", 9)).pack(anchor="w", padx=28)

        self.main = tk.Frame(self, bg=BG)
        self.main.pack(side="left", fill="both", expand=True)
        self.topbar = tk.Frame(self.main, bg=WHITE, height=78)
        self.topbar.pack(fill="x")
        self.topbar.pack_propagate(False)
        self.title_var = tk.StringVar()
        tk.Label(self.topbar, textvariable=self.title_var, bg=WHITE, fg=NAVY,
                 font=("Arial", 21, "bold")).pack(side="left", padx=34, pady=18)
        right = tk.Frame(self.topbar, bg=WHITE)
        right.pack(side="right", padx=33)
        tk.Label(right, text="Monday, 16 November 2026", bg=WHITE, fg=MUTED,
                 font=("Arial", 10, "bold")).pack(side="left", padx=(0, 23))
        tk.Label(right, text="AS", bg=TEAL, fg=WHITE, width=3, height=1,
                 font=("Arial", 11, "bold")).pack(side="left")
        self.content = tk.Frame(self.main, bg=BG)
        self.content.pack(fill="both", expand=True)

    def show_page(self, name):
        self.active_page = name
        self.title_var.set(name)
        for item, button in self.nav_buttons.items():
            button.configure(bg=TEAL if item == name else NAVY,
                             fg=WHITE if item == name else "#C8D8E5")
        for child in self.content.winfo_children():
            child.destroy()
        getattr(self, f"page_{name.lower()}")()

    def card(self, parent, title, value, note, accent):
        f = tk.Frame(parent, bg=WHITE, highlightbackground=LINE, highlightthickness=1)
        tk.Frame(f, bg=accent, width=5).pack(side="left", fill="y")
        inner = tk.Frame(f, bg=WHITE)
        inner.pack(side="left", fill="both", expand=True, padx=18, pady=15)
        tk.Label(inner, text=title.upper(), bg=WHITE, fg=MUTED, font=("Arial", 9, "bold")).pack(anchor="w")
        tk.Label(inner, text=value, bg=WHITE, fg=NAVY, font=("Arial", 23, "bold")).pack(anchor="w", pady=(4, 1))
        tk.Label(inner, text=note, bg=WHITE, fg=accent, font=("Arial", 10, "bold")).pack(anchor="w")
        return f

    def section_header(self, parent, title, subtitle=""):
        f = tk.Frame(parent, bg=BG)
        tk.Label(f, text=title, bg=BG, fg=NAVY, font=("Arial", 15, "bold")).pack(anchor="w")
        if subtitle:
            tk.Label(f, text=subtitle, bg=BG, fg=MUTED, font=("Arial", 10)).pack(anchor="w", pady=(2, 0))
        return f

    def button(self, parent, text, command=None, filled=True):
        return tk.Button(parent, text=text, command=command, bd=0, padx=15, pady=8,
                         bg=TEAL if filled else WHITE, fg=WHITE if filled else TEAL,
                         activebackground="#00766F", activeforeground=WHITE,
                         font=("Arial", 10, "bold"), cursor="hand2")

    def page_dashboard(self):
        wrap = tk.Frame(self.content, bg=BG)
        wrap.pack(fill="both", expand=True, padx=32, pady=25)
        h = tk.Frame(wrap, bg=BG); h.pack(fill="x", pady=(0, 20))
        self.section_header(h, "Welcome back, Admin", "Here is what is happening at FitCore today.").pack(side="left")
        self.button(h, "+ Add Member", self.open_member_form).pack(side="right")
        cards = tk.Frame(wrap, bg=BG); cards.pack(fill="x")
        metrics = [("Total Members", str(len(self.members)), "+12 this month", TEAL),
                   ("Active Memberships", "186", "92% of members", "#3563B8"),
                   ("Today's Check-ins", "64", "+18% vs yesterday", ORANGE),
                   ("Monthly Revenue", "₹1,84,500", "+8.4% this month", "#8756C5")]
        for i, data in enumerate(metrics):
            c = self.card(cards, *data); c.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 12, 0))
            cards.columnconfigure(i, weight=1)
        bottom = tk.Frame(wrap, bg=BG); bottom.pack(fill="both", expand=True, pady=(25, 0))
        left = tk.Frame(bottom, bg=WHITE, highlightbackground=LINE, highlightthickness=1)
        left.pack(side="left", fill="both", expand=True, padx=(0, 14))
        tk.Label(left, text="Membership Overview", bg=WHITE, fg=NAVY, font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=20, pady=(18, 3))
        tk.Label(left, text="Active members by plan", bg=WHITE, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", padx=20)
        chart = tk.Frame(left, bg=WHITE); chart.pack(fill="both", expand=True, padx=25, pady=20)
        plans = [("Premium", 78, TEAL), ("Gold", 61, "#3563B8"), ("Basic", 47, ORANGE)]
        for label, count, color in plans:
            row = tk.Frame(chart, bg=WHITE); row.pack(fill="x", pady=13)
            tk.Label(row, text=label, width=10, anchor="w", bg=WHITE, fg=TEXT, font=("Segoe UI", 10)).pack(side="left")
            track = tk.Frame(row, bg="#E7EDF4", height=12); track.pack(side="left", fill="x", expand=True, padx=8); track.pack_propagate(False)
            tk.Frame(track, bg=color, width=int(count * 3.5), height=12).pack(side="left")
            tk.Label(row, text=str(count), width=4, bg=WHITE, fg=MUTED, font=("Segoe UI", 10, "bold")).pack(side="right")
        right = tk.Frame(bottom, bg=WHITE, width=300, highlightbackground=LINE, highlightthickness=1)
        right.pack(side="right", fill="y"); right.pack_propagate(False)
        tk.Label(right, text="Recent Activity", bg=WHITE, fg=NAVY, font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=20, pady=(18, 12))
        for text, stamp, color in [("Aarav Sharma checked in", "10:24 AM", TEAL), ("New payment received", "09:46 AM", "#3563B8"), ("Rohan's plan expires soon", "09:12 AM", ORANGE), ("Kavya joined Premium", "Yesterday", "#8756C5")]:
            r = tk.Frame(right, bg=WHITE); r.pack(fill="x", padx=20, pady=9)
            tk.Label(r, text="●", bg=WHITE, fg=color, font=("Segoe UI", 10)).pack(side="left")
            tx = tk.Frame(r, bg=WHITE); tx.pack(side="left", padx=8)
            tk.Label(tx, text=text, bg=WHITE, fg=TEXT, font=("Segoe UI", 9)).pack(anchor="w")
            tk.Label(tx, text=stamp, bg=WHITE, fg=MUTED, font=("Segoe UI", 8)).pack(anchor="w")

    def page_members(self):
        self.member_table_page("Members", "Manage profiles, plans, and member status", self.members, ["Member ID", "Name", "Plan", "Status", "Expiry"])

    def member_table_page(self, heading, sub, rows, cols):
        wrap = tk.Frame(self.content, bg=BG); wrap.pack(fill="both", expand=True, padx=32, pady=25)
        h = tk.Frame(wrap, bg=BG); h.pack(fill="x", pady=(0, 20))
        self.section_header(h, heading, sub).pack(side="left")
        self.button(h, "+ Add Member", self.open_member_form).pack(side="right")
        search = tk.Entry(wrap, font=("Segoe UI", 10), bd=0, bg=WHITE, fg=TEXT, highlightbackground=LINE, highlightthickness=1)
        search.insert(0, "Search members by name or ID...")
        search.pack(fill="x", ipady=9, pady=(0, 15))
        box = tk.Frame(wrap, bg=WHITE, highlightbackground=LINE, highlightthickness=1); box.pack(fill="both", expand=True)
        tree = ttk.Treeview(box, columns=cols, show="headings")
        for col in cols: tree.heading(col, text=col); tree.column(col, width=140, anchor="w")
        for row in rows: tree.insert("", "end", values=row)
        tree.pack(fill="both", expand=True, padx=1, pady=1)
        foot = tk.Frame(wrap, bg=BG); foot.pack(fill="x", pady=14)
        tk.Label(foot, text=f"Showing {len(rows)} members (demo data)", bg=BG, fg=MUTED, font=("Segoe UI", 9)).pack(side="left")
        self.button(foot, "View profile", lambda: self.info("Member profile", "Select a member in a full version to view their complete profile."), False).pack(side="right")

    def page_memberships(self):
        wrap = tk.Frame(self.content, bg=BG); wrap.pack(fill="both", expand=True, padx=32, pady=25)
        h = tk.Frame(wrap, bg=BG); h.pack(fill="x", pady=(0, 18))
        self.section_header(h, "Membership Plans", "Configure plans and compare active subscriptions").pack(side="left")
        self.button(h, "+ Create Plan", lambda: self.info("Create plan", "This front-end prototype would open a plan editor here.")).pack(side="right")
        cards = tk.Frame(wrap, bg=BG); cards.pack(fill="x")
        for i, (name, price, color, features) in enumerate([( "Basic", "₹999 / month", ORANGE, ["Gym floor access", "Standard equipment", "Locker access"]), ("Gold", "₹1,499 / month", "#3563B8", ["Everything in Basic", "Group classes", "2 guest passes"]), ("Premium", "₹2,199 / month", TEAL, ["Everything in Gold", "Personal trainer", "Nutrition review"]) ]):
            card = tk.Frame(cards, bg=WHITE, highlightbackground=LINE, highlightthickness=1); card.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 14, 0)); cards.columnconfigure(i, weight=1)
            tk.Frame(card, bg=color, height=6).pack(fill="x")
            tk.Label(card, text=name, bg=WHITE, fg=NAVY, font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=22, pady=(21, 3))
            tk.Label(card, text=price, bg=WHITE, fg=color, font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=22)
            tk.Frame(card, bg=LINE, height=1).pack(fill="x", padx=22, pady=18)
            for feature in features: tk.Label(card, text=f"✓  {feature}", bg=WHITE, fg=TEXT, font=("Segoe UI", 9)).pack(anchor="w", padx=22, pady=5)
            self.button(card, "Edit plan", lambda n=name: self.info("Plan selected", f"{n} plan editor opened (demo)."), False).pack(anchor="w", padx=22, pady=22)

    def page_attendance(self):
        wrap = tk.Frame(self.content, bg=BG); wrap.pack(fill="both", expand=True, padx=32, pady=25)
        h = tk.Frame(wrap, bg=BG); h.pack(fill="x", pady=(0, 20))
        self.section_header(h, "Attendance", "Track member check-ins for today").pack(side="left")
        self.button(h, "✓  Record Check-in", self.open_checkin).pack(side="right")
        total = self.card(wrap, "Today's Check-ins", str(64 + len(self.attendance)), "Live session count", TEAL); total.pack(fill="x", pady=(0, 20))
        rows = self.attendance or [["Aarav Sharma", "M-1001", "10:24 AM", "Checked in"], ["Priya Nair", "M-1002", "09:58 AM", "Checked in"], ["Kavya Iyer", "M-1004", "09:16 AM", "Checked in"]]
        self.member_table_page_attendance(wrap, rows)

    def member_table_page_attendance(self, parent, rows):
        box = tk.Frame(parent, bg=WHITE, highlightbackground=LINE, highlightthickness=1); box.pack(fill="both", expand=True)
        cols = ["Member Name", "Member ID", "Check-in Time", "Status"]
        tree = ttk.Treeview(box, columns=cols, show="headings")
        for c in cols: tree.heading(c, text=c); tree.column(c, width=170, anchor="w")
        for r in rows: tree.insert("", "end", values=r)
        tree.pack(fill="both", expand=True, padx=1, pady=1)

    def page_payments(self):
        rows = [["INV-2026-042", "Aarav Sharma", "Premium", "₹2,199", "Paid"], ["INV-2026-041", "Priya Nair", "Gold", "₹1,499", "Paid"], ["INV-2026-040", "Rohan Mehta", "Basic", "₹999", "Pending"]]
        self.member_table_page("Payments", "Review invoices and payment status", rows, ["Invoice", "Member", "Plan", "Amount", "Status"])

    def page_trainers(self):
        rows = [["T-01", "Neha Kapoor", "Strength & Conditioning", "18 members"], ["T-02", "Arjun Singh", "CrossFit", "15 members"], ["T-03", "Meera Das", "Yoga & Mobility", "22 members"]]
        self.member_table_page("Trainers", "Manage fitness professionals and assignments", rows, ["Trainer ID", "Name", "Specialisation", "Active Clients"])

    def page_reports(self):
        wrap = tk.Frame(self.content, bg=BG); wrap.pack(fill="both", expand=True, padx=32, pady=25)
        self.section_header(wrap, "Reports", "Quick summaries for the current month").pack(anchor="w", pady=(0, 20))
        reports = [("Membership Summary", "Plan-wise active and expiring members"), ("Revenue Report", "Payments received and pending balances"), ("Attendance Report", "Daily check-in trends and engagement")]
        for title, desc in reports:
            r = tk.Frame(wrap, bg=WHITE, highlightbackground=LINE, highlightthickness=1); r.pack(fill="x", pady=7)
            tk.Label(r, text="▥", bg=WHITE, fg=TEAL, font=("Segoe UI", 20)).pack(side="left", padx=20, pady=15)
            tx = tk.Frame(r, bg=WHITE); tx.pack(side="left", fill="x", expand=True)
            tk.Label(tx, text=title, bg=WHITE, fg=NAVY, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(16, 1))
            tk.Label(tx, text=desc, bg=WHITE, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", pady=(0, 15))
            self.button(r, "Generate", lambda t=title: self.info("Report ready", f"{t} generated for preview. No file is saved in this prototype."), False).pack(side="right", padx=20)

    def page_settings(self):
        wrap = tk.Frame(self.content, bg=BG); wrap.pack(fill="both", expand=True, padx=32, pady=25)
        self.section_header(wrap, "Settings", "Gym details and front-end preferences").pack(anchor="w", pady=(0, 20))
        card = tk.Frame(wrap, bg=WHITE, highlightbackground=LINE, highlightthickness=1); card.pack(fill="x")
        for label, value in [("Gym name", "FitCore Fitness Studio"), ("Contact email", "hello@fitcore.demo"), ("Business hours", "06:00 AM - 10:00 PM")]:
            r = tk.Frame(card, bg=WHITE); r.pack(fill="x", padx=22, pady=14)
            tk.Label(r, text=label, width=18, anchor="w", bg=WHITE, fg=MUTED, font=("Segoe UI", 10)).pack(side="left")
            e = tk.Entry(r, font=("Segoe UI", 10), bd=0, bg="#F3F7FA", fg=TEXT); e.insert(0, value); e.pack(side="left", fill="x", expand=True, ipady=8)
        self.button(card, "Save changes", lambda: self.info("Changes saved", "Settings are updated for this session only.")).pack(anchor="e", padx=22, pady=(5, 22))

    def open_member_form(self):
        top = tk.Toplevel(self); top.title("Add New Member"); top.configure(bg=WHITE); top.resizable(False, False); top.transient(self); top.grab_set()
        tk.Label(top, text="Add New Member", bg=WHITE, fg=NAVY, font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", padx=28, pady=(25, 5))
        tk.Label(top, text="Information is available during this session only.", bg=WHITE, fg=MUTED, font=("Segoe UI", 9)).grid(row=1, column=0, columnspan=2, sticky="w", padx=28, pady=(0, 18))
        fields = {}; labels = [("Full name", ""), ("Phone number", ""), ("Email address", "")]
        for i, (label, val) in enumerate(labels, 2):
            tk.Label(top, text=label, bg=WHITE, fg=TEXT, font=("Segoe UI", 9, "bold")).grid(row=i, column=0, sticky="w", padx=28, pady=(8, 3))
            e = tk.Entry(top, width=32, font=("Segoe UI", 10), bg="#F3F7FA", fg=TEXT, bd=0); e.insert(0, val); e.grid(row=i, column=1, padx=(8, 28), pady=(8, 3), ipady=7); fields[label] = e
        tk.Label(top, text="Membership plan", bg=WHITE, fg=TEXT, font=("Segoe UI", 9, "bold")).grid(row=5, column=0, sticky="w", padx=28, pady=(10, 18))
        plan = ttk.Combobox(top, values=["Basic", "Gold", "Premium"], state="readonly", width=29); plan.set("Gold"); plan.grid(row=5, column=1, padx=(8, 28), pady=(10, 18))
        def save():
            name = fields["Full name"].get().strip()
            if not name:
                messagebox.showwarning("Missing name", "Please enter the member's full name.", parent=top); return
            mid = f"M-{1000 + len(self.members) + 1}"
            self.members.append([mid, name, plan.get(), "Active", "16 Dec 2026"])
            top.destroy(); self.show_page("Members")
            messagebox.showinfo("Member added", f"{name} has been added for this session.", parent=self)
        self.button(top, "Cancel", top.destroy, False).grid(row=6, column=0, padx=28, pady=(0, 25), sticky="w")
        self.button(top, "Add Member", save).grid(row=6, column=1, padx=28, pady=(0, 25), sticky="e")

    def open_checkin(self):
        top = tk.Toplevel(self); top.title("Record Check-in"); top.configure(bg=WHITE); top.transient(self); top.grab_set(); top.resizable(False, False)
        tk.Label(top, text="Record Check-in", bg=WHITE, fg=NAVY, font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=28, pady=(24, 6))
        tk.Label(top, text="Choose a member to add a session check-in.", bg=WHITE, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", padx=28, pady=(0, 17))
        choice = ttk.Combobox(top, values=[f"{x[1]} ({x[0]})" for x in self.members], state="readonly", width=35); choice.current(0); choice.pack(padx=28, pady=(0, 20))
        def submit():
            text = choice.get(); name, mid = text.rsplit(" (", 1); self.attendance.insert(0, [name, mid[:-1], "Just now", "Checked in"])
            top.destroy(); self.show_page("Attendance")
        self.button(top, "Check In", submit).pack(anchor="e", padx=28, pady=(0, 25))

    def info(self, title, message):
        messagebox.showinfo(title, message, parent=self)


if __name__ == "__main__":
    GymApp().mainloop()
