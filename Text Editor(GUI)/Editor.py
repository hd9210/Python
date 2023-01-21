
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser,font,messagebox,filedialog
import os


root = tk.Tk()
root.geometry('1200x800')
root.title("Editor")
root.wm_iconbitmap('icon.ico')
main_menu=tk.Menu(root)

##################### main menu ###############################

# Cascade 
file=tk.Menu(main_menu,tearoff=False)
edit=tk.Menu(main_menu,tearoff=False)
view=tk.Menu(main_menu,tearoff=False)
color_theme=tk.Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color theme",menu=color_theme)

#file icons
new_icon= tk.PhotoImage(file='icons2/new.png')
open_icon= tk.PhotoImage(file='icons2/open.png')
save_icon= tk.PhotoImage(file='icons2/save.png')
save_as_icon= tk.PhotoImage(file='icons2/save_as.png')
exit_icon= tk.PhotoImage(file='icons2/exit.png')



## Edit icon
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')

#View icon
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')

## Color Theme icon
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_plus_icon=tk.PhotoImage(file='icons2/night_blue.png')


color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_plus_icon)
theme_choice = tk.StringVar()

color_dict={'Light Default':('#000000','#ffffff'),
'Light Plus':('#474747','#e0e0e0'),'Dark':('#c4c4c4','#2d2d2d'),
'Red':('#2d2d2d','#ffe8e8'),'Monokai':('#d3b774','#474747'),
'Night Plus':('#ededed','#6b9dc2')}

##################### Toolbar ###############################

#font box
tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(11)
font_box.grid(row=0,column=0,padx=5)

# size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=15,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)

## Bold button
bold_icon=tk.PhotoImage(file='icons2/bold.png')

bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

# Italic Button
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

# Underline Button
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# Font Color Button
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

## Align Left Button

align_left_icon=tk.PhotoImage(file='icons2/al.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

## Ailgn Center Button
align_center_icon=tk.PhotoImage(file='icons2/ac.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

## Align Right Button
align_right_icon=tk.PhotoImage(file='icons2/ar.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

#####################  Text Editor ###############################

text_editor=tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font functionality

current_font_family='Arial'
current_font_size=12

def change_font(root):
       global current_font_family
       current_font_family=font_family.get()
       text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(root):
       global current_font_size
       current_font_size=size_var.get()
       text_editor.configure(font=(current_font_family,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_font_size)
font_box.bind("<<ComboboxSelected>>",change_font)

text_editor.configure(font=('Arial',12))


# Buttons Functionality

# Bold
def bold():
       b=tk.font.Font(font=text_editor['font']).actual()
       if b['weight']=='normal':
              text_editor.configure(font=(current_font_family,current_font_size,'bold'))
       if b['weight']=='bold':
              text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=bold)

#Italic
def italic():
       b=tk.font.Font(font=text_editor['font']).actual()
       if b['slant']=='roman':
              text_editor.configure(font=(current_font_family,current_font_size,'italic'))
       if b['slant']=='italic':
              text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=italic)

# Under Line 
def underline():
       b=tk.font.Font(font=text_editor['font']).actual()
       if b['underline']==0:
              text_editor.configure(font=(current_font_family,current_font_size,'underline'))
       if b['underline']==1:
              text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=underline)


# Font Color

def change_font_color():
       color_var=tk.colorchooser.askcolor()
       text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)


## Align Left 

def align_left():
       text_content=text_editor.get(1.0,'end')
       text_editor.tag_config('left',justify=tk.LEFT)
       text_editor.delete(1.0,tk.END)
       text_editor.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command=align_left)

## Align Center 

def align_center():
       text_content=text_editor.get(1.0,'end')
       text_editor.tag_config('center',justify=tk.CENTER)
       text_editor.delete(1.0,tk.END)
       text_editor.insert(tk.INSERT,text_content,'center')
align_center_btn.configure(command=align_center)

## Align Right

def align_right():
       text_content=text_editor.get(1.0,'end')
       text_editor.tag_config('right',justify=tk.RIGHT)
       text_editor.delete(1.0,tk.END)
       text_editor.insert(tk.INSERT,text_content,'right')
align_right_btn.configure(command=align_right)

##################### Status Bar ###############################

status_bar=ttk.Label(root,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed= False
def changed(event=None):
       global text_changed
       if text_editor.edit_modified():
              text_changed=True
              words=len(text_editor.get(1.0,'end-1c').split())
              characters=len(text_editor.get(1.0,'end-1c'))
              status_bar.config(text=f' Characters : {characters} Words : {words}')
       text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)


##################### Addition Functionality ###############################

# Global Variable
url=''

# new 
def new_file(event=None):
       global url
       url=''
       text_editor.delete(1.0,tk.END)

# open

def open_file(event=None):
       global url
       url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('Pdf File','*.pdf'),('All Files','*.*')))
       try:
              with open(url,'r') as fr:
                     text_editor.delete(1.0,tk.END)
                     text_editor.insert(1.0,fr.read())
       except FileNotFoundError:
              return
       except:
              return
       root.title(os.path.basename(url))

# Save

