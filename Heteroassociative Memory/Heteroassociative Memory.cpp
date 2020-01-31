#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
	int xVal[8][6];
	int tVal[8][2];
	int wVal[8][2];
	int i,j,k;

	
//	Input data training set
	for (i = 0; i < 8; i++)
	{	
		for (j = 0; j < 6; j++)
		{
			cout<<"Input X values["<<i+1<<"]"<<"["<<j+1<<"]: "; cin>>xVal[i][j];
			cout<<endl;
		}

		for (k = 0; k < 2; k++)
		{
			cout<<"Input T values["<<i+1<<"]"<<"["<<k+1<<"]: "; cin>>tVal[i][k];
			/* code */
		}
		cout<<endl;
	}

	//Initializing default weight
	for(i = 0; i < 6; i++) {
		for (j = 0; j < 2; j++)
		{
			wVal[i][j] = 0;
			cout<<"wVal["<<i+1<<"]"<<"["<<j+1<<"]"<<" = "<<wVal[i][j]<<endl;
			/* code */
		}
	}

	//execution
	cout<<"\n\nPerubahan bobot: \n";
	for (i = 0; i < 8; i++) {
		cout<<"Data ke-"<<i+1<<endl;
		for (j = 0; j < 6; j++)
		{
			for (k = 0; k < 2; k++) {
				wVal[j][k] = wVal[j][k] + xVal[i][j]*tVal[i][k];
				cout<<"wVal["<<j+1<<"]"<<"["<<k+1<<"]"<<" = "<<wVal[j][k]<<endl;
			    //wVal[j+1][k] = wVal[j][k];
			}
			/* code */
		}
		cout<<"\n\n";
	}

	//Data Testing
	testing:
	cout<<endl;
	int tempA, tempB, xTest, y_ln1, y_ln2;
	for (i = 0; i <6; i++) {
		cout<<"Input X test value: "; cin>>xTest;
		tempA = tempA + xTest*wVal[i][0];
		tempB = tempB + xTest*wVal[i][1];
	}

	if (tempA > 0)
	{
		y_ln1 = 1;
	}
	else if (tempA < 0)
	{
		y_ln1 = -1;
	}
	else {
		y_ln1 = 0;
	}

	if (tempB > 0)
	{
		y_ln2 = 1;
	}
	else if (tempB < 0)
	{
		y_ln2 = -1;
	}
	else {
		y_ln2 = 0;
	}

	cout<<" Penjumlahan terbobot ke-1 (y_ln1) = "<<tempA<<"------->"<<y_ln1<<endl;
	cout<<" Penjumlahan terbobot ke-2 (y_ln1) = "<<tempB<<"------->"<<y_ln2<<endl;

	char option;
	cout<<"Repeat the test? [Y/N] : ";cin>>option;
	if (option != 'N')
	{
		tempA = 0;
		tempB = 0;
		goto testing;
	}




	/* code */
	return 0;
}
