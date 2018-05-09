/** SEGFAULT after running the first test (NULL input) **/


#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char *abbreviate(const char *phrase)
{
    //Return NULL if input NULL
    if(phrase == NULL)
    {
        return NULL;
    }

    size_t phrase_len = strlen(phrase);
    // Maximum length for acronym assumed as equal as input string
    char *acronym = calloc(phrase_len+1, sizeof(char));

    //Return NULL if input is empty string
    if(phrase_len == 0)
    {
        return NULL;
    }

    // Word separator flag
    // Initialized to 'true' so we get the first non-alpha char
    bool separator = true;

    // Index for letters in the acronym
    size_t acronym_i = 0;
    
    // Iterate over the input string
    for(size_t i=0; i<phrase_len; i++)
    {
        //If current char is non-alpha (and is neither an apostrophe),
        //maybe a word begin in the next char
        if(!isalpha(phrase[i]) && phrase[i] != '\'')
        {
            separator = true;
        }
        else
            // If previous char is a separator, add current char to acronym string
            if(separator)
            {
                acronym[acronym_i] = toupper(phrase[i]);
                acronym_i++;
                separator = false;
            }
    }

    //DEBUG MESSAGE
    printf("acronym: %s\n", acronym);

    return acronym;
}

