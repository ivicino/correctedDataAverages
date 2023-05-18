# Need to get averages from corrected data (data - mean) and uncorrected data
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import warnings
# Ignore future warnings:
warnings.simplefilter('ignore')

''' Constants'''
# Constants used for the GUI colors
Blue = '#87B7E1'
Red = '#D0281A'
Grey = "#D6DADE"

root=tk.Tk(screenName="Ian's window")
root.config(background = Grey)

frame = tk.Frame(root, bg = Grey)
frame.pack()

# Attempt to change tkinter theme
style = ttk.Style(root)
style.theme_use('classic')  # I like the classic theme

# declaring string variable for the file path and answers to questions
col = tk.IntVar()
nameList = [0]  
colList = [0]

listaver02D1 = []
listaver02D2 = []
listaver02D3 = []
listaver02D4 = []

listaver01D1 = []
listaver01D2 = []
listaver01D3 = []
listaver01D4 = []

listaver005D1 = []
listaver005D2 = []
listaver005D3 = []
listaver005D4 = []

listaver001D1 = []
listaver001D2 = []
listaver001D3 = []
listaver001D4 = []

listaver000D1 = []
listaver000D2 = []
listaver000D3 = []
listaver000D4 = []

"""_______________________________________________________________________________"""

# Function for opening the file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "c:\\",
                                          title = "Select a File",
                                          filetypes = (("Excel files",
                                                        "*.xlsx*"),
                                                        ))
    label_file_explorer.configure(text="File Opened: "+filename)
    nameList.append(filename)

def colnum():
    colnumber = col.get()
    print(f"Your data will come from column {colnumber}")
    colList.append(colnumber)
    X = colList[-1] 
    return X

