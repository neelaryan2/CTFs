#include<iostream>
#include "flag.h"
#include <string>
#include <vector>
// flag.h contains the real name with few more fake ones;)
using namespace std;


void do_stuff(string name) {

    for ( int i = 0 ; i < name.length(); i += 2)
        arr[i] = int(name[i]) + 1;

    for ( int i = 0; i < name.length() / 2; i++)
        arr[i * 2 + 1] = int(name[i * 2 + 1]) - 1;

    for ( int i = 0 ; i < name.length(); i++)
        cout << arr[i] << " ";

    cout << endl;
}

int main() {
    do_stuff(namea);
    cout << endl;
    do_stuff(nameb);
    cout << endl;
    do_stuff(namec);
    cout << endl;
    do_stuff(named);
    cout << endl;
    do_stuff(namee);
    cout << endl;
    do_stuff(namef);
    cout << endl;
}

//output is
//111 47 117 94 56 103 102 94 100 47 115 113 52 115 96 48

// 118 94 50 104 101 115

// 56 103 106 52 96 48 116 94 101 50 103 48 111 100 117 107 122 94 111 47 56 94 110 120 96 109 53 108 52

// 53 108 98 121 50 109 104 94 118 94 100 113 53 98 108 50 101 94 50 115 96 115 105 50 96 109 53 108 102 94 106 52 96 101 55 117 104 101 55 50

// 118 94 110 48 104 103 56 94 55 50 96 98 109 47 54 100 96 50 111 47 86 102 105

// 108 120 53 94 99 48 115 47 34 32 96 109 49 115 96 100 121 111 52 98 56 100 101 94 103 113 49 108 96 116
