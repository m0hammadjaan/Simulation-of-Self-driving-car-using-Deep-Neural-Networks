class SpeedoMeter
{
    constructor(car)
    {
        this.car = car;
        this.spread = Math.PI*2
    }
    draw(ctx)
    {
        ctx.beginPath();
        ctx.arc(100, 75, 50, 0, 2 * Math.PI);
        ctx.stroke();
    }
}