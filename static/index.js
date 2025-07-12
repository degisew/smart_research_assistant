const form = document.getElementById("input_form");
const spinner = document.getElementById("spinner");
const result = document.getElementById("result");
const profilePic = document.getElementById("profile-pic");
const summary = document.getElementById("summary");
const facts = document.getElementById("facts");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  result.style.display = "none";
  spinner.style.display = "";

  const formData = new FormData(form);

  try {
    const response = await fetch("/process", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();

    profilePic.src = data.picture_url;
    summary.textContent = data.summary_and_facts.summary;
    renderList(facts, data.summary_and_facts.facts);

    result.style.display = "";
  } catch (err) {
    console.error("Error:", err);
    alert("Something went wrong while processing the form.");
  } finally {
    spinner.style.display = "none";
  }
});

function renderList(container, items) {
  container.innerHTML = "";
  const ul = document.createElement("ul");

  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    ul.appendChild(li);
  }

  container.appendChild(ul);
}