def submit():

    X = colnum()    # makes X = the column number... 

    loadfile = str(nameList[-1])
    # loadfile = '.' + loadfile[17:]
    print("Your excel file path is : " + loadfile)
    df = pd.DataFrame(pd.read_excel(loadfile))
    # print(df)


    #02
    aver1 = df.iloc[[3, 4, 5], [X]].mean()
    for i in aver1:
        listaver02D1.append(i)
    aver2 = df.iloc[[63, 64, 65], [X]].mean()
    for i in aver2:
        listaver02D1.append(i)
    aver3 = df.iloc[[123, 124, 125], [X]].mean()
    for i in aver3:
        listaver02D1.append(i)
    aver4 = df.iloc[[183, 184, 185], [X]].mean()
    for i in aver4:
        listaver02D1.append(i)

    aver11 = df.iloc[[6, 7, 8], [X]].mean()
    for i in aver11:
        listaver02D2.append(i)
    aver21 = df.iloc[[66, 67, 68], [X]].mean()
    for i in aver21:
        listaver02D2.append(i)
    aver31 = df.iloc[[126, 127, 128], [X]].mean()
    for i in aver31:
        listaver02D2.append(i)
    aver41 = df.iloc[[186, 187, 188], [X]].mean()
    for i in aver41:
        listaver02D2.append(i)

    aver12 = df.iloc[[9, 10, 11], [X]].mean()
    for i in aver12:
        listaver02D3.append(i)
    aver22 = df.iloc[[69, 70, 71], [X]].mean()
    for i in aver22:
        listaver02D3.append(i)
    aver32 = df.iloc[[129, 130, 131], [X]].mean()
    for i in aver32:
        listaver02D3.append(i)
    aver42 = df.iloc[[189, 190, 191], [X]].mean()
    for i in aver42:
        listaver02D3.append(i)

    aver13 = df.iloc[[12, 13, 14], [X]].mean()
    for i in aver13:
        listaver02D4.append(i)
    aver23 = df.iloc[[72, 73, 74], [X]].mean()
    for i in aver23:
        listaver02D4.append(i)
    aver33 = df.iloc[[132, 133, 134], [X]].mean()
    for i in aver33:
        listaver02D4.append(i)
    aver43 = df.iloc[[192, 193, 194], [X]].mean()
    for i in aver43:
        listaver02D4.append(i)


    # 01
    aver101 = df.iloc[[15, 16, 17], [X]].mean()
    for i in aver101:
        listaver01D1.append(i)
    aver201 = df.iloc[[75, 76, 77], [X]].mean()
    for i in aver201:
        listaver01D1.append(i)
    aver301 = df.iloc[[135, 136, 137], [X]].mean()
    for i in aver301:
        listaver01D1.append(i)
    aver401 = df.iloc[[195, 196, 197], [X]].mean()
    for i in aver401:
        listaver01D1.append(i)

    aver1101 = df.iloc[[18, 19, 20], [X]].mean()
    for i in aver1101:
        listaver01D2.append(i)
    aver2101 = df.iloc[[78, 79, 80], [X]].mean()
    for i in aver2101:
        listaver01D2.append(i)
    aver3101 = df.iloc[[138, 139, 140], [X]].mean()
    for i in aver3101:
        listaver01D2.append(i)
    aver4101 = df.iloc[[198, 199, 200], [X]].mean()
    for i in aver4101:
        listaver01D2.append(i)

    aver1201 = df.iloc[[21, 22, 23], [X]].mean()
    for i in aver1201:
        listaver01D3.append(i)
    aver2201 = df.iloc[[81, 82, 83], [X]].mean()
    for i in aver2201:
        listaver01D3.append(i)
    aver3201 = df.iloc[[141, 142, 143], [X]].mean()
    for i in aver3201:
        listaver01D3.append(i)
    aver4201 = df.iloc[[201, 202, 203], [X]].mean()
    for i in aver4201:
        listaver01D3.append(i)

    aver1301 = df.iloc[[24, 25, 26], [X]].mean()
    for i in aver1301:
        listaver01D4.append(i)
    aver2301 = df.iloc[[84, 85, 86], [X]].mean()
    for i in aver2301:
        listaver01D4.append(i)
    aver3301 = df.iloc[[144, 145, 146], [X]].mean()
    for i in aver3301:
        listaver01D4.append(i)
    aver4301 = df.iloc[[204, 205, 206], [X]].mean()
    for i in aver4301:
        listaver01D4.append(i)


    #005
    aver1005 = df.iloc[[27, 28, 29], [X]].mean()
    for i in aver1005:
        listaver005D1.append(i)
    aver2005 = df.iloc[[87, 88, 89], [X]].mean()
    for i in aver2005:
        listaver005D1.append(i)
    aver3005 = df.iloc[[147, 148, 149], [X]].mean()
    for i in aver3005:
        listaver005D1.append(i)
    aver4005 = df.iloc[[207, 208, 209], [X]].mean()
    for i in aver4005:
        listaver005D1.append(i)

    aver11005 = df.iloc[[30, 31, 32], [X]].mean()
    for i in aver11005:
        listaver005D2.append(i)
    aver21005 = df.iloc[[90, 91, 92], [X]].mean()
    for i in aver21005:
        listaver005D2.append(i)
    aver31005 = df.iloc[[150, 151, 152], [X]].mean()
    for i in aver31005:
        listaver005D2.append(i)
    aver41005 = df.iloc[[210, 211, 212], [X]].mean()
    for i in aver41005:
        listaver005D2.append(i)

    aver12005 = df.iloc[[33, 34, 35], [X]].mean()
    for i in aver12005:
        listaver005D3.append(i)
    aver22005 = df.iloc[[93, 94, 95], [X]].mean()
    for i in aver22005:
        listaver005D3.append(i)
    aver32005 = df.iloc[[153, 154, 155], [X]].mean()
    for i in aver32005:
        listaver005D3.append(i)
    aver42005 = df.iloc[[213, 214, 215], [X]].mean()
    for i in aver42005:
        listaver005D3.append(i)

    aver13005 = df.iloc[[36, 37, 38], [X]].mean()
    for i in aver13005:
        listaver005D4.append(i)
    aver23005 = df.iloc[[96, 97, 98], [X]].mean()
    for i in aver23005:
        listaver005D4.append(i)
    aver33005 = df.iloc[[156, 157, 158], [X]].mean()
    for i in aver33005:
        listaver005D4.append(i)
    aver43005 = df.iloc[[216, 217, 218], [X]].mean()
    for i in aver43005:
        listaver005D4.append(i)


    #001
    aver1001 = df.iloc[[39, 40, 41], [X]].mean()
    for i in aver1001:
        listaver001D1.append(i)
    aver2001 = df.iloc[[99, 100, 101], [X]].mean()
    for i in aver2001:
        listaver001D1.append(i)
    aver3001 = df.iloc[[159, 160, 161], [X]].mean()
    for i in aver3001:
        listaver001D1.append(i)
    aver4001 = df.iloc[[219, 220, 221], [X]].mean()
    for i in aver4001:
        listaver001D1.append(i)

    aver11001 = df.iloc[[42, 43, 44], [X]].mean()
    for i in aver11001:
        listaver001D2.append(i)
    aver21001 = df.iloc[[102, 103, 104], [X]].mean()
    for i in aver21001:
        listaver001D2.append(i)
    aver31001 = df.iloc[[162, 163, 164], [X]].mean()
    for i in aver31001:
        listaver001D2.append(i)
    aver41001 = df.iloc[[222, 223, 224], [X]].mean()
    for i in aver41001:
        listaver001D2.append(i)

    aver12001 = df.iloc[[45, 46, 47], [X]].mean()
    for i in aver12001:
        listaver001D3.append(i)
    aver22001 = df.iloc[[105, 106, 107], [X]].mean()
    for i in aver22001:
        listaver001D3.append(i)
    aver32001 = df.iloc[[165, 166, 167], [X]].mean()
    for i in aver32001:
        listaver001D3.append(i)
    aver42001 = df.iloc[[225, 226, 227], [X]].mean()
    for i in aver42001:
        listaver001D3.append(i)

    aver13001 = df.iloc[[48, 49, 50], [X]].mean()
    for i in aver13001:
        listaver001D4.append(i)
    aver23001 = df.iloc[[108, 109, 110], [X]].mean()
    for i in aver23001:
        listaver001D4.append(i)
    aver33001 = df.iloc[[168, 169, 170], [X]].mean()
    for i in aver33001:
        listaver001D4.append(i)
    aver43001 = df.iloc[[228, 229, 230], [X]].mean()
    for i in aver43001:
        listaver001D4.append(i)


    #000
    aver1000 = df.iloc[[51, 52, 53], [X]].mean()
    for i in aver1000:
        listaver000D1.append(i)
    aver2000 = df.iloc[[111, 112, 113], [X]].mean()
    for i in aver2000:
        listaver000D1.append(i)
    aver3000 = df.iloc[[171, 172, 173], [X]].mean()
    for i in aver3000:
        listaver000D1.append(i)
    aver4000 = df.iloc[[231, 232, 233], [X]].mean()
    for i in aver4000:
        listaver000D1.append(i)

    aver11000 = df.iloc[[54, 55, 56], [X]].mean()
    for i in aver11000:
        listaver000D2.append(i)
    aver21000 = df.iloc[[114, 115, 116], [X]].mean()
    for i in aver21000:
        listaver000D2.append(i)
    aver31000 = df.iloc[[174, 175, 176], [X]].mean()
    for i in aver31000:
        listaver000D2.append(i)
    aver41000 = df.iloc[[234, 235, 236], [X]].mean()
    for i in aver4000:
        listaver000D2.append(i)

    aver12000 = df.iloc[[57, 58, 59], [X]].mean()
    for i in aver12000:
        listaver000D3.append(i)
    aver22000 = df.iloc[[117, 118, 119], [X]].mean()
    for i in aver22000:
        listaver000D3.append(i)
    aver32000 = df.iloc[[177, 178, 179], [X]].mean()
    for i in aver32000:
        listaver000D3.append(i)
    aver42000 = df.iloc[[237, 238, 239], [X]].mean()
    for i in aver42000:
        listaver000D3.append(i)

    aver13000 = df.iloc[[60, 61, 62], [X]].mean()
    for i in aver13000:
        listaver000D4.append(i)
    aver23000 = df.iloc[[120, 121, 122], [X]].mean()
    for i in aver23000:
        listaver000D4.append(i)
    aver33000 = df.iloc[[180, 181, 182], [X]].mean()
    for i in aver33000:
        listaver000D4.append(i)
    aver43000 = df.iloc[[240, 241, 242], [X]].mean()
    for i in aver43000:
        listaver000D4.append(i)

    '''End of Submit function'''

