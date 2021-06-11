import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('chinpad text editor')
#main_application.wm_iconbitmap('icon.ico')

#**************************main menu**********************************
main_menu = tk.Menu()
############file menu#########
file_menu = tk.Menu(main_menu,tearoff=False)
#file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

#img=tk.Label(main_application,image=open_icon)

#edit menu
edit_menu = tk.Menu(main_menu,tearoff=False)

#edit icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_icon = tk.PhotoImage(file='icons2/clear_all.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

#view menu
view_menu = tk.Menu(main_menu,tearoff=False)
#icons
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

#colour theme
color_theme_menu = tk.Menu(main_menu,tearoff=False)
#icons
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')

theme_variable = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict = {
    'Light Default' : ('black','white'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Light Blue' : ('#ededed','#6b9dc2')
} 

#cascade
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)
main_menu.add_cascade(label='Colour Theme',menu=color_theme_menu)

#>>>>>>>>>>>>>>>>>>>>>>>>>>end main menu>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

############################################toool bar###########################################
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill = tk.X) 

#font box
font_tuple = tk.font.families()
fontfamily = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width = 30,textvariable=fontfamily,state="readonly" )
font_box['values']=font_tuple
font_box.current(12)
font_box.grid(row=0,column=0,padx=5)

#size box
size = tk.IntVar()
size_tuple =tuple(range(2,100,2))
size_box = ttk.Combobox(tool_bar,width =10,textvariable=size,state='readonly')
size_box['values']=size_tuple
size_box.current(5)
size_box.grid(row=0,column=1,padx=5)

#bold button
bold_icon = tk.PhotoImage(file = 'icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image = bold_icon )
bold_btn.grid(row = 0,column=2,padx =5)

#italic button
italic_icon = tk.PhotoImage(file = 'icons2/italic.png')
italic_btn = ttk.Button(tool_bar,image = italic_icon)
italic_btn.grid(row = 0,column=3,padx =5)
#under line button
underline_icon = tk.PhotoImage(file = 'icons2/underline.png')
underline_btn = ttk.Button(tool_bar,image = underline_icon)
underline_btn.grid(row = 0,column=4,padx =5)

#font color btn
font_color_icon = tk.PhotoImage(file = 'icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar,image = font_color_icon)
font_color_btn.grid(row = 0,column=5,padx =5)

#align left btn
align_left_icon = tk.PhotoImage(file = 'icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar,image = align_left_icon)
align_left_btn.grid(row = 0,column=6,padx =5)

#align center btn
align_center_icon = tk.PhotoImage(file = 'icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar,image = align_center_icon)
align_center_btn.grid(row = 0,column=7,padx =5)

#align right btn
align_right_icon = tk.PhotoImage(file = 'icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar,image = align_right_icon)
align_right_btn.grid(row = 0,column=8,padx =5)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.end tool bar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
############################################text editor#########################################
text_editor = tk.Text(main_application)
text_editor.config(wrap = "word",relief =tk.FLAT) #new line should start with a new word

scroll_bar =tk.Scrollbar(main_application)
scroll_bar.pack(side = tk.RIGHT,fill=tk.Y)
text_editor.focus_set()
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)   #connecting scroll bar to text editor
text_editor.config(yscrollcommand=scroll_bar.set) #conecting text editor to scroll bar

#text font and size functionality
current_font_family = "Arial"
current_font_size = 12

def change_font(main_application):
    global current_font_family
    current_font_family=fontfamily.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)

def change_size(main_application):
    global current_font_size
    current_font_size=size.get()
    text_editor.configure(font=(current_font_family,current_font_size))

size_box.bind('<<ComboboxSelected>>',change_size)

text_editor.configure(font=('Arial',12))

#######BUTTONS FUNCTIONALITY###### 
def change_bold():
    #print(tk.font.Font(font = text_editor['font])).actual()   -- it will give the information about the font used in the text editor
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] =='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))    
    else:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command = change_bold)

#######italic btn functionality#####
def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] =='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))    
    else:
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

italic_btn.configure(command = change_italic)

#####under line button functionality...
def change_underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] ==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))    
    else:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command = change_underline)

####################font colour functionality####

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    #print(color_var)
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

#######align functionality
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)

def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>text editor ends>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#####################################status bar#####################################################

