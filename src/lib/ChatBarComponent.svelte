<script>
    import Button from "$lib/ExampleComponent.svelte";

    export let disabled = false;
    let message = "";
    export let sendMessageToAPI = () => {};

    let listOfCommands = ["/help", "/clear", "/conclude"];
    let showCommandList = false;

    async function sendMessage() {
        if (message.trim()) {
            sendMessageToAPI(message);
            message = ""; // Clear the input box after sending
            showCommandList = false; // Hide the commands list
        }
    }

    function handleInput(event) {
        if (message.startsWith("/")) {
            showCommandList = true;
        } else {
            showCommandList = false;
        }
    }

    function selectCommand(command) {
        message = command; // Set the selected command as the input value
        showCommandList = false; // Hide the commands list
    }
</script>

<div class="c">
    {#if showCommandList}
    <ul class="command-list">
        {#each listOfCommands as command}
        <li on:click={() => selectCommand(command)}>{command}</li>
        {/each}
    </ul>
    {/if}
    <input 
        class="chat-input" 
        placeholder="Ask me anything about plant"
        bind:value={message}
        on:input={handleInput}
        on:keydown={(event) => event.key == "Enter" && sendMessage()}
        disabled={disabled}
    />
    <Button onclick={sendMessage} name="Send" />
</div>

<style>
    .c {
        position: relative; /* Ensures proper positioning of the command list */
    }

    .chat-input {
        width: calc(100% - 70px);
        border: 1px solid #8CC342;
        border-radius: 10px;
        margin: 10px 0;
        padding: 10px;
        outline: none; /* Remove default browser focus outline */
        transition: border 0.2s ease-in-out; /* Smooth transition effect */
    }

    .chat-input:focus {
        border: 2px solid #8CC342; /* Increase border width */
    }

    .command-list {
        list-style: none;
        margin: 0;
        padding: 5px;
        background: #f9f9f9;
        border: 1px solid #8CC342;
        border-radius: 5px;
        max-width: calc(100% - 70px);
        position: absolute; /* Float the command list above the input */
        bottom: 100%; /* Position it above the input */
        margin-bottom: 5px; /* Add some spacing between the list and the input */
        z-index: 10;
    }

    .command-list li {
        padding: 5px 10px;
        cursor: pointer;
        transition: background 0.2s ease-in-out;
    }

    .command-list li:hover {
        background: #e0e0e0;
    }
</style>
