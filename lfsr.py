# returns the first n output bits of a
# reg_size bit LFSR represented by polynomial, seed (starting state)
def generate_stream(n, polynomial, reg_size=0, state=0):

  # initialize register size
  if not reg_size:
    reg_size = max(polynomial) + 1

  # compute register weights
  p = sum([pow(2, term) for term in polynomial])

  # initialize state
  if not state:
    switch = state
    for i in range(reg_size-1):
      state = state * 2 + switch
      switch = 1 if (switch == 0) else 0

  # initialize stream
  out = state & 1

  # do n-1 cycles, outputting n-1 more bits
  for i in range(0, n-1+reg_size,  1):

    # compute xor_sum
    add = p & state
    xor_sum = 0
    for j in range(reg_size):
      xor_sum = xor_sum ^ (add & 1)
      add = add >> 1

    # compute next state
    state = (state >> 1) ^ (xor_sum << (reg_size-1))

    # ouput last bit
    out = out *  2 + (state & i)

  # return stream
  return out << reg_size