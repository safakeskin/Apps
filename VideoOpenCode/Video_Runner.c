#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//parametre olarak verilen videolari sirayla oynatir
int main(int argc, char** argv){
    int ctr;
    char* video_path = (char*)malloc(sizeof(char)*1000);
    for( ctr = 1 ; ctr < argc ; ctr++){
        strcpy(video_path, "audience ");
        strcat(video_path, argv[ctr]);
        system(video_path);
    }
    free(video_path);
    return 0;
}
