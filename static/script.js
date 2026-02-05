async function loadStatus(){
let res = await fetch("/status");
let data = await res.json();

let box = document.getElementById("box");
let info = document.getElementById("info");

box.innerHTML = data.desk;

if(data.desk=="Occupied"){
box.className="status-box occupied";
}else{
box.className="status-box empty";
}

info.innerHTML = `
Device: ${data.device}<br>
Distance: ${data.distance}<br>
Location: ${data.location}
`;
}

setInterval(loadStatus,3000);
