from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image


class signinwindow:
    def __init__(self):
        self.signin_window = Toplevel()
        self.signin_window.title('Cadastrar Usuários | By Rafa Said')
        self.signin_window.resizable(False, False)
        self.signin_window.wm_iconbitmap('logo.ico')

        # ========== LABELS ==========
        Label(self.signin_window, text='Cadastrar', font='Ariel').grid(row=0, column=0, sticky=W, pady=10)
        Label(self.signin_window, text='Usuário', font='Ariel, 12').grid(row=1, column=0)
        Label(self.signin_window, text='Senha', font='Ariel, 12').grid(row=2, column=0, pady=(0, 20))

        # ========== CAIXAs DE TEXTO ==========
        Entry(self.signin_window, font='Ariel, 10').grid(row=1, column=1)
        Entry(self.signin_window, font='Ariel, 10').grid(row=2, column=1, pady=(0, 20))

        # ========== BUTTON ==========
        user_add = Button(self.signin_window, text='Cadastrar', font='Ariel, 15', background='white')
        user_add.grid(row=1, column=2, rowspan=2, padx=20, pady=(0, 20))

        view_existing = Button(self.signin_window, text='Visualizar cadastros', background='white')
        view_existing.grid(row=3, column=0, rowspan=2, columnspan=4, padx=20, pady=(0, 20), sticky=W + E)

        self.signin_window.mainloop()



class loginwindow:
    def __init__(self):
        self.login_window = Toplevel()
        self.login_window.title('Login | By Rafa Said')
        self.login_window.resizable(False, False)
        self.login_window.wm_iconbitmap('logo.ico')

        # ========== LABELS ==========
        Label(self.login_window, text='Login', font='Ariel').grid(row=0, column=0, sticky=W, pady=10)
        Label(self.login_window, text='Usuário', font='Ariel, 12').grid(row=1, column=0)
        Label(self.login_window, text='Senha', font='Ariel, 12').grid(row=2, column=0)

        # ========== CAIXAs DE TEXTO ==========
        self.username = Entry(self.login_window, font='Ariel, 10').grid(row=1, column=1)
        #a função show='*' mostra um * enquanto a senha estiver sendo digitada
        self.password = Entry(self.login_window, font='Ariel, 10', show='*').grid(row=2, column=1)

        # ========== RADIO BUTTON ==========
        Radiobutton(self.login_window, text='Usuário', value=1).grid(row=3, column=0, pady=15)
        Radiobutton(self.login_window, text='Administrador', value=1).grid(row=3, column=1)

        # ========== BUTTON ==========
        self.but = Button(self.login_window, text='Entrar', font='Ariel, 17')
        self.but.grid(row=1, column=2, rowspan=2, pady=20)

        self.login_window.mainloop()


class mainwindow():

    # função para informações sobre o desenvolvedor
    def about_us(self):
        messagebox.showinfo('rafasaid@gmail.com',
                            'Este aplicativo para gerenciamento de alunos foi criado por \n\nRafael Said (rafasaid@gmail.com)\n\nProgramador em:\n\nPython\n\nJava\n\nAndroid\n\n\n')

    # função para entrar
    def create_signin(self):
        try:
            signinwindow()
        except:
            raise Exception('Não foi possível abrir este formulário!')

    # função para o login
    def create_login(self):
        try:
            loginwindow()
        except:
            raise Exception('Não foi possível abrir o formulário!')

    # função para abrir o help em um navegador
    def helpp(self):
        import os, webbrowser
        from urllib.request import pathname2url
        url = 'file:{}'.format(pathname2url(os.path.abspath('help.html')))
        webbrowser.open(url)

    # função para fechar a janela
    def quit_window(self):
        if messagebox.askokcancel('rafasaid@gmail.com', 'Deseja realmente sair?'):
            self.root.destroy()


    def __init__(self):
        # ========== Configurações da janela principal ==========
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.quit_window)
        self.root.wm_iconbitmap('logo.ico')
        self.root.title('Cadastro de alunos | By Rafa Said')
        # configurações da imagem de fundo
        self.img = ImageTk.PhotoImage(Image.open('logo.png'))
        self.panel = Label(self.root, image = self.img)
        self.panel.grid(row=0, column=0)

        # ========== LABELS ==========
        Label(self.root, text='RAFA SAID', font='Times, 20', foreground='blue').grid(row=1, column=0, sticky=W+E, padx=40)

        Label(self.root, text='Cadastro de Alunos', font='Times, 29', foreground='red4').grid(row=2, column=0, sticky=W+E, padx=40)

        Label(self.root, text='By rafasaid@gmail.com', font='Arial, 12').grid(row=3, column=0, columnspan=2, sticky=W+E, pady=20)

        Label(self.root, text='Fazer login para continuar', font='Arial, 18').grid(row=4, column=0, columnspan=2, sticky=W+E, pady=5)

        # ========== BOTÕES ==========
        self.but = Button(self.root, text='LOGIN', command=self.create_login)
        self.but.configure(width=18, height=2, foreground='white', background='orange4')
        self.but.grid(row=5, column=0, columnspan=2, sticky=N, pady=30)

        # ========== MENU ==========
        self.menu_bar = Menu(self.root)
        self.menu_bar.add_separator()

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Entrar', command=self.create_signin)
        self.file_menu.add_separator()

        self.file_menu.add_command(label='Sair', command=self.quit_window)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.menu_bar.add_separator()

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='Ajuda', command=self.helpp)
        self.help_menu.add_separator()
        self.help_menu.add_command(label='Sobre', command=self.about_us)
        self.menu_bar.add_cascade(label='Ajuda', menu=self.help_menu)

        self.root.configure(menu=self.menu_bar)
        self.root.mainloop()


        self.root.mainloop()

try:
    mainwindow()
except:
    raise Exception('A janela não pode ser criada!')