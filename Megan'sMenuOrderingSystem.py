import tkinter
import tkinter.messagebox


class menuOrder:
    def __init__(self):

        # MAIN WINDOW 
        # create the main window 
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title('Menu Ordering System')
        self.mainWindow.configure(bg='#b39978')
        self.mainWindow.geometry("700x400")

        # create the different frames in the main window
        self.topFrame = tkinter.Frame(self.mainWindow)
        self.secondFrame = tkinter.Frame(self.mainWindow)
        self.thirdFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        self.topFrame.configure(bg='#b39978')
        self.secondFrame.configure(bg='#b39978')
        self.thirdFrame.configure(bg='#b39978')
        self.bottomFrame.configure(bg='#b39978')

        # create 3 frames to be inside the second frame
        self.second1Frame = tkinter.Frame(self.secondFrame)
        self.second2Frame = tkinter.Frame(self.secondFrame)
        self.second3Frame = tkinter.Frame(self.secondFrame)

        self.second1Frame.configure(bg='#b39978')
        self.second2Frame.configure(bg='#b39978')
        self.second3Frame.configure(bg='#b39978')

        # pack the 3 frames inside the second frame
        self.second1Frame.pack(side='left')
        self.second2Frame.pack(side='left')
        self.second3Frame.pack(side='left')

        # create 3 frames to be inside the third frame
        self.third1Frame = tkinter.Frame(self.thirdFrame)
        self.third2Frame = tkinter.Frame(self.thirdFrame)
        self.third3Frame = tkinter.Frame(self.thirdFrame)

        self.third1Frame.configure(bg='#b39978')
        self.third2Frame.configure(bg='#b39978')
        self.third3Frame.configure(bg='#b39978')

        # pack the 3 frames inside the third frame
        self.third1Frame.pack(side='left')
        self.third2Frame.pack(side='left')
        self.third3Frame.pack(side='left')

        # pack the frames in the main window
        self.topFrame.pack()
        self.secondFrame.pack()
        self.thirdFrame.pack()
        self.bottomFrame.pack()
        
   
        
        # create the widget for title labels
        self.titleLabel = tkinter.Label(self.topFrame, text="Megan's Cafe's Menu 🍽️", background='#b39978')
        self.titleLabel.config(font=('Montserrat', 24, 'bold'))
        # pack the title label
        self.titleLabel.pack()

        #create the widgets for food options
        self.appLabel = tkinter.Label(self.second1Frame, text='Appetizers', background='#b39978')
        self.fishLabel = tkinter.Label(self.second2Frame, text='Fish', background='#b39978')
        self.steaksLabel = tkinter.Label(self.second3Frame, text='Steaks', background='#b39978')
        self.pastaLabel = tkinter.Label(self.third1Frame, text='Pasta', background='#b39978')
        self.sidesLabel = tkinter.Label(self.third2Frame, text='Sides', background='#b39978')
        self.drinksLabel = tkinter.Label(self.third3Frame, text='Drinks', background='#b39978')

        self.appLabel.config(font=('Montserrat', 20, 'bold'))
        self.fishLabel.config(font=('Montserrat', 20, 'bold'))
        self.steaksLabel.config(font=('Montserrat', 20, 'bold'))
        self.pastaLabel.config(font=('Montserrat', 20, 'bold'))
        self.sidesLabel.config(font=('Montserrat', 20, 'bold'))
        self.drinksLabel.config(font=('Montserrat', 20, 'bold'))

        self.appLabel.pack(side='top')
        self.fishLabel.pack(side='top')
        self.steaksLabel.pack(side='top')
        self.pastaLabel.pack(side='top')
        self.sidesLabel.pack(side='top')
        self.drinksLabel.pack(side='top')

        # create quit button and calculate total
        self.quitButton = tkinter.Button(self.bottomFrame, text='Quit', command=self.mainWindow.destroy, bg='#b39978')
        self.continueButton = tkinter.Button(self.bottomFrame, text='Continue', command=self.continueButton, bg='#b39978')


        # pack the quit and calculate bill button
        self.quitButton.pack()
        self.continueButton.pack()

        

        # create options in APPETIZERS
        self.appVar1 = tkinter.IntVar()
        self.appVar2 = tkinter.IntVar()
        self.appVar3 = tkinter.IntVar()
        self.appVar4 = tkinter.IntVar()
     
        self.app1 = tkinter.Checkbutton(self.second1Frame, text='Ceaser Salad - $15', variable = self.appVar1, bg='#b39978')
        self.app2 = tkinter.Checkbutton(self.second1Frame, text='Calamari - $20', variable = self.appVar2, bg='#b39978')
        self.app3 = tkinter.Checkbutton(self.second1Frame, text='French Onion Soup - $15', variable = self.appVar3, bg='#b39978')
        self.app4 = tkinter.Checkbutton(self.second1Frame, text='Shrimp Cocktail - $22', variable = self.appVar4, bg='#b39978')

        self.app1.pack(side='top')
        self.app2.pack(side='top')
        self.app3.pack(side='top')
        self.app4.pack(side='top')

        # create options in FISH
        self.fishVar1 = tkinter.IntVar()
        self.fishVar2 = tkinter.IntVar()
        self.fishVar3 = tkinter.IntVar()
        self.fishVar4 = tkinter.IntVar()
     
        self.fish1 = tkinter.Checkbutton(self.second2Frame, text='Seared Tuna - $45', variable = self.fishVar1, bg='#b39978')
        self.fish2 = tkinter.Checkbutton(self.second2Frame, text='Miso Black Cod - $45', variable = self.fishVar2, bg='#b39978')
        self.fish3 = tkinter.Checkbutton(self.second2Frame, text='Salmon - $35', variable = self.fishVar3, bg='#b39978')
        self.fish4 = tkinter.Checkbutton(self.second2Frame, text='Panko Crusted Habliut - $30', variable = self.fishVar4, bg='#b39978')

        self.fish1.pack(side='top')
        self.fish2.pack(side='top')
        self.fish3.pack(side='top')
        self.fish4.pack(side='top')

        # create options in STEAKS
        self.steakVar1 = tkinter.IntVar()
        self.steakVar2 = tkinter.IntVar()
        self.steakVar3 = tkinter.IntVar()
        self.steakVar4 = tkinter.IntVar()
     
        self.steak1 = tkinter.Checkbutton(self.second3Frame, text='Filet Mignon 6 oz - $70', variable = self.steakVar1, bg='#b39978')
        self.steak2 = tkinter.Checkbutton(self.second3Frame, text='Striploin 10 oz - $65', variable = self.steakVar2, bg='#b39978')
        self.steak3 = tkinter.Checkbutton(self.second3Frame, text='Ribeye 20 oz - $90', variable = self.steakVar3, bg='#b39978')
        self.steak4 = tkinter.Checkbutton(self.second3Frame, text='Porterhouse 40 oz - $200', variable = self.steakVar4, bg='#b39978')

        self.steak1.pack(side='top')
        self.steak2.pack(side='top')
        self.steak3.pack(side='top')
        self.steak4.pack(side='top')

        # create options in PASTA
        self.pastaVar1 = tkinter.IntVar()
        self.pastaVar2 = tkinter.IntVar()
        self.pastaVar3 = tkinter.IntVar()
        self.pastaVar4 = tkinter.IntVar()
     
        self.pasta1 = tkinter.Checkbutton(self.third1Frame, text='Ragu - $20', variable = self.pastaVar1, bg='#b39978')
        self.pasta2 = tkinter.Checkbutton(self.third1Frame, text='Rosé - $18', variable = self.pastaVar2, bg='#b39978')
        self.pasta3 = tkinter.Checkbutton(self.third1Frame, text='Carbonara - $25', variable = self.pastaVar3, bg='#b39978')
        self.pasta4 = tkinter.Checkbutton(self.third1Frame, text='Lasagna - $28', variable = self.pastaVar4, bg='#b39978')

        self.pasta1.pack(side='top')
        self.pasta2.pack(side='top')
        self.pasta3.pack(side='top')
        self.pasta4.pack(side='top')

        # create options in SIDES
        self.sidesVar1 = tkinter.IntVar()
        self.sidesVar2 = tkinter.IntVar()
        self.sidesVar3 = tkinter.IntVar()
        self.sidesVar4 = tkinter.IntVar()
     
        self.sides1 = tkinter.Checkbutton(self.third2Frame, text='Fries - $5', variable = self.sidesVar1, bg='#b39978')
        self.sides2 = tkinter.Checkbutton(self.third2Frame, text='Mash Potato - $10', variable = self.sidesVar2, bg='#b39978')
        self.sides3 = tkinter.Checkbutton(self.third2Frame, text='Sweet Potato Fries - $7', variable = self.sidesVar3, bg='#b39978')
        self.sides4 = tkinter.Checkbutton(self.third2Frame, text='Creamed Spinach - $10', variable = self.sidesVar4, bg='#b39978')

        self.sides1.pack(side='top')
        self.sides2.pack(side='top')
        self.sides3.pack(side='top')
        self.sides4.pack(side='top')

        # create options in DRINKS
        self.drinksVar1 = tkinter.IntVar()
        self.drinksVar2 = tkinter.IntVar()
        self.drinksVar3 = tkinter.IntVar()
        self.drinksVar4 = tkinter.IntVar()
     
        self.drinks1 = tkinter.Checkbutton(self.third3Frame, text='Red Wine of the Day - $10', variable = self.drinksVar1, bg='#b39978')
        self.drinks2 = tkinter.Checkbutton(self.third3Frame, text='White Wine of the Day - $10', variable = self.drinksVar2, bg='#b39978')
        self.drinks3 = tkinter.Checkbutton(self.third3Frame, text='Pop - $3', variable = self.drinksVar3, bg='#b39978')
        self.drinks4 = tkinter.Checkbutton(self.third3Frame, text='Sparkling Water - $7', variable = self.drinksVar4, bg='#b39978')

        self.drinks1.pack(side='top')
        self.drinks2.pack(side='top')
        self.drinks3.pack(side='top')
        self.drinks4.pack(side='top')


    def continueButton(self):

        tip = 0.0

        
        # create a widget to describe what the entry box is for 
        self.tipLabel = tkinter.Label(self.bottomFrame, text = 'Enter how much tip you would like to give (%)', bg='#b39978')
        # configure the tip label
        self.tipLabel.config(font=('Montserrat', 20, 'bold'))
        # pack the tip label
        self.tipLabel.pack(side='left')


        # create the tip entry
        self.tipEntry = tkinter.Entry(self.bottomFrame, width='12')
        # pack the tip entry 
        self.tipEntry.pack(side='left')

   
        self.calcBill = tkinter.Button(self.bottomFrame, text='Calculate Bill', command=self.calcBill, bg='#b39978')
        self.calcBill.pack()
        
        self.subTotal = 0

        # add total of all the appetizers 
        if self.appVar1.get() == 1:
            self.subTotal += 15
        if self.appVar2.get() == 1:
            self.subTotal += 20
        if self.appVar3.get() == 1:
            self.subTotal += 15
        if self.appVar4.get()== 1:
            self.subTotal += 22

        # add total of all the fish
        if self.fishVar1.get() == 1:
            self.subTotal += 45
        if self.fishVar2.get() == 1:
            self.subTotal += 45
        if self.fishVar3.get() == 1:
            self.subTotal += 35
        if self.fishVar4.get()== 1:
            self.subTotal += 30

        # add total of all the steaks
        if self.steakVar1.get() == 1:
            self.subTotal += 70
        if self.steakVar2.get() == 1:
            self.subTotal += 65
        if self.steakVar3.get() == 1:
            self.subTotal += 90
        if self.steakVar4.get()== 1:
            self.subTotal += 200

        # add total of all the pasta
        if self.pastaVar1.get() == 1:
            self.subTotal += 20
        if self.pastaVar2.get() == 1:
            self.subTotal += 18
        if self.pastaVar3.get() == 1:
            self.subTotal += 25
        if self.pastaVar4.get()== 1:
            self.subTotal += 28

        # add total of all the sides
        if self.sidesVar1.get() == 1:
            self.subTotal += 5
        if self.sidesVar2.get() == 1:
            self.subTotal += 10
        if self.sidesVar3.get() == 1:
            self.subTotal += 7
        if self.sidesVar4.get()== 1:
            self.subTotal += 10

        # add total of all the drinks
        if self.drinksVar1.get() == 1:
            self.subTotal += 10
        if self.drinksVar2.get() == 1:
            self.subTotal += 10
        if self.drinksVar3.get() == 1:
            self.subTotal += 3
        if self.drinksVar4.get()== 1:
            self.subTotal += 7

        

         
    def calcBill(self):
        tipPercent = float(self.tipEntry.get())
        
        tipDecimal = tipPercent * 0.01

        subTotal = int(self.subTotal)

        tax = subTotal * .13

        total = subTotal * 1.13

        tip = total * tipDecimal

        tipTotal = total + tip
        
        # create info box
        tkinter.messagebox.showinfo('bill',
                                    '\nSubtotal: $' + str(subTotal)
                                    + ' '
                                    + '\nTax: $' + str(tax)
                                    + ' '
                                    + '\nTotal: $' + str(total)
                                    + ' '
                                    + '\nTip: $' + str(tip))
    

        
        

        tkinter.mainloop()
    

            

        
        
 

# create an instance of menuOrder
menu_order = menuOrder()

        
    
