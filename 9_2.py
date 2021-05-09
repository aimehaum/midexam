class Engine
{
    int power;
    public Engine(int p)
    {
        power = p;
    }
}

class Car
{
    string model = "Porshe";
    Engine engine;
    public Car()
    {
        this.engine = new Engine(360);
    }
}