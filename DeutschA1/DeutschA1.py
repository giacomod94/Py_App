#json internet
import random
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
#kivy.require("1.9.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView 
from kivy.properties import StringProperty 
from kivy.properties import ObjectProperty 
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from kivy.uix.button import Label
#from gtts import gTTS 
#from kivy.core.audio import SoundLoader 
import webbrowser
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.config import Config 

Config.set('graphics', 'resizable', True) 





class IntroScreen(Screen):

    #def verify_credentials(self):
        #if self.ids["login"].text == "Ichliebe" and self.ids["passw"].text == "Deutsch":
            #self.manager.current = "Index"
    pass
                             

class IndexScreen(Screen):
    pass

class A11Screen(Screen):
    pass

class A12Screen(Screen):
    pass
    

class L1Screen(Screen):
    def __init__(self, **kwargs):
        super(L1Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 1')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 1')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
        
    def change(self):
        ScreenManagement.MY_GLOBAL = '1'
        ScreenManagement.SCREEN = 'L1'
        
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    
class L2Screen(Screen):
    def __init__(self, **kwargs):
        super(L2Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 2')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 2')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
        
    def change(self):
        ScreenManagement.MY_GLOBAL = '2'
        ScreenManagement.SCREEN = 'L2'
        
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    
class L3Screen(Screen):
    def __init__(self, **kwargs):
        super(L3Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 3')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 3')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
        
    def change(self):
        ScreenManagement.MY_GLOBAL = '3'
        ScreenManagement.SCREEN = 'L3'
        
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    
    
class L4Screen(Screen):
    def __init__(self, **kwargs):
        super(L4Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 4')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 4')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
        
    def change(self):
        ScreenManagement.MY_GLOBAL = '4'
        ScreenManagement.SCREEN = 'L4'
        
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
        

class L5Screen(Screen):
    def __init__(self, **kwargs):
        super(L5Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 5')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 5')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '5'
        ScreenManagement.SCREEN = 'L5'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L6Screen(Screen):
    def __init__(self, **kwargs):
        super(L6Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 6')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 6')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '6'
        ScreenManagement.SCREEN = 'L6'

    
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L7Screen(Screen):
    def __init__(self, **kwargs):
        super(L7Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 7')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 7')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '7'
        ScreenManagement.SCREEN = 'L7'

        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L8Screen(Screen):
    def __init__(self, **kwargs):
        super(L8Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 8')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 8')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '8'
        ScreenManagement.SCREEN = 'L8'

        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L9Screen(Screen):
    def __init__(self, **kwargs):
        super(L9Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 9')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 9')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '9'
        ScreenManagement.SCREEN = 'L9'

        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L10Screen(Screen):
    def __init__(self, **kwargs):
        super(L10Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 10')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 10')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '10'
        ScreenManagement.SCREEN = 'L10'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L11Screen(Screen):
    def __init__(self, **kwargs):
        super(L11Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 11')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 11')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '11'
        ScreenManagement.SCREEN = 'L11'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L12Screen(Screen):
    def __init__(self, **kwargs):
        super(L12Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 12')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 12')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '12'
        ScreenManagement.SCREEN = 'L12'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L13Screen(Screen):
    def __init__(self, **kwargs):
        super(L13Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 13')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 13')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '13'
        ScreenManagement.SCREEN = 'L13'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L14Screen(Screen):
    def __init__(self, **kwargs):
        super(L14Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 14')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 14')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '14'
        ScreenManagement.SCREEN = 'L14'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L15Screen(Screen):
    def __init__(self, **kwargs):
        super(L15Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 15')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 15')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '15'
        ScreenManagement.SCREEN = 'L15'
        
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L16Screen(Screen):
    def __init__(self, **kwargs):
        super(L16Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 16')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 16')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '16'
        ScreenManagement.SCREEN = 'L16'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L17Screen(Screen):
    def __init__(self, **kwargs):
        super(L17Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 17')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 17')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '17'
        ScreenManagement.SCREEN = 'L17'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L18Screen(Screen):
    def __init__(self, **kwargs):
        super(L18Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 18')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 18')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '18'
        ScreenManagement.SCREEN = 'L18'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L19Screen(Screen):
    def __init__(self, **kwargs):
        super(L19Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 19')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 19')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '19'
        ScreenManagement.SCREEN = 'L19'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L20Screen(Screen):
    def __init__(self, **kwargs):
        super(L20Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 20')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 20')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '20'
        ScreenManagement.SCREEN = 'L20'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L21Screen(Screen):
    def __init__(self, **kwargs):
        super(L21Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 21')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 21')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '21'
        ScreenManagement.SCREEN = 'L21'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L22Screen(Screen):
    def __init__(self, **kwargs):
        super(L22Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 22')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 22')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '22'
        ScreenManagement.SCREEN = 'L22'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L23Screen(Screen):
    def __init__(self, **kwargs):
        super(L23Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 23')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 23')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '23'
        ScreenManagement.SCREEN = 'L23'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass

