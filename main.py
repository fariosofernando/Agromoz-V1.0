from kivy.metrics import sp
from kivy.uix.widget import Widget
from config.hippoclasses import Models
from config.hippoclasses import ConfigMyapp
models = Models()
models.Builder.load_file('conception.kv')


class Barras(models.BoxLayout):
    ...
class BarrasP(models.BoxLayout):
    ...
class BarrasU(models.BoxLayout):
    ...

class PrimaryView(models.BoxLayout):
    def __init__(
        self, **kw
        ):
        super(PrimaryView, self).__init__(**kw)

    def animation_to_barras(
        self,object, *args
    ):
        anim = models.Animation(width = sp(200), duration =.05, t='in_back')
        anim.start(object)

    def animation_to_barras_bind(
        self, object, text, *args
    ):
        anim = models.Animation(width = sp(170), duration =.05, t='in_back') 
        anim.start(object)

    def animation_to_barras_button(
        self, object, *args
    ):
        anim = models.Animation(width = sp(70), duration= .05, t= 'in_back')
        anim.start(object)
        object.text = 'Negociar'

    def animation_to_barras_button_bind(
        self, object, *args
    ):
        anim = models.Animation(width = sp(10), duration= .05, t= 'in_back')
        anim.start(object)
        object.text = ''

    def animation_to_barrasp_button(
        self, object, *args
    ):
        anim = models.Animation(width = sp(70), duration= .05, t= 'in_back')
        anim.start(object)
        object.text = 'Editar'

    def animation_to_barrasp_button_bind(
        self, object, *args
    ):
        anim = models.Animation(width = sp(10), duration= .05, t= 'in_back')
        anim.start(object)
        object.text = ''

    def animation_to_barrasp(
        self,object, *args
    ):
        anim = models.Animation(width = sp(200), duration =.05, t='in_back')
        anim.start(object)

    def animation_to_barrasp_bind(
        self, object, text, *args
    ):
        anim = models.Animation(width = sp(170), duration =.05, t='in_back') 
        anim.start(object)
    def animation_to_barrasu(
        self,object, *args
    ):
        anim = models.Animation(width = sp(200), duration =.05, t='in_back')
        anim.start(object)

    def animation_to_barrasu_bind(
        self, object, text, *args
    ):
        anim = models.Animation(width = sp(170), duration =.05, t='in_back') 
        anim.start(object)


    def animation_to_barrasu_button(
        self, object, *args
    ):
        anim = models.Animation(width = sp(70), duration= .05, t= 'in_back')
        anim.start(object)
        object.text = 'Ver'

    def animation_to_barrasu_button_bind(
        self, object, *args
    ):
        anim = models.Animation(width = sp(10), duration= 1, t= 'in_back')
        anim.start(object)
        object.text = ''

    def animation_drop(
        self, drop, *args
    ):
        anim = models.Animation(pos_hint = {'top': .95 , 'x': .001}, duration= 1, t = 'in_back', opacity= 1)
        anim.start(drop)
        
    def animation_drop_back(
        self, drop, *args
    ):
        anim = models.Animation(pos_hint = {'top': .95 , 'x': -1}, duration= 1, t = 'in_back', opacity=0)
        anim.start(drop)
        drop.dismiss()


class RunmyApp(models.Aplicativo):
    def build(
        self
    ):  
        #ConfigMyapp().size_myscreen()
        return PrimaryView()

RunmyApp().run()