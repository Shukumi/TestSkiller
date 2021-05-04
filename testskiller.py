from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

atkk = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 9, 10]
defk = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 10]
elek = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
hpk = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
pls = [0,5,10,15,20,28,36,46,56,68,80,95,110,128,148,173]
punkte = 0
class Tstskl:
	def __init__(self, master):
		self.master = master
		master.title("Testskiller")
		master.resizable(False, False)
		#master.wm_attributes('-transparentcolor', 'white')
		#self.master.geometry('510x340+100+200')
		img = ImageTk.PhotoImage(Image.open("nb4.jpg"))
		w = img.width()
		h = img.height()
		self.master.geometry('%dx%d+0+0' % (w,h))
		background_label = Label(self.master, image=img)
		background_label.photo= img
		background_label.place(x=0, y=0, relwidth=1, relheight=1)
		Label(master, text ="Job:", font = "Verdana 11 italic").grid(row=3,column=2)
		self.job = Spinbox(master, from_=0, to=99)
		self.job.grid(row=3, column=3)
		Label(master, text ="Plus:", font = "Verdana 11 italic").grid(row=4,column=2)
		self.plus = Spinbox(master, from_=0, to=15)
		

		self.plus.grid(row=4, column=3)
		def counter_label(label,typ):
			def count():
				try:
					if typ=="atk":
						label.config(text="Max-ATK: " + str(100-int(self.eatksl.get())-int(self.egessl.get())))
						label.after(200, count)
					elif typ =="def":
						label.config(text="Max-DEF: " + str(100-int(self.edefsl.get())-int(self.egessl.get())))
						label.after(200, count)
					elif typ =="ele":
						label.config(text="Max-ELE: " + str(100-int(self.eelesl.get())-int(self.egessl.get())))
						label.after(200, count)
					elif typ =="hp":
						label.config(text="Max-HP: " + str(100-int(self.ehpsl.get())-int(self.egessl.get())))
						label.after(200, count)	
					elif typ =="pkt":
						if int(self.job.get()) > 20 and int(self.job.get()) < 100:
							try:
								punkte = ((int(self.job.get())*3)-20*3)+pls[int(self.plus.get())]
							except IndexError:
								pass
						else:
							punkte = 0
						restpunkte = 0
						atkskill = int(self.eatk.get())
						defskill = int(self.edef.get())
						eleskill = int(self.eele.get())
						hpskill = int(self.ehp.get())
						try:
							for i in range(0,atkskill+1):
								restpunkte += atkk[i]
							for i in range(0,defskill+1):
								restpunkte += defk[i]
							for i in range(0,eleskill+1):
								restpunkte += elek[i]
							for i in range(0,hpskill+1):
								restpunkte += hpk[i]
							label.config(text="Restpunkte: " + str(punkte - restpunkte))
							if punkte-restpunkte >= 0:
								label.config(fg="green")
							else:
								label.config(fg="red")
						except IndexError:
							pass
						
						"""print (punkte)
						print (restpunkte)"""
						label.after(200, count)	
					elif typ == "end-atk":
						label.config(text="ATK: " + str(int(self.eatk.get())+int(self.eatksl.get())+int(self.egessl.get())))
						label.after(200, count)	
					elif typ == "end-def":
						label.config(text="DEF: " + str(int(self.edef.get())+int(self.edefsl.get())+int(self.egessl.get())))
						label.after(200, count)	
					elif typ == "end-ele":
						label.config(text="ELE: " + str(int(self.eele.get())+int(self.eelesl.get())+int(self.egessl.get())))
						label.after(200, count)	
					elif typ == "end-hp":
						label.config(text="HP: " + str(int(self.ehp.get())+int(self.ehpsl.get())+int(self.egessl.get())))
						label.after(200, count)	
					else:
						pass
				except ValueError:
					#label.config(text='ZahlenPLS')
					label.after(200,count)
			count()
			
		def show_boerse():
			batk = int(self.eatk.get())+int(self.eatksl.get())+int(self.egessl.get())
			bdef = int(self.edef.get())+int(self.edefsl.get())+int(self.egessl.get())
			bele = int(self.eele.get())+int(self.eelesl.get())+int(self.egessl.get())
			bhp = int(self.ehp.get())+int(self.ehpsl.get())+int(self.egessl.get())
			ak = 0
			tc = 0
			cc = 0
			cd = 0
			hpa = 0
			mpa = 0
			meiden = 0
			acc = 0
			allresi = 0
			mdef = 0
			adef = 0
			es = 0
			if batk >= 1:
				ak += 5
			if batk >= 10:
				tc += 10
			if batk >= 20:
				cc += 2
			if batk >= 30:
				tc += 10
				ak += 5
			if batk >= 40:
				cd += 10
			if batk >= 50:
				hpa +=200
				mpa += 200
			if batk >= 60:
				tc += 15
			if batk >= 70:
				tc += 15
				ak += 5
			if batk >= 80:
				cc += 3
			if batk >= 90:
				cd += 20
			if batk >= 100:
				tc += 20
				ak+= 5 
				cc +=3
				cd +=20
				hpa +=200
				mpa +=200
				
			if bdef >= 10:
				meiden += 5
			if bdef >= 20:
				acc += 2
			if bdef >= 30:
				hpa += 100
			if bdef >= 40:
				acc += 2
			if bdef >= 50:
				meiden += 5
			if bdef >= 60:
				hpa += 200
			if bdef >= 70:
				acc += 3
			if bdef >= 75:
				allresi+=2
			if bdef >= 80:
				acc +=3
				meiden +=10
			if bdef >= 90:
				allresi +=3
			if bdef >= 95:
				hpa +=300
			if bdef >= 100:
				meiden += 20
				allresi +=5
				
			if bele >= 1:
				es +=2
			if bele >= 10:
				mpa += 100
			if bele >= 20:
				mdef += 5
			if bele >= 30:
				es += 2
				allresi += 2
			if bele >= 40:
				mpa +=100
			if bele >= 50:
				mdef +=5
			if bele >= 60:
				es +=2
				allresi +=3
			if bele >= 70:
				mpa += 100
			if bele >= 80:
				mdef +=5
			if bele >= 90:
				es += 2
				allresi +=4
			if bele >= 100:
				es +=2
				mpa +=200
				mdef +=5
				allresi +=6
				
			if bhp >= 5:
				ak +=5
			if bhp >= 10:
				ak +=5
			if bhp >= 15:
				ak += 5
			if bhp >= 20:
				ak += 5
				adef += 10
			if bhp >= 25:
				ak +=5
			if bhp >= 30:
				ak += 5
			if bhp >= 35:
				ak += 5
			if bhp >= 40:
				ak +=5
				adef +=15
			if bhp >= 45:
				ak +=10
			if bhp >= 50:
				ak +=10
				allresi += 2
			if bhp >= 55:
				ak += 10
			if bhp >= 60:
				ak +=10
			if bhp >= 65:
				ak +=10
			if bhp >= 70:
				ak += 10
				adef += 20
			if bhp >= 75:
				ak += 15
			if bhp >= 80:
				ak += 15
			if bhp >= 85:
				ak += 15
				acc +=1
			if bhp >= 86:
				acc +=1
			if bhp >= 87:
				acc +=1
			if bhp >= 88:
				acc +=1
			if bhp >= 90:
				ak += 15
				adef += 25
			if bhp >= 91:
				meiden +=2
			if bhp >= 92:
				meiden +=2
			if bhp >= 93:
				meiden +=2
			if bhp >= 94:
				meiden +=2
			if bhp >= 95:
				ak +=20
				meiden +=2
			if bhp >= 96:
				meiden +=2
			if bhp >= 97:
				meiden +=2
			if bhp >= 98:
				meiden +=2
			if bhp >= 99:
				meiden +=2
			if bhp >= 100:
				meiden +=2
				ak+=20
				adef +=30
				allresi +=3
				acc +=1
				
			xx = " Börsenskills : \n" + "Deine Angriffskraft wird erhöht um: " + str(ak) 
			xxx = "\n Deine Trefferchance wird erhöht um: " + str(tc) + "\n Deine Critchance wird erhöht um: " + str(cc)
			xxxx =  "\n Dein Critschaden wird erhöht um: " + str(cd) + "\n Deine HP werden erhöht um: " + str(hpa) 
			xxxxx = "\n Deine MP werden erhöht um: " + str(mpa) + "\n Dein Meiden wird erhöht um: " + str(meiden) 
			xxxxxx = "\n Die Chance, dass du gecrittet wirst, verringert sich um: " + str(acc) + "\n Deine Magedef wird erhöht um: " + str(mdef) 
			xxxxxxx = "\n Deine Alldef wird erhöht um: " + str(adef) + "\n Deine Allresi wird erhöht um: " + str(allresi) 
			xy = "\n Dein Elementarschaden wird erhöht um: " + str(es)
			messagebox.showinfo("Deine Börsenskills!",xx + xxx + xxxx + xxxxx + xxxxxx + xxxxxxx + xy)
			
			"""
			ak = 0
			tc = 0
			cc = 0
			cd = 0
			hpa = 0
			mpa = 0
			meiden = 0
			acc = 0
			allresi = 0
			mdef = 0
			adef = 0
			es = 0
			"""

		Label(master, text ="Willkommen!", font = "Verdana 12 italic bold", bg="lightblue").grid(row=0,column=3)
		Label(master, text ="SLs:", font = "Verdana 12 italic", bg="lightblue").grid(row=1,column=0)
		self.close_button = Button(master, text="Close", command=master.quit, bg="lightblue").grid(row=10,column=3, sticky="nsew",pady=10)
		self.close_button = Button(master, text="Börsenskills", command=show_boerse, bg="lightblue").grid(row=9,column=3, sticky="nsew",pady=10)
		self.eatksl = Entry(root)
		self.eatksl.grid(row=1, column=1)
		self.eatksl.insert(END, '0')
		self.edefsl = Entry(root)
		self.edefsl.grid(row=1, column=2)
		self.edefsl.insert(END, '0')
		self.eelesl = Entry(root)
		self.eelesl.grid(row=1, column=3)
		self.eelesl.insert(END, '0')
		self.ehpsl = Entry(root)
		self.ehpsl.grid(row=1, column=4,padx=10)
		self.ehpsl.insert(END, '0')
		self.egessl = Entry(root)
		self.egessl.grid(row=1, column=5)
		self.egessl.insert(END, '0')
		self.maxatk = Label(master, text="", font = "Verdana 10 italic bold", fg="blue", bg="lightblue")
		self.maxatk.grid(row=2,column=1)
		counter_label(self.maxatk,"atk")
		self.maxatk = Label(master, text="", font = "Verdana 10 italic bold", fg="blue", bg="lightblue")
		self.maxatk.grid(row=2,column=2)
		counter_label(self.maxatk,"def")
		self.maxatk = Label(master, text="", font = "Verdana 10 italic bold", fg="blue", bg="lightblue")
		self.maxatk.grid(row=2,column=3)
		counter_label(self.maxatk,"ele")
		self.maxatk = Label(master, text="", font = "Verdana 10 italic bold", fg="blue", bg="lightblue")
		self.maxatk.grid(row=2,column=4)
		counter_label(self.maxatk,"hp")
		
		Label(master, text ="ATK:", font = "Verdana 11 italic", bg="lightblue").grid(row=3,column=0,pady=10)
		self.eatk = Spinbox(master, from_=0, to=100)
		self.eatk.grid(row=3, column=1)
		Label(master, text ="DEF:", font = "Verdana 11 italic", bg="lightblue").grid(row=4,column=0,pady=10)
		self.edef = Spinbox(master, from_=0, to=100)
		self.edef.grid(row=4, column=1)
		Label(master, text ="ELE:", font = "Verdana 11 italic", bg="lightblue").grid(row=5,column=0,pady=10)
		self.eele = Spinbox(master, from_=0, to=100)
		self.eele.grid(row=5, column=1)
		Label(master, text ="HP:", font = "Verdana 11 italic", bg="lightblue").grid(row=6,column=0,pady=10)
		self.ehp = Spinbox(master, from_=0, to=100)
		self.ehp.grid(row=6, column=1)
		self.restpunkte = Label(master, text="", font = "Verdana 11 italic bold", fg="blue", bg="lightblue")
		self.restpunkte.grid(row=7,column=1,pady=10)
		counter_label(self.restpunkte,"pkt")
		self.endatk = Label(master, text="", font = "Verdana 12 italic", fg="blue", bg="lightblue")
		self.endatk.grid(row=8,column=1,pady=10)
		counter_label(self.endatk,"end-atk")
		self.enddef = Label(master, text="", font = "Verdana 12 italic ", fg="blue", bg="lightblue")
		self.enddef.grid(row=8,column=2)
		counter_label(self.enddef,"end-def")
		self.endele = Label(master, text="", font = "Verdana 12 italic ", fg="blue", bg="lightblue")
		self.endele.grid(row=8,column=3)
		counter_label(self.endele,"end-ele")
		self.endhp = Label(master, text="", font = "Verdana 12 italic", fg="blue", bg="lightblue")
		self.endhp.grid(row=8,column=4)
		counter_label(self.endhp,"end-hp")
		root.columnconfigure(0, weight=0)
		root.rowconfigure(0, weight=0)


		
		
		
	
		

root = Tk()
my_gui = Tstskl(root)
root.mainloop()