def RunProg():
    print('\n 0.2 Data:______________________________________\n')
    print( ' '.join(map(str, listaver02D1)))
    
    print( ' '.join(map(str, listaver02D2)))
    
    print( ' '.join(map(str, listaver02D3)))
    
    print( ' '.join(map(str, listaver02D4)))

    print('\n end 0.2______________________________________\n')

    print('\n 0.1 Data:______________________________________\n')
    print( ' '.join(map(str, listaver01D1)))
    
    print( ' '.join(map(str, listaver01D2)))
    
    print( ' '.join(map(str, listaver01D3)))
    
    print( ' '.join(map(str, listaver01D4)))

    print('\n end 0.1______________________________________\n')

    print('\n 0.05 Data:______________________________________\n')
    print( ' '.join(map(str, listaver005D1)))
    
    print( ' '.join(map(str, listaver005D2)))
    
    print( ' '.join(map(str, listaver005D3)))
    
    print( ' '.join(map(str, listaver005D4)))

    print('\n end 0.05______________________________________\n')

    print('\n 0.01 Data:______________________________________\n')
    print( ' '.join(map(str, listaver001D1)))
    
    print( ' '.join(map(str, listaver001D2)))
    
    print( ' '.join(map(str, listaver001D3)))
    
    print( ' '.join(map(str, listaver001D4)))

    print('\n end 0.01______________________________________\n')

    print('\n 0.00 Data:______________________________________\n')
    print( ' '.join(map(str, listaver000D1)))
    
    print( ' '.join(map(str, listaver000D2)))
    
    print( ' '.join(map(str, listaver000D3)))
    
    print( ' '.join(map(str, listaver000D4)))

    print('\n end 0.00______________________________________\n')

