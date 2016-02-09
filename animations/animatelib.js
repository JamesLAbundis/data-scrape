
class CircleEvent{

	constructor(elem,deaths){
		this.elem=elem;
		this.death=deaths;
	}
	get deaths(){
		return this.deaths;
	}
}

class EventHolder{
	var events =[];

	constructor(){

	}

	get eventArray(){
		return events;
	}

	addEvent(circ){
		events.push(circ);
	}
}

class Point{

	var x_pos=0;
	var y_pos=0;

	constructor(x_pos,y_pos){
		this.x_pos=xpos;
		this.y_pos=ypos;
	}

	get xCoord(){
		return x_pos;
	}
	get yCoord(){
		return y_pos;
	}
	function output(){
		return (String)x_pos+" "+ (String)y_pos;

	}

}

function getPositions(width,height,numCircles){
	var points [];
	var xDelta=(int)width/3; //cast to int to make even pixels
	var yDelta=(int)height/(numCircles+1);

	//nested for loop to construct point----> point []
	for(i=0;i<width;i+=xDelta){

		for(j=0; j<height;j+=yDelta){
			var point=new Point(i,j);
			points.push(Point)
		}
	}
	return points;
}







