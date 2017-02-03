#include<stdio.h>
void floyd(int n,int arr[][n])
{

	int i,j,k;
	for(i=0;i<n;i++)
	{//printf("hi1\n");
		for(j=0;j<n;j++)
		{//printf("hi2\n");
			//*((arr+j*n)+i)>=100000;
			if(arr[j][i]>=100000)
				continue;
			for(k=0;k<n;k++)
			{//printf("hi3\n");
			//	if(*((arr+j*n)+k)>*((arr+j*n)+i)+*((arr+i*n)+k))
				if(arr[j][k]>arr[j][i]+arr[i][k])
			//		*((arr+j*n)+k)=*((arr+j*n)+i)+*((arr+i*n)+k);
					arr[j][k]=arr[j][i]+arr[i][k];
			}
		}
	}
	int q,u,v;
scanf("%d",&q);
for(i=0;i<q;i++)
{
	scanf("%d %d",&u,&v);
	if(arr[u-1][v-1]>=100000)
		printf("-1\n");
	else printf("%d\n",arr[u-1][v-1]);
}
	return;
}
int main(){
int n,m;
int high = 100000;
scanf("%d %d",&n,&m);
int dist[n][n];
int i,j;
for(i=0;i<n;i++)
{	
    for(j=0;j<n;j++)
        dist[i][j]=high;
}
int u,v,w;
for(i=0;i<m;i++)
{
    scanf("%d %d %d",&u,&v,&w);

	dist[u-1][v-1]=w;
}
for(i=0;i<n;i++)
{	
	dist[i][i]=0;
}

floyd(n,dist);


}