def save_file(event=None):
       global url
       try:
              if url:
                     content=str(text_editor.get(1.0,tk.END))
                     with open(url,'w',encoding='utf-8') as fw:
                            fw.write(content)
              else:
                     url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('Pdf File','*.pdf'),('All Files','*.*')))
                     content2=text_editor.get(1.0,tk.END)
                     url.write(content2)
                     url.close()
       except:
              return

# Save As
def save_as(event=None):
       global url
       try:
              content=str(text_editor.get(1.0,tk.END))
              url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('Pdf File','*.pdf'),('All Files','*.*')))
              url.write(content)
              url.close()
       except:
              return

## Exit 

def exit_file(event=None):
       global url,text_changed
       try:
              if text_changed:
                     mbox = messagebox.askyesnocancel('Warning','Do you want to save the file ?')
                     if mbox is True:
                            if url:
                                   content=text_editor.get(1.0,tk.END)
                                   with open(url,'w','utf-8') as fw:
                                          fw.write(content)
                                          root.destroy()
                            else:
                                   content2=str(text_editor.get(1.0,tk.END))
                                   url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('Pdf File','*.pdf'),('All Files','*.*')))
                                   url.write(content2)
                                   url.close()
                                   root.destroy()
                     elif mbox is False:
                            root.destroy()
              else:
                     root.destroy()
       
       except:
              return
                            

       

#File Commands

file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator = 'Ctrl+N',command=new_file)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator = 'Ctrl+O',command=open_file)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator = 'Ctrl+S',command=save_file)
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator = 'Ctrl+ALT+S',command=save_as)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator = 'Ctrl+Q',command=exit_file)

# Find

def find_func(event=None):
       def find():
              word=find_input.get()
              text_editor.tag_remove('match','1.0',tk.END)
              matches=0
              if word:
                     start_pos='1.0'
                     while True:
                            start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                            if not start_pos:
                                   break
                            end_pos=f'{start_pos}+{len(word)}c'
                            text_editor.tag_add('match',start_pos,end_pos)
                            matches+=1
                            start_pos=end_pos
                            text_editor.tag_config('match',foreground='red',background='yellow')


# Replace       
       
       def replace(): 
              word=find_input.get()
              replace_text=replace_input.get()
              content=text_editor.get(1.0,tk.END)
              new_content=content.replace(word,replace_text)
              text_editor.delete(1.0,tk.END)
              text_editor.insert(1.0,new_content)

       find_dialog=tk.Toplevel()
       find_dialog.geometry("450x200+500+200")
       find_dialog.title("Find")
       find_dialog.resizable(0,0)

       #frame

       find_frame=ttk.LabelFrame(find_dialog,text='Find/Replace')
       find_frame.pack(pady=20)
       text_find_label=ttk.Label(find_frame,text='Find : ')
       text_replace_label=ttk.Label(find_frame,text='Replace : ')

       find_input=ttk.Entry(find_frame,width=30)
       replace_input=ttk.Entry(find_frame,width=30)

       find_btn=ttk.Button(find_frame,text='Find',command=find)
       replace_btn=ttk.Button(find_frame,text='Replace',command=replace)

       text_find_label.grid(row=0,column=0,padx=4,pady=4)
       text_replace_label.grid(row=1,column=0,padx=4,pady=4)

       find_input.grid(row=0,column=1,padx=4,pady=4)
       replace_input.grid(row=1,column=1,padx=4,pady=4)

       find_btn.grid(row=2,column=0 , padx=8,pady =4)
       replace_btn.grid(row=2,column=1, padx=8,pady =4)

       
       find_dialog.mainloop()




# Edit Commands
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

#View Commands

show_toolbar=tk.BooleanVar()
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar.set(True)

def hide_toolbar():
       global show_toolbar
       if show_toolbar:
              tool_bar.pack_forget()
              show_toolbar=False
       else:
              text_editor.pack_forget()
              status_bar.pack_forget()
              tool_bar.pack(side=tk.TOP,fill=tk.X)
              text_editor.pack(fill=tk.BOTH,expand=True)
              status_bar.pack(side=tk.BOTTOM)
              show_toolbar=True

def hide_statusbar():
              global show_statusbar
              if show_statusbar:
                     status_bar.pack_forget()
                     show_statusbar=False
              
              else:
                     status_bar.pack(side=tk.BOTTOM)
                     show_statusbar=True



view.add_checkbutton(label="ToolBar",image=tool_bar_icon,onvalue=True,variable=show_toolbar,offvalue=0,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="StatusBar",image=status_bar_icon,onvalue=True,variable=show_statusbar,offvalue=0,compound=tk.LEFT,command=hide_statusbar)



## Color_theme Commands
count=0
def change_theme():
       chosen_theme=theme_choice.get()
       color_tuple=color_dict.get(chosen_theme)
       fg_color=color_tuple[0]
       bg_color=color_tuple[1]
       text_editor.config(background=bg_color,fg=fg_color)

for i in color_dict:
       color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
       count+=1
##***************************************************************************##


root.config(menu=main_menu)

## Bind Shortcut Keys

root.bind('<Control-n>',new_file)
root.bind('<Control-o>',open_file)
root.bind('<Control-s>',save_file)
root.bind('<Control-Alt-s>',save_as)
root.bind('<Control-q>',exit_file)

root.mainloop()
