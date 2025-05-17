#include <stdio.h>
#include <string.h>

int main(){


char word[100];
char reverse[100];
int flag = 1;

printf("PALINDROME CHECKER\n");

printf("Enter a word:");
fgets(word , sizeof(word), stdin);
word[strcspn(word, "\n")] = '\0';

int length = strlen(word);

for(int i = 0; i < length; i++){

    reverse[i] = word[length - i - 1];
}

reverse[strcspn(reverse, "\n")] = '\0';

for(int i = 0; i < length; i++){

    if(reverse[i] != word[i]){

        flag = 0;
        break;
    }
}

if(flag){

    printf("The word is a palindrome");
}
else{

    printf("The word is not a palindrome");
}

return 0;

}