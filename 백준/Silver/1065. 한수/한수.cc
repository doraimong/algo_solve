#include <stdio.h>

int main(){
	int get,count=0;
	scanf("%d",&get);
	
	for(int i=1; i<=get; i++)
	{
		if(i<10){count++;}
		else if(i<100){		//10의자리수 ~ 99까지를 다룬다  
			count++;
			
		}
		else if(i<1000){				//100~999
			int a,b,c; 
			a=(i/100);		//100의 자리수  
			b=(i%100)/10;		//10의 자리수 
			c=(i%10);			//1의 자리수  
			if(a-b == b-c){count++;}
		}
	}
	printf("%d",count); 
	
	return 0;
}