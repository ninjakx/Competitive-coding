//https://practice.geeksforgeeks.org/problems/most-frequent-word-in-an-array-of-strings
#include<bits/stdc++.h>
#include<sstream>
using namespace std;
int main()
{   int t;
    cin>>t;
    while(t--)
    {
    map <string,int> a;
    int n;
    string line,word;
    cin>>n;
    string c[1000];
    
    while(n--)
        {   cin>>word;
            ++a[word];
        }
      
    int curMax = 0;
    string that_word;
    for(auto it = a.cbegin(); it != a.cend(); ++it ) 
    {   
        if (it ->second > curMax) 
        {
            that_word = it->first;
            curMax = it->second;
        }
    }
cout <<that_word<<endl;   
}
    
    return 0;
    
}
