<script>
    import Button from "$lib/ExampleComponent.svelte";

    export let disabled = false
    let message = "";
    export let sendMessageToAPI = () => {};

    async function sendMessage() {
        if (message.trim()) {
            sendMessageToAPI(message);
            message = ""; // Clear the input box after sending
        }
    }

</script>
<div class="c">
    <input 
    class="chat-input" 
    placeholder="Ask me anything"
    bind:value={message}
    on:keydown={(event) => event.key == "Enter" && sendMessage()}
    disabled={disabled}/>
<Button onclick = {sendMessage} name="Send"/>
</div>


<style>
    .chat-input {
        width: calc(100% - 70px);
        border: 1px solid #49cc9a;
        border-radius: 10px;
        margin: 10px 0;
        padding: 10px;
        outline: none; /* Remove default browser focus outline */
        transition: border 0.2s ease-in-out; /* Smooth transition effect */
    }

    .chat-input:focus {
        border: 2px solid #49cc9a; /* Increase border width */
    }

</style>