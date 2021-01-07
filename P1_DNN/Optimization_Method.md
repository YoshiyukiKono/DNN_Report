# 最適化手法


```python
class SGD:
  def update(self, params, grads):
    for key in params.keys():
      params[key] -= self.lr * grads[key]
```

```python
class Momentum:

  def init_v_if_needed(params):
    if self.v is None:
      self.v = {}
      for key, val in params.items():
        self.v[key] = np.zeros_like(val) # 元の配列と同じ形の配列に0を代入
        
  def update(self, params, grads):
    init_v_if_needed(params)
    for key in params.keys():
      self.v[key] = self.momentum*self.v[key] - self.lr*grads[key]
      params[key] += self.v[key]
```

```python
class Nesterov:
  def update(self, params, grads):
    init_v_if_needed(params)
    for key, val in params.items():
      self.v[key] *= self.momentum
      self.v[key] -= self.lr * grads[key]
      params[key] += self.momentum * self.momentum * self.v[key]
      params[key] -= (1 + self.momentum) * self.lr * grads[key]
```

```python
class AdaGrad:
  def update(self, params, grads):
    init_v_if_needed(params)
    for key, val in params.items():
      self.h[key] += grads[key] * grads[key]
      params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key] + 1e-7)
```

```python
class RMSProp:
  def update(self, params, grads):
    init_v_if_needed(params)
    for key, val in params.items():
      self.h[key] *= self.decay_rate
      self.h[key] += (1 - self.decay_rate) * grads[key] * grads[key]
      params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key] + 1e-7)
```

```python
class Adam:
  def init_v_m_if_needed(params):
    if self.m is None:
      self.m, self.v = {}, {}
      for key, val in params.items():
        self.m[key] = np.zeros_like(val) # 元の配列と同じ形の配列に0を代入
        self.v[key] = np.zeros_like(val) # 元の配列と同じ形の配列に0を代入

  def update(self, params, grads):
    init_v_m_if_needed(params)
    self.iter +=1
    for key, val in params.items():
      self.m[key] = self.rho1 * self.m[key] + (1 - self.rho1) * grads[key]
      self.v[key] = self.rho2 * self.v[key] + (1 - self.rho2) * (grads[key]**2)
      m = self.m[key] / (1 - self.rho1**self.iter)
      v = self.v[key] / (1 - self.rho2**self.iter)
      params[key] -= self.lr * m / (np.sqrt(v) + self.epsilon)
```
