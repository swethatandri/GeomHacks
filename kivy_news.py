from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import robin_stocks as rh
import NewsPuller 
 
def finance_news():
        rh.login("email","password",store_session = True)
        print("logging in ...")
        q = open('/Users/adarshbulusu/Desktop/Kivy_News/StockMovements.txt','w')
        q.write("THESE ARE THE STOCKS THAT HAD THE BIGGEST GAINS RECENTLY!!!\n")
        q.write("\n")
        
        
        for i in range(len(rh.get_top_movers('up'))):
            q.write('\n')
            q.writelines(rh.get_top_movers('up')[i].get('symbol'))
            q.writelines(rh.get_top_movers('up')[i].get('description'))
            q.writelines("\n")
        
        q.write(("THESE ARE THE STOCKS THAT HAD THE BIGGEST LOSSES RECENTLY\n"))
        for i in range(len(rh.get_top_movers('down'))):
            q.write('\n')
            q.writelines(rh.get_top_movers('down')[i].get('symbol'))
            q.writelines(rh.get_top_movers('down')[i].get('description'))
            q.write("\n")
        
        q.close()
        
class Grid(GridLayout):
    def __init__(self,**kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 2
        
        
        self.inside = GridLayout()
        self.inside.cols = 2
        
        self.add_widget(Label(text = 'CovidNews has the latest breaking headlines for Covid-19',font_size = 30))
        self.add_widget(Label(text = 'CovidStocks has the latest market changes and strategies', font_size = 30))
        
        self.add_widget(Label(text = 'Please fill out your personal information'))
        
        self.cols = 3
        self.inside.add_widget(Label(text = "First Name: "))
        self.firstName = TextInput(multiline = False)
        self.inside.add_widget(self.firstName)
        
        self.inside.add_widget(Label(text = "Last Name: "))
        self.lastName = TextInput(multiline = False)
        self.inside.add_widget(self.lastName)
        
        self.inside.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)
        
        self.add_widget(self.inside)
        
        self.submit = Button(text = "Click for CovidNews", font_size = 30)
        self.submit.bind(on_press = self.news_pressed)
        self.add_widget(self.submit)
        
        self.submit1 = Button(text = "Click for CovidStocks", font_size = 30)
        self.submit.bind(on_press = self.finance_pressed)
        self.add_widget(self.submit1)



    def finance_pressed(self,instance):
        finance_news()
            
       
    def news_pressed(self,instance):
        NewsPuller.getNews()
    

class App(App):
    def build(self):
        return Grid()
    


if __name__ == '__main__':
    App().run()