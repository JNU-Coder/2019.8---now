#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int Divisor(int x)//判断因数数量的函数
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

int max(int x1, int x2)//取较大值函数
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
    //初始化，打开文件

    while (!I.eof())
    {
        getline(I, line);
        stringstream words(line);//获取字符
        words >> t1;
        words >> t2;
        x1 = (int)atof(t1.c_str());
        x2 = (int)atof(t2.c_str());//将字符转换为int类型
        if (x1 > x2)
        {
            cout << "error!" << endl;
            break; //不符合题目要求（a≤b)
        }
        O << max(Divisor(x1), Divisor(x2)) << "\n";//判断并将结果写入文件
    }
    I.close();
    O.close();

    return 0;
}