def cleararray():
    listaver02D1.clear()
    listaver02D2.clear()
    listaver02D3.clear()
    listaver02D4.clear()

    listaver01D1.clear()
    listaver01D2.clear()
    listaver01D3.clear()
    listaver01D4.clear()

    listaver005D1.clear()
    listaver005D2.clear()
    listaver005D3.clear()
    listaver005D4.clear()

    listaver001D1.clear()
    listaver001D2.clear()
    listaver001D3.clear()
    listaver001D4.clear()

    listaver000D1.clear()
    listaver000D2.clear()
    listaver000D3.clear()
    listaver000D4.clear()

    print('Array\'s have been nuked!!!!')


#%% Putting frames in the TK window

# Create a File Explorer label
label_file_explorer = tk.Label(frame, text = "Find your file :)", width = 100, height = 1,fg = "white", bg = 'black')
button_explore = tk.Button(frame, text = "Browse Files", command = browseFiles)
# Button that will call the Submit function for the file browser
Enter = tk.Button(frame, text = 'Enter Excel File', command = submit)


colText = tk.Label(frame, text = "What column is your data in?",bg = Blue ,fg = "black", font=('calibre',10,'normal'))
colEntery = tk.Entry(frame, textvariable = col, font = ('calibre',10,'normal'), bg="white", fg = 'black')
Enter2 = tk.Button(frame, text = 'Enter column number', command = colnum)

Run_button = tk.Button(root, text = 'Run Program', command = RunProg)

clearButton = tk.Button(frame, text = 'Clear the arrays.', command = cleararray)

#%% Place the widgets on to the window
clearButton.grid(row = 0, column=0)
colText.grid(row = 2, column=0)
colEntery.grid(row = 3, column=0)
Enter2.grid(row = 4, column=0)

label_file_explorer.grid(row = 5, column = 0)
button_explore.grid(row = 6, column = 0)
Enter.grid(row = 7, column = 0)

Run_button.pack(pady=20)



root.mainloop()

