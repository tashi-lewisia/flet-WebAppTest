import flet as ft
from source.ViewManager import ViewManager as VM

######## 全てのビューを統括するクラス ########
class MainView(ft.Stack):
    def __init__(self):
        super().__init__(expand = True, ref = VM.refMainView)

        #GUIの設定
        self.controls = self.GetView()

        pass

    ################################################################################
    #                                GUIレイアウト
    ################################################################################
    def GetView(self):
        layout =[
                    ft.Column(
                        [
                            ft.ElevatedButton(
                                text = "Click",
                                on_click= VM.ButtonClick,
                                ),
                            ft.Text(
                                "OK",
                                ref = VM.refText,
                                ),
                            ft.Container(
                                bgcolor=ft.colors.AMBER,
                                expand=True,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        expand=True,
                    )
                ]


        return layout

    ################################################################################
    #                                method
    ################################################################################
    # ページへ追加時に呼ばれる関数
    def did_mount(self):
        VM.StartViewUpdate()
        return super().did_mount()

    # ページから削除時に呼ばれる関数
    def will_unmount(self):
        #既存のループを終了する.
        VM.StopViewUpdate()
        return super().will_unmount()

