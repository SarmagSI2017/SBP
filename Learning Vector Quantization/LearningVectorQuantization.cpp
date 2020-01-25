#include <iostream>
#include <cmath> //for sqrt function
using namespace std;

int main()
{
	//initiation
	float alfa = 0.05; //alfa value
	int maxEpoh = 10; //max iteration
	int epoh = 0; //begin interation
	// float wVal[2][6]; //accepting the new weight values
	int i,j,k; //for looping xD
	float tempA, tempB; // storing temporary values for sqrt operation 
	int y_ln; //Test the sqrt value of tempA and tempB

	int wDataSet[2][6] = {
		{1,0,0,0,1,0},  //Class 1
		{0,1,1,1,1,0} // Class 2
	};
	int dataSet[8][6] = {
		{0, 0, 1, 0, 0, 1}, //Class 1 --> target = 1 --> index 0,
		{0, 0, 1, 0, 1, 0}, //Class 1 --> target = 1 --> index 0,
		{0, 1, 0, 0, 0, 1}, //Class 1 --> target = 1 --> index 0,
		{1, 0, 1, 0, 1, 1}, //Class 1 --> target = 1 --> index 0,
		{0, 0, 1, 1, 0, 0}, //Class 2 --> target = 2 --> index 1,
		{0, 1, 0, 1, 0, 0}, //Class 2 --> target = 2 --> index 1,
		{1, 0, 0, 1, 0, 1}, //Class 2 --> target = 2 --> index 1,
		{0, 1, 1, 1, 1, 1}  //Class 2 --> target = 2 --> index 1,
	};

//	 Penjelasan di atas: artinya class di sini (Cj kalo di buku)  diasumsikan sebagai target data, dan karena make array.
//	 kita mulai dari angka 0
//	 karena itu kita buat lagi variabel untuk targetnya (bisa pake cara lain, cuman di sini biar gampang aja)

	int t[8] = {0,0,0,0,1,1,1,1}; // <--- Masukkin indexnya

	while(epoh < maxEpoh) {
		epoh = epoh + 1;
		cout<<"Epoh ke-"<<epoh<<" : "<<endl;
		for (i = 0; i < 8; i++)
		{	
			for (int j = 0; j < 6; j++)
			{
				tempA = tempA + pow(dataSet[i][j] - wDataSet[0][j], 2); // tempA will get the value for this overall operation
				tempB = tempB + pow(dataSet[i][j] - wDataSet[1][j], 2); // tempB will get the value for this overall operation
				/* code */
			}

			tempA=sqrt(tempA); //Taking sqrt value of TempA
			tempB=sqrt(tempB); //Taking sqrt value of tempB
			cout<<"Jarak pada:"<<endl;
			cout<<"   bobot ke-1 = "<<tempA<<endl;
			cout<<"   bobot ke-2 = "<<tempB<<endl;
			
			//testing via y_ln (using hard limit method (binary 0 1) (see the architecture diagram on page 190)
			if (tempA <= tempB)
			{
				y_ln = 0;
				/* code */
			}
			else {
				y_ln = 1;
			}

			for (k = 0; k < 6; k++) {
				if (y_ln == t[i])
				{
					wDataSet[y_ln][k] = wDataSet[y_ln][k] + alfa*(dataSet[i][k] - wDataSet[y_ln][k]); //Rumus LVQ untuk fix W value baru ada di buku halaman 189
					wDataSet[y_ln][k] = round(wDataSet[y_ln][k]);
					cout<<"w["<<y_ln+1<<"]"<<"["<<k+1<<"]"<<" = "<<wDataSet[y_ln][k]<<endl;
				}

				else {
					wDataSet[y_ln][k] = wDataSet[y_ln][k] - alfa*(dataSet[i][k] - wDataSet[y_ln][k]); //yang di atas di tambah, ini dikurang
					wDataSet[y_ln][k] = round(wDataSet[y_ln][k]);
					cout<<"w["<<y_ln+1<<"]"<<"["<<k+1<<"]"<<" = "<<wDataSet[y_ln][k]<<endl;	
				}
			}

			tempA = 0; //kembalikan ke nilai awal
			tempB = 0; //kembalikan ke nilai awal
		} // bracket untuk for i

		alfa = alfa-0.1*alfa;
	} // bracket buat while epoh

	//print hasil akhir w1 dan w2
	cout<<"\n\n";
	for (i = 0; i < 2; i++) {
		for (j = 0; j < 6; j++) {
			cout<<"w"<<i+1<<" = "<<wDataSet[i][j]<<" "<<endl;
		}
	}

	//Testing LVQ by using manual input
	int dSetTest; //for inputing the values
	for (i = 0; i < 6; i++) {
		cout<<"Input dataset test value: ["<<i+1<<"] : "; cin>>dSetTest;
		tempA = tempA + pow(dSetTest - wDataSet[0][j], 2);
		tempB = tempB + pow(dSetTest - wDataSet[1][j], 2);
	}

	tempA=sqrt(tempA); //Taking sqrt value of TempA
	tempB=sqrt(tempB); //Taking sqrt value of tempB
	cout<<"Jarak pada:"<<endl;
	cout<<"   bobot ke-1 = "<<tempA<<endl;
	cout<<"   bobot ke-2 = "<<tempB<<endl;

	if (tempA <= tempB)
		{
			y_ln = 0;
			/* code */
		}
		else {
			y_ln = 1;
		}

	cout<<"Input termasuk dalam target(class): "<<y_ln+1<<endl;
	return 0;
}