status_bar = ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
status_bar.config(foreground = 'white',background ='black')

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        charecters = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f'Charecters:{charecters} Words:{words}') 
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)       
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>end status bar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

######################################main menu functions#############################
#files commands

##variable
url = ''

##new functionalty
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)
    main_application.title('chinpad')    

file_menu.add_command(label ="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command = new_file)

##open functions

def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetype=(('Text File','*.txt'),("All Files",'*.*')))
    try:
        with open(url) as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
            main_application.title(os.path.basename(url))  
    except FileNotFoundError:
        return
    except:
        return        
      

file_menu.add_command(label ="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+P",command=open_file)

##save functionality###

def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode ='w',defaultextension = '.txt   ',filetype=(('Text File','*.txt'),("All Files",'*.*')))     
            content2=str(text_editor.get(1.0,tk.END))
            url.write(content2)
            url.close()
    except:
    
        return


file_menu.add_command(label ="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+s",command = save_file)


#save _as functionality...

def save_as(event = None):
    global url
    try:
        url = filedialog.asksaveasfile(mode ='w',defaultextension = '.txt   ',filetype=(('Text File','*.txt'),("All Files",'*.*')))     
        content2=str(text_editor.get(1.0,tk.END))
        url.write(content2)
        url.close()
    except:
        return

file_menu.add_command(label ="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="Alt+S ",command=save_as)

#####Exit option fuctionality#####

def exit_func(event= None):
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file?')
            if mbox is True:
                save_file()
                main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()

    except:
        return                


file_menu.add_command(label ="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Q",command = exit_func)

#Edit menu commands

######find functionality#############

def find_func(event = None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos='1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground = 'red',background ='blue')        
    

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialouge = tk.Toplevel()
    find_dialouge.geometry('450x250+500+200')
    find_dialouge.title('Find/Replace')
    find_dialouge.resizable(0,0)

    #frame

    find_frame = ttk.LabelFrame(find_dialouge,text='Find/Replace')
    find_frame.pack(pady=20)

    ##labels 
    text_find_label = ttk.Label(find_frame,text = "Find : " )
    text_replace_label = ttk.Label(find_frame,text = "Replace : " )

    ##entry box
    find_input = ttk.Entry(find_frame,width = 30)
    replace_input = ttk.Entry(find_frame,width = 30)

    #buttons
    find_btn = ttk.Button(find_frame,text='Find',command=find)
    replace_btn = ttk.Button(find_frame,text='replace',command = replace)

    #Label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    #button
    find_btn.grid(row = 2,column =0 ,padx=70,pady=4)
    replace_btn.grid(row = 2,column =1 ,padx=10,pady=0)
    
    find_dialouge.mainloop()



#adding icons
edit_menu.add_command(label ="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+c",command=lambda:text_editor.event_generate("<Control c>"))
edit_menu.add_command(label ="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+x",command = lambda:text_editor.event_generate("<Control x>"))
edit_menu.add_command(label ="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit_menu.add_command(label ="Clear All",image=clear_icon,compound=tk.LEFT,accelerator="Ctrl+d",command = lambda:text_editor.delete(1.0,tk.END))
edit_menu.add_command(label ="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+f",command = find_func)

#view_menu commands
#adding  cheak buttons


show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar,show_statusbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill = tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        if show_statusbar:
            status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else :
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True


view_menu.add_checkbutton(label ="Tool Bar",onvalue=True,offvalue=0,variable = show_toolbar,  image=tool_bar_icon,compound=tk.LEFT,command = hide_toolbar)
view_menu.add_checkbutton(label ="Status Bar",onvalue=1,offvalue=False,variable = show_statusbar,  image=status_bar_icon,compound=tk.LEFT,command = hide_statusbar)

#colour theme menu commands

def change_theme():
    chosen_theme = theme_variable.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background = bg_color,fg=fg_color)



count = 0
for i in color_dict:
    color_theme_menu.add_radiobutton(label = i, image = color_icons[count], variable = theme_variable,compound=tk.LEFT,command = change_theme)
    count+=1
#.................................................end main menu..................


main_application.configure(menu = main_menu)
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Alt-s>",save_as)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)
main_application.bind("<Control-d>",lambda event = None:text_editor.delete(1.0,tk.END))





main_application.mainloop()   