def rnn_net(xs, W, U, V):
  """
  """
  b_size, n_seq = xs.shape[:2]
  h_size = W.shape[0]
  hiddens = np.zeros((b_size, n_seq, hidden_size), dtype=xs.dtype)
  for t in xs.shape[1]:
    hiddens[:, t] = _activation(x[:,t].dot(W.T) + hiddens[:,t-1]dot(U.T))
  outputs = _activation(hiddens.dot(V.T))
  return hiddens, outputs
