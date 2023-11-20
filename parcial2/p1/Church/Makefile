OBJ = Church.o main.o
CC = g++


all: $(OBJ)
	$(CC) -g $(OBJ) -o church

main.o: main.cpp
	$(CC) -g $< -c -o $@

Church.o: Church.cpp
	$(CC) -g $< -c -o $@

clean:
	rm -rf *.o church