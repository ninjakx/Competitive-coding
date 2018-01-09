#include <iostream>
#include <vector>
#include <stdio.h>      /* printf */
#include <stdlib.h>     /* abs */
#include <utility>      /* pair */
#include <algorithm>    /* sort */
#define maxim 1e9
using namespace std;

vector< int > nodes;           // vector for storing customers 




int main(){

        int mat[4][4];
        int val[4][4] = {{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}};
        
// Adjancency Matrix to compute distance and show in the form of matrix
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{	mat[i][j] = val[i][j];
		}
		if(i!=0)
		nodes.push_back(i); // nodes of customers index

	}
	int mindist = maxim;
	do{
		int distance =0 ;
		int prev = 0; //starting from initial pos
		for(int i=0;i<4;i++)
		{
			distance+=mat[prev][nodes[i]];
			prev = nodes[i];
		}
		distance += mat[prev][0]; // adding distance btw starting and last visited node
		if(distance < mindist)
			mindist = distance;
	}while(next_permutation(nodes.begin(),nodes.end())); //changes order of nodes
	
	//for(int i=0;i<(int)nodes.size();i++)
	//	cout<<nodes.at(i) <<endl;
	cout<<mindist<<endl;
	return 0;
}
