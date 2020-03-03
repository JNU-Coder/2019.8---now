#include<iostream>
using namespace std;

int main()
{
	float x1[3][3], x2[3][3], x3[3][3] = { 0 };
	int k, j, i;
	for (j = 0; j < 3; j++)
	{
		for (i = 0; i < 3; i++)
		{
			cin >> x1[j][i];
		}
	}
	for (j = 0; j < 3; j++)
	{
		for (i = 0; i < 3; i++)
		{
			cin >> x2[j][i];
		}
	}
	for (j = 0; j < 3; j++)
	{
		for (i = 0; i < 3; i++)
		{
			for(k = 0;k < 3; k++)
			{
				x3[i][j] += x1[i][k] * x2[k][j];
			}
		}
	}
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
			cout << x3[i][j] << " ";
		cout << endl;
	}
	return 0;
}