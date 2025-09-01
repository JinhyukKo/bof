CC = gcc
CFLAGS = -Wall -s -fno-stack-protector -no-pie

TARGET = town
SRC = *.c

all : $(TARGET)

$(TARGET) : $(SRC)
	$(CC) -I $(INCLUDE) $(CFLAGS) -g -o $(TARGET) $^

dbg : $(SRC)
	$(CC) -I $(INCLUDE) -DDEBUG -g -o $(TARGET) $^

clean:
	rm -rf $(TARGET)
