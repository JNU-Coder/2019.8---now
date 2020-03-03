#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int Divisor(int x)//�ж����������ĺ���
{
    int r = (int)sqrt(1.0 * x);
    int sum = 0;
    if (r * r == x)
    {
        sum++;
        r--;
    }
    for (int i = 1; i <= r; i++)
        if (x % i == 0)
        {
            sum += 2;
        }
    return sum;
}

int max(int x1, int x2)//ȡ�ϴ�ֵ����
{
    if (x1 > x2)
        return x1;
    else
        return x2;
}

int main()
{
    string line;
    string t1 = "", t2 = "";
    int x1, x2;
    ifstream I("input.txt");
    ofstream O("output.txt");
    //��ʼ�������ļ�

    while (!I.eof())
    {
        getline(I, line);
        stringstream words(line);//��ȡ�ַ�
        words >> t1;
        words >> t2;
        x1 = (int)atof(t1.c_str());
        x2 = (int)atof(t2.c_str());//���ַ�ת��Ϊint����
        if (x1 > x2)
        {
            cout << "error!" << endl;
            break; //��������ĿҪ��a��b)
        }
        O << max(Divisor(x1), Divisor(x2)) << "\n";//�жϲ������д���ļ�
    }
    I.close();
    O.close();

    return 0;
}
