const questionBox = document.getElementById("question");

const askButton = document.getElementById("askButton");

const answerBox = document.getElementById("answer");

//console.log("JavaScript loaded!")

askButton.addEventListener("click", async function () {

    const question = questionBox.value;

    const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        }
    );

    const data = await response.json();

    answerBox.textContent = data.answer;

});