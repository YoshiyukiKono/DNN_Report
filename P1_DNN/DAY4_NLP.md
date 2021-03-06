# NLP

## Encoder-Decoderモデル

- 入力系列が内部状態にEncodeされ、内部状態から系列Decodeされる。


### RNN
- 再帰処理を時間軸に展開できる

### 言語モデル

単語の並びに対して、尤度すなわち文章として自然かを確率で評価する。
同時確率を事後確率に分解して表せる

時刻t-1までの情報で、時刻tの事後確率を求めることが目標　－＞このことで、同時確率が計算できる


argmaxP(I, hava, a , w)

## まとめ
- RNNは系列情報を内部状態に変換することができる
- 文章の書く単語が現れる際の同時確率は、事後確率で分解できる
  - したがって、事後確率を求めることがRNNの目標となる
- 言語モデルを再現するようにRNNの重みが学習されていれば、ある時点の次の単語を予測することができる。
  - 先頭単語を与えれば文章を生成することも可能

### Seq2seq

Encoder: Source -> Embed -> Encoder RNN

Decoder: Embed -> Decoder RNN -> Softmax -> output (教師データとの差分からLossをとることができ、誤差逆伝播によるモデルの更新が可能)

Decoder側の構造は言語モデルRNNとほぼ同じだが、隠れ状態の初期値にEncoderの内部情報(h)を受け取る

RNNの内部状態の初期値は決まっている

### Teacher Forcing
正解ラベルを直接Decoderの入力にする

### Scheduled Sampling
確率的にTeacher Forcingを用いる

### BLEUスコア
翻訳で使われる指標。翻訳の精度を相対的に計ることができる。

## Transformer

### Attention 注意機構
翻訳先の各単語を選択する際に、翻訳元の文中の各単語の隠れ状態を利用

Attentionは辞書オブジェクト
QUeryに一致するkeyを索引し、対応するvalueを取り出す操作であると見做すことができる。
辞書オブジェクトの機能と同じ

#### Attention種類
- Dot-prodct Attention
- Attentive Attention

### Transformer
- RNNを使わない。

- Encoderでは、はじめに文字の位置情報を単語ベクトルに付加

- Decoderでは、未来の単語を見ないようにマスク


- ソース・ターゲット注意機構
- 自己注意機構

- セルフアテンションが重要：CNNと類比して考えることができる

### Position-Wise Feed-Forward Networks

- 位置情報を保持したまま順伝播させる

- ２層の全結合NN
- 線形変換 -> ReLu -> 線形変換


### Multi-Head Attention

- 重みパラメタの異なる８個のヘッドを使用

- ８個のScaled Dot-Product
- Attentionの出力をConcat
- それぞれのヘッドが異なる種類の情報を収集

### Position Encoding
- 単語の位置情報をエンコード

- 縦軸が単語の位置、横軸が成分の次元

## BERT (Bidirectional Encoder Rrepresentations from Transformers
- Transformerのエンコーダーで構成される
- 事前学習と再学習の２段階で学習が行われる

### OpenAI GPT
- unidirectional モデル
- 過去の単語だけを使って将来の単語を予想
