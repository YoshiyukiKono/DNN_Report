# データセットの連結
行方向に連結するか、列方向に連結するかで`concat`か`merge`を用いる。

### 行方向の連結 concat

#### Series
```
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])
```

#### DataFrame
```
def make_df(cols, ind):
  return pd.DataFrame({c: [str(c) + str(i) for i in ind] for c in cols}, ind)
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
pd.concat([df1, df2])
```
連結時に、片方にない列のあたいは欠損値となる。
```
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
pd.concat([df5, df6])
```
連結方法の指定で、innerを指定すると両方のDataFrameにある列のみを使う。
```
pd.concat([df5, df6], join='inner')
```

### 行方向の連結 append
```
df1.append(df2)
```
### 列方向の連結 concat( ,axis=1)
```
pd.concat([df3, df4], axis=1)
```
### 列方向の連結 merge

```
```
