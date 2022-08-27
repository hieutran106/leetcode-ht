int balancedStringSplit(char * s){
    int result = 0;
    int num_left = 0;
    int num_right = 0;
    while (*s != '\0') {
        if (*s == 'R') {
            num_right++;
        } else {
            num_left++;
        }
        if (num_left == num_right) {
            result++;
            num_left = 0;
            num_right = 0;
        }
        s++;
    }
    return result;
}