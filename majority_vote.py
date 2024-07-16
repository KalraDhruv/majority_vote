import sys
import pandas as pd

def main():
    train_file = sys.argv[1]
    test_file = sys.argv[2]
    train_label = sys.argv[3]
    test_label = sys.argv[4]
    train_metrics = sys.argv[5]
    classifier = MajorityVote()
    classifier.findLabel(train_file)
    print(f"Majority Label: {classifier.majority_label}")


class MajorityVote:
    def __init__(self):
        self.majority_label = None

    def findLabel(self, train_file):
        train = pd.read_csv(train_file, sep='\t')

        # Taking the predictions from the dataframe

        predictions = train.iloc[:, train.shape[1] - 1]
        count_one = 0
        count_zero=0
        label_one= predictions[0]
        label_zero = None

        # For the case of 2 labels only!
        for i in range(predictions.shape[0]):
           if predictions[i] == predictions[0]:
               count_one+=1
           else:
               if label_zero == None:
                    label_zero= predictions[i]
           count_zero+=1

        if count_one>count_zero:
            self.majority_label = label_one
        elif count_zero>count_one:
            self.majority_label = label_zero
        else:
            if label_one - label_zero > 0:
                self.majority_label = label_one
            else:
                self.majority_label = label_zero


if __name__ == '__main__':
   main()