import flet as ft
from source import ENV_LIST as ENV
from source.MainView import MainView


class MainApp():
    def __init__(self):
        pass

    def build(self, page: ft.Page):
        #AppWindowの基本設定
        page.bgcolor =ft.colors.BACKGROUND#ft.colors.AMBER# page.window_bgcolor = ft.colors.TRANSPARENT
        # page.bgcolor = ft.colors.TRANSPARENT
        #page.theme = ft.theme.Theme(color_scheme_seed=ENV.PLOT_DEFAULT_COLOR)
        page.theme_mode = "dark"

        page.title = ENV.APP_NAME
        #page.window.always_on_top = ENV.WINDOW_ALWAYS_ON_TOP
        page.spacing = 0
        page.padding = 0
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # page.window.resizable = True
        # page.window.maximized = False
        # page.window.full_screen = False

        # page.window.width = ENV.DEFAULT_PAGE_WIDTH
        # page.window.height = ENV.DEFAULT_PAGE_HEIGHT

        #コントロールの追加
        page.add(MainView())




    def run(self):
        #check : configファイルの読み込みする？
        #appの起動
        ft.app(target=self.build)
        pass
        #ENVの値をconfigファイルに保存

############################## Run ##############################
if __name__ == '__main__':
    MainApp().run() #GUIアプリを起動する


