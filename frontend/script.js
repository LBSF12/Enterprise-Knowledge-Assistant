const questionBox = document.getElementById("question");
const askButton = document.getElementById("askButton");
const chatBox = document.getElementById("chat");


// =====================================
// Create chat message
// =====================================

function addMessage(role, text, sources = []) {

    const row = document.createElement("div");

    row.classList.add("message-row");
    row.classList.add(role);


    // Avatar
    const avatar = document.createElement("div");

    avatar.classList.add("avatar");


    if (role === "user") {

        avatar.classList.add("avatar-user");
        avatar.textContent = "👤";

    } 
    else {

        avatar.classList.add("avatar-assistant");
        avatar.textContent = "🤖";

    }


    // Bubble container
    const bubble = document.createElement("div");

    bubble.classList.add("bubble");


    // Message text
    const bubbleText = document.createElement("div");

    bubbleText.classList.add("bubble-text");


    bubble.appendChild(bubbleText);


    /*
        User messages appear immediately.

        Assistant messages use typing animation.
    */

    if (role === "assistant") {

        typeWriter(
            bubbleText,
            text
        );

    }
    else {

        bubbleText.textContent = text;

    }



    // ================================
    // Sources
    // ================================

    if (sources.length > 0) {


        const sourceBox = document.createElement("div");

        sourceBox.classList.add("sources-box");


        const title = document.createElement("div");

        title.classList.add("sources-box-title");

        title.textContent = "Sources";


        sourceBox.appendChild(title);



        for (const source of sources) {


            const sourceRow = document.createElement("div");

            sourceRow.classList.add("source-row");



            sourceRow.innerHTML = `

                <div class="source-main">

                    <div class="source-file">
                        📄 ${source.file}
                    </div>


                    <div class="source-dept">
                        ${source.department}
                    </div>

                </div>


                <div class="source-score">

                    ${(source.score * 100).toFixed(1)}%

                </div>

            `;


            sourceBox.appendChild(sourceRow);

        }


        bubble.appendChild(sourceBox);

    }



    row.appendChild(avatar);

    row.appendChild(bubble);


    chatBox.appendChild(row);


    chatBox.scrollTop = chatBox.scrollHeight;


}




// =====================================
// Typing animation
// =====================================

async function typeWriter(element, text, speed = 25) {


    element.textContent = "";


    const words = text.split(" ");


    for (const word of words) {


        element.textContent += word + " ";


        chatBox.scrollTop = chatBox.scrollHeight;


        await new Promise(resolve =>

            setTimeout(resolve, speed)

        );

    }

}




// =====================================
// Thinking message
// =====================================


function addThinkingMessage() {


    const row = document.createElement("div");


    row.classList.add(
        "message-row",
        "assistant"
    );


    row.id = "thinking-message";



    row.innerHTML = `

        <div class="avatar avatar-assistant">
            🤖
        </div>


        <div class="bubble">

            <div class="bubble-text">

                Thinking...

            </div>

        </div>

    `;


    chatBox.appendChild(row);


    chatBox.scrollTop = chatBox.scrollHeight;

}




function removeThinkingMessage() {


    const thinking = document.getElementById(
        "thinking-message"
    );


    if (thinking) {

        thinking.remove();

    }

}





// =====================================
// Send question
// =====================================

async function sendQuestion() {


    const question = questionBox.value.trim();



    if (question === "") {

        return;

    }



    // Show user question

    addMessage(
        "user",
        question
    );



    // Clear input

    questionBox.value = "";



    // Show thinking

    addThinkingMessage();



    // Disable while waiting

    askButton.disabled = true;

    questionBox.disabled = true;

    askButton.textContent = "...";



    try {


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



        console.log(
            "API Response:",
            data
        );



        // Remove thinking

        removeThinkingMessage();



        // Show answer

        addMessage(

            "assistant",

            data.answer,

            data.sources

        );



    }


    catch(error) {


        console.error(
            error
        );


        removeThinkingMessage();



        addMessage(

            "assistant",

            "Sorry, an error occurred while contacting the AI service."

        );


    }



    finally {


        askButton.disabled = false;


        questionBox.disabled = false;


        askButton.textContent = "➤";


        questionBox.focus();


    }


}




// =====================================
// Button click
// =====================================

askButton.addEventListener(

    "click",

    sendQuestion

);





// =====================================
// Press ENTER to send
// =====================================

questionBox.addEventListener(

    "keydown",

    function(event) {


        if (event.key === "Enter") {


            event.preventDefault();


            sendQuestion();


        }


    }

);