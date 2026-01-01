import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


# === Стиль: тёмная тема с акцентами ===
def setup_style():
    style = ttk.Style()
    style.theme_use('clam')

    bg_color = "#2C2C2C"
    fg_color = "#FFFFFF"
    accent = "#007ACC"
    button_hover = "#005A99"

    style.configure("TFrame", background=bg_color)
    style.configure("TLabel", background=bg_color, foreground=fg_color, font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
    style.map("TButton",
              background=[('active', button_hover)],
              foreground=[('active', 'white')])

    style.configure("TLabelframe", background=bg_color, foreground=accent, font=("Segoe UI", 12, "bold"))
    style.configure("TLabelframe.Label", background=bg_color, foreground=accent)

    style.configure("Treeview", background="#3C3C3C", foreground=fg_color,
                    fieldbackground="#3C3C3C", rowheight=28, font=("Segoe UI", 10))
    style.map('Treeview', background=[('selected', accent)])
    style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background=accent, foreground="white")

    # Сброс всех настроек списка (для Combobox — на случай, если останется)
    style.configure("TCombobox", fieldbackground="white", background="white", foreground="black")
    style.map('TCombobox', fieldbackground=[('readonly', 'white')], selectbackground=[('focus', accent)])


# === Тест: проверка знаний ===
class TestWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Мост Уитстона — Тест")
        self.master.geometry("1100x700")
        self.master.minsize(900, 600)
        setup_style()

        main_frame = ttk.Frame(self.master, padding="30")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)

        title = ttk.Label(main_frame, text="🧪 Тест: Реохордный или одинарный мост?", 
                          font=("Segoe UI", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 30), sticky=tk.N)

        # Вопрос 1
        q1_label = ttk.Label(main_frame, text="1. Какая схема — РЕОХОРДНЫЙ мост Уитстона?", 
                             font=("Segoe UI", 12))
        q1_label.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        self.answer1 = tk.StringVar(value="none")
        self.answer2 = tk.StringVar(value="none")

        images1 = ttk.Frame(main_frame)
        images1.grid(row=2, column=0, columnspan=2, pady=(0, 20))

        try:
            img1 = Image.open("Реоходный мост Уинстона.png").resize((300, 200), Image.Resampling.LANCZOS)
            self.photo1 = ImageTk.PhotoImage(img1)
            ttk.Label(images1, image=self.photo1).grid(row=0, column=0, padx=15)
            ttk.Radiobutton(images1, text="Реохордный", variable=self.answer1, value="reochord") \
                .grid(row=1, column=0, pady=5)
        except:
            ttk.Label(images1, text="📷 Реохордный мост", font=("Segoe UI", 10)).grid(row=0, column=0, padx=15)

        try:
            img2 = Image.open("Одинарный мост Уинстона.png").resize((300, 200), Image.Resampling.LANCZOS)
            self.photo2 = ImageTk.PhotoImage(img2)
            ttk.Label(images1, image=self.photo2).grid(row=0, column=1, padx=15)
            ttk.Radiobutton(images1, text="Одинарный", variable=self.answer1, value="single") \
                .grid(row=1, column=1, pady=5)
        except:
            ttk.Label(images1, text="📷 Одинарный мост", font=("Segoe UI", 10)).grid(row=0, column=1, padx=15)

        # Вопрос 2
        q2_label = ttk.Label(main_frame, text="2. Какая схема — ОДИНАРНЫЙ мост Уитстона?", 
                             font=("Segoe UI", 12))
        q2_label.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(20, 10))

        images2 = ttk.Frame(main_frame)
        images2.grid(row=4, column=0, columnspan=2, pady=(0, 20))

        if hasattr(self, 'photo1'):
            ttk.Label(images2, image=self.photo1).grid(row=0, column=0, padx=15)
            ttk.Radiobutton(images2, text="Одинарный", variable=self.answer2, value="reochord") \
                .grid(row=1, column=0, pady=5)
        else:
            ttk.Label(images2, text="📷 Реохордный мост").grid(row=0, column=0, padx=15)

        if hasattr(self, 'photo2'):
            ttk.Label(images2, image=self.photo2).grid(row=0, column=1, padx=15)
            ttk.Radiobutton(images2, text="Одинарный", variable=self.answer2, value="single") \
                .grid(row=1, column=1, pady=5)
        else:
            ttk.Label(images2, text="📷 Одинарный мост").grid(row=0, column=1, padx=15)

        check_btn = ttk.Button(main_frame, text="✅ Проверить и продолжить", 
                              command=self.check_answers, width=30)
        check_btn.grid(row=5, column=0, columnspan=2, pady=30)

    def check_answers(self):
        correct1 = (self.answer1.get() == "reochord")
        correct2 = (self.answer2.get() == "single")

        if correct1 and correct2:
            messagebox.showinfo("✅ Отлично!", "Все верно! Запускаем симуляцию...")
            self.master.destroy()
            root = tk.Tk()
            SimulationWindow(root)
            root.mainloop()
        else:
            messagebox.showwarning("❌ Повторите", "Проверьте ответы и попробуйте снова.")


