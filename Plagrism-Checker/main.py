from difflib import SequenceMatcher

with open ('data1.txt') as f1, open ('data2.txt') as f2:
    data_file1 = f1.read()
    data_file2 = f2.read()
    matches = SequenceMatcher(None,data_file1,data_file2,data_file2).ratio()
    print(f'Similarity ratio: {matches * 100:.2f}%')
