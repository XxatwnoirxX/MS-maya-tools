# !/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------
#   ScriptName  : ControllerGenerator
#   Author      : Atsushi Hirata
#   Since       : 2022/11
#   Update      : None
#----------------------------------------------

import maya.cmds as cmds
from maya.common.ui import LayoutManager

#変数の初期化
windowName = "ControllerGenerator"
window_width = 500
window_height = 500
controllerType = "CNT_CUBE"
mode = ""

#python3.10で実装予定のパターンマッチング構文(match case)対応バージョン
#maya2022ではまだ未実装のため使用不可
"""
#コントローラーを作成
def MakeController(self, controllerType):
    #match構文でコントローラーのタイプを判別、作成の処理を実行する
    cv = ""
    match controllerType:
        case "CNT_CUBE":
            cv = cmds.curve(d=1, p=[(0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5)
            , (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5)
            , (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5)
            , (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5)]
            ,k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], n="controller1")
        case "CNT_CIRCLE":
            cv = cmds.circle(nr=[0,1,0], r=1, o=True, ch=True, n="controller1")
        case _:
            #例外処理
            raise ValueError("controllerType Error! : コントローラーの指定変数が正しくありません。ツールを再起動してください。")
        
    #作成したコントローラーの名前を返す
    return cv
"""

#コントローラーを作成
def MakeController(self, controllerType):
    cv = ""

    #elif文でコントローラーのタイプを判別、作成の処理を実行する
    if controllerType == "CNT_CUBE":
        cv = cmds.curve(n="controller1", d=1,
                        p=[(0.5, 0.5, 0.5)
                        , (0.5, 0.5, -0.5)
                        , (-0.5, 0.5, -0.5)
                        , (-0.5, -0.5, -0.5)
                        , (0.5, -0.5, -0.5)
                        , (0.5, 0.5, -0.5)
                        , (-0.5, 0.5, -0.5)
                        , (-0.5, 0.5, 0.5)
                        , (0.5, 0.5, 0.5)
                        , (0.5, -0.5, 0.5)
                        , (0.5, -0.5, -0.5)
                        , (-0.5, -0.5, -0.5)
                        , (-0.5, -0.5, 0.5)
                        , (0.5, -0.5, 0.5)
                        , (-0.5, -0.5, 0.5)
                        , (-0.5, 0.5, 0.5)]
                        ,k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

    elif controllerType == "CNT_DIA":
        cv = cmds.curve(n="controller1", d=1, 
                        p=[(0, 1, 0)
                        , (1, 0, 0)
                        , (0, 0, 1)
                        , (-1, 0, 0)
                        , (0, 0, -1)
                        , (0, 1, 0)
                        , (0, 0, 1)
                        , (0, -1, 0)
                        , (0, 0, -1)
                        , (1, 0, 0)
                        , (0, 1, 0)
                        , (-1, 0, 0)
                        , (0, -1, 0)
                        , (1, 0, 0)]
                        , k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    elif controllerType == "CNT_FATCROSS":
        cv = cmds.curve(n="controller1", d=1, 
                        p=[(2, 0, 1)
                        , (2, 0, -1)
                        , (1, 0, -1)
                        , (1, 0, -2)
                        , (-1, 0, -2)
                        , (-1, 0, -1)
                        , (-2, 0, -1)
                        , (-2, 0, 1)
                        , (-1, 0, 1)
                        , (-1, 0, 2)
                        , (1, 0, 2)
                        , (1, 0, 1)
                        , (2, 0, 1)],
                        k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    
    elif controllerType == "CNT_CIRCLE":
        cv = cmds.circle(n="controller1", nr=[0,1,0], r=1, o=True, ch=True)
    
    elif controllerType == "CNT_SQARE":
        cv = cmds.nurbsSquare(n="controller1", c=[0, 0, 0], nr=[0, 1, 0]
                            , sl1=1, sl2=1, sps=1 ,d=3, ch=True)

    else:
        #例外処理
        raise ValueError("controllerType Error! : コントローラーの指定変数が正しくありません。ツールを再起動してください。")

    #作成したコントローラーの名前を返す
    return cv

#実装済み
#"CNT_CUBE","CNT_CIRCLE"

def main(self, mode):
    #選択中のオブジェクトの位置を取得
    pos = []
    rot  = []
    i = 0
    node = []
    ctrName = ""
    
    #選択中のオブジェクトをリストとして取得
    node = cmds.ls(selection = True)

    #選択しているノードがあるか判定
    if(0 == len(node)):
        #コントローラーを作成＆名前を取得
        ctrName = MakeController(self, mode)
    else:
        #ノードを選択していた場合それら全てにコントローラを作成し、コントローラをそれぞれの位置へ移動させる。
        for n in node:
            ctrName = MakeController(self, mode)

            #トランス、ロットを取得
            pos = cmds.xform(n, q=True, t=True, ws=True)
            rot = cmds.xform(n, q=True, ro=True, ws=True)

            #コントローラーの名前を参照＆選択したノードの場所へスナップ
            cmds.xform(ctrName, t=[pos[0], pos[1], pos[2]])
            cmds.rotate(rot[0], rot[1], rot[2], ctrName)


def GUI():
    global windowName
    #既にGUIが存在する時に古いほうを消す処理
    if cmds.window(windowName, ex=1):
        cmds.deleteUI(windowName)
    cmds.window(windowName, title=windowName, rtf=True, w=window_width, h=window_height, mnb=False, mxb=False, s=True)

    #GUIを作成
    with LayoutManager(cmds.tabLayout(imw=1, imh=1)) as tabs:
        with LayoutManager(cmds.gridLayout("controller",nc=5, cwh=[50, 50])) as grid01:
            #cmds.text("Normal" , al="center", w=window_width)
            cmds.iconTextButton(st="iconAndTextHorizontal", image1='CNT_CUBE.png'
            , l='cube', c="main('self', 'CNT_CUBE')")

            cmds.iconTextButton(st="iconAndTextHorizontal", image1='CNT_DIA.png'
            , l='dia', c="main('self', 'CNT_DIA')")

            cmds.iconTextButton(st="iconAndTextHorizontal", image1='CNT_FATCROSS.png'
            , l='FatCross', c="main('self', 'CNT_FATCROSS')")

            cmds.iconTextButton(st="iconAndTextHorizontal", image1='CNT_CIRCLE.png'
            , l='circle', c="main('self', 'CNT_CIRCLE')")

            cmds.iconTextButton(st="iconAndTextHorizontal", image1='CNT_SQARE.png'
            , l='sqare', c="main('self', 'CNT_SQARE')")
    
    cmds.showWindow(windowName)

def ControllerGenerator():
    GUI()

if __name__ == '__main__':  
    ControllerGenerator()
