async function loadStatus(){
  const res = await fetch("/status");
  const data = await res.json();

  const box = document.getElementById("box");
  const info = document.getElementById("info");

  box.innerHTML = data.desk;

  if(data.desk === "Occupied"){
    box.className = "status-box occupied";
  } else {
    box.className = "status-box empty";
  }

  info.innerHTML = `
    <b>Device:</b> Arduino Uno<br>
    <b>Sensor:</b> HC-SR04 Ultrasonic<br>
    <b>Distance:</b> ${data.distance}<br>
    <b>Status Update:</b> Just now
  `;
}

setInterval(loadStatus, 3000);