class L24Screen(Screen):
    def __init__(self, **kwargs):
        super(L24Screen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION 24')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION 24')['Es'].split('\n\n')
        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = '24'
        ScreenManagement.SCREEN = 'L24'
        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i.replace('\n',''))
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass
 
class VerbenScreen(Screen):
    def __init__(self, **kwargs):
        super(VerbenScreen, self).__init__(**kwargs)
        self.Al = JsonStore("A1deutsch.json").get('LEKTION Verben')['Al'].split('\n\n')
        self.Es = JsonStore("A1deutsch.json").get('LEKTION Verben')['Es'].split('\n\n')
        self.ex1Al = JsonStore("A1deutsch.json").get('LEKTION Verben')['ex1Al'].split('\n\n')
        self.ex1Es = JsonStore("A1deutsch.json").get('LEKTION Verben')['ex1Es'].split('\n\n')
        self.ex2Al = JsonStore("A1deutsch.json").get('LEKTION Verben')['ex2Al'].split('\n\n')
        self.ex2Es = JsonStore("A1deutsch.json").get('LEKTION Verben')['ex2Es'].split('\n\n')

    def change(self):
        ScreenManagement.MY_GLOBAL = 'Verben'
        ScreenManagement.SCREEN = 'Verben'
        ScreenManagement.control = '1'

    def bck(self):

        ScreenManagement.control = '0'

        
    def test(self):
        lista = []
        j = 0
        try:
            for i in self.Al:
                lista.append(i)
                lista.append(self.Es[j].replace('\n',''))
                j +=1
        except:
            return lista[2:]
        return lista[2:]
    pass


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        App.get_running_app()
        
        self.num = random.choice(range(4))
        self.test = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Al'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')
        self.solution = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Es'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')
        self.randnum = random.choice(range(len(self.solution))),random.choice(range(len(self.solution))),random.choice(range(len(self.solution))),random.choice(range(len(self.solution)))
        



#load data from json
    def load(self):
        if JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['perc']:
            self.ids.perc.text = str(JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['perc'])
        else:
            self.ids.perc.text = '0'

#write data in the json
    def save(self):

        if ScreenManagement.MY_GLOBAL == 'Verben':
            JsonStore("A1deutsch.json").put('LEKTION '+ScreenManagement.MY_GLOBAL,Al =JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Al'], Es = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Es'] ,ex1Al = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex1Al'],ex1Es = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex1Es'],ex2Al = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex2Al'],ex2Es = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex2Es'], perc=float(self.ids.perc.text))

        else:    
            JsonStore("A1deutsch.json").put('LEKTION '+ScreenManagement.MY_GLOBAL,Al =JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Al'], Es = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Es'] , perc=float(self.ids.perc.text))
        
#update if choose right
    def updateP(self):
        if self.check():
            self.ids.perc.text = str(float("{0:.2f}".format(float(self.ids.perc.text)+100/len(self.test))))
            #self.check()
            if float(self.ids.perc.text) >= 100:
                self.ids.perc.text = '100'

        else:
            self.ids.perc.text = '100'
        
#update if choose wrong
    def updateN(self):
        if self.check():

            self.ids.perc.text = str(float("{0:.2f}".format(float(self.ids.perc.text)-2*100/len(self.test))))
            if float(self.ids.perc.text) <= 0:
                self.ids.perc.text = '0'
        else:
            self.ids.perc.text = '100'



#check if we have complete the class
    def check(self):
        if float(self.ids.perc.text) >=100:
            self.ids.perc.text = str(100)
            self.ids.perc.color = 0,0.55,0.22,1
            return False
        else:
            return True

#no answer is the same of wrong
    def noanswer(self):
        if ((self.ids.btn0.background_normal == self.ids.btn1.background_normal) and (self.ids.btn2.background_normal == self.ids.btn3.background_normal)) :
            self.updateN()
 
    


