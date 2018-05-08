#include "isogram.h"
#include <string.h>
#include <ctype.h>


bool is_isogram(const char phrase[])
{
    // Initialize an array for counting the char occurences
    int alphabet['z'-'a'] = { 0 };

    int phrase_length = strlen(phrase);
    for (int i=0; i<phrase_length; i++){
        char c = tolower(phrase[i]);

        // Skip if current char is non-alphanumeric
        if(!isalpha(c)) continue;

        // Return false if the char is found more than once
        if (alphabet[c-'a'] > 0){
            return false;
        }
        // Increment char count
        alphabet[c-'a'] +=1;
    }

    return true;
}

