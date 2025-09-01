#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>
#include <fcntl.h>

struct person{
    uint8_t * name;
    uint64_t typeflag;
    union{
        struct adult{
            uint32_t age;
            uint32_t job_idx;
        } adult;

        struct child{
            uint32_t job_idx;
            uint32_t age;
        } child;
    }type;
};


#define TOWN_SIZE 16
struct person * town[TOWN_SIZE] = {};
char * job_names[TOWN_SIZE] = {};
char * flag = NULL;

#define CHILD 1
#define ADULT 2
#define NAME_SIZE 0x10
#define JOB_SIZE 0x10
