const form = document.getElementById("input_form");
const spinner = document.getElementById("spinner");
const result = document.getElementById("result");
const summary = document.getElementById("summary");
const background = document.getElementById("background");
const competitors = document.getElementById("competitors");
const questions = document.getElementById("questions");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  result.style.display = "none";
  spinner.style.display = "block";

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
    summary.textContent = data.parsed_data.summary;
    background.textContent = data.parsed_data.team_background

    renderList(competitors, data.parsed_data.competitors);
    renderList(questions, data.parsed_data.questions);

    result.style.display = "block";
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
