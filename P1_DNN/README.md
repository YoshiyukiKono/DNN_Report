# 深層学習

[![JDLA](http://ai999.careers/bnr_jdla.png)](http://study-ai.com/jdla/)

## イントロ

Pattern Recognition and Machine Learning by Christopher M. Bishop
https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf

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
  
  ノーフリーランチ定理
  
  ## DAY1
  
  論点整理・考察
  
  実装演習・考察
  
### 関連参考
  
## DAY2

## DAY3
  
### 関連記事レポート
  
[オルタナティブデータと自然言語処理(NLP)](https://github.com/YoshiyukiKono/dsml_01_nlp)
  
## DAY4
  

  
