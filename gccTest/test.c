#include <stdio.h>

int fib(int n);

int main()
{
	int i;
	for (i=0;i<20;i++)
	{
		printf("fib[%d] = %d\n",i,fib(i));
	}
}

int fib(int n) {
	if (n == 0 || n == 1) {
		return 1;
	} else {
		return fib(n-1)+fib(n-2);
	}
}