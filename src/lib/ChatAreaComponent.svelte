<script>
    import ChatBarComponent from "./ChatBarComponent.svelte";
    import MessageBubbleComponent from "./MessageBubbleComponent.svelte";

    let messages = [
        { content: "Hi, I am plant. How can I help you", type: "ai" },
    ];

    let loading = false;

    async function callAPI(message) {
        messages = [...messages, { content: "...", type: "waiting" }];
        loading = true;
        await new Promise((resolve) => setTimeout(resolve, 5000)); 
        messages.pop();

        let AIresponse = "Hi, there is two plants on this text. \n I am *Rose* and I am *Iris*";
        messages = [...messages, { content: AIresponse, type: "ai" }];

        loading = false;
    }

    async function sendMessage(message) {
        messages = [...messages, { content: message, type: "human" }];
        await callAPI(message);
    }
</script>

<div class="chat-container p-16 w-full">
    <div class="messages">
        {#each messages as message}
            <MessageBubbleComponent content={message.content} type={message.type}></MessageBubbleComponent>
        {/each}
    </div>
    <ChatBarComponent disabled={loading} sendMessageToAPI={sendMessage}></ChatBarComponent>
</div>

<style>
    .chat-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        height: 100vh; /* Or set a specific height for your container */
    }

    .messages {
        flex-grow: 1;
        overflow-y: auto; /* Allow scrolling if there are many messages */
    }
</style>
