CC=g++
CFLAGS= -Wall -Wextra
LD=g++

all: clean compile link

clean:
	rm -rf out/
	mkdir out
preprocessor: 
	$(CC) $(CFLAGS) src/Tools/Preprocessor/comments.cpp src/Tools/Preprocessor/fdescriptor.cpp -o out/preprocessor.o
tools: 
	$(CC) $(CFLAGS) src/Tools/lexer.cpp -o out/lexer.o
api: 
	$(CC) $(CFLAGS) src/Api/debug.cpp -o out/api.o
sys: 
	$(CC) $(CFLAGS) src/Sys/color.cpp src/Sys/unix.cpp -o out/sys.o
main: 
	$(CC) $(CFLAGS) src/main.cpp src/NApp.cpp -o out/main.o
compile: preprocessor tools api sys main
link:
	$(LD) src/preprocessor.o src/lexer.o src/api.o src/sys.o src/main.o
