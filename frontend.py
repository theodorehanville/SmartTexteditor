# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:42:33 2020

@author: Theodore Hanville Anyika
"""
#importing modules
import tkinter as tk
import backend
from tkinter import filedialog
from tkinter import messagebox


# menubar
class MenuBar():
    
    """
    This class creates the Menubar. Its attributes are various functionalities on the meny bar. Its parent class
    is the SmartEditor class.
    """
    
    def __init__(self,parent):
        font_specs = ('ubuntu',7) # setting font
        
        # initializing menubar
        menubar = tk.Menu(parent.window, font=font_specs)
        parent.window.config(menu=menubar)
        
        # initializing drop downs
        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        Edit_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        read_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        listen_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        
        # setting commands
        file_dropdown.add_command(label="New File",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open File",
                                   accelerator="Ctrl+O",
                                   command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                   accelerator="Ctrl+s",
                                   command=parent.save)
        file_dropdown.add_command(label="Save As",
                                   accelerator="Ctrl+Shift+S",
                                   command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  command=parent.window.destroy)
        
        about_dropdown.add_command(label="Release Notes",
                                   command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="About",
                                   command=self.show_about_message)
        
        # adding cascades
        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="Edit")
        menubar.add_cascade(label="Read")
        menubar.add_cascade(label="Listen")
        menubar.add_cascade(label="About",menu=about_dropdown)
        
        
    def show_about_message(self):
        box_title = "About SmartEditor"
        box_message = "Smart text editor"
        messagebox.showinfo(box_title,box_message)
        
    def show_release_notes(self):
        box_title = "Version 1.0"
        box_message = "Created by Theodore Hanville Anyika"
        messagebox.showinfo(box_title,box_message)
        
        

# statusbar
class StatusBar():
    
    """
    This class houses the status bar.
    """
    
    def __init__(self,parent):
        
        font_specs = ('Times New Roman',10)     # initializing font
        
        # initializing attributes
        self.status = tk.StringVar()
        self.status.set("SmartEditor - 0.1")
        self.label = tk.Label(parent.textbox, textvariable=self.status, fg="black",
                         bg="lightgrey", anchor="sw", font=font_specs)
        
        # setting label position
        self.label.pack(side=tk.BOTTOM, fill=tk.BOTH)
        
    def update_status(self,*args):
        """
        Updates status bar.
        """
        if isinstance(args[0],bool):
            self.status.set("Your file has been saved")
        else:
            self.status.set("SmartEditor - 0.1")



# SmartEditor holds the root window
class SmartEditor():
    
    """
    This class houses the root window.
    """
    
    def __init__(self,window):
        
        # initializing the main window
        window.title("Untitled - SmartEditor")
        window.geometry("1000x550")
        
        # initializing attributes
        font_specs = ('Times New Roman',12)      # setting font type
        self.window = window
        self.filename = None
        self.textbox = tk.Text(window,font=font_specs)     # creating textbox
        self.scroll = tk.Scrollbar(window,command=self.textbox.yview)  # creating scrollbar
        
        # configuring attributes
        self.textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.textbox.configure(yscrollcommand=self.scroll.set)
        
        # instantiating other classes
        self.menubar = MenuBar(self)
        self.statusbar = StatusBar(self)
        self.bind_shortcourts()
        
       
    def set_windows_title(self,name=None,*args):
       
        """
        Sets window title
        
        args: None
        return: None
        """
        if name:
            self.window.title(name + " - SmartEditor")
        else:
            self.window.title("Untitled - SmartEditor")
        

    def new_file(self,*args):
        
        """
        Creates new file
        
        args: None
        return: None
        """
        self.textbox.delete(1.0,tk.END)  
        self.filename = None
        self.set_windows_title()
        
   
    def save(self,*args):
        
        """
        Saves new edits on files. Saves new file using self.save_as(), if new file hasnt been previously saved.
        
        args: None
        return: None
        """
        if self.filename:
            try:
                textbox_content = self.textbox.get(1.0,tk.END)
                with open(self.filename,"w") as f:
                    f.write(textbox_content)
                self.statusbar.update_status(True)
             
            except Exception as e:
                print(e)
        else:
            self.save_as()
        
        
    def save_as(self,*args):
        
        """
        Saves new files.
        
        args: None
        return: None
        """
        try:
            new_file  = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                                     defaultextension=".txt",
                                                   filetypes=[("All Files","*.*"),
                                                              ("Text Files","*.txt"),
                                                              ("Python Scripts","*.py"),
                                                              ("Markdown Documents","*.md"),
                                                              ("java script","*.js"),
                                                              ("HTML","*.html"),
                                                              ("CSS documents","*.css")]
        )
            textbox_content = self.textbox.get(1.0,tk.END)
            with open(new_file, "w") as f:
                f.write(textbox_content)
            self.statusbar.update_status(True)
            
            self.filename = new_file
            self.set_windows_title(self.filename)
        
                            
        except Exception as e:
            print(e)
        
    def open_file(self, *args):
        
        """
        Opens new file.
        
        args: None
        return: None
        """
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("All Files","*.*"),
                                                              ("Text Files","*.txt"),
                                                              ("Python Scripts","*.py"),
                                                              ("Markdown Documents","*.md"),
                                                              ("java script","*.js"),
                                                              ("HTML","*.html"),
                                                              ("CSS documents","*.css")]
        )
        if self.filename:
            self.textbox.delete(1.0,tk.END)
            with open(self.filename,"r") as f:
                self.textbox.insert(1.0,f.read())
            
            self.set_windows_title(self.filename)
    
    def bind_shortcourts(self,*args):
        self.textbox.bind('<Control-n>', self.new_file)
        self.textbox.bind('<Control-o>', self.open_file)
        self.textbox.bind('<Control-s>', self.save)
        self.textbox.bind('<Control-S>', self.save_as)
        self.textbox.bind('<Key>', self.statusbar.update_status)
        


if __name__=='__main__':
    # initializing GUI window
    window = tk.Tk()
    editor = SmartEditor(window)
    window.mainloop()