# === Основная симуляция ===
class SimulationWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("🔧 Мост Уитстона — Симуляция")
        self.master.geometry("1200x850")
        self.master.minsize(1000, 700)
        setup_style()

        # Данные
        self.materials = {
            "Константан": {"resistivity": 0.49e-6},
            "Латунь":     {"resistivity": 0.08e-6}
        }
        self.diameters = [1.0, 0.5, 0.7, 0.7, 0.35, 0.5]
        self.length = 1.0
        self.delta_l = 0.5

        self.l1 = 500
        self.l2 = 500
        self.R = 2.0
        self.current_material = "Константан"
        self.selected_diameter = 1.0

        main_frame = ttk.Frame(self.master, padding="25")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Настройка сетки
        main_frame.columnconfigure(0, weight=1)   # схема
        main_frame.columnconfigure(1, weight=2)   # управление
        main_frame.columnconfigure(2, weight=3)   # результаты
        main_frame.rowconfigure(1, weight=3)
        main_frame.rowconfigure(3, weight=5)
        main_frame.rowconfigure(2, weight=1)

        # Заголовок
        title = ttk.Label(main_frame, text="🔬 Симуляция моста Уитстона", 
                          font=("Segoe UI", 18, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=(0, 25), sticky=tk.N)

        # === Левая панель: схема ===
        left_frame = ttk.LabelFrame(main_frame, text="🔌 Схема", padding="15")
        left_frame.grid(row=1, column=0, rowspan=3, padx=(0, 15), pady=(0, 15), sticky=(tk.N, tk.S, tk.W, tk.E))
        left_frame.columnconfigure(0, weight=1)

        try:
            img = Image.open("Реоходный мост Уинстона.png").resize((280, 200), Image.Resampling.LANCZOS)
            self.schema_img = ImageTk.PhotoImage(img)
            ttk.Label(left_frame, image=self.schema_img).grid(row=0, column=0, pady=(0, 10))
        except:
            canvas = tk.Canvas(left_frame, width=280, height=200, bg="#3C3C3C", highlightthickness=0)
            canvas.create_text(140, 100, text="Схема моста Уитстона", fill="white", font=("Segoe UI", 10))
            canvas.grid(row=0, column=0, pady=(0, 10))

        ttk.Label(left_frame, text="🔹 Rₓ — неизвестное\n🔹 R — эталон\n🔹 l₁, l₂ — плечи\n", 
                  foreground="#B0B0B0", font=("Segoe UI", 10), justify=tk.LEFT).grid(row=1, column=0, sticky=tk.W)

        # === Центр: управление ===
        center_frame = ttk.LabelFrame(main_frame, text="⚙️ Управление", padding="15")
        center_frame.grid(row=1, column=1, padx=10, pady=(0, 15), sticky=(tk.N, tk.S, tk.W, tk.E))
        center_frame.columnconfigure(0, weight=1)
        for i in range(12): center_frame.rowconfigure(i, weight=1)

        # Ползунок l1
        ttk.Label(center_frame, text="🔹 Длина l₁ (мм):", font=("Segoe UI", 11)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.l1_slider = ttk.Scale(center_frame, from_=0, to=1000, orient=tk.HORIZONTAL, command=self.update_l1)
        self.l1_slider.set(self.l1)
        self.l1_slider.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        self.l1_value_label = ttk.Label(center_frame, text=f"l₁ = {self.l1} мм", font=("Segoe UI", 10))
        self.l1_value_label.grid(row=2, column=0, sticky=tk.W)
        self.l2_value_label = ttk.Label(center_frame, text=f"l₂ = {self.l2} мм", font=("Segoe UI", 10))
        self.l2_value_label.grid(row=3, column=0, sticky=tk.W, pady=(0, 15))

        # Выбор R
        ttk.Label(center_frame, text="🔹 Эталонное R:", font=("Segoe UI", 11)).grid(row=4, column=0, sticky=tk.W, pady=(5, 5))
        self.R_var = tk.StringVar(value="2 Ом")
        ttk.Radiobutton(center_frame, text="2 Ом (параллельно)", variable=self.R_var, value="2 Ом", command=self.update_R) \
            .grid(row=5, column=0, sticky=tk.W)
        ttk.Radiobutton(center_frame, text="10 Ом (последовательно)", variable=self.R_var, value="10 Ом", command=self.update_R) \
            .grid(row=6, column=0, sticky=tk.W, pady=(0, 15))

        # === ВЫБОР МАТЕРИАЛА — КНОПКИ ===
        ttk.Label(center_frame, text="🔹 Материал:", font=("Segoe UI", 11)).grid(row=7, column=0, sticky=tk.W, pady=(0, 5))
        
        self.mat_frame = ttk.Frame(center_frame)
        self.mat_frame.grid(row=8, column=0, sticky=tk.W, pady=(0, 10))
        self.mat_buttons = {}
        for i, mat in enumerate(self.materials):
            btn = tk.Button(self.mat_frame, text=mat, font=("Segoe UI", 11, "bold"),
                            bg="white", fg="black", relief="raised", width=12,
                            command=lambda m=mat: self.select_material(m))
            btn.grid(row=0, column=i, padx=(0, 10))
            self.mat_buttons[mat] = btn
        self.mat_buttons[self.current_material].config(bg="#007ACC", fg="white")  # выделение

        # === ВЫБОР ДИАМЕТРА — КНОПКИ ===
        ttk.Label(center_frame, text="🔹 Диаметр (мм):", font=("Segoe UI", 11)).grid(row=9, column=0, sticky=tk.W, pady=(5, 5))
        
        self.dia_frame = ttk.Frame(center_frame)
        self.dia_frame.grid(row=10, column=0, sticky=tk.W, pady=(0, 10))
        self.dia_buttons = {}
        for i, d in enumerate(sorted(set(self.diameters))):
            btn = tk.Button(self.dia_frame, text=str(d), font=("Segoe UI", 11),
                            bg="white", fg="black", relief="raised", width=6,
                            command=lambda diam=d: self.select_diameter(diam))
            btn.grid(row=0, column=i, padx=(0, 8))
            self.dia_buttons[d] = btn
        self.dia_buttons[self.selected_diameter].config(bg="#007ACC", fg="white")

        # === Правая панель: результаты ===
        right_frame = ttk.LabelFrame(main_frame, text="📊 Результаты", padding="15")
        right_frame.grid(row=1, column=2, rowspan=2, padx=(0, 0), pady=(0, 15), sticky=(tk.N, tk.S, tk.W, tk.E))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(1, weight=2)
        right_frame.rowconfigure(2, weight=3)
        right_frame.rowconfigure(3, weight=0)

        # Формулы
        formula = ttk.Label(right_frame, text="📘 Формулы:\n"
                                              "Rₓ = R × (l₁/l₂)\n"
                                              "ΔRₓ = Rₓ × (Δl/l₁ + Δl/l₂)\n"
                                              "R_теор = ρ·l / S", 
                            font=("Consolas", 11), background="#383838", foreground="#A0D6F1")
        formula.grid(row=0, column=0, pady=(0, 15), sticky=tk.W)

        # Расчёты
        self.calc_frame = ttk.LabelFrame(right_frame, text="🧮 Расчёты", padding="12")
        self.calc_frame.grid(row=1, column=0, sticky=(tk.N, tk.S, tk.W, tk.E), pady=(0, 10))
        self.calc_frame.columnconfigure(0, weight=1)
        self.update_calculations()

        # Информация
        self.info_frame = ttk.LabelFrame(right_frame, text="ℹ️ Материал", padding="10")
        self.info_frame.grid(row=2, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.update_material_info()

        # Кнопки — ровно под информацией
        buttons_frame = ttk.Frame(right_frame)
        buttons_frame.grid(row=3, column=0, pady=(15, 0), sticky=tk.W)
        ttk.Button(buttons_frame, text="🎯 Сбалансировать мост", 
                  command=self.balance_bridge, width=25).grid(row=0, column=0, pady=3)
        ttk.Button(buttons_frame, text="📈 Построить R(1/d²)", 
                  command=self.plot_graph, width=25).grid(row=1, column=0, pady=3)

        # === Кнопка: добавить измерение ===
        ttk.Button(main_frame, text="➕ Добавить в таблицу", command=self.add_to_table, width=20) \
            .grid(row=2, column=1, pady=(10, 10))

        # === Таблица ===
        bottom_frame = ttk.LabelFrame(main_frame, text="📋 Данные", padding="10")
        bottom_frame.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.rowconfigure(0, weight=1)

        columns = ("№", "Мат", "d", "R", "l₁", "l₂", "Rₓ", "ΔRₓ", "R_теор")
        self.tree = ttk.Treeview(bottom_frame, columns=columns, show="headings", height=6)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=60 if col == "№" else 70)
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        vsb = ttk.Scrollbar(bottom_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.grid(row=0, column=1, sticky=(tk.N, tk.S))

        ttk.Button(bottom_frame, text="🗑️ Очистить таблицу", command=self.clear_table) \
            .grid(row=1, column=0, pady=(10, 0), sticky=tk.W)

        self.measurement_count = 0

    # === Методы выбора ===
    def select_material(self, mat):
        self.current_material = mat
        for m in self.mat_buttons:
            self.mat_buttons[m].config(bg="white", fg="black")
        self.mat_buttons[mat].config(bg="#007ACC", fg="white")
        self.update_material_info()
        self.update_calculations()

    def select_diameter(self, d):
        self.selected_diameter = d
        for diam in self.dia_buttons:
            self.dia_buttons[diam].config(bg="white", fg="black")
        self.dia_buttons[d].config(bg="#007ACC", fg="white")
        self.update_calculations()

    # === Остальные методы (без изменений) ===
    def update_l1(self, value):
        self.l1 = int(float(value))
        self.l2 = 1000 - self.l1
        self.l1_value_label.config(text=f"l₁ = {self.l1} мм")
        self.l2_value_label.config(text=f"l₂ = {self.l2} мм")
        self.update_calculations()

    def update_R(self):
        self.R = float(self.R_var.get().split()[0])
        self.update_calculations()

    def calculate_theoretical_R(self):
        rho = self.materials[self.current_material]["resistivity"]
        d_m = self.selected_diameter / 1000
        S = 3.14159 * (d_m ** 2) / 4
        return rho * self.length / S

    def calculate_uncertainty(self, R_x):
        if self.l1 == 0 or self.l2 == 0:
            return float('inf')
        return R_x * (self.delta_l / self.l1 + self.delta_l / self.l2)

    def update_calculations(self):
        for widget in self.calc_frame.winfo_children():
            widget.destroy()
        R_x = self.R * self.l1 / self.l2 if self.l2 != 0 else float('inf')
        delta_Rx = self.calculate_uncertainty(R_x) if self.l2 != 0 else float('inf')
        R_theor = self.calculate_theoretical_R()

        data = [
            (f"l₁ = {self.l1} мм", f"l₂ = {self.l2} мм"),
            (f"R = {self.R:.1f} Ом", ""),
            (f"Rₓ = {R_x:.4f} Ом", "") if R_x != float('inf') else ("⚠️ l₂ = 0", ""),
        ]
        if R_x != float('inf'):
            data += [
                (f"ΔRₓ = {delta_Rx:.4f} Ом", ""),
                (f"R_теор = {R_theor:.4f} Ом", ""),
            ]
        for i, (col1, col2) in enumerate(data):
            ttk.Label(self.calc_frame, text=col1, font=("Segoe UI", 10)).grid(row=i, column=0, sticky=tk.W, pady=2)
            if col2:
                ttk.Label(self.calc_frame, text=col2, font=("Segoe UI", 10)).grid(row=i, column=1, sticky=tk.W, padx=(20, 0))

    def update_material_info(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        mat = self.materials[self.current_material]
        ttk.Label(self.info_frame, text=f"🔹 {self.current_material}", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self.info_frame, text=f"ρ = {mat['resistivity']:.2e} Ом·м", font=("Segoe UI", 10)).grid(row=1, column=0, sticky=tk.W)

    def balance_bridge(self):
        if self.l2 == 0:
            messagebox.showerror("Ошибка", "l₂ не может быть 0!")
            return
        R_x = self.R * self.l1 / self.l2
        messagebox.showinfo("✅ Баланс", f"Мост сбалансирован!\nRₓ = {R_x:.4f} Ом")

    def add_to_table(self):
        if self.l2 == 0:
            messagebox.showerror("Ошибка", "l₂ не может быть 0!")
            return
        R_x = self.R * self.l1 / self.l2
        delta_Rx = self.calculate_uncertainty(R_x)
        R_theor = self.calculate_theoretical_R()
        self.tree.insert("", "end", values=(
            self.measurement_count + 1,
            self.current_material[:3],
            f"{self.selected_diameter:.2f}",
            f"{self.R:.1f}",
            self.l1,
            self.l2,
            f"{R_x:.4f}",
            f"{delta_Rx:.4f}",
            f"{R_theor:.4f}"
        ))
        self.measurement_count += 1

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.measurement_count = 0

    def plot_graph(self):
        diameters = [1.0, 0.7, 0.5, 0.35]
        d_inv_sq = [1/(d**2) for d in diameters]
        R_exp = []
        for item in self.tree.get_children():
            vals = self.tree.item(item, "values")
            mat, d = vals[1], float(vals[2])
            rx = float(vals[6])
            if mat == "Кон" and d in diameters:
                R_exp.append(rx)
        if len(R_exp) < 4:
            messagebox.showwarning("⚠️", "Измерьте все 4 проводника из константана.")
            return
        plt.figure(figsize=(7, 5), facecolor="#2C2C2C")
        ax = plt.gca()
        ax.set_facecolor("#3C3C3C")
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('white')
        plt.scatter(d_inv_sq, R_exp, color="#FFB347", s=100, edgecolors='white', linewidth=1.5)
        plt.plot(d_inv_sq, R_exp, '--', color='cyan', alpha=0.8)
        plt.xlabel("1/d² (1/мм²)", color='white', fontsize=12)
        plt.ylabel("Rₓ, Ом", color='white', fontsize=12)
        plt.title("Rₓ(1/d²) — Константан", color='white', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()


def main():
    root = tk.Tk()
    TestWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
