# 物体検知とセマンティックセグメンテーション Object Detection and Semantic Segmentation

分類：画像に対するクラスラベル

物体検知：Bounding Box [bbox/BB]

意味領域分割 Semantic Segmentation：ピクセルに対するクラスラベル

個体領域分割 Instance Segmentaion: 個体ごとの区別

代表的データセット

VOC12　(Visual Object Classes)
ILSVRC17 (ImageNet Scale Visual Recognition Challenge) ImageNetのサブセット
MS COCO18（Microsoft Common Object in Context）
OICOD18 (Open Images Challenge Object Detection) Open Images V4のサブセット

Instance Annotation / 物体個別のラベル (ILSVRC17以外)

IoU: Intersection over Union

物体位置の予測レベル評価方法

IoU = Area of Overlap / Area of Union

IoU = TP / (TP + FP + FN): Jaccard係数



Frames per Second

物体検知のフレームワーク
- ２段階検出器　Two-stage detector
候補領域の検出とクラス推定を別々に行う
精度が高い傾向
計算量が大きく推論も遅い

- １段階検出器 One-stage detector
候補領域の検出とクラス推定を同時に行う
精度が低い傾向

## SSD: Single Shot Detector

One-stage Detectorとして、YOLOと並んで有名

Default Boxを使う

VGG16: SSDのベースネットワークになっている

計算量が小さく推論も早い

Non-Maximum Suppression
一つの物体に複数のBBが見つかるー＞IoUを計算（重なり具合がわかる。近い場合は、Confidenceが高いものをとる。低い場合は、別の物体として解釈）

Hard Negative Mining

背景と認識されるネガティブクラスと、ポジティブクラスのバランスの不均衡が生じる
ー＞PosiとNegaの比を最大３倍に抑える。

損失関数
ConfidenceとLocationに依存していることを抑える

DSSD: Deconvolutional SSD
ベースネットワークがResNetになっている。

# Semantic Segmentation

## アップサンプリング

### Deconvolution/Transposed Convolution

FCN

低レイヤーPooling層の出力をelement-wise additionすることでローカルな情報を保管してからUp-samplingする。

### U-Net

Encoder-Decoderモデル

Skip-connection: Encode前の情報をDecodeに用いる

アップサンプリングしたものと低レイヤーとの結合の仕方がFCNと異なる(チャネル方向への結合)


### Unpooling

Poolingした時の位置情報を覚えておく。どこが最大の情報を持っていたのか（switch variables）を保持しておく

### Dilated Convolution

Convolutionの段階で受容野を広げる工夫
