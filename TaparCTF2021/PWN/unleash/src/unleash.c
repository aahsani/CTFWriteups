#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int UNLEASHED = 0;

// 0x08048a9c  set_leasher
// 0x08048abf  shell


void set_leasher()
{
    printf("LEASHED!");
    UNLEASHED = 1;
}

void shell()
{
    printf("Almost UNLEASHed!");
    if (UNLEASHED == 1)
    {
        char *buf;
        int fd = open("pwn/flag", O_RDONLY);
        read(fd, &buf, 50);
        printf("%.*s", 50, &buf);
    }
}

void HI(int num)
{
    printf("Hi Num: %d\n", num);
}

void seems()
{
    printf("You look like one!\n");
}

int main()
{
    setbuf(stdout, 0);
    int (*seem)() = seems;
    int (*hii)() = HI;
    char buffer[40];
    printf(" _______ _______ ______ _______ ______ _______ _______ _______ \n"
	"(_______|_______|_____ (_______|_____ (_______|_______|_______)\n"
	"    _    _______ _____) )______ _____) )          _    _____   \n"
	"   | |  |  ___  |  ____/  ___  |  __  / |        | |  |  ___)  \n"
	"   | |  | |   | | |    | |   | | |  \\ \\ |_____   | |  | |      \n"
	"   |_|  |_|   |_|_|    |_|   |_|_|   |_\\______)  |_|  |_|      \n"
	"\n\n=========================== unleash ===========================\n\n");
    printf("What Would a Hacker say!?\n> ");
    fgets(buffer, 50, stdin);
    hii();
    seem();

}

