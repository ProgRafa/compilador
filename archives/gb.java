class Factorial
{
    public static void main()
    {
	    Fac fac = new Fac()
        fac.ComputeFac();
    }
}

class Fac 
{
    public int ComputeFac()
    {
        int num = 10;
        int fac = num;
        
        for(int aux = 9; aux > 0; aux--)
        {
            fac *= aux;  
        }
        
        return num_aux;
    }
}