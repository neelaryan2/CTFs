#include <stdio.h>
#include <string.h>

int main() {
  char input[48];
  int i, valid;
  puts("Hello World");
  puts("Welcome to the Flag checker program. Please enter your flag here, and we will verify whetherit is correct!");
  scanf("%s", input);
  valid = 1;

  // 0-7    -> +3
  // 9-15   -> -5
  // 17-24  -> +7
  // 25-34  -> -13
  // 38-42  -> -13

  for (i = 0; i < 43; i++) {
    if (i > 7) {
      if (i < 9 || i > 15) {
        if (i < 17 || i > 24) {
          if (i < 23 || i > 34) {
            if (i < 44 && i > 37) {
              input[i] = input[i] - 13;
            }
          }
          else {
            input[i] = input[i] - 13;
          }
        }
        else {
          input[i] = input[i] + 7;
        }
      }
      else {
        input[i] = input[i] - 5;
      }
    }
    else {
      input[i] = input[i] + 3;
    }
  }
  for (i = 0; i < 43; i++) {
    char chr = input[i];
    if (chr < 0) {
      chr = chr + 3;
    }
    input[i] = chr / 4;
  }
  for (i = 0; i < 43; i++) {
    input[i] = input[i] * 3;
  }
  i = strcmp(input, "3E3?6]QHKTHQQBEETTNKZQ]K]?K<KHH<BQ<KQT<QHNT");
  if (i != 0) {
    valid = 0;
  }
  if (valid == 0) {
    puts("ACCESS DENIED");
  }
  else {
    puts("ACCESS GRANTED");
  }
  return 0;
}

