from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.registration_screen import RegistrationScreen
from screens.upload_screen import UploadScreen
from screens.admin_screen import AdminScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrationScreen(name='register'))
        sm.add_widget(UploadScreen(name='upload'))
        sm.add_widget(AdminScreen(name='admin'))
        return sm

if __name__ == "__main__":
    MyApp().run()
