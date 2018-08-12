#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main()
{
    int fd = open("./file.txt", "ORDONLY|OCREAT");
    close(fd);
    return 0;
}
