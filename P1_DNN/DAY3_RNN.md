# DAY3 RNN
## Section 1) 再帰型ニューラルネットワークの概念
### 1-1 RNN全体像
#### 1-1-1 RNNとは

時系列データに対応可能なニューラルネットワーク



##### 確認テスト
RNNでは、重みが３種類
- W_in：入力から現在の中間層を定義する際に掛けられる重み
- W_out：中間層から出力を定義する際に掛けられる重み
- W：前の中間層から現在の中間層に至る部分の重み

##### バイナリ加算
右から左に向かって時間的なつながりのある情報ととらえることができる（値の繰り上がり）

##### 演習チャレンジ
構文木


#### 1-1-2 時系列データ
#### 1-1-3 RNNについて


### 1-2 BPTT
#### 1-2-1 BPTTとは
#### 1-2-2 BPTTの数学的記述
#### 1-2-3 BPTTの全体像

## Section 2) LSTM
### 2-1 CEC (Constant Error Carousel)
### 2-2 入力ゲートと出力ゲート
### 2-3 忘却ゲート
### 2-4 覗き穴結合

### 実装
#### 1.
```
c_t = c_t-1 ⊗ f) ̟⊕　(g ⊗ i)
```
```
c_next = (c_prev * forget_gate) + ( g * input_gate)
```
#### 2. 隠れベクトル計算

```
h_next = np.tanh(h_prev) * outputgate
```

## Section 3) GRU (Gated Recurrent Unit)
- LSTMよりも内部構造が単純、学習にかかる時間が少ない
- リセットゲートと更新ゲートの２つのゲートを持つ
- LSTM同様RNNの勾配消失問題を緩和
- LSTMの持っている記憶セルはない

LSTMとGRUはタスクによって使い分ける必要がある。

## Section 4) 双方向RNN
## Section 5) Seq2Seq
## Section 6) Word2vec
## Section 7) AttentionMechanism
