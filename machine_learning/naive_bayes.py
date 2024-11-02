from collections import defaultdict
import math

class NaiveBayes:
    def __init__(self):
        self.prior_probabilities = defaultdict(float)
        self.feature_count = defaultdict(lambda: defaultdict(int))
        self.total_samples = 0
        self.total_features_per_class = defaultdict(int)

    def train(self, data):
        # Count occurrences for each label and feature
        for label, features in data:
            self.prior_probabilities[label] += 1
            self.total_samples += 1

            for feature in features:
                self.feature_count[label][feature] += 1
                self.total_features_per_class[label] += 1

        # Calculate the log of prior probabilities for numerical stability
        for label in self.prior_probabilities:
            self.prior_probabilities[label] = math.log(self.prior_probabilities[label] / self.total_samples)

    def predict(self, features):
        max_log_prob = float('-inf')
        best_label = None

        for label, log_prior in self.prior_probabilities.items():
            # Start with log of the prior probability
            log_prob = log_prior

            for feature in features:
                # Calculate the log of the conditional probability with Laplace smoothing
                feature_count = self.feature_count[label][feature]
                total_features = self.total_features_per_class[label]
                feature_probability = (feature_count + 1) / (total_features + len(self.feature_count[label]))
                log_prob += math.log(feature_probability)

            if log_prob > max_log_prob:
                max_log_prob = log_prob
                best_label = label

        return best_label

    def display(self):
        print("Prior Probabilities (Log):")
        for label, log_prob in self.prior_probabilities.items():
            print(f"{label}: {math.exp(log_prob)}")  # Convert back to original probability for readability

if __name__ == "__main__":
    nb = NaiveBayes()

    # Training data: (label, [features])
    training_data = [
        ("Spam", ["free", "win", "money"]),
        ("Spam", ["free", "win"]),
        ("Not Spam", ["hello", "friend"]),
        ("Not Spam", ["meeting", "tomorrow"])
    ]

    nb.train(training_data)
    nb.display()

    # Test data
    test_features = ["hello", "friend"]
    result = nb.predict(test_features)
    print(f"Predicted: {result}")
