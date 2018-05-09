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


    // Not sure if really needed, but makes a copy of 'phrase' as 'phrase_copy'
    size_t phrase_len = strlen(phrase);
    
    char *phrase_copy = calloc(phrase_len+1, sizeof(char));
    strncpy(phrase_copy, phrase, phrase_len);
    
    char *acronym = calloc(phrase_len+1, sizeof(char));

    //Return NULL if input is empty string
    if(phrase_len == 0)
    {
        return NULL;
    }

    
    // Word separator flag
    // Is set to 'true' so we get the first non-alpha char
    bool separator = true;

    // Index for letters in the acronym
    size_t acronym_i = 0;
    
    for(size_t i=0; i<phrase_len && phrase_copy[i] != '\0'; i++)
    {
        //If current char is non-alpha (and is neither an apostrophe),
        //maybe a word begin in the next char
        if(!isalpha(phrase_copy[i]) && phrase_copy[i] != '\'')
        {
            separator = true;
        }
        else
            // If previous char is a separator, add current char to acronym string
            if(separator)
            {
                acronym[acronym_i] = toupper(phrase_copy[i]);
                acronym_i++;
                separator = false;
            }
    }
    // Add a terminator to the end of acronym
    // Probably not needed, as we used calloc
    acronym[acronym_i] = '\0';

    //DEBUG MESSAGE
    printf("acronym: %s\n", acronym);

    return acronym;
}

