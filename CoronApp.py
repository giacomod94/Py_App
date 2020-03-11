#coronapp
#json
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
#from gtts import gTTS 
from kivy.core.audio import SoundLoader 
import webbrowser


class IntroScreen(Screen):
    pass   


class ItalyScreen(Screen):
    def __init__(self, **kwargs):
        super(ItalyScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/italy/'
        
class SpainScreen(Screen):
    def __init__(self, **kwargs):
        super(SpainScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/spain/'
        
class GermanScreen(Screen):
    def __init__(self, **kwargs):
        super(GermanScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/germany/'
        
        
class IranScreen(Screen):
    def __init__(self, **kwargs):
        super(IranScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/iran/'
        
        
class USAScreen(Screen):
    def __init__(self, **kwargs):
        super(USAScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/us/'
        
        
class FranceScreen(Screen):
    def __init__(self, **kwargs):
        super(FranceScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/France/'
        
        
class SKoreaScreen(Screen):
    def __init__(self, **kwargs):
        super(SKoreaScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/south-korea/'
        
        
class ChinaScreen(Screen):
    def __init__(self, **kwargs):
        super(ChinaScreen, self).__init__(**kwargs)

        #Clock.schedule_once(lambda *args: self.load())
    def change(self):
        ScreenManagement.MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/China/'
        
        
        
        
class ScreenManagement(ScreenManager):
    MY_GLOBAL = 'https://www.worldometers.info/coronavirus/country/italy/'


    pass

        
        
class MyButton(Button):
    def __init__(self,**kwargs):
        super(MyButton,self).__init__(**kwargs)
        self.markup = True
        self.background_normal = ''
        self.background_color = [1, 0, 0, 1]
        self.color = [0,0,0,1]
        self.font_size = 100

    
    def on_click(self):
        
        webbrowser.open(ScreenManagement.MY_GLOBAL)
            
            
presentation = Builder.load_string('''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import webbrowser webbrowser


<MyButton>:
    on_press: 
        self.on_click()
        
<ButtonBack@Button>:
    text:'Back'
    pos_hint: {"right":0.6, "top":0.2}
    background_normal: ''
    background_color: 1, 0, 0, 1
    color: 0,0,0,1
    size_hint: 0.2, 0.1
    on_release: app.root.current = "Index"
        
<IndexButton@Button>:

    markup: True
    background_normal: ''
    background_color: 1, 1, 1, 1
    font_size: 50
 
ScreenManagement:
    transition: FadeTransition()
    IntroScreen:
    ItalyScreen:
    SpainScreen:
    GermanScreen:
    IranScreen:
    USAScreen:
    FranceScreen:
    SKoreaScreen:
    ChinaScreen:
    

<IntroScreen>:
	name: "Index"
    canvas.before:
        Color:
            rgba: 1, 0.55, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
    

        GridLayout:
            orientation: "vertical"
            size_hint_y: 1
            padding: 20,20,20,20
            height: self.minimum_height\n
            row_default_height: 60
            cols:3
            
                
            IndexButton:

            IndexButton:
                font_size: 60
                text:"[color=0a0a0a][i]CoronApp[/i][/color]"  
            IndexButton:
            
            IndexButton:
                text:"[color=27408b][i]GLOBAL[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/')
            IndexButton:
                text:"[color=cd0000][i]ITALY[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/italy/')
            IndexButton:
                text:"[color=cd0000][i]SPAIN[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/spain/')
            IndexButton:
                text:"[color=cd0000][i]GERMANY[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/germany/')
            IndexButton:
                text:"[color=cd0000][i]CHINA[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/China/')
            IndexButton:
                text:"[color=cd0000][i]SOUTH KOREA[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/south-korea/')
            IndexButton:
                text:"[color=cd0000][i]IRAN[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/iran/')
            IndexButton:
                text:"[color=cd0000][i]FRANCE[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/France/')
            IndexButton:
                text:"[color=cd0000][i]USA[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/country/us/')
            IndexButton:
                text:"[color=27408b][i]WORLD TAB[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/#countries')
            IndexButton:
                text:"[color=27408b][i]OPINIONS[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/coronavirus-expert-opinions/')
            IndexButton:
                text:"[color=27408b][i]NEWS[/i][/color]"
                on_release: webbrowser.open('https://www.worldometers.info/coronavirus/#news')
           
 
 
                
<ItalyScreen>:
	name: "Italy" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:
                
                
<SpainScreen>:
	name: "Spain" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:

                
                
<GermanScreen>:
	name: "Germany" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:
            
<ChinaScreen>:
	name: "China" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:
            
<SKoreaScreen>:
	name: "Skorea" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:
            
<FranceScreen>:
	name: "France" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:
            
<USAScreen>:
	name: "USA" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:
            
            
<IranScreen>:
	name: "Iran" 
    on_pre_enter: root.change() 
    BoxLayout:

        FloatLayout:    
            
            padding: 20,20,20,20
            MyButton:
                text:'Push Me'
                on_release: self.on_click()
            ButtonBack:

                
                
            
            
        
            ''')



#store.get('LEKTION 24')['Al']
        



class MainApp(App):
    
    
    
    
    def build(self):
        
        self.icon = 'icon.png'

        return presentation


if __name__ == "__main__":
    MainApp().run()

        
        
   