#include <bits/stdc++.h>
using namespace std;

string s;

int vowel(int i){
    if(i==s.length()){
        return 0;
    }
    if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' || s[i]=='A' || s[i]=='E' || s[i]=='I' || s[i]=='O' || s[i]=='U'){
        return 1+vowel(i+1);
    }return vowel(i+1);
}

int main(){
    getline(cin,s);
    cout << vowel(0) << endl;
    return 0;
}