class SimpleNN:
    def __init__(self, w1, w2, b):
        self.weight1 = w1
        self.weight2 = w2
        self.bias = b

    def activate(self, input1, input2):
        # Calculate the weighted sum
        total = input1 * self.weight1 + input2 * self.weight2 + self.bias
        # Apply the step activation function
        return 1 if total > 0 else 0

if __name__ == "__main__":
    # AND Gate
    and_gate = SimpleNN(1.0, 1.0, -1.5)
    print("AND Gate Results:")
    for i in range(2):
        for j in range(2):
            print(f"{i} AND {j} = {and_gate.activate(i, j)}")

    # OR Gate
    or_gate = SimpleNN(1.0, 1.0, -0.5)
    print("\nOR Gate Results:")
    for i in range(2):
        for j in range(2):
            print(f"{i} OR {j} = {or_gate.activate(i, j)}")
