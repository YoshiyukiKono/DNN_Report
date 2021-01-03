# TensorFlowの実装演習

## 構成要素

### constant

計算グラフの定義に用いる定数

実際の値を確認するにはセッションを開始して処理を実行する必要がある。

### variables

計算グラフの定義に用いる変数

`assign()`により値を代入する。

セッションのはじめに初期化する必要がある。

`global_variables_initializer()`を実行する(すべての変数を初期化する)。

### placeholder

データは未定のままグラフを構築し、具体的な値は実行する時に与えるためのデータ格納場所。

値は、`Session.run()`の引数`feed_dict`に指定する。

#### 参考情報

[TensorFlowの定数、変数、プレースホルダーの使い方](https://note.nkmk.me/python-tensorflow-constant-variable-placeholder/)

基本構成要素の概説

[TensorFlow のカリキュラム](https://www.tensorflow.org/resources/learn-ml?hl=ja)

本家リソース

[私はいかにしてTensorFlowデベロッパー認定資格に合格したか](https://ainow.ai/2020/08/14/225743/)

E資格との比較など
