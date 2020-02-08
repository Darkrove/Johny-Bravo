from tkinter import *
root = Tk()

mycanvas = Canvas(root,bg='yellow',height=600,width=1200)
mycanvas.pack()
#shoulder
mycanvas.create_polygon(520,330,350,410,520,600,fill='black',smooth=True)
mycanvas.create_polygon(620,370,750,400,670,600,fill='black',smooth=True)
mycanvas.create_polygon(480,400,280,370,260,600,360,600,fill='black',smooth=TRUE)
mycanvas.create_polygon(700,370,850,400,900,600,670,600,fill='black',smooth=True)

#neck
mycanvas.create_polygon(525,340,480,440,670,440,625,340,fill='bisque',outline='black',width=4)
#Face
mycanvas.create_polygon(500,200,650,200,620,350,530,350,fill='bisque',joinstyle='round',outline='black',width=4)
mycanvas. create_line(575,285,575,295,fill='black',width=3)
mycanvas.create_arc(510,300,620,400,style='arc',start=80,extent=10,width=3)
mycanvas.create_arc(520,300,650,400,style='arc',start=90,extent=10,width=3)

#x=550,y=275,r=20
#glasses
mycanvas.create_oval(510,255,570,295,fill='black')
#x=600,y=275,r=20
mycanvas.create_oval(580,255,640,295,fill='black')
mycanvas.create_line(520,265,620,265,width=5)
#hair
#571,120,110
mycanvas.create_arc(461,10,681,230,style='arc',width=4,start=140,extent=90,fill='yellow')
mycanvas.create_line(488,50,530,40,width=3)
#610,115,110
arc=mycanvas.create_arc(500,5,720,225,style='arc',width=4,start=140,extent=70,fill='yellow')
#650,125,110
mycanvas.create_arc(540,15,760,235,style='arc',width=4,start=140,extent=65,fill='yellow')
mycanvas.create_line(530,40,563,53,width=3)
#530,125,110
mycanvas.create_arc(410,15,640,235,style='arc',width=4,start=330,extent=55,fill='yellow')
#560,140,90
mycanvas.create_arc(470,50,650,230,style='arc',width=4,start=38,extent=50,fill='yellow')
#570,125,110
mycanvas.create_arc(460,15,680,235,style='arc',width=4,start=315,extent=55,fill='yellow')
mycanvas.create_line(630,78,680,105,width=3)
#smile
mycanvas.create_oval(615,310,600,310,fill='black',outline='black',width=3)
#body
mycanvas.create_polygon(490,400,660,400,670,440,480,440,smooth=TRUE,fill='black')
#570,250,100
mycanvas.create_arc(480,370,680,420,start=200,extent=120,fill='black',width=45,style='arc')
#tshirt
mycanvas.create_rectangle(450,400,680,550,fill='black')
mycanvas.create_rectangle(300,500,550,550,fill='black')
mycanvas.create_polygon(100,550,1100,550,1100,600,100,600,fill='yellow')
mycanvas.create_line(100,550,1100,550)
mycanvas.create_rectangle(400,450,800,550,fill='black')
mycanvas.create_arc(300,400,400,600,outline='blue',style='arc',start=330,extent=40,width=3)
mycanvas.create_arc(750,400,950,600,outline='blue',style='arc',start=170,extent=40,width=3)
#text
mycanvas.create_text(200,300,text='Johnny Bravo',font=('AR BERKLEY',35),fill='black')
mainloop()
