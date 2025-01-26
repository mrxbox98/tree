<script lang="ts">
    import ChatBarComponent from "./ChatBarComponent.svelte";
    import MessageBubbleComponent from "./MessageBubbleComponent.svelte";
    import HelpModal from "./HelpModal.svelte";

    import { getCity, getLatLong } from "./client";

    let messages = [
        { content: "Hi, I am YourPlantFriend, an AI where you can useful information about starting planting in your area. How can I help you today?", type: "ai" },
    ];

    let loading = false;
    let showHelpModal = false; // Control the visibility of the help modal

    async function callAPI(message: string) {
        let previousMessage = '';


        for (let message of messages) {
            previousMessage += message.type+": " + message.content + "\n";
        }

        messages = [...messages, { content: "...", type: "waiting" }];
        loading = true;
        
        let location = await getLatLong();
        let city = await getCity(location.lat, location.long);


        let req = await fetch(`http://database.emblems.report:8000/generate`, {
            method: "POST",
            body: JSON.stringify({
                previousMessage,
                location: city,
                userInput: message,
            }),
            headers: {
                "Content-Type": "application/json",
            }
        })

        let res = await req.json();

        messages.pop();

        let AIresponse = res;
        messages = [...messages, { content: AIresponse, type: "ai" }];

        loading = false;
    }

    async function sendMessage(message) {
        if (message == "/help") {
            showHelpModal = true; // Show the help modal
            return;
        } else if (message == "/clear") {
            messages = [
                { content: "Hi, I am YourPlantFriend, an AI where you can useful information about starting planting in your area. How can I help you today?", type: "ai" },
            ]; // Clear chat
            return;
        }

        messages = [...messages, { content: message, type: "human" }];
        await callAPI(message);
    }

    function closeHelpModal() {
        showHelpModal = false; // Close the help modal
    }
</script>

<div class="chat-container p-16 w-full">
    <div class="messages">
        {#each messages as message}
            <MessageBubbleComponent content={message.content} type={message.type}></MessageBubbleComponent>
        {/each}
    </div>
    <ChatBarComponent disabled={loading} sendMessageToAPI={sendMessage}></ChatBarComponent>

    {#if showHelpModal}
        <HelpModal on:close={closeHelpModal} />
    {/if}
</div>

<style>
    .chat-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        height: 100vh;
    }

    .messages {
        flex-grow: 1;
        overflow-y: auto;
    }
</style>
