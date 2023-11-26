from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
from roboflow import Roboflow

# Main Window & Configuration
window = tk.Tk()
window.title("Traffic violation Detection")
window.geometry('1000x700')

# top label
message = tk.Label(text="Traffic violation Detection system", bg="black", fg="white", width=38,height=3, font=('times', 30, ' bold '))
message.place(x=35, y=20)

# function defined to start the main application
# created a start button
def start_fun():
    window.destroy()
Button(window, text="▶ START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", cursor="hand2", borderwidth=3, relief="raised").place(x =150 , y =500 )


exit1 = False
# function created for exiting from window
# exit button created
def exit_win():
    global exit1
    exit1 = True
    window.destroy()
Button(window, text="❌ EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", cursor="hand2", borderwidth=3, relief="raised").place(x =680 , y = 500 )

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()



if exit1==False:
    filename1=""
    # Main Window & Configuration of window1
    window1 = tk.Tk()
    window1.title("Traffic violation Detection system")
    window1.geometry('1000x700')

    # ---------------------------- image section ------------------------------------------------------------
    def image_option():
        window1.destroy()
        # new windowi created for image section
        windowi = tk.Tk()
        windowi.title("Traffic violation Detection system")
        windowi.geometry('1000x700')

        # function defined to open the image
        def open_img():
            global filename1

            filename1 = filedialog.askopenfilename(title="Select Image file", parent = windowi)
            path_text1.delete("1.0", "end")
            path_text1.insert(END, filename1)

        # function defined to detect the image
        def det_img():
            global filename1

            image_path = filename1
            if(image_path==""):
                mbox.showerror("Error", "No Image File Selected!", parent = windowi)
                return
            
            info1.config(text="Status : Detecting...")
            rf = Roboflow(api_key="5iv8W4pYjIcNJW4IK0I8")
            project = rf.workspace().project("team-8-cse1-vnrvjiet")
            model = project.version(1).model
            pred =  model.predict(image_path, confidence=40, overlap=30).json()
            print(pred)
            info1.config(text="Status : Detected...")
            try:
                mbox.showinfo("Verdict", {pred['predictions'][0]['class']})
            except:
                mbox.showinfo("Verdict", "nothing is detected")

        def prev_img():
            global filename1
            img = cv2.imread(filename1, 1)
            cv2.imshow("Selected Image Preview", img)

        # for images ----------------------
        lbl1 = tk.Label(windowi,text="DETECT  FROM\nIMAGE", font=("Arial", 50, "underline"),fg="brown")
        lbl1.place(x=230, y=20)
        lbl2 = tk.Label(windowi,text="Selected Image", font=("Arial", 30),fg="green")
        lbl2.place(x=80, y=200)
        path_text1 = tk.Text(windowi, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
        path_text1.place(x=80, y = 260)

        Button(windowi, text="SELECT", command=open_img, cursor="hand2", font=("Arial", 20), bg="light green", fg="blue").place(x=220, y=350)
        Button(windowi, text="PREVIEW",command=prev_img, cursor="hand2", font=("Arial", 20), bg = "yellow", fg = "blue").place(x = 410, y = 350)
        Button(windowi, text="DETECT",command=det_img, cursor="hand2", font=("Arial", 20), bg = "orange", fg = "blue").place(x = 620, y = 350)

        info1 = tk.Label(windowi,font=( "Arial", 30),fg="gray")
        info1.place(x=100, y=430)

    # options -----------------------------
    lbl1 = tk.Label(text="OPTIONS", font=("Arial", 50, "underline"),fg="brown")  # same way bg
    lbl1.place(x=340, y=20)

    # image on the main window
    # pathi = "Images\image1.jpg"
    # imgi = ImageTk.PhotoImage(Image.open(pathi))
    paneli = tk.Label(window1)
    paneli.place(x = 90, y = 110)

    # created button for all three option
    Button(window1, text="DETECT  FROM   IMAGE ➡",command=image_option, cursor="hand2", font=("Arial",30), bg = "light green", fg = "blue").place(x = 350, y = 150)

    # function defined to exit from window1
    def exit_win1():
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            window1.destroy()

    # created exit button
    Button(window1, text="❌ EXIT",command=exit_win1,  cursor="hand2", font=("Arial", 25), bg = "red", fg = "blue").place(x = 440, y = 600)

    window1.protocol("WM_DELETE_WINDOW", exit_win1)
    window1.mainloop()
