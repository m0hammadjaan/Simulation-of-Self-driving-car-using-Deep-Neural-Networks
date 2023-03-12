const canvas=document.getElementById("myCanvas");
canvas.width=470;

const ctx = canvas.getContext("2d");
const road=new Road(canvas.width/2,canvas.width*0.9, 7);
const car=new Car(road.getLaneCenter(3),100,30,50, "Player");

const traffic = 
[
    new Car(road.getLaneCenter(random()),200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-1800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-2000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-2200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-2400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-2600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-2700,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-3800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-4800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-5000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-5200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-5400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-5600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-5900,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-6800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-7800,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-8000,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-8200,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-8400,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
    new Car(road.getLaneCenter(random()),-8600,30,50, "DUMMY", getRandomSpeed(), getRandomColor()),
];
for (let i = 1; i < 1000; i++)
{
    traffic.push(new Car(road.getLaneCenter(random()),-i*100,30,50, "DUMMY", getRandomSpeed(), getRandomColor()));
}

animate();

function animate(){
    if(!car.damaged)
    {
        document.getElementById('speed').innerHTML = Math.round(Math.abs(car.speed * 10));
        for(let i = 0; i < traffic.length; i++)
        {
            traffic[i].update(road.borders, []);
        }

        car.update(road.borders, traffic);

        canvas.height=window.innerHeight;

        ctx.save();
        ctx.translate(0,-car.y+canvas.height*0.7);

        road.draw(ctx);
        for(let i = 0; i < traffic.length; i++)
        {
            traffic[i].draw(ctx);
        }
        car.draw(ctx);

        ctx.restore();
        requestAnimationFrame(animate);
    }
    else
    {
        document.getElementById('speed').innerHTML = "DEAD";
    }
}