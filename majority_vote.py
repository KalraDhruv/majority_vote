import sys
if __name__ == '__main__':
    train_file = sys.argv[1]
    test_file = sys.argv[2]
    train_label = sys.argv[3]
    test_label = sys.argv[4]
    train_metrics = sys.argv[5]
    print(f"The train file is: {train_file}")
    print(f"The test file is: {test_file}")
    print(f"The test label file is: {test_label}")
    print(f"The train label file is: {train_label}")
    print(f"The train metrics file is: {train_metrics}")
