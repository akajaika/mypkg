# mypkg
## robosys2024 課題2

このパッケージは、一つの基準となる写真とその他の写真の類似度をOpenCVのライブアリである特徴量マッチング（A-KAZE）を用いて出力するROS2パッケージです。

また、このパッケージは千葉工業大学 未来ロボティクス学科 2024年度 ロボットシステム学内で行った内容に、課題で作成したファイルを追加したものです。

[![test](https://github.com/akajaika/robosys2024_2/actions/workflows/test.yml/badge.svg)](https://github.com/akajaika/robosys2024_2/actions/workflows/test.yml)

このリポジトリ内の[similality_images.py](https://github.com/akajaika/robosys2024_2/blob/main/mypkg/similality_images.py)は、[ピーター (id:tetrapod117)](https://tetlab117.hatenablog.com/about)の[PythonとOpenCVを用いた顔の類似度判定についての話](https://tetlab117.hatenablog.com/entry/2017/09/28/163638)を参考に作られています。

## 使用環境
- ROS2 Humble
- Ubuntu22.04
- OpenCV 4.10.0

## テスト済みの環境
  * GitHub Actions 2.321.0
    * Ubuntu 22.04 LTS
        * Python 3.10.6

## similality_images 使い方
/mypkg/mypkg/images　の中に基準となるpngファイルをtarget.pngという名前で1枚入れます。また、比較したいpngファイルを任意の数入れsimilality_imagesを実行します。出力された数値が低いほど、類似度が高いということを示します。

```shell
$ cd mypkg/mypkg/
$ python3 similality_images.py
```

受信例(別端末にて)

```shell
$ python3 test_listener.py
[INFO] [1736071964.498597056] [similarity_listener]: Received similarity data: array('f', [141.43011474609375, 146.19354248046875])
[INFO] [1736071964.499113665] [similarity_listener]: Received filenames: スクリーンショット 2024-12-10 155148.png, スク リーンショット 2024-12-27 192639.png
```

imagesに入っている写真はすべて比較されます。Received similarity dataの数値の順番は、Received filenamesの順番と同じです。
(test_listenerはあくまでテスト用のプログラムであり動作を保証するものではありません。)

## ノード名など
node: similarity_publisher

Topics:
* publisher1: similar
    - 類似度を浮動小数で出力する
* publisher2: file_names 
  - 文字列でファイル名を出力する

## 著作権・ライセンス
  * このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
  * © 2025 Kai Nonaka
  * [A-KAZE](https://github.com/pablofdezalc/akaze)(BSD-3-Clause license)
