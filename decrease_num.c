#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define FULL_STACK -1
typedef struct current
{
	int n;
	char *num;
} current;

long long decrease_num(int n, current cur)
{
	int i;
	int idx;
	int len;

	if (cur.n == n)
		return (strtoll(cur.num, NULL, 10));
	else if (strncmp(cur.num, "9876543210", 10) == 0 && cur.n < n)
		return (-1);
	idx = FULL_STACK;
	len = strlen(cur.num);
	for (i = len - 1; i > 0; i--)
		if ((cur.num[i] - '0' + 1 < cur.num[i - 1] - '0') && cur.num[i] != '9')
		{
			idx = i;
			break ;
		}
	if (idx == FULL_STACK)
	{
		int new;
		if (cur.num[0] == '9')
		{
			new = len;
			cur.num = realloc(cur.num, len + 1 + 1);
			cur.num[0] = new + '0';
			for (i = 1; i < len + 1; i++)
				cur.num[i] = cur.num[i - 1] - 1;
			cur.num[i] = 0;
		}
		else
		{
			cur.num[0]++;
			for (i = len - 1; i > 0; i--)
				cur.num[i] = len - 1 - i + '0';
		}
	}
	else
	{
		cur.num[idx]++;
		if (idx != len - 1)
		{
			i = len - 1;
			while (i > idx)
			{
				cur.num[i] = len - 1 - i + '0';
				i--;
			}
		}
	}
	cur.n++;
	return (decrease_num(n, cur));
}

int	main(void)
{
	int n;
	scanf("%d", &n);
	current cur;
	if (n < 10)
		printf("%d\n", n);
	else
	{
		cur.n = 10;
		cur.num = strdup("10");
		long long result = decrease_num(n, cur);
		printf("%lld\n", result);
	}
}
