function generateVitals() {
  const heartRate = Math.floor(Math.random() * (135 - 90) + 90);
  const oxygen = Math.floor(Math.random() * (100 - 85) + 85);

  let risk = "Stable";

  if (heartRate > 120 || oxygen < 90) {
    risk = "Critical";
  } else if (heartRate > 100) {
    risk = "Moderate";
  }

  return {
    heartRate,
    oxygen,
    risk
  };
}

function updateDashboard() {
  const vitals = generateVitals();

  const heartRateEl = document.getElementById("heartRate");
  const oxygenEl = document.getElementById("oxygen");
  const riskEl = document.getElementById("risk");

  if (heartRateEl) {
    heartRateEl.innerText = `${vitals.heartRate} BPM`;
  }

  if (oxygenEl) {
    oxygenEl.innerText = `${vitals.oxygen}%`;
  }

  if (riskEl) {
    riskEl.innerText = vitals.risk;
  }
}

setInterval(updateDashboard, 3000);

window.onload = updateDashboard;