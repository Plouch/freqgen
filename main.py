import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana",12)


class FreqApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, "Frequency generator")
		container = tk.Frame(self)
		self.geometry("550x300")
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		frame = StartPage(container, self)
		self.frames[StartPage] = frame

		frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

def checkAll(freq):
	for i in freq:
		if len(i)<3 and freq["check"].get()==1 :freq[i].set(1)
		elif len(i)<3 and freq["check"].get()==0 :freq[i].set(0)

def freqGen(freq,frequence):
	frequency = ""
	if freq["weekly"].get()==1:frequency+="W-"
	
	if freq["monthly"].get()==1:
		frequency+="M-"
		if freq["monthday"].get():
			frequency+=freq["monthday"].get()+"D"

	if freq["check"].get()==1:
		frequency="W-7D"
	else :
		for i in freq : 
			if i=="mo" and freq[i].get() == 1:
				frequency+="Mo"
			if i=="tu" and freq[i].get() == 1:
				frequency+="Tu"
			if i=="we" and freq[i].get() == 1:
				frequency+="We"
			if i=="th" and freq[i].get() == 1:
				frequency+="Th"
			if i=="fr" and freq[i].get() == 1:
				frequency+="Fr"
			if i=="sa" and freq[i].get() == 1:
				frequency+="Sa"
			if i=="su" and freq[i].get() == 1:
				frequency+="Su"

	if freq["beg"].get() == 1 :
		frequency += "BP"
	if freq["mid"].get() == 1 :
		frequency += "MP"
	if freq["end"].get() == 1 :
		frequency += "EOP"
	if freq["occ_on"].get() == 1 : 
		frequency+="-O"
	if freq["occ_after"].get() == 1 : 
		frequency+="-A"

	frequence.set(frequency)
	return frequency

class StartPage(tk.Frame):	

	def __init__(self, parent, controller):
		freq = dict()
		freq["weekly"]=tk.IntVar(value=0)
		freq["monthly"]=tk.IntVar(value=0)
		freq["check"]=tk.IntVar(value=0)
		freq["mo"]=tk.IntVar()
		freq["tu"]=tk.IntVar()
		freq["we"]=tk.IntVar()
		freq["th"]=tk.IntVar()
		freq["fr"]=tk.IntVar()
		freq["sa"]=tk.IntVar()
		freq["su"]=tk.IntVar()

		freq["beg"]=tk.IntVar()
		freq["mid"]=tk.IntVar()
		freq["end"]=tk.IntVar()
		
		freq["monthday"] = tk.IntVar()
		freq["occ_on"]=tk.IntVar()
		freq["occ_after"]=tk.IntVar()
		frequence = tk.StringVar(value="Frequency")

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="Frequency generator", font=LARGE_FONT)
		label.grid(row=0, column=0, ipady=10)
		
		button = ttk.Button(self, text="Generate Frequency", command=lambda: freqGen(freq,frequence))
		button.grid(row=13, column=0)

		entry = ttk.Entry(self,state="readonly",textvariable=frequence)
		entry.grid(row=13, column=1)

		label_week = ttk.Checkbutton(self,text="Weekly frequency", variable=freq["weekly"])
		label_week.grid(row=2, column=0, sticky="w", padx=10)

		checkbox1 = ttk.Checkbutton(self, text="Every Day", variable=freq["check"], command=lambda: checkAll(freq))
		checkbox1.grid(row=3, column=0, sticky="w", padx=10)
		checkbox1 = ttk.Checkbutton(self, text="Monday", variable=freq["mo"])
		checkbox1.grid(row=4, column=0, sticky="w", padx=10)
		checkbox1 = ttk.Checkbutton(self, text="Tuesday", variable=freq["tu"])
		checkbox1.grid(row=5, column=0, sticky="w", padx=10)
		checkbox1 = ttk.Checkbutton(self, text="Wednesday", variable=freq["we"])
		checkbox1.grid(row=6, column=0, sticky="w", padx=10)
		checkbox1 = ttk.Checkbutton(self, text="Thursday", variable=freq["th"])
		checkbox1.grid(row=7, column=0, sticky="w", padx=10)
		checkbox1 = ttk.Checkbutton(self, text="Friday", variable=freq["fr"])
		checkbox1.grid(row=8, column=0, sticky="w", padx=10)
		checkbox1 = ttk.Checkbutton(self, text="Saturday", variable=freq["sa"])
		checkbox1.grid(row=9, column=0, sticky="w", padx=10)
		checkbox1 = ttk.Checkbutton(self, text="Sunday", variable=freq["su"])
		checkbox1.grid(row=10, column=0, sticky="w", padx=10)

		label_month = ttk.Checkbutton(self,text="Monthly frequency", variable=freq["monthly"])
		label_month.grid(row=2, column=1,columnspan=2, sticky="w")

		# checkbox2 = ttk.Checkbutton(self, text="January", variable=freq["Jan"])
		# checkbox2.grid(row=3, column=1, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="February", variable=freq["Feb"])
		# checkbox2.grid(row=4, column=1, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="March", variable=freq["Mar"])
		# checkbox2.grid(row=5, column=1, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="April", variable=freq["Apr"])
		# checkbox2.grid(row=6, column=1, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="May", variable=freq["May"])
		# checkbox2.grid(row=7, column=1, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="June", variable=freq["Jun"])
		# checkbox2.grid(row=8, column=1, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="July", variable=freq["Jul"])
		# checkbox2.grid(row=3, column=2, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="August", variable=freq["Aug"])
		# checkbox2.grid(row=4, column=2, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="September", variable=freq["Sep"])
		# checkbox2.grid(row=5, column=2, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="October", variable=freq["Oct"])
		# checkbox2.grid(row=6, column=2, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="November", variable=freq["Nov"])
		# checkbox2.grid(row=7, column=2, sticky="w")
		# checkbox2 = ttk.Checkbutton(self, text="December", variable=freq["Dec"])
		# checkbox2.grid(row=8, column=2, sticky="w")

		label_onday = ttk.Label(self,text="Day of the month:")
		label_onday.grid(row=3, column=1,sticky="w")
		entry_day = ttk.Entry(self,textvariable=freq["monthday"])
		entry_day.grid(row=3, column=2)

		checkbox3 = ttk.Checkbutton(self, text="On Date", variable=freq["occ_on"])
		checkbox3.grid(row=5,column=1, sticky="w")
		checkbox4 = ttk.Checkbutton(self, text="Afte Date", variable=freq["occ_after"])
		checkbox4.grid(row=6,column=1, sticky="w")
		checkbox5 = ttk.Checkbutton(self, text="Beginning of period", variable=freq["beg"])
		checkbox5.grid(row=7,column=1, sticky="w")
		checkbox6 = ttk.Checkbutton(self, text="Middle of period", variable=freq["mid"])
		checkbox6.grid(row=8,column=1, sticky="w")
		checkbox7 = ttk.Checkbutton(self, text="End of period", variable=freq["end"])
		checkbox7.grid(row=9,column=1, sticky="w")
		


app = FreqApp()
app.mainloop()
