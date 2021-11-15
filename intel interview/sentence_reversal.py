def reversal(sentence):
    words = sentence.split()
    length = len(words) - 1
    result_list = []
    while length >= 0:
        result_list.append(words[length])
        length -= 1
    return " ".join(result_list)


print(reversal("Hi good afternoon"))