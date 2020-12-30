# Deep Learning 概念

## シグモイド関数

Sigmoid(z) = f(z)の時の、微分値f'(z)
```
f(z) ( 1 - f(z) )
```
シグモイド関数の微分値はシグモイド関数それ自体であらわすことができる。

## 逆伝播
移動する方向と逆の入力を演算に適用する。

xで微分する＝xが(微小に)変化した際にyがどれだけ(微小に)変化するか

z = x*yのとき
∂z/∂x = ∂/∂x (x*y) = y

# GAN

## LAPGAN
CNNを利用。低解像度画像から高解像度画像を生成
## ACGAN
Generatorに入力ノイズとしてのベクトルと入力画像のクラス情報を同時に与え、Discriminatorが生成画像の真偽に加え、クラスの判別も行う
## DCGAN
Generatorに入力ノイズとしてベクトルだけを与え、Discriminatorが生成画像の真偽判定を行う
## SNGAN
Spectral normalizationを提案
