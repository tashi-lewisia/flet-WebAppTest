###
#   MVVMモデルにおける、いわゆるViewModelに相当するクラス
#   アプリ全体のビューの変更を一括で管理する.
#
#   繋がり方は以下の通り
#   各view ----(DM.command関数)---> DataManager ----(import)---> 各メソッド
#          <---(flet Ref機能) ----
#
#   ViewManagerはアプリにつき１つのみ（インスタンスは生成しない）想定なので
#   基本はクラス変数、クラス関数として定義していく.
###
###
#   import
###
import flet as ft
import asyncio

from source import ENV_LIST as ENV
from source.BackEnd import BackEnd as BE


class ViewManager():
    def __init__(self):
        pass
    ################################################################################
    #                                クラス変数
    ################################################################################
    #   Ref 機能
    refMainView = ft.Ref[ft.Stack]()
    refText = ft.Ref[ft.Text]()

    # viewのupdateを行うかどうか
    runningViewUpdate = False

    ################################################################################
    #                                  メソッド
    ################################################################################
    # ビューを定期的に更新する
    @classmethod
    async def ViewUpdate(cls):
        while cls.runningViewUpdate:
            #各データをviewに渡す 
            #!(BEで勝手にデータが変更される全てのrefに対して行う)
            #!要素が多い場合は、ちゃんとobseverなどの手法を取り入れた方が良さそう
            cls.UpdateRef(cls.refText, "value", BE.count)


            # リフレッシュレートの時間だけ待つ
            await asyncio.sleep(ENV.REFRESH_RATE)
        pass



    #ビューの更新を開始する
    @classmethod
    def StartViewUpdate(cls):
        #新しいスレッドで描画を開始する
        cls.runningViewUpdate = True
        cls.refMainView.current.page.run_task(cls.ViewUpdate)
        pass


    #ビューの更新を終了する
    @classmethod
    def StopViewUpdate(cls):
        cls.runningViewUpdate = False
        pass


    #データが変更されていれば見た目を更新する
    @classmethod
    def UpdateRef(cls, ref, varName, newValue):
        #値が変更されているかを確認する
        if  getattr(ref.current, varName) != newValue:
            #変更されていればRefの方の値を更新する
            setattr(ref.current, varName, newValue)
            ref.current.update()



    @classmethod
    def ButtonClick(cls,e):
        BE.IncrementCount()