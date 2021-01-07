## 機械学習・深層学習 概念

[Pattern Recognition and Machine Learning by Christopher M. Bishop](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)

### 識別モデルと生成モデル

- 識別(discriminative, backward) - p(C_k|x)
  - 条件（与えられたデータ）の下でのC_kである確率
- 生成(generative, forward) - p(x|C_k)
  - 条件（あるクラスに属する）の下でのデータC_kの分布
#### 識別モデル
- 決定木
- ロジスティック回帰
- SVN
- NN
#### 生成モデル
- 隠れマルコフモデル
- ベイジアンネットワーク
- 変分オートエンコーダー(VAE)
- 敵対性生成ネットワーク(GAN)

### 識別器の開発アプローチ
- 生成モデル
  - ベイズの定理により、生成モデル(p(x|C_k))を識別に利用することができる
  - 確率的な識別
  - データのクラス条件付き密度
- 識別モデル（確率的識別モデル）
  - 確率的な識別
  - データがクラスに属する確率
- 識別関数（決定的識別モデル）
  - 決定的な識別
  
## 万能近似定理（universal approximation properties）

https://www.deeplearningbook.org/contents/mlp.html
  
## 特徴量

### 次元の呪い
空間の次元が増えるのに対応して問題の複雑さが指数関数的に大きくなる。

### 超級面現象
高次元空間の場合、データが超球面上に分布しやすくなってしまう。

### 特徴選択
特徴量組み合わせ最適化。次元数を減らす。
#### フィルタ法
分散などの統計量を使って学習前に使用する特徴量を決定する。
#### 埋め込み法
L1正則化付き学習などによって学習と同時に使用する特徴量を決定する。
#### ラッパー法
選択と学習を交互に繰り返す。


## ノーフリーランチ定理
