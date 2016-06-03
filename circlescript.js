function scaleNum(num){
		var rawResult=Math.floor(Math.log10(num)*20);

		if(rawResult>75){
			rawResult=75;
		}

		if(rawResult<35){
			rawResult=35;
		}

		return rawResult;
	}
		

function dwCircOne(scale,canvas,index){
	//ensures circle will not overflow out of div
	canvas.style.width=(scale*2)+"px";
	canvas.style.height=(scale*2)+"px";
	canvas.width=scale*2;
	canvas.height=scale*2;

	canvas.style.opacity=0.5;

	var context=canvas.getContext('2d');
  	context.shadowOffsetX = 5;
	context.shadowOffsetY = 5;
	context.shadowBlur = 4;
	context.shadowColor = 'rgba(30,30,30, 0.5)';
		
	// Draw circle
	context.beginPath();
	//3rd argument is the radius
	//this must be scaled
	context.arc(scale,scale,scale, 0, 2 * Math.PI, false);
	if(index<=3){
		context.fillStyle = "#0000FF";
		context.fill();
	}
	else if(index<=8){
		context.fillStyle = "#b30000";
		context.fill();
	}
	else{
		context.fillStyle = "#FFD700";
		context.fill();
	}
	
	}

function setGraph(){
	//sloviansk-kramatorsk-marinka-mariupol-horlivka-debaltseve-iloviask
	var xCoords= [156,154,153,149,240,217,199,204,176,178];

	var yCoords= [217,236,365,492,299,265,305,490,349,492];
	//list of canvas objects
	var borders=document.getElementsByClassName("bord");

	var xOffset=document.getElementById("battlemap").style.left;
	var yOffset=document.getElementById("battlemap").style.top;
	

	for(i=0; i<borders.length; i++){
			
		//sets a x and y positioning for animations
		borders[i].style.position="absolute";

		
		//Sets y position
  		borders[i].style.top = (yCoords[i])+'px';
  		//Sets x position
  		borders[i].style.left=(xCoords[i])+'px';
  		//Draws circle for each canvas
  			
  		dwCircOne(10,borders[i],i);
	}
}

function drawDescription(){
	var scale=35;
	var dprCirc=document.getElementById("dpr");
	var ukrCirc=document.getElementById("ukr");
	var ceaseCirc=document.getElementById("cease");

	dprCirc.style.opacity=0.5;
	ukrCirc.style.opacity=0.5;
	ceaseCirc.style.opacity=0.5;

	dprCirc.style.width=(scale*2)+"px";
	dprCirc.style.height=(scale*2)+"px";
	dprCirc.width=scale*2;
	dprCirc.height=scale*2;

	ukrCirc.style.width=(scale*2)+"px";
	ukrCirc.style.height=(scale*2)+"px";
	ukrCirc.width=scale*2;
	ukrCirc.height=scale*2;

	ceaseCirc.style.width=(scale*2)+"px";
	ceaseCirc.style.height=(scale*2)+"px";
	ceaseCirc.width=scale*2;
	ceaseCirc.height=scale*2;

	var context1=dprCirc.getContext('2d');
	var context2=ukrCirc.getContext('2d');
	var context3=ceaseCirc.getContext('2d');

	context1.beginPath();
	context1.arc(scale,scale,scale, 0, 2 * Math.PI, false);
	context1.fillStyle = "#0000FF";
	context1.fill();

	context1.font = "bold 12px Arial";
	context1.fillStyle = "white";
	context1.textAlign = "center";
	context1.fillText("DPR", dprCirc.width/2, dprCirc.height/2);

	context2.beginPath();
	context2.arc(scale,scale,scale, 0, 2 * Math.PI, false);
	context2.fillStyle = "#b30000";
	context2.fill();

	context2.font = "bold 12px Arial";
	context2.fillStyle = "white";
	context2.textAlign = "center";
	context2.fillText("UAF", ukrCirc.width/2, ukrCirc.height/2);

	context3.beginPath();
	context3.arc(scale,scale,scale, 0, 2 * Math.PI, false);
	context3.fillStyle = "#FFD700";
	context3.fill();

	context3.font = "bold 12px Arial";
	context3.fillStyle = "white";
	context3.textAlign = "center";
	context3.fillText("Ceasefire", ceaseCirc.width/2, ceaseCirc.height/2);
}


function scaleNum(num){
		var rawResult=Math.floor(Math.log10(num)*40);

		if(rawResult>150){
			rawResult=150;
		}

		if(rawResult<50){
			rawResult=50;
		}

		return rawResult;
	}
		

function dwCircTwo(scale,canvas,nums){
	//ensures circle will not overflow out of div
	canvas.style.width=(scale*2+10)+"px";
	canvas.style.height=(scale*2+10)+"px";
	canvas.width=scale*2+10;
	canvas.height=scale*2+10;

			
	var context=canvas.getContext('2d');
  	context.shadowOffsetX = 5;
	context.shadowOffsetY = 5;
	context.shadowBlur = 4;
	context.shadowColor = 'rgba(30,30,30, 0.5)';
		
	// Draw circle (red)
	context.beginPath();
	//3rd argument is the radius
	//this must be scaled
	context.arc(scale,scale,scale, 0, 2 * Math.PI, false);

	if(nums==0){
		nums="N/A";
		context.fillStyle = "#808080";
	}

	else{
		context.fillStyle = "#b30000";
	}
	context.fill();
	//Draws text one circle
	context.font = "18px Arial";
	context.fillStyle = "white";
	context.textAlign = "center";
	context.fillText(nums+" ", canvas.width/2-5, canvas.height/2-12);
	//writes description for number in circle
	context.font = " italic 12px Arial";
	context.fillStyle = "white";
	context.textAlign = "center";
	context.fillText("civilian", (canvas.width/2)-5,(canvas.height/2)+2);

	context.font = " italic 12px Arial";
	context.fillStyle = "white";
	context.textAlign = "center";
	context.fillText("casualties", (canvas.width/2)-5,(canvas.height/2)+14);
}

function makeBattles(){
	//is casualties=0 then it is unknown
	var civCasual=[100,36,500,9,0,0,11,0,2,0,20];

	//list of canvas objects
	var circs=document.getElementsByClassName("circ");
	var divHolder=document.getElementsByClassName("circontainer");

	//var exam=document.getElementsByClassName("battle");
	
	var yOffset=118;
		

	for(i=0; i<circs.length; i++){
				
		//sets a x and y positioning for animations
		//circs[i].style.position="absolute";

			
		//Sets y position
	  	//circs[i].style.top = yOffset+'px';
	  	//Sets x position
	  	//circs[i].style.left=xOffset+'px';
	  	//Draws circle for each canvas
	  	var scale=scaleNum(civCasual[i]);
	  		dwCircTwo(scale,circs[i],civCasual[i]);
		}
	}

