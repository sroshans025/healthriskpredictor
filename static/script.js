document.getElementById("healthForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    age: document.getElementById("age").value,
    gender: document.getElementById("gender").value,
    systolic: document.getElementById("systolic").value,
    diastolic: document.getElementById("diastolic").value,
    cholesterol: document.getElementById("cholesterol").value,
    glucose: document.getElementById("glucose").value,
    bmi: document.getElementById("bmi").value,
    smoking: document.getElementById("smoking").value,
  };

  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await res.json();

    document.getElementById("heart_risk").textContent = "❤️ Heart Disease: " + result.heart_risk;
    document.getElementById("diabetes").textContent = "💉 Diabetes: " + result.diabetes;
    document.getElementById("stroke_risk").textContent = "🧠 Stroke: " + result.stroke_risk;
    document.getElementById("bp_category").textContent = "💓 Blood Pressure: " + result.bp_category;

    document.getElementById("loading").classList.add("hidden");
    document.getElementById("result").classList.remove("hidden");
  } catch (err) {
    alert("Error connecting to server. Check console for details.");
    console.error(err);
    document.getElementById("loading").classList.add("hidden");
  }
});

document.getElementById("resetBtn").addEventListener("click", () => {
  document.getElementById("healthForm").reset();
  document.getElementById("result").classList.add("hidden");
});
