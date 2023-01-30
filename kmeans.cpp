#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#define NCLUSTERS 3
using namespace std;

float d(float x1, float y1, float x2, float y2)
{
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main(void)
{

    ifstream entrada;
    ofstream saida1, saida2, saida3, saida4;
    float x[3000], y[3000];
    int cluster[3000];
    float xm[NCLUSTERS], ym[NCLUSTERS];
    int k = NCLUSTERS;
    int tam[NCLUSTERS];
    int change = 1;
    entrada.open("./data.dat");
    saida1.open("./data1.dat");
    saida2.open("./data2.dat");
    saida3.open("./data3.dat");
    // inicializa tamanho clusters
    for (int i = 0; i < NCLUSTERS; i++)
        tam[i] = 0;
    // inicializa membershipt

    for (int i = 0; i < 3000; i++)
    {

        entrada >> x[i];
        entrada >> y[i];
        cluster[i] = rand() % NCLUSTERS;
        tam[cluster[i]]++;
    }

    while (change == 1)
    {
        change = 0;
        for (int i = 0; i < k; i++)
        {
            tam[i] = 0;
        }

        for (int i = 0; i < 3000; i++)
        {

            tam[cluster[i]]++;
        }

        // calcula centroides

        for (int i = 0; i < k; i++)
        {
            xm[i] = 0.0;
            ym[i] = 0.0;
            for (int j = 0; j < 3000; j++)
            {
                if (cluster[j] == i)
                {
                    xm[i] = xm[i] + x[j];
                    ym[i] = ym[i] + y[j];
                }
            }
            if (tam[i] > 0)
            {
                xm[i] /= (double)tam[i];
                ym[i] /= (double)tam[i];
            }
            else
            {
                xm[i] = 0.0;
                ym[i] = 0.0;
            }
        }

        // reassocia dados a novos centroides
        for (int j = 0; j < 3000; j++)
        {

            float distancia = d(x[j], y[j], xm[cluster[j]], ym[cluster[j]]);
            for (int i = 0; i < k; i++)
            {
                float dist_current = d(x[j], y[j], xm[i], ym[i]);
                if (dist_current < distancia)
                {
                    distancia = dist_current;
                    cluster[j] = i;
                    change = 1;
                }
            }
        }
    }
    /*
        int elementos[NCLUSTERS];
        for (int i=0; i<k; i++)
        {
            float mediax=0;
            float mediay=0;
            elementos[i]=0;
            for (int j=0; j<3000; j++)
                if (cluster[j]==i)
                {

                    mediax+=x[j];
                    mediay+=y[j];
                    elementos[i]=elementos[i]+1;
                }
            //cout << mediax << " " << mediay << endl;
            if (elementos[k]>0)
            {
                xm[i]=mediax/(float)elementos[k];
                ym[i]=mediay/(float)elementos[k];
            }
        }



        for (int i=0; i<k; i++)
        {

            //cout << xm[i] << " " << ym[i] << " tam:" << elementos[i] << endl;
            //saida1 << xm[i] << " " << ym[i] << endl;
        }
    */
    for (int j = 0; j < 3000; j++)
    {
        switch (cluster[j])
        {
        case 0:
            saida1 << x[j] << " " << y[j] << endl;
            break;
        case 1:
            saida2 << x[j] << " " << y[j] << endl;
            break;
        case 2:
            saida3 << x[j] << " " << y[j] << endl;
            break;
        }
    }
    for (int i = 0; i < 3; i++)
    {
        saida4 << xm[i] << " " << ym[i] << endl;
    }

    entrada.close();
    saida1.close();
    saida2.close();
    saida3.close();
    saida4.close();
}
