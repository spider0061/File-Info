from tkinter import *
from tkinter.filedialog import askopenfile 
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from nltk import tokenize

global h1,h2,h3,h4,h5,h6,panel
fileadd=""
original_content=""
matched_sentences=""

def open_file(arg):
    if(arg==1): 
      file = askopenfile(mode ='r', filetypes=[("Text files","*.txt")]) 
      global fileadd
      fileadd=file.name
    else:
      file=open(str(fileadd),"r")
    if file is not None: 
        content = file.read() 
    file_content=content
    global original_content
    original_content=content
    file_content_sentences=content
    common_words=['the','of','is','in','at','and','you','that','was']
    dic=dict()
    for word in file_content.split():
      if word in dic.keys(): 
        dic[word] += 1
      else: 
        dic[word] = 1
    minstr=""
    maxstr=""
    mi=100000;
    ma=0;
    for key in dic.keys():
      if(dic[key]<mi and (key not in common_words)):
       mi=dic[key]
       minstr=key
      
      if(dic[key]>ma and (key not in common_words)):
       ma=dic[key]
       maxstr=key
    h1.config(text=str(content.count('.')))
    h2.config(text=str(content.count('\n')))
    h3.config(text=str(len(content.split())))
    h4.config(text=maxstr)
    h5.config(text=minstr)
    plt.bar(dic.keys(), dic.values(),color='g')
    plt.xticks(rotation='vertical')
    plt.savefig('histo.png',dpi=100)
    img2 =Image.open("histo.png")
    img2=img2.resize((600,300),Image.ANTIALIAS)
    img2= ImageTk.PhotoImage(img2)
    panel.config(image=img2)
    panel.image = img2

def open_keyword_file():
	file = askopenfile(mode ='r', filetypes=[("Text files","*.txt")]) 
	global content
  if file is not None: 
      content = file.read() 
  keywords=content.split('\n')
  global original_content
  sentences=tokenize.sent_tokenize(original_content)
  global matched_sentences
  matched_sentences=""
  for word in keywords:
    if(word==''):
      break
    else:
      for senten in sentences:
        if(word in senten):
          matched_sentences=matched_sentences+str(senten)+'\n'
  h6.config(text=matched_sentences)

def close_window(root): 
    root.destroy()

root = Tk()
root.geometry("800x800")
btn1 = Button(root, text ='Open', command = lambda:open_file(1)) 
btn1.pack(side=LEFT, anchor=NW,pady=2)
btn2 = Button(root, text ='Refresh', command = lambda:open_file(2)) 
btn2.pack(side=LEFT, anchor=NW,pady=2)
btn3 = Button(root, text ='Close', command = lambda:close_window(root)) 
btn3.pack(side=RIGHT,anchor=NW,pady=2)

h1h= Label(root,text="Number of Sentences:");
h1h.pack(pady=2)
h1= Label(root,text="");
h1.pack(pady=2)

h2h= Label(root,text="Number of New Lines:");
h2h.pack(pady=2)
h2= Label(root,text="");
h2.pack(pady=2)

h3h= Label(root,text="Number of Words:");
h3h.pack(pady=2)
h3= Label(root,text="");
h3.pack(pady=2)

h4h= Label(root,text="Most occurring word:");
h4h.pack(pady=2)
h4= Label(root,text="");
h4.pack(pady=2)

h5h= Label(root,text="Least occurring word:");
h5h.pack(pady=2)
h5= Label(root,text="");
h5.pack(pady=2)

img =Image.open("sample.jpg")
img=img.resize((200,200),Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(root, image=img,width=200)
panel.pack(side=TOP,anchor=NE,fill="both")

btn4 = Button(root, text ='Open Keywords File', command = lambda:open_keyword_file()) 
btn4.pack(pady=2)

h6h= Label(root,text="Matched Sentences from the given input file are:");
h6h.pack(pady=2)
h6= Label(root,text="");
h6.pack(pady=2)

root.mainloop()