#if word = bad word we refres
    def checkword(self):
        if self.ids.btn.text[0:10] == '[i]LEKTION':
           self.refres()
        
        elif (self.ids.btn0.text[0:10] == '[i]LECCIÓN') or (self.ids.btn1.text[0:10] == '[i]LECCIÓN') or (self.ids.btn2.text[0:10] == '[i]LECCIÓN') or (self.ids.btn3.text[0:10] == '[i]LECCIÓN'):
            self.refres()

        elif self.ids.btn0.text == self.ids.btn1.text or self.ids.btn0.text == self.ids.btn2.text or self.ids.btn0.text == self.ids.btn3.text or self.ids.btn1.text == self.ids.btn2.text or self.ids.btn1.text == self.ids.btn3.text or self.ids.btn2.text == self.ids.btn3.text:
            self.refres()
        else:

            for i in ScreenManagement.Badlist:
                i = '[i]'+i+'[/i]'
    
                if (self.ids.btn0.text == i) or (self.ids.btn1.text == i) or (self.ids.btn2.text == i) or (self.ids.btn3.text == i):
                    self.refres()





#test interaction
    def on_click0(self):
        try:
            if self.solution.index(self.ids.btn0.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                #self.ids.btn0.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                self.ids.btn0.background_normal = 'indImageGreen.png'
                self.ids.btn0.background_down = 'PageImageGreen.png'
                self.updateP()
            else:
                self.updateN()
                #self.ids.btn0.text = '[color=cd0000][i]Sehr schlecht[/i][/color]!'
                self.ids.btn0.background_normal = 'indImageRed.png'
                self.ids.btn0.background_down = 'indImageRed.png'
                if self.solution.index(self.ids.btn1.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    self.ids.btn1.background_normal = 'indImageGreen.png'
                    self.ids.btn1.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn2.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn2.background_normal = 'indImageGreen.png'
                    self.ids.btn2.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn3.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn3.background_normal = 'indImageGreen.png'
                    self.ids.btn3.background_down = 'indImageGreen.png'
        except:
            self.ids.btn0.text = self.ids.btn0.text
            
    def on_click1(self):
        try:
            if self.solution.index(self.ids.btn1.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                #self.ids.btn1.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                self.ids.btn1.background_normal = 'indImageGreen.png'
                self.ids.btn1.background_down = 'indImageGreen.png'
                self.updateP()
            else:
                self.updateN()
                #self.ids.btn1.text = '[color=cd0000][i]Sehr schlecht[/i][/color]!'
                self.ids.btn1.background_normal = 'indImageRed.png'
                self.ids.btn1.background_down = 'indImageRed.png'
                if self.solution.index(self.ids.btn0.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    self.ids.btn0.background_normal = 'indImageGreen.png'
                    self.ids.btn0.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn2.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn2.background_normal = 'indImageGreen.png'
                    self.ids.btn2.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn3.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn3.background_normal = 'indImageGreen.png'
                    self.ids.btn3.background_down = 'indImageGreen.png'
        except:
            self.ids.btn1.text = self.ids.btn1.text
            
    def on_click2(self):
        try:
            if self.solution.index(self.ids.btn2.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                self.ids.btn2.background_normal = 'indImageGreen.png'
                self.ids.btn2.background_down = 'indImageGreen.png'
                self.updateP()
            else:
                self.updateN()
                #self.ids.btn2.text = '[color=cd0000][i]Sehr schlecht[/i][/color]!'
                self.ids.btn2.background_normal = 'indImageRed.png'
                self.ids.btn2.background_down = 'indImageRed.png'
                if self.solution.index(self.ids.btn1.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    self.ids.btn1.background_normal = 'indImageGreen.png'
                    self.ids.btn1.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn0.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn0.background_normal = 'indImageGreen.png'
                    self.ids.btn0.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn3.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn3.background_normal = 'indImageGreen.png'
                    self.ids.btn3.background_down = 'indImageGreen.png'
        except:
            self.ids.btn2.text = self.ids.btn2.text
            
    def on_click3(self):
        try:
            if self.solution.index(self.ids.btn3.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                #self.ids.btn3.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                self.ids.btn3.background_normal = 'indImageGreen.png'
                self.ids.btn3.background_down = 'indImageGreen.png'
                self.updateP()
            else:
                self.updateN()
                #self.ids.btn3.text = '[color=cd0000][i]Sehr schlecht[/i][/color]!'
                self.ids.btn3.background_normal = 'indImageRed.png'
                self.ids.btn3.background_down = 'indImageRed.png'
                if self.solution.index(self.ids.btn1.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    self.ids.btn1.background_normal = 'indImageGreen.png'
                    self.ids.btn1.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn2.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn2.background_normal = 'indImageGreen.png'
                    self.ids.btn2.background_down = 'indImageGreen.png'
                elif self.solution.index(self.ids.btn0.text.replace('[i]','').replace('[/i]','')) == self.test.index(self.ids.btn.text.replace('[i]','').replace('[/i]','')):
                    #self.ids.btn2.text = '[color=006400][i]Sehr gut[/i][/color]!!'
                    self.ids.btn0.background_normal = 'indImageGreen.png'
                    self.ids.btn0.background_down = 'indImageGreen.png'
        except:
            self.ids.btn3.text = self.ids.btn3.text


#to update the gameScreen page          
    def refres(self):

        self.num = random.choice(range(4))
        self.solution = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Es'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')
        self.test = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Al'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')
        self.randnum = random.choice(range(len(self.solution))),random.choice(range(len(self.solution))),random.choice(range(len(self.solution))),random.choice(range(len(self.solution)))
        self.ids.btn.text = '[i]'+self.test[self.randnum[self.num]]+'[/i]'
        self.ids.btn0.text = '[i]'+self.solution[self.randnum[0]]+'[/i]'
        self.ids.btn1.text = '[i]'+self.solution[self.randnum[1]]+'[/i]'
        self.ids.btn2.text = '[i]'+self.solution[self.randnum[2]]+'[/i]'
        self.ids.btn3.text = '[i]'+self.solution[self.randnum[3]]+'[/i]'
        self.ids.btn3.background_normal = 'PageImage.png'
        self.ids.btn3.background_down = 'indImage.png'
        self.ids.btn2.background_normal = 'PageImage.png'
        self.ids.btn2.background_down = 'indImage.png'
        self.ids.btn1.background_normal = 'PageImage.png'
        self.ids.btn1.background_down = 'indImage.png'
        self.ids.btn0.background_normal = 'PageImage.png'
        self.ids.btn0.background_down = 'indImage.png'
        self.checkword()
        #self.load()
        


#popup to explain % in gamescreen       
    def popp(self):
         p = PopupP()
         p.open()
            

#button of recycleview       
class MyButton(Button):
    def __init__(self,**kwargs):
        super(MyButton,self).__init__(**kwargs)
        self.markup = True
        self.background_normal = 'PageImage.png'
        #self.background_color = [1, 1, 1, 1]
        if ScreenManagement.SCREEN == 'Verben':
            self.background_down = 'indImage.png'
        else:
            self.background_down = 'PageImage.png'

        self.border = 50,50,50,50
        self.color = [0,0,0,1]
        self.font_size = 35
        self.text_size: self.size
        self.valign: 'middle'
        self.halign: 'right'

        #self.size_hint_y = 100 #doesn't work
        

    
    def on_click(self):
        
        if ScreenManagement.SCREEN == 'Verben':
            try: 
                PopButton.data = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Al'].split('\n\n')[1:].index(self.text.replace('[/i]','').replace('[i]',''))
            except:
                try:
                    PopButton.data = JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['Es'].split('\n\n')[1:].index(self.text.replace('[/i]','').replace('[i]',''))
                except:
                    print('da implementare')


            self.fire_popup()
        else:
            pass
        '''
        if ScreenManagement.control == '0':
        
            webbrowser.open('https://context.reverso.net/traduccion/aleman-espanol/'+self.text.replace('[i]','').replace('[/i]','').replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace(' -n','').replace(' -s','').replace(' -en','').replace(' -..e','').replace(' -e',''))
        else:
            webbrowser.open('https://context.reverso.net/traduccion/aleman-espanol/'+self.text.replace('[i]','').replace('[/i]','').replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace(' -n','').replace(' -s','').replace(' -en','').replace(' -..e','').replace(' -e','').split()[0])
        '''
    def fire_popup(self):
        pops=SimplePopup()
        pops.open()
        




#Pupup botton
class PopButton(Button):
    def __init__(self,**kwargs):
        super(PopButton,self).__init__(**kwargs)
        self.markup = True
        self.background_normal = ''
        self.background_color= 244/255,209/255,167/255,1
        self.background_down = ''
        self.font_size = 70
        self.size= self.texture_size
        self.halign= 'center'
        self.data = 0
        #self.on_press= dismiss()

        
        try:
            self.text = '[color=000000][u]1[/u][/color]'+'\n'+JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex1Al'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')[PopButton.data] +'\n\n'+ JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex1Es'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')[PopButton.data]+'\n\n\n'+'[color=000000][u]2[/u][/color]'+'\n'+JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex2Al'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')[PopButton.data] +'\n\n'+ JsonStore("A1deutsch.json").get('LEKTION '+ScreenManagement.MY_GLOBAL)['ex2Es'].replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace('\n\n\n','\n\n').split('\n\n')[PopButton.data]
        except:
            self.text = 'da implementare'
        #self.text_size= root.width, None




class SimplePopup(Popup):
    def __init__(self,**kwargs):
        super(SimplePopup,self).__init__(**kwargs)
        #self.padding = (Window.size[0]/20,0,Window.size[0]/20,0)
        self.id = 'pop'
        self.size_hint= 1, 1
        self.auto_dismiss= False
        self.title= 'Beispielen'
        self.separator_color = 1,0.55,0,1
        self.title_font = 'Roboto'
        self.title_size = 50
        self.title_color = 1,1,1,1
        self.title_align = 'center'
        self.content= PopButton(on_release = self.dismiss,text_size= (Window.size[0]-Window.size[0]/10, None))#cool part
        

class PopupP(Popup):
    def __init__(self,**kwargs):
        super(PopupP,self).__init__(**kwargs)
        #self.id = 'pop'
        self.size_hint= 1, 1
        self.auto_dismiss= False
        self.title= 'FORTSCHRITT'
        self.separator_color = 1,0.55,0,1
        self.title_font = 'Roboto'
        self.title_size = 50
        self.title_color = 1,1,1,1
        self.title_align = 'center'
        self.content= Button(on_release = self.dismiss,text_size= (Window.size[0]-Window.size[0]/10, None), text = '[u]Use this to see your progress[/u]',markup = True,background_normal = '',background_color= (244/255,209/255,167/255,1),background_down = '',font_size = 70,halign= 'center')
      

    
#store = JsonStore('A1deutsch.json')
class ScreenManagement(ScreenManager):
    MY_GLOBAL = '1'
    SCREEN = ''
    control = '0'
    Badlist = ['LECCIÓN','Otras palabras clave','Personal','Trabajo y Formación','Otras palabras importantes']
    #user = 'c2DEUTSCH'
    #userpassword = 'c2DEUTSCH'
    pass

        

    
presentation = Builder.load_string('''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import webbrowser webbrowser
#:import Window kivy.core.window.Window


<MyButton>:
    on_release: 
        self.on_click()
        #webbrowser.open('https://context.reverso.net/traduccion/aleman-espanol/'+self.text.replace('[i]','').replace('[/i]','').replace('[/color]','').replace('[color=27408b]','').replace('[color=cd0000]','').replace(' -n','').replace(' -s','').replace(' -en','').replace(' -..e','').replace(' -e',''))
        #print(self.state)
<IndexButton@Button>:
    
    markup: True
    background_normal:'indImage.png'
    background_down:'PageImage.png'
    border:60,60,60,60
    font_size: 50
    


<Back1Button@Button>:
    markup: True
    background_normal:'backImage1.png'
    background_down:'backImage1.png'
    #border:60,60,60,60
    #font_size: 50



<BoxLayoutPage@BoxLayout>:
    #padding:20,20,20,20
    orientation:'vertical'
    canvas.before:
        Color:
            rgba: 244/255,209/255,167/255,1
        Rectangle:
            pos: self.pos
            size: self.size


<BoxLayoutPage1@BoxLayout>:
    #padding:20,20,20,20
    orientation:'horizontal'
    canvas.before:
        Color:
            rgba: 244/255,209/255,167/255,1
        Rectangle:
            pos: self.pos
            size: self.size
        

<BoxLayoutPage2@BoxLayout>:
    #padding:20,20,20,20
    orientation:'horizontal'
    
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
        
            
<RecycleView>:
    
    RecycleGridLayout:
        cols:2
        default_size_hint: 1, None
        size_hint: 1,None
        height: self.minimum_height
        spacing: 10,90
        
        
        #row_default_height: 110
        #row_force_default: True
        
        
        
        
   
<ButtonBack@Button>:
    #text: "[i]Back[/i]"
    #pos_hint: {"right":0.4, "top":0.95}
    #color:0,0,0,1
    background_normal :'back.png'
    background_down :'back.png'
    #size_hint: 0.3, 0.9
    markup: True
    #font_size: 60

  
            
<GameButton@Button>:
    
    font_size: 60
	color: 0,0,0,1
    markup: True
	#size_hint: 0.2, 0.1
    background_down: 'indImage.png'
    background_normal: 'indImage.png'
    border: 30,30,30,30




    
ScreenManagement:
    transition: FadeTransition()
    IntroScreen:
    IndexScreen:
    A11Screen:
    A12Screen:
    L1Screen:
    L2Screen:
    L3Screen:
    L4Screen:
    L5Screen:
    L6Screen:
    L7Screen:
    L8Screen:
    L9Screen:
    L10Screen:
    L11Screen:
    L12Screen:
    L13Screen:
    L14Screen:
    L15Screen:
    L16Screen:
    L17Screen:
    L18Screen:
    L19Screen:
    L20Screen:
    L21Screen:
    L22Screen:
    L23Screen:
    L24Screen:
    VerbenScreen:
    GameScreen:


<IntroScreen>:
    name: "login_page"

    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 244/255,209/255,167/255,1
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            orientation: 'vertical'
            

            FloatLayout:                
                Label:
                    font_size: Window.size[0]/7.2
                    markup: True
                    text: "[i]c2 DEUTSCH\\n    niveu A1[/i]"
                    pos_hint: {"right":1, "top":1}
                    color: 1,1,1,1
                    size_hint: 1, 1
        #BoxLayout:
            #size_hint_y: 0.35
            #markup: True
            #padding:120,0,120,650
            #orientation: 'vertical'
            #size_hint_y: 0.5
                
            #TextInput:
                
                #id: login
                #font_size:80
                #text: 'Ichliebe'
                #multiline: False

            #TextInput:
                
                #id: passw
                #password: True # hide password
                #font_size:80
                #text: 'Deutsch'
                #multiline: False

                Button:
                    size_hint_y : 0.1
                    text:'¿Quieres saber más sobre nosotros?'
                    font_size : 40
                    background_normal: ''
                    background_color: 244/255,209/255,167/255,1
                    background_down: ''
                    pos_hint: {"right":1, "top":0.37}
                    on_press: webbrowser.open('https://www.c2deutsch.com/?gclid=EAIaIQobChMIpO30n_Ce6AIVRUPTCh2A3gDlEAAYASAAEgKjQPD_BwE')


        BoxLayoutPage2:
            size_hint_y: 0.1
            orientation:'vertical'
                
            
            Button:   
                font_size: 50
                color: 0,0,0,1
                size_hint: 1, 1
                markup: True
                background_color: 1,1,1,1
                background_normal: ''
                background_down: ''
            
                text: "[i]BEGINNEN[/i]"
                #on_release: root.verify_credentials()
                on_release: app.root.current = "Index" 


<IndexScreen>:
     
    name: "Index"
    canvas.before:
        Color:
            rgba: 244/255,209/255,167/255,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        padding:35,20,35,20
    

        GridLayout:
            orientation: "vertical"
            size_hint_y: 1
            padding: 40,Window.size[1]/4,40,Window.size[1]/4
            height: self.minimum_height\n
            row_default_height: 60
            cols:1
            spacing:80,Window.size[1]/13
            
            
                
            IndexButton:
                font_size: 100
                color: 244/255,209/255,167/255,1
                text:"[i]A1.1[/i]"
                on_release: 
                    app.root.current = "A11"    
            IndexButton:
                font_size:100
                color: 244/255,209/255,167/255,1
                text:"[i]A1.2[/i]"  
                on_release: 
                    app.root.current = "A12"        
            IndexButton:
                font_size: 100
                color: 244/255,209/255,167/255,1
                text:"[i]Verben[/i]"
                on_release: app.root.current = "Verben"
            

            
<A11Screen>:
     
    name: "A11"
    canvas.before:
        Color:
            rgba: 244/255,209/255,167/255,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        padding:50,20,50,20
        BoxLayoutPage1:
            size_hint_y: 0.2
            FloatLayout:   
                Back1Button:
                    on_release: 
                        app.root.current = "Index"  
                    size_hint: 0.2, 0.4
                    pos_hint: {"right":0.2, "top":0.75}
                    #size_hint_x: 0.1
                
                Label:
                    text: 'Lektionen'
                    font_size:80
                    pos_hint: {"right":1, "top":0.60}
                    
                
               
        
    

        GridLayout:
            orientation: "vertical"
            size_hint_y: 1
            padding: 20,Window.size[1]/13,20,Window.size[1]/12
            height: self.minimum_height\n
            row_default_height: 60
            spacing:50,50
            cols:3
            
                
 
     

            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]1[/i]"
                on_release: app.root.current = "L1"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]2[/i]"
                on_release: app.root.current = "L2"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]3[/i]"
                on_release: app.root.current = "L3"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]4[/i]"
                on_release: 
                    app.root.current = "L4"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]5[/i]"
                on_release: app.root.current = "L5"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]6[/i]"
                on_release: app.root.current = "L6"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]7[/i]"
                on_release: app.root.current = "L7"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]8[/i]"
                on_release: app.root.current = "L8"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]9[/i]"
                on_release: app.root.current = "L9"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]10[/i]"
                on_release: app.root.current = "L10"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]11[/i]"
                on_release: app.root.current = "L11"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]12[/i]"
                on_release: app.root.current = "L12"           

<A12Screen>:
	name: "A12"
    canvas.before:
        Color:
            rgba: 244/255,209/255,167/255,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        padding:50,20,50,20
        BoxLayoutPage1:
            size_hint_y: 0.2
            FloatLayout:   
                Back1Button:
                    on_release: 
                        app.root.current = "Index"  
                    size_hint: 0.2, 0.4
                    pos_hint: {"right":0.2, "top":0.75}
                    #size_hint_x: 0.1
                
                Label:
                    text: 'Lektionen'
                    font_size:80
                    pos_hint: {"right":1, "top":0.60}
    

        GridLayout:
            orientation: "vertical"
            size_hint_y: 1
            padding: 20,Window.size[1]/13,20,Window.size[1]/12
            height: self.minimum_height\n
            row_default_height: 60
            spacing:50,50
            cols:3
            
                


                

            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]13[/i]"
                on_release: app.root.current = "L13"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]14[/i]"
                on_release: app.root.current = "L14"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]15[/i]"
                on_release: app.root.current = "L15"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]16[/i]"
                on_release: app.root.current = "L16"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]17[/i]"
                on_release: app.root.current = "L17"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]18[/i]"
                on_release: app.root.current = "L18"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]19[/i]"
                on_release: app.root.current = "L19"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]20[/i]"
                on_release: app.root.current = "L20"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]21[/i]"
                on_release: app.root.current = "L21"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]22[/i]"
                on_release: app.root.current = "L22"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]23[/i]"
                on_release: app.root.current = "L23"
            IndexButton:
                color:244/255,209/255,167/255,1
                text:"[i]24[/i]"
                on_release: app.root.current = "L24"

<L1Screen>:
	name: "L1"      
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]
        BoxLayoutPage2:
            size_hint_y: 0.1


            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
<L2Screen>:
	name: "L2"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L3Screen>:
	name: "L3"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L4Screen>:
	name: "L4"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L5Screen>:
	name: "L5"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L6Screen>:
	name: "L6"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L7Screen>:
	name: "L7"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L8Screen>:
	name: "L8"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L9Screen>:
	name: "L9"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L10Screen>:
	name: "L10"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L11Screen>:
	name: "L11"
    on_pre_enter: root.change()         
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
<L12Screen>:
	name: "L12"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A11" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L13Screen>:
	name: "L13"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L14Screen>:
	name: "L14"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L15Screen>:
	name: "L15"   
    on_pre_enter: root.change()   
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L16Screen>:
	name: "L16"     
    on_pre_enter: root.change() 
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L17Screen>:
	name: "L17"   
    on_pre_enter: root.change()   
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L18Screen>:
	name: "L18"   
    on_pre_enter: root.change()   
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L19Screen>:
	name: "L19"  
    on_pre_enter: root.change()    
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L20Screen>:
	name: "L20"  
    on_pre_enter: root.change()    
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L21Screen>:
	name: "L21"   
    on_pre_enter: root.change()   
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
<L22Screen>:
	name: "L22"  
    on_pre_enter: root.change()    
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L23Screen>:
	name: "L23"    
    on_pre_enter: root.change()  
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game" 
                    
                    
                    
<L24Screen>:
	name: "L24" 
    on_pre_enter: root.change()     
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
        
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]  
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: app.root.current = "A12" 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                on_press:root.change()
                on_release:
                    app.root.current = "Game"
                    
                    
<VerbenScreen>:
	name: "Verben"  
    on_pre_enter: root.change()  
    BoxLayoutPage:
        BoxLayoutPage1:
            size_hint_y: 0.1

            Label:
                text: root.Al[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            Label:
                text: root.Es[0].replace('[color=cd0000]','').replace('[/color]','')
                font_size : 70
            
        RecycleView:
            viewclass: 'MyButton'
            data:[{'text': str('[i]'+x+'[/i]')} for x in root.test()]   
            
        BoxLayoutPage2:
            size_hint_y: 0.1
            ButtonBack:
                on_release: 
                    app.root.current = "Index"
                    root.bck() 
            Button:
                background_normal : ''
                background_color: 1,1,1,1
                text:'TEST'
                background_down : ''
                color:0,0,0,1
                font_size : 70
                on_press:root.change()
                on_release:
                    app.root.current = "Game"

        


  
<GameScreen>:

	name: "Game"
    on_pre_enter:
        root.refres()
        root.load()
    
    
    canvas.before:
        Color:
            rgba: 244/255,209/255,167/255,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:

        orientation: "vertical"
        #padding: 30,30,30,30

        BoxLayout:

            orientation: "vertical"
            padding:50,0,50,0
            size_hint_y: 0.1

            FloatLayout:   
                Back1Button:
                    on_release:
                        app.root.current = root.manager.SCREEN
                    size_hint: 0.2, 1
                    pos_hint: {"right":0.2, "top":0.75}
                    #size_hint_x: 0.1
        BoxLayout:

            orientation: "vertical"
            padding: 30,30,30,30
            size_hint_y: 0.2

            FloatLayout:   


                Label:
                    
                    markup: True
                    font_size: 70
                    text: '[i]Was ist...?[/i]'
                    pos_hint: {"right":0.615, "top":1}
                    color: 1,1,1,1
                    size_hint: 0.2, 0.1
                
                
                Label:
                    id:btn
                    markup: True
                    font_size: 90
                    size: self.texture_size
                    halign: 'center'
                    text_size: (self.width-self.width/20, None)
                    text: '[i]'+root.test[root.randnum[root.num]]+'[/i]'
                    pos_hint: {"right":1, "top":0}
                    color: 1,1,1,1
                    size_hint: 1, 0.1




        BoxLayout:

            orientation: "vertical"
            padding: 30,30,30,30

            GridLayout:
                
                spacing: '40dp'
                orientation: "vertical"
                
                padding: 30,Window.size[1]/10,30,Window.size[1]/10
                
                row_default_height: 60
                cols:1
                


               
                
                GameButton:
                    id: btn0
                    text: '[i]'+root.solution[root.randnum[0]]+'[/i]'
                    on_release: root.on_click0()
                    
                GameButton:
                    id: btn1
                    text: '[i]'+root.solution[root.randnum[1]]+'[/i]'
                    on_release: root.on_click1()
                    
                GameButton:
                    id: btn2
                    text: '[i]'+root.solution[root.randnum[2]]+'[/i]'
                    on_release: root.on_click2()
                       
                GameButton:
                    id: btn3
                    text: '[i]'+root.solution[root.randnum[3]]+'[/i]'
                    on_release: root.on_click3()
                
  
        BoxLayoutPage2:
            size_hint_y: 0.15
            canvas.before:
                Color:
                    rgba: 244/255,209/255,167/255,1
                Rectangle:
                    pos: self.pos
                    size: self.size

                    
            FloatLayout:
                Button:
                    background_normal: 'prova.png'
                    background_down: 'prova.png'
                    size_hint: 0.2, 1
                    pos_hint: {"right":1, "top":1}
                    #background_color: 244/255,209/255,167/255,1
                    #text:'nächste'
                    font_size : 80
                    on_press:
                        root.noanswer()
                    on_release:
                        root.refres()
                        root.save()
                        

                Button:
                    background_normal : ''
                    background_down: ''
                    background_color: 244/255,209/255,167/255,1
                    markup: True
                    color:1,1,1,1
                    size_hint: 0.2, 1
                    font_size: 50
                    text: '%'
                    pos_hint: {"right":0.4, "top":1}
                    color: 1,1,1,1
                    on_press: root.popp()
                Button:
                    id:perc
                    background_normal : ''
                    background_down: ''
                    background_color: 244/255,209/255,167/255,1
                    markup: True
                    size_hint: 0.2, 1
                    font_size: 100
                    color:1,1,1,1
                    text: '0'
                    pos_hint: {"right":0.6, "top":1}
                    color: 1,1,1,1
                    on_press: root.popp()
                    
                    

            



        
            ''')



#store.get('LEKTION 24')['Al']
        



class MainApp(App):
    
    
    
    
    
    def build(self):
        
        
        self.icon = 'icon.png'

        return presentation

    def on_start(self):
        #print(ScreenManagement.uno)
        #ScreenManagement.uno+=1
        pass

    def on_pause(self):

      # Here you can save data if needed
      return True

    def on_stop(self):
        
        #print('Saludos!')
        pass
      


if __name__ == "__main__":
    MainApp().run()
