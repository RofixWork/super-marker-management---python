from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import asksaveasfile
import random
class Super(Toplevel):
    def __init__(self, root):
        super().__init__(root)

        #variables
        self.buyer_name = StringVar()
        self.buyer_number = StringVar()
        self.invoice_number = StringVar(value = str(random.randint(1000, 9999)))
        self.boqoliat_total = StringVar()
        self.electric_tools_total = StringVar()
        self.house_tools_total = StringVar()
        self.invoice_content = None

        #electric tools vars
        self.electric_tool_1 = DoubleVar()
        self.electric_tool_2 = DoubleVar()
        self.electric_tool_3 = DoubleVar()
        self.electric_tool_4 = DoubleVar()
        self.electric_tool_5 = DoubleVar()
        self.electric_tool_6 = DoubleVar()
        self.electric_tool_7 = DoubleVar()
        self.electric_tool_8 = DoubleVar()
        self.electric_tool_9 = DoubleVar()
        self.electric_tool_10 = DoubleVar()
        self.electric_tool_11 = DoubleVar()
        self.electric_tool_12 = DoubleVar()
        self.electric_tool_13 = DoubleVar()
        self.electric_tool_14 = DoubleVar()

        #home tools vars
        self.home_tool_1 = DoubleVar()
        self.home_tool_2 = DoubleVar()
        self.home_tool_3 = DoubleVar()
        self.home_tool_4 = DoubleVar()
        self.home_tool_5 = DoubleVar()
        self.home_tool_6 = DoubleVar()
        self.home_tool_7 = DoubleVar()
        self.home_tool_8 = DoubleVar()
        self.home_tool_9 = DoubleVar()
        self.home_tool_10 = DoubleVar()
        self.home_tool_11 = DoubleVar()
        self.home_tool_12 = DoubleVar()
        self.home_tool_13 = DoubleVar()
        self.home_tool_14 = DoubleVar()
        self.home_tool_15 = DoubleVar()
        self.home_tool_16 = DoubleVar()
        self.home_tool_17 = DoubleVar()
        self.home_tool_18 = DoubleVar()
        self.home_tool_19 = DoubleVar()

         #Legumes vars
        self.legum_1 = DoubleVar()
        self.legum_2 = DoubleVar()
        self.legum_3 = DoubleVar()
        self.legum_4 = DoubleVar()
        self.legum_5 = DoubleVar()
        self.legum_6 = DoubleVar()
        self.legum_7 = DoubleVar()
        self.legum_8 = DoubleVar()
        self.legum_9 = DoubleVar()
        self.legum_10 = DoubleVar()
        self.legum_11 = DoubleVar()
        self.legum_12 = DoubleVar()
        self.legum_13 = DoubleVar()
        self.legum_14 = DoubleVar()
        self.legum_15 = DoubleVar()
        self.legum_16 = DoubleVar()
        self.legum_17 = DoubleVar()
        self.legum_18 = DoubleVar()
        self.legum_19 = DoubleVar()

        self.bg= '#072c39'
        self.title("Super Market")
        self.geometry("1255x600+50+50")
        self.iconbitmap("./favicon.ico")
        self.resizable(False, False)

        self.font = {
            'family': 'Arial Rounded MT Bold',
            "size": 14,
            "weight_bold":"bold",
            "weight_normal":"normal",
        }

        self.left_frame()
        self.right_frame()

        self.grid_layout()

        self.welcome()

        self.mainloop()

    def grid_layout(self):
        self.grid_columnconfigure((0, 1), weight=1, uniform='column')
        self.grid_rowconfigure(0, weight=1, uniform='row')

    def left_frame(self):
        left_frame = Frame(self)
        left_frame.grid(row=0, column=0, sticky='nswe')

        self.customer_info_frame(left_frame)
        self.actions_frame(left_frame)
        self.frame_electric_tools(left_frame)


        left_frame.grid_columnconfigure((0,1), weight=1, uniform='column')
        left_frame.grid_rowconfigure(0, weight=4, uniform='row')
        left_frame.grid_rowconfigure(1, weight=1, uniform='row')

    def right_frame(self):
        right_frame = Frame(self, bg=self.bg)
        right_frame.grid(row=0, column=1, sticky='nswe')
        self.frame_legumes(right_frame)
        self.frame_household_supplies(right_frame)
        
        right_frame.grid_columnconfigure((0,1), weight=1, uniform='column')
        right_frame.grid_rowconfigure(0, weight=1, uniform='row')

    def frame_legumes(self, root):
         #left
        frame_1 = Frame(root, bg=self.bg)
        frame_1.grid(row=0, column=0, sticky='wesn', padx=3, pady=3)
        Label(frame_1, text='بقوليات',bg=self.bg, fg='orange', font=(self.font['family'], self.font['size'], self.font['weight_normal']), anchor='center').grid(column=0, row=0,columnspan=2, sticky='we')

        Label(frame_1, text='الارز',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=1, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_1).grid(column=0, row=1, sticky='we')

        Label(frame_1, text='فاصولياء',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=3, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_2).grid(column=0, row=3, sticky='we')

        Label(frame_1, text='عدس',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=4, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_3).grid(column=0, row=4, sticky='we')

        Label(frame_1, text='معكرونة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=5, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_4).grid(column=0, row=5, sticky='we')

        Label(frame_1, text='حمص',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=6, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_5).grid(column=0, row=6, sticky='we')

        Label(frame_1, text='فول',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=7, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_6).grid(column=0, row=7, sticky='we')

        Label(frame_1, text='الملح',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=8, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_7).grid(column=0, row=8, sticky='we')

        Label(frame_1, text='كامون',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=9, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_8).grid(column=0, row=9, sticky='we')

        Label(frame_1, text='سكر',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=10, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_9).grid(column=0, row=10, sticky='we')

        Label(frame_1, text='اسود فلفل',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=11, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_10).grid(column=0, row=11, sticky='we')

        Label(frame_1, text='احمر فلفل',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=12, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_11).grid(column=0, row=12, sticky='we')

        Label(frame_1, text='اللوبيا',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=13, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_12).grid(column=0, row=13, sticky='we')

        Label(frame_1, text='بازلاء',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=14, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_13).grid(column=0, row=14, sticky='we')

        Label(frame_1, text='القمح',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=15, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_14).grid(column=0, row=15, sticky='we')

        Label(frame_1, text='الشعير',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=16, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_15).grid(column=0, row=16, sticky='we')

        Label(frame_1, text='الشوفان',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=17, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_16).grid(column=0, row=17, sticky='we')

        Label(frame_1, text='الذرة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=18, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_17).grid(column=0, row=18, sticky='we')

        Label(frame_1, text='الكاكاو حبوب',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=19, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_18).grid(column=0, row=19, sticky='we')

        Label(frame_1, text='برغل',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=2, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.legum_19).grid(column=0, row=2, sticky='we')

        frame_1.grid_columnconfigure((0,1), weight=1, uniform='column')
        for row in range(0, 20):
            frame_1.rowconfigure(row, weight=1, uniform='column')
        #left

    def frame_household_supplies(self, root):
         #left
        frame_1 = Frame(root, bg=self.bg)
        frame_1.grid(row=0, column=1, sticky='wesn', padx=3, pady=3)
        Label(frame_1, text='المنزلية اللوازم',bg=self.bg, fg='orange', font=(self.font['family'], self.font['size'], self.font['weight_normal']), anchor='center').grid(column=0, row=0,columnspan=2, sticky='we')

        Label(frame_1, text='مصفاة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=1, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_1).grid(column=0, row=1, sticky='we')

        Label(frame_1, text='صحن',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=2, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_2).grid(column=0, row=2, sticky='we')

        Label(frame_1, text='كأس',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=3, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_3).grid(column=0, row=3, sticky='we')

        Label(frame_1, text='ابريق',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=4, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_4).grid(column=0, row=4, sticky='we')

        Label(frame_1, text='سكين',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=5, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_5).grid(column=0, row=5, sticky='we')

        Label(frame_1, text='شوك',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=6, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_6).grid(column=0, row=6, sticky='we')

        Label(frame_1, text='طنجرة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=7, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_7).grid(column=0, row=7, sticky='we')

        Label(frame_1, text='سلة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=8, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_8).grid(column=0, row=8, sticky='we')

        Label(frame_1, text='ملاعق',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=9, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_9).grid(column=0, row=9, sticky='we')

        Label(frame_1, text='صينية',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=10, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_10).grid(column=0, row=10, sticky='we')

        Label(frame_1, text='الخلط وعاء',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=11, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_11).grid(column=0, row=11, sticky='we')

        Label(frame_1, text='عنب فتاحة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=12, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_12).grid(column=0, row=12, sticky='we')

        Label(frame_1, text='مقشرة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=13, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_13).grid(column=0, row=13, sticky='we')

        Label(frame_1, text='التقطيع لوح',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=14, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_14).grid(column=0, row=14, sticky='we')

        Label(frame_1, text='حفارة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=15, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_15).grid(column=0, row=15, sticky='we')

        Label(frame_1, text='قمامة سلة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=16, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_16).grid(column=0, row=16, sticky='we')

        Label(frame_1, text='اكياس',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=17, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_17).grid(column=0, row=17, sticky='we')

        Label(frame_1, text='عصارة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=18, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_18).grid(column=0, row=18, sticky='we')

        Label(frame_1, text='مقلاة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=19, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.home_tool_19).grid(column=0, row=19, sticky='we')

        frame_1.grid_columnconfigure((0,1), weight=1, uniform='column')
        for row in range(0, 20):
            frame_1.rowconfigure(row, weight=1, uniform='column')
    
    def frame_electric_tools(self, root):
        frame_1 = Frame(root, bg=self.bg)
        frame_1.grid(row=0, column=1, sticky='wesn', padx=1, pady=1)


        Label(frame_1, text='الكترونية ادوات',bg=self.bg, fg='orange', font=(self.font['family'], self.font['size'], self.font['weight_normal']), anchor='center').grid(column=0, row=0,columnspan=2, sticky='we')

        Label(frame_1, text='تلفزيون',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=1, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_1).grid(column=0, row=1, sticky='we', padx=3)

        Label(frame_1, text='غسالة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=2, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_2).grid(column=0, row=2, sticky='we', padx=3)

        Label(frame_1, text='مكرويف',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=3, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_3).grid(column=0, row=3, sticky='we', padx=3)

        Label(frame_1, text='فرن غاز',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=4, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_4).grid(column=0, row=4, sticky='we', padx=3)

        Label(frame_1, text='مقلاة كهربائية',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=5, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_5).grid(column=0, row=5, sticky='we', padx=3)

        Label(frame_1, text='مروحة سقف',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=6, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_6).grid(column=0, row=6, sticky='we', padx=3)

        Label(frame_1, text='مروحة ارضية',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=7, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_7).grid(column=0, row=7, sticky='we', padx=3)

        Label(frame_1, text='تلفزيون 32',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=8, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_8).grid(column=0, row=8, sticky='we', padx=3)

        Label(frame_1, text='تلفزيون 64',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=9, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_9).grid(column=0, row=9, sticky='we', padx=3)

        Label(frame_1, text='فلتر ماء',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=10, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_10).grid(column=0, row=10, sticky='we', padx=3)

        Label(frame_1, text='غسالة اوتو',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=11, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_11).grid(column=0, row=11, sticky='we', padx=3)

        Label(frame_1, text='فتاحة مكواة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=12, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_12).grid(column=0, row=12, sticky='we', padx=3)

        Label(frame_1, text='مقشرة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=13, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_13).grid(column=0, row=13, sticky='we', padx=3)

        Label(frame_1, text='مبردة',bg=self.bg, fg='white', font=(self.font['family'], 10, self.font['weight_normal'])).grid(column=1, row=14, sticky='e')
        
        Entry(frame_1, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tool_14).grid(column=0, row=14, sticky='we', padx=3)

        frame_1.grid_columnconfigure((0,1), weight=1, uniform='column')
        for row in range(0, 15):
            frame_1.rowconfigure(row, weight=1, uniform='column')

    def customer_info_frame(self, root):
        customer_frame = Frame(root, bg=self.bg)

        # top
        top_frame = Frame(customer_frame, bg=self.bg)
        top_frame.grid(row=0, column=0, sticky='wesn')

        Label(top_frame, text='Buyer Data',bg=self.bg, fg='orange', font=(self.font['family'], self.font['size'], self.font['weight_normal'])).grid(column=0, row=0, sticky='we')

        # middle
        middle_frame = Frame(top_frame, bg=self.bg)
        middle_frame.grid(row=1, column=0, sticky='wesn')

        Label(middle_frame, text='Buyer Name:',bg=self.bg, fg='white', font=(self.font['family'], 8, self.font['weight_normal'])).grid(column=0, row=0, sticky='w')
        
        Entry(middle_frame, font=(self.font['family'], 10, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.buyer_name).grid(column=1, row=0, sticky='we')

        Label(middle_frame, text='Buyer Number:',bg=self.bg, fg='white', font=(self.font['family'], 8, self.font['weight_normal'])).grid(column=0, row=1, sticky='w')

        Entry(middle_frame, font=(self.font['family'], 10, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.buyer_number).grid(column=1, row=1, sticky='we')

        Label(middle_frame, text='Invoice Number:',bg=self.bg, fg='white', font=(self.font['family'], 8, self.font['weight_normal'])).grid(column=0, row=2, sticky='w')

        Entry(middle_frame, font=(self.font['family'], 10, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.invoice_number).grid(column=1, row=2, sticky='we')

        Button(middle_frame,text='Search', font=(self.font['family'], 10, self.font['weight_normal']), justify='center', cursor='hand2').grid(column=2, row=0,rowspan=3, sticky='wesn', padx=3, pady=8)
        

        middle_frame.grid_columnconfigure((0,1,2), weight=1, uniform='column')
        middle_frame.grid_rowconfigure((0,1,2), weight=1, uniform='row')

        Label(top_frame, text='[Invoice]',bg=self.bg, fg='orange', font=(self.font['family'], self.font['size'], self.font['weight_normal'])).grid(column=0, row=2, sticky='we')


        top_frame.grid_columnconfigure(0, weight=1, uniform='column')
        top_frame.grid_rowconfigure(0, weight=1, uniform='row')
        top_frame.grid_rowconfigure(1, weight=3, uniform='row')
        top_frame.grid_rowconfigure(2, weight=1, uniform='row')
        # bottom
        bottom_frame = Frame(customer_frame)
        bottom_frame.grid(row=1, column=0, sticky='wesn')

        self.invoice_content = ScrolledText(bottom_frame, font=(self.font['family'], 10, self.font['weight_normal']))
        self.invoice_content.place(relwidth=1, relheight=1, x=0, y=0)

        customer_frame.grid(column=0, row=0, sticky='wesn', padx=1, pady=1)
        
        customer_frame.grid_columnconfigure(0, weight=1, uniform='column')
        customer_frame.grid_rowconfigure(0, weight=2, uniform='row')
        customer_frame.grid_rowconfigure(1, weight=3, uniform='row')

    def actions_frame(self, root):
        actions_frame = Frame(root)

        actions_frame.grid(column=0, row=1, columnspan=2, sticky='wesn', padx=1, pady=1)

        #left
        left_frame = Frame(actions_frame, bg=self.bg)
        left_frame.grid(row=0, column=0, sticky='nswe')

        Label(left_frame, text='Total account for legumes:',bg=self.bg, fg='white', font=(self.font['family'], 8, self.font['weight_normal'])).grid(column=0, row=0, sticky='w')

        Entry(left_frame, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.boqoliat_total).grid(column=1, row=0, sticky='we')

        Label(left_frame, text='Household supplies account:',bg=self.bg, fg='white', font=(self.font['family'], 8, self.font['weight_normal'])).grid(column=0, row=1, sticky='w')

        Entry(left_frame, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.house_tools_total).grid(column=1, row=1, sticky='we')

        Label(left_frame, text='Electrical appliances account:',bg=self.bg, fg='white', font=(self.font['family'], 8, self.font['weight_normal'])).grid(column=0, row=2, sticky='w')

        Entry(left_frame, font=(self.font['family'], 12, self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.electric_tools_total).grid(column=1, row=2, sticky='we')

        left_frame.grid_columnconfigure((0,1), weight=2, uniform='column')
        left_frame.grid_columnconfigure(1, weight=1, uniform='column')
        left_frame.grid_rowconfigure((0,1,2), weight=1, uniform='row')

        #right
        right_frame = Frame(actions_frame, bg=self.bg)
        right_frame.grid(row=0, column=1, sticky='nswe')

        Button(right_frame,text='Total', font=(self.font['family'], 10, self.font['weight_normal']), justify='center', cursor='hand2', bg='orange', fg='#111', command=self.total).grid(column=0, row=0, sticky='wesn', padx=4, pady=2)

        Button(right_frame,text='Clear', font=(self.font['family'], 10, self.font['weight_normal']), justify='center', cursor='hand2', bg='orange', fg='#111', command=self.clear).grid(column=0, row=1, sticky='wesn', padx=4, pady=2)

        Button(right_frame,text='Export Invoice', font=(self.font['family'], 10, self.font['weight_normal']), justify='center', cursor='hand2', bg='orange', fg='#111', command=self.print).grid(column=1, row=0, sticky='wesn', padx=4, pady=2)

        Button(right_frame,text='Exit', font=(self.font['family'], 10, self.font['weight_normal']), justify='center', cursor='hand2', bg='orange', fg='#111', command=self.destroy).grid(column=1, row=1, sticky='wesn', padx=4, pady=2)

        right_frame.grid_columnconfigure((0,1), weight=1, uniform='column')
        right_frame.grid_rowconfigure((0,1), weight=1, uniform='row')

        actions_frame.grid_columnconfigure((0,1), weight=1, uniform='column')
        actions_frame.grid_rowconfigure(0, weight=2, uniform='row')

    def total(self):
        roz = self.legum_1.get() * 1
        fasolya = self.legum_2.get() * 1
        adas = self.legum_3.get() * 1
        ma3karona = self.legum_4.get() * 3
        homs = self.legum_5.get() * 2
        fol = self.legum_6.get() * 1
        mil7 = self.legum_7.get() * 1.5
        kamon = self.legum_8.get() * 1
        sugar = self.legum_9.get() * 2
        folfol_aswad = self.legum_10.get() * 1
        folfol_a7mar = self.legum_11.get() * 1
        lobya = self.legum_12.get() * 1
        bazilaie = self.legum_13.get() * 1
        qam7 = self.legum_14.get() * 1
        cha3ir = self.legum_15.get() * 5
        chufan = self.legum_16.get() * 4
        dura = self.legum_17.get() * 1.5
        hobob_cacaoe = self.legum_18.get() * 3.5
        burgel = self.legum_19.get() * 1.5

        legums_total = roz + burgel + fasolya + adas + ma3karona + homs + fol + mil7 + kamon + sugar + folfol_aswad + folfol_a7mar + lobya + bazilaie + qam7 + cha3ir + chufan + dura + hobob_cacaoe

        tv = self.electric_tool_1.get() * 1000
        rasala = self.electric_tool_2.get() * 1000
        maiekrowif = self.electric_tool_3.get() * 200
        raz_forn = self.electric_tool_4.get() * 500
        miqlat_kahrabaieya = self.electric_tool_5.get() * 100
        mirwa7at_saqf = self.electric_tool_6.get() * 150
        mirwa7at_ardiya = self.electric_tool_7.get() * 200
        tv_32 = self.electric_tool_8.get() * 1000
        tv_64 = self.electric_tool_9.get() * 1000
        filter_water = self.electric_tool_10.get() * 40
        rasala_auto = self.electric_tool_11.get() * 1500
        fata7at_mikwat = self.electric_tool_12.get() * 40
        moqachira = self.electric_tool_13.get() * 5
        mobarida = self.electric_tool_14.get() * 30

        electric_tools_total = tv + rasala + maiekrowif + raz_forn + miqlat_kahrabaieya + mirwa7at_saqf + mirwa7at_ardiya + tv_32 + tv_64 + filter_water + rasala_auto + fata7at_mikwat + moqachira + mobarida

        misfat = self.home_tool_1.get() * 1
        sa7n = self.home_tool_2.get() * 10
        kaies = self.home_tool_3.get() * 5
        ibriq = self.home_tool_4.get() * 3
        sikin = self.home_tool_5.get() * 2
        chouk = self.home_tool_6.get() * 1
        tangara = self.home_tool_7.get() * 4
        salato = self.home_tool_8.get() * 1
        mala3iq = self.home_tool_9.get() * 2
        siniya = self.home_tool_10.get() * 10
        wi3aie_al5alt = self.home_tool_11.get() * 10
        fata7at_3inab = self.home_tool_12.get() * 10
        moqachira = self.home_tool_13.get() * 1
        law7_taqti3 = self.home_tool_14.get() * 15
        hafara = self.home_tool_15.get() * 5
        salat_qomama = self.home_tool_16.get() * 4
        akias = self.home_tool_17.get() * 1
        asara = self.home_tool_18.get() * 30
        miqlat = self.home_tool_19.get() * 10

        house_tools_total = misfat + sa7n + kaies + ibriq + sikin + chouk + tangara + salato + mala3iq + siniya + wi3aie_al5alt + fata7at_3inab + moqachira + law7_taqti3 + hafara + salat_qomama + akias + asara + miqlat

        self.boqoliat_total.set(str(f"$ {legums_total}"))
        self.electric_tools_total.set(str(f"$ {electric_tools_total}"))
        self.house_tools_total.set(str(f"$ {house_tools_total}"))

        self.invoice_content.delete('1.0', END)
        self.invoice_content.insert(END, 'Welcome to the Invoice Management System!\n')
        self.invoice_content.insert(END, "\n===================================")
        self.invoice_content.insert(END, f"\n\tInvoice NUM: {self.invoice_number.get()}")
        self.invoice_content.insert(END, f"\n\tName: {self.buyer_name.get()}")
        self.invoice_content.insert(END, f"\n\tPhone: {self.buyer_number.get()}")
        self.invoice_content.insert(END, "\n===================================")
        self.invoice_content.insert(END, "\n\tPrice\tNumber\tProducts")
        self.invoice_content.insert(END, "\n===================================")

        if self.legum_1.get() != 0:
            self.invoice_content.insert(END, f"\n\t{roz}\t{self.legum_1.get()}\troz")
        if self.legum_2.get() != 0:
            self.invoice_content.insert(END, f"\n\t{fasolya}\t{self.legum_2.get()}\tfasolya")
        if self.legum_3.get() != 0:
            self.invoice_content.insert(END, f"\n\t{adas}\t{self.legum_3.get()}\tadas")
        if self.legum_4.get() != 0:
            self.invoice_content.insert(END, f"\n\t{ma3karona}\t{self.legum_4.get()}\tma3karona")
        if self.legum_5.get() != 0:
            self.invoice_content.insert(END, f"\n\t{homs}\t{self.legum_5.get()}\thoms")
        if self.legum_6.get() != 0:
            self.invoice_content.insert(END, f"\n\t{fol}\t{self.legum_6.get()}\tfol")
        if self.legum_7.get() != 0:
            self.invoice_content.insert(END, f"\n\t{mil7}\t{self.legum_7.get()}\tmil7")
        if self.legum_8.get() != 0:
            self.invoice_content.insert(END, f"\n\t{kamon}\t{self.legum_8.get()}\tkamon")
        if self.legum_9.get() != 0:
            self.invoice_content.insert(END, f"\n\t{sugar}\t{self.legum_9.get()}\tsugar")
        if self.legum_10.get() != 0:
            self.invoice_content.insert(END, f"\n\t{folfol_aswad}\t{self.legum_10.get()}\tfolfol_aswad")
        if self.legum_11.get() != 0:
            self.invoice_content.insert(END, f"\n\t{folfol_a7mar}\t{self.legum_11.get()}\tfolfol_a7mar")
        if self.legum_12.get() != 0:
            self.invoice_content.insert(END, f"\n\t{lobya}\t{self.legum_12.get()}\tlobya")
        if self.legum_13.get() != 0:
            self.invoice_content.insert(END, f"\n\t{bazilaie}\t{self.legum_13.get()}\tbazilaie")
        if self.legum_14.get() != 0:
            self.invoice_content.insert(END, f"\n\t{qam7}\t{self.legum_14.get()}\tqam7")
        if self.legum_15.get() != 0:
            self.invoice_content.insert(END, f"\n\t{cha3ir}\t{self.legum_15.get()}\tcha3ir")
        if self.legum_16.get() != 0:
            self.invoice_content.insert(END, f"\n\t{chufan}\t{self.legum_16.get()}\tchufan")
        if self.legum_17.get() != 0:
            self.invoice_content.insert(END, f"\n\t{dura}\t{self.legum_17.get()}\tdura")
        if self.legum_18.get() != 0:
            self.invoice_content.insert(END, f"\n\t{hobob_cacaoe}\t{self.legum_18.get()}\thobob_cacaoe")
        if self.legum_19.get() != 0:
            self.invoice_content.insert(END, f"\n\t{burgel}\t{self.legum_19.get()}\tburgel")

        if self.home_tool_1.get() != 0:
            self.invoice_content.insert(END, f"\n\t{misfat}\t{self.home_tool_1.get()}\tmisfat")
        if self.home_tool_2.get() != 0:
            self.invoice_content.insert(END, f"\n\t{sa7n}\t{self.home_tool_2.get()}\tsa7n")
        if self.home_tool_3.get() != 0:
            self.invoice_content.insert(END, f"\n\t{kaies}\t{self.home_tool_3.get()}\tkaies")
        if self.home_tool_4.get() != 0:
            self.invoice_content.insert(END, f"\n\t{ibriq}\t{self.home_tool_4.get()}\tibriq")
        if self.home_tool_5.get() != 0:
            self.invoice_content.insert(END, f"\n\t{sikin}\t{self.home_tool_5.get()}\tsikin")
        if self.home_tool_6.get() != 0:
            self.invoice_content.insert(END, f"\n\t{chouk}\t{self.home_tool_6.get()}\tchouk")
        if self.home_tool_7.get() != 0:
            self.invoice_content.insert(END, f"\n\t{tangara}\t{self.home_tool_7.get()}\ttangara")
        if self.home_tool_8.get() != 0:
            self.invoice_content.insert(END, f"\n\t{salato}\t{self.home_tool_8.get()}\tsalato")
        if self.home_tool_9.get() != 0:
            self.invoice_content.insert(END, f"\n\t{mala3iq}\t{self.home_tool_9.get()}\tmala3iq")
        if self.home_tool_10.get() != 0:
            self.invoice_content.insert(END, f"\n\t{siniya}\t{self.home_tool_10.get()}\tsiniya")
        if self.home_tool_11.get() != 0:
            self.invoice_content.insert(END, f"\n\t{wi3aie_al5alt}\t{self.home_tool_11.get()}\twi3aie_al5alt")
        if self.home_tool_12.get() != 0:
            self.invoice_content.insert(END, f"\n\t{fata7at_3inab}\t{self.home_tool_12.get()}\tfata7at_3inab")
        if self.home_tool_13.get() != 0:
            self.invoice_content.insert(END, f"\n\t{moqachira}\t{self.home_tool_13.get()}\tmoqachira")
        if self.home_tool_14.get() != 0:
            self.invoice_content.insert(END, f"\n\t{law7_taqti3}\t{self.home_tool_14.get()}\tlaw7_taqti3")
        if self.home_tool_15.get() != 0:
            self.invoice_content.insert(END, f"\n\t{hafara}\t{self.home_tool_15.get()}\thafara")
        if self.home_tool_16.get() != 0:
            self.invoice_content.insert(END, f"\n\t{salat_qomama}\t{self.home_tool_16.get()}\tsalat_qomama")
        if self.home_tool_17.get() != 0:
            self.invoice_content.insert(END, f"\n\t{akias}\t{self.home_tool_17.get()}\takias")
        if self.home_tool_18.get() != 0:
            self.invoice_content.insert(END, f"\n\t{asara}\t{self.home_tool_18.get()}\tasara")
        if self.home_tool_19.get() != 0:
            self.invoice_content.insert(END, f"\n\t{miqlat}\t{self.home_tool_19.get()}\tmiqlat")


        if self.electric_tool_1.get() != 0:
            self.invoice_content.insert(END, f"\n\t{tv}\t{self.electric_tool_1.get()}\tTV")
        if self.electric_tool_2.get() != 0:
            self.invoice_content.insert(END, f"\n\t{rasala}\t{self.electric_tool_2.get()}\trasala")
        if self.electric_tool_3.get() != 0:
            self.invoice_content.insert(END, f"\n\t{maiekrowif}\t{self.electric_tool_3.get()}\tMicrowave")
        if self.electric_tool_4.get() != 0:
            self.invoice_content.insert(END, f"\n\t{raz_forn}\t{self.electric_tool_4.get()}\tOven")
        if self.electric_tool_5.get() != 0:
            self.invoice_content.insert(END, f"\n\t{miqlat_kahrabaieya}\t{self.electric_tool_5.get()}\tElectric Kettle")
        if self.electric_tool_6.get() != 0:
            self.invoice_content.insert(END, f"\n\t{mirwa7at_saqf}\t{self.electric_tool_6.get()}\tCeiling Fan")
        if self.electric_tool_7.get() != 0:
            self.invoice_content.insert(END, f"\n\t{mirwa7at_ardiya}\t{self.electric_tool_7.get()}\tFloor Fan")
        if self.electric_tool_8.get() != 0:
            self.invoice_content.insert(END, f"\n\t{tv_32}\t{self.electric_tool_8.get()}\t32-inch TV")
        if self.electric_tool_9.get() != 0:
            self.invoice_content.insert(END, f"\n\t{tv_64}\t{self.electric_tool_9.get()}\t64-inch TV")
        if self.electric_tool_10.get() != 0:
            self.invoice_content.insert(END, f"\n\t{filter_water}\t{self.electric_tool_10.get()}\tWater Filter")
        if self.electric_tool_11.get() != 0:
            self.invoice_content.insert(END, f"\n\t{rasala_auto}\t{self.electric_tool_11.get()}\tAutomatic Washer")
        if self.electric_tool_12.get() != 0:
            self.invoice_content.insert(END, f"\n\t{fata7at_mikwat}\t{self.electric_tool_12.get()}\tIron Holder")
        if self.electric_tool_13.get() != 0:
            self.invoice_content.insert(END, f"\n\t{moqachira}\t{self.electric_tool_13.get()}\tVacuum Cleaner")
        if self.electric_tool_14.get() != 0:
            self.invoice_content.insert(END, f"\n\t{mobarida}\t{self.electric_tool_14.get()}\tCooler")

        self.invoice_content.insert(END, "\n===================================")
        self.invoice_content.insert(END, f"\n\tTotal: ${legums_total + house_tools_total + electric_tools_total}")
        self.invoice_content.insert(END, "\n===================================")

            

    def clear(self):
        self.invoice_number.set('')
        self.buyer_name.set('')
        self.buyer_number.set('')
        self.legum_1.set(0)
        self.legum_2.set(0)
        self.legum_3.set(0)
        self.legum_4.set(0)
        self.legum_5.set(0)
        self.legum_6.set(0)
        self.legum_7.set(0)
        self.legum_8.set(0)
        self.legum_9.set(0)
        self.legum_10.set(0)
        self.legum_11.set(0)
        self.legum_12.set(0)
        self.legum_13.set(0)
        self.legum_14.set(0)
        self.legum_15.set(0)
        self.legum_16.set(0)
        self.legum_17.set(0)
        self.legum_18.set(0)
        self.legum_19.set(0)

        self.electric_tool_1.set(0)
        self.electric_tool_2.set(0)
        self.electric_tool_3.set(0)
        self.electric_tool_4.set(0)
        self.electric_tool_5.set(0)
        self.electric_tool_6.set(0)
        self.electric_tool_7.set(0)
        self.electric_tool_8.set(0)
        self.electric_tool_9.set(0)
        self.electric_tool_10.set(0)
        self.electric_tool_11.set(0)
        self.electric_tool_12.set(0)
        self.electric_tool_13.set(0)
        self.electric_tool_14.set(0)

        self.home_tool_1.set(0)
        self.home_tool_2.set(0)
        self.home_tool_3.set(0)
        self.home_tool_4.set(0)
        self.home_tool_5.set(0)
        self.home_tool_6.set(0)
        self.home_tool_7.set(0)
        self.home_tool_8.set(0)
        self.home_tool_9.set(0)
        self.home_tool_10.set(0)
        self.home_tool_11.set(0)
        self.home_tool_12.set(0)
        self.home_tool_13.set(0)
        self.home_tool_14.set(0)
        self.home_tool_15.set(0)
        self.home_tool_16.set(0)
        self.home_tool_17.set(0)
        self.home_tool_18.set(0)
        self.home_tool_19.set(0)

        self.invoice_content.delete('1.0', END)
        self.invoice_content.insert(END, 'Welcome to the Invoice Management System!\n')
        self.invoice_content.insert(END, "\n===================================")
        self.invoice_content.insert(END, f"\n\tInvoice NUM: {self.invoice_number.get()}")
        self.invoice_content.insert(END, f"\n\tName: {self.buyer_name.get()}")
        self.invoice_content.insert(END, f"\n\tPhone: {self.buyer_number.get()}")
        self.invoice_content.insert(END, "\n===================================")
        self.invoice_content.insert(END, "\n\tPrice\tNumber\tProducts")
        self.invoice_content.insert(END, "\n===================================")

        self.boqoliat_total.set('')
        self.electric_tools_total.set('')
        self.house_tools_total.set('')

    def welcome(self):
        self.invoice_content.delete('1.0', END)
        self.invoice_content.insert(END, 'Welcome to the Invoice Management System!\n')
        self.invoice_content.insert(END, "\n===================================")
        self.invoice_content.insert(END, f"\n\tInvoice NUM: {self.invoice_number.get()}")
        self.invoice_content.insert(END, f"\n\tName: {self.buyer_name.get()}")
        self.invoice_content.insert(END, f"\n\tPhone: {self.buyer_number.get()}")
        self.invoice_content.insert(END, "\n===================================")
        self.invoice_content.insert(END, "\n\tPrice\tNumber\tProducts")
        self.invoice_content.insert(END, "\n===================================")

    def print(self):
        if self.buyer_number.get().strip() == '' or self.buyer_name.get().strip() == '' or self.invoice_number.get().strip() == '':
            showerror('Error', 'Please fill all required fields.')
            return
        
        file =  asksaveasfile(filetypes=(
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ), defaultextension='*.txt')
        
        if file:
            file.write(self.invoice_content.get("1.0", 'end'))
        
            showinfo('Success', 'Invoice saved successfully.')

        file.close()