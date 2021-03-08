#include "heating_helper_progs.c"

double A;
double FSTAR10 = 0.01;
int main()
{
A =  RHOcrit*pow(CMperMPC, -3);
printf("%e\n", A );
}
