int count_word(char *sentence)
{
    int space_num = 0;
    for (int i = 0; *(sentence + i) != '\0'; i++)
    {
        char c = *(sentence + i);
        if (c == ' ')
        {
            space_num++;
        }
    }
    return space_num + 1;
}

int mostWordsFound(char **sentences, int sentencesSize)
{
    int max = 0;
    for (int i = 0; i < sentencesSize; i++)
    {
        char *sentence = *(sentences+i);
        int word_num = count_word(sentence);
        if (word_num > max) {
            max = word_num;
        }
    }
    return max;
}

