<script>
    export let content = "Error";
    export let type;
    export let color = "grey";
    export let float = "left"

    if (type == "ai") {
        color = "#49cc9a";
    }
    else {
        color = "#cdd1d0";
        float = "right"
    }
</script>

<div class="flex">
    <div class="bubble {type}" style="background-color: {color};">
        {content}
    </div>
</div>


<style>

    .bubble.ai {
        justify-content: flex-start; /* Align AI messages to the left */
    }

    .bubble.human {
        background-color: black;
        margin-left: auto;
    }

    .bubble {
        color: white;
        display: inline-block;; /* Keeps the bubble size fitting the text */
        padding: 10px; /* Adds space around the text inside the bubble */
        border-radius: 10px; /* Gives rounded corners */
        max-width: 100%; /* Prevents bubbles from overflowing */
        word-wrap: break-word; /* Breaks long words if necessary */
        max-width: 40%;
    }
</style>