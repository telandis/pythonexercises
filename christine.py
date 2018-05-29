"""
Question 2. In perl, take article and count the unique words in descending order.
Output should be two columns, count and word, with count going in greatest to smallest order.


Question 3. Do the same as perl but also take a range of count to display.
For example, from 100 to 200 will only display word count from 100 to 200 words

"""
from bisect import bisect_left, bisect_right

def unique_words(lower_bound, upper_bound, absolute_path):
    unique_words = {}
    with open (absolute_path) as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                #print(word)
                unique_words[word] = unique_words.get(word, 0) + 1

    sorted_key_list = sorted(unique_words, key=unique_words.get)

    sorted_values = []
    for j in sorted_key_list:
        sorted_values.append(unique_words[j])

    lower_index = bisect_left(sorted_values, lower_bound)
    upper_index = bisect_right(sorted_values, upper_bound)
    for i in range(upper_index-1, lower_index-1, -1):
        #print(str(sorted_key_list[i]) + "    " + str(unique_words[sorted_key_list[i]]))
        #sfdgdsgsdgfdsgsdf of of
        print('{: <30} {: <30}'.format(str(sorted_key_list[i]), str(unique_words[sorted_key_list[i]])))

unique_words(0,8,"/Users/victorzhu/Downloads/article.txt")
