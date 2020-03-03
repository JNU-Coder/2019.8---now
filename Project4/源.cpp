#include<iostream>
using namespace std;

template<class ElemType>
class sort
{
public:
	int Select_Sort(ElemType* Arry, int n)//—°‘Ò≈≈–Ú
	{
		int i, j;
		for (i = 0; i < n - 1; i++)
		{
			int min = i;
			for (j = i + 1; j < n; j++)
			{
				if (Arry[j] < Arry[min])
				{
					min = j;
				}
			}
			int temp = Arry[min];
			Arry[min] = Arry[i];
			Arry[i] = temp;
		}
		return 0;
	}

	int Bubble_Sort(ElemType* Arry, int n)//√∞≈›≈≈–Ú
	{
		int i, j, t, k;
		for (i = 0; i < n - 1; i++)
		{
			for (j = 0; j < n - i - 1; j++)
			{
				if (Arry[j] > Arry[j + 1])
				{
					t = Arry[j];
					Arry[j] = Arry[j + 1];
					Arry[j + 1] = t;
				}
			}
		}
		return 0;
	}

	int Insert_Sort(ElemType* Arry, int n)//≤Â»Î≈≈–Ú
	{
		int i, j;
		int t;
		for (i = 1; i < n; i++)
		{
			t = Arry[i];
			for (j = i; (j > 0) && (Arry[j - 1] > t); j--)
			{
				Arry[j] = Arry[j - 1];
			}
			Arry[j] = t;
		}
		return 0;
	}

	void print(ElemType* Arry, int n)//¥Ú”° ‰≥ˆ
	{
		for (int i = 0; i < n; i++)
		{
			cout << Arry[i] << " ";
		}
		cout << endl;
		return;
	}
};

int main()
{
	int A0[] = { 03, 47, 43, 73, 86, 36, 96, 47, 36, 61, 46, 98, 63, 71, 62, 97, 74, 24, 67, 62 };
	int N = 20;
	int A1[20], A2[20];
	for (int i = 0; i < N; i++)
	{
		A1[i] = A2[i] = A0[i];
	}
	sort < int> s;
	// ‰»Î£¨≥ı ºªØ

	cout << "≈≈–Ú«∞" << endl;
	s.print(A0, N);
	s.print(A1, N);
	s.print(A2, N);
	cout << "\n" << endl;
	//≈≈–Ú«∞

	cout << "≤Â»Î≈≈–Ú:";
	s.Insert_Sort(A0, N);
	s.print(A0, N);
	cout << "—°‘Ò≈≈–Ú:";
	s.Select_Sort(A1, N);
	s.print(A1, N);
	cout << "√∞≈›≈≈–Ú:";
	s.Bubble_Sort(A2, N);
	s.print(A2, N);
	//≈≈–Ú∫Û
	return 0;
}

