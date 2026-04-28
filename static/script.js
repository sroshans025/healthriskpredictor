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

  const btn = document.getElementById("predictBtn");
  const originalBtnText = btn.innerHTML;
  btn.disabled = true;

  // Manage UI States
  document.getElementById("defaultState").classList.add("hidden");
  document.getElementById("result").classList.add("hidden");
  document.getElementById("loading").classList.remove("hidden");

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await res.json();

    // Helper to color code the risk
    const formatRisk = (riskStr) => {
        if(riskStr.includes("High") || riskStr.includes("Hazard") || riskStr.includes("Danger")) {
            return `<span class="text-rose-500">${riskStr}</span>`;
        } else if(riskStr.includes("Moderate") || riskStr.includes("Borderline")) {
            return `<span class="text-amber-500">${riskStr}</span>`;
        } else {
            return `<span class="text-emerald-500">${riskStr}</span>`;
        }
    };

    document.getElementById("heart_risk").innerHTML = formatRisk(result.heart_risk);
    document.getElementById("diabetes").innerHTML = formatRisk(result.diabetes);
    document.getElementById("stroke_risk").innerHTML = formatRisk(result.stroke_risk);
    
    // BP Category
    document.getElementById("bp_category").innerHTML = result.bp_category;

    // Simulate a brief calculation delay for dramatic effect
    setTimeout(() => {
        document.getElementById("loading").classList.add("hidden");
        
        const resultCard = document.getElementById("result");
        resultCard.classList.remove("hidden");
        // Trigger reflow for animation
        void resultCard.offsetWidth;
        
        btn.disabled = false;
    }, 800);

  } catch (err) {
    alert("Error connecting to server. Check console for details.");
    console.error(err);
    document.getElementById("loading").classList.add("hidden");
    document.getElementById("defaultState").classList.remove("hidden");
    btn.disabled = false;
  }
});

document.getElementById("resetBtn").addEventListener("click", () => {
  document.getElementById("healthForm").reset();
  
  // Reset States
  document.getElementById("result").classList.add("hidden");
  document.getElementById("defaultState").classList.remove("hidden");
});
