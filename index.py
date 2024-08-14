from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter.messagebox import showinfo, showerror
from super import Super 
class App(Tk):
    def __init__(self):
        super().__init__()

        #variables
        self.username = StringVar()
        self.password = StringVar()

        self.bg = "#f4f4f4"
        self.font = {
            'family': 'Arial Rounded MT Bold',
            "size": 14,
            "weight_bold":"bold",
            "weight_normal":"normal",
        }

        self.title("SuperMarket")
        self.geometry("800x500+100+100")
        self.iconbitmap("./favicon.ico")
        self.resizable(False, False)
        self.config(bg=self.bg)

        Label(self, text='Super Market System', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='#072c39', fg='orange', pady=8).grid(column=0, row=0, sticky='wesn')

        self.frame = Frame(self)
        self.frame.grid(column=0, row=1, sticky='wesn')

        self.grid_layout()

        self.create_left_frame()
        self.create_right_frame()

        self.mainloop()

    def grid_layout(self):
        self.grid_columnconfigure(0, weight=1, uniform='column')
        self.grid_rowconfigure(0, weight=1, uniform='row')
        self.grid_rowconfigure(1, weight=8, uniform='row')

        #frame layout
        self.frame.grid_columnconfigure(0, weight=1, uniform='column')
        self.frame.grid_columnconfigure(1, weight=2, uniform='column')
        self.frame.grid_rowconfigure(0, weight=1, uniform='row')

    def create_left_frame(self):
        left_frame = Frame(self.frame, bg="#072c39")
        left_frame.grid(column=0, row=0, sticky='wesn')

        Label(left_frame, text='Super Market System', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='#072c39', fg='white').grid(column=0, row=0, sticky='wesn')

        Button(left_frame, text='Facebook', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='orange', fg='#111', cursor='hand2', command=lambda: self.open_url("https://www.facebook.com")).grid(column=0, row=1, sticky='wesn', pady=10, padx=5)

        Button(left_frame, text='Telegram', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='orange', fg='#111', cursor='hand2',command=lambda: self.open_url("https://web.telegram.org/k/")).grid(column=0, row=2, sticky='wesn', pady=10, padx=5)
    
        Button(left_frame, text='Youtube', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='orange', fg='#111', cursor='hand2',command=lambda: self.open_url("https://youtube.com")).grid(column=0, row=3, sticky='wesn', pady=10, padx=5)
    
        Button(left_frame, text='About the developer', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='orange', fg='#111', cursor='hand2', command=self.about_the_developer).grid(column=0, row=4, sticky='wesn', pady=10, padx=5)
    
        Button(left_frame, text='Project Overview', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='orange', fg='#111', cursor='hand2', command=self.project_overview).grid(column=0, row=5, sticky='wesn', pady=10, padx=5)
    
        Button(left_frame, text='Exit', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='orange', fg='#111', cursor='hand2', command=lambda: exit()).grid(column=0, row=6, sticky='wesn', pady=10, padx=5)

        left_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1, uniform='row')
        left_frame.grid_columnconfigure(0, weight=1, uniform='column')

    def create_right_frame(self):
        right_frame = Frame(self.frame)
        right_frame.grid(column=1, row=0, sticky='wesn')

        self.img = ImageTk.PhotoImage(Image.open('./shop.png').resize((300,300)))
        lbl = Label(right_frame, bg='#f6f6f6',image=self.img)
        lbl.grid(column=0, row=0,sticky='wesn')

        #auth frame
        auth_frame = Frame(right_frame, bg='#072c39')
        auth_frame.grid(column=0, row=1, sticky='wesn')

        Label(auth_frame, text='Username:', font=(self.font['family'], self.font['size'], self.font['weight_bold']), bg='#072c39', fg='white').grid(column=0, row=0, sticky='we')

        Entry(auth_frame, font=(self.font['family'], self.font['size'], self.font['weight_normal']), bg='#072c39', fg='white', justify='center', textvariable=self.username).grid(column=1, row=0, sticky='we')

        Label(auth_frame, text='Password:', font=(self.font['family'], self.font['size'], self.font['weight_normal']), bg='#072c39', fg='white').grid(column=0, row=1, sticky='we')

        Entry(auth_frame, font=(self.font['family'], self.font['size'], self.font['weight_normal']), bg='#072c39', fg='white', justify='center', show='*', textvariable=self.password).grid(column=1, row=1, sticky='we')

        Button(auth_frame, text='Login', font=(self.font['family'], self.font['size'], self.font['weight_normal']), bg='orange', fg='#111', cursor='hand2', command=self.login).grid(column=2, row=0,rowspan=2, sticky='wesn', padx=12, pady=12)

        auth_frame.grid_columnconfigure((0,1,2), weight=1, uniform='column')
        auth_frame.grid_columnconfigure(1, weight=2, uniform='column')
        auth_frame.grid_columnconfigure(2, weight=1, uniform='column')
        auth_frame.grid_rowconfigure((0,1), weight=1, uniform='row')
        #auth frame

        right_frame.grid_rowconfigure(0, weight=3, uniform='row')
        right_frame.grid_rowconfigure(1, weight=1, uniform='row')
        right_frame.grid_columnconfigure(0, weight=1, uniform='column')

    def login(self):
        username = self.username.get()
        password = self.password.get()
        if username.lower().strip() == 'rofix' and password.lower().strip() == '123456':
            showinfo('Login', 'Login successful')
            Super(self)
        else:
            showerror('Login', 'Invalid credentials')

    def open_url(self, url):
        webbrowser.open_new_tab(url)
    
    def about_the_developer(self):
        showinfo('Developer', "Rofix Work")
    
    def project_overview(self):
        showinfo("Project Overview", 'A supermarket app allows users to browse, search, and purchase groceries and household items online. It typically includes features like product categories, a shopping cart, secure payment options, and delivery tracking. The app may also offer promotions, loyalty rewards, and personalized recommendations to enhance the shopping experience.')



if __name__ == "__main__":